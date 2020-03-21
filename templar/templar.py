from jinja2 import Environment, FileSystemLoader
import yaml
import os


root_dir = os.path.dirname(os.path.abspath("templar"))
variable_dir = os.path.join(root_dir, 'source/variable')
template_dir = os.path.join(root_dir, 'source/template')
build_dir = os.path.join(root_dir, 'build')


def get_filedirs(search_dir):
    files = list()
    subdirs = list()
    for (dirpath, dirnames, filenames) in os.walk(search_dir):
        files += [os.path.join(dirpath, f) for f in filenames]
        subdirs += [os.path.join(dirpath, d) for d in dirnames]
    return files, subdirs


def main():

    print("Templar started!")

    #print("Path Root: " + root_dir)
    #print("Path Variable: " + variable_dir)
    #print("Path Template: " + template_dir)
    #print("Path Build: " + build_dir)

    # First, check if the destination folder is empty
    files, subdirs = get_filedirs(build_dir)
    if files or subdirs:
        print("Build folder is not empty - exit!")
        return
    print("Build folder is empty - let's continue...")


    # Load the variable data
    print("Loading variables started")
    files, subdirs = get_filedirs(variable_dir)
    variables = dict()
    for file in files:
        if file.endswith('.yaml') or file.endswith('.yml'):
            with open(file, 'r') as stream:
                variables.update(yaml.full_load(stream))
            print("Loading variables from %s" % file)
    print("Loading variables finished")
    
    # Get all the files to render
    files, subdirs = get_filedirs(template_dir)

    # Sort dirs by length
    subdirs.sort(key=len)

    # Create all subfolders in build directory
    print("Creating new folders")
    for subdir in subdirs:
        newdir = subdir.replace(template_dir, build_dir)
        if not os.path.exists(newdir):
            os.mkdir(newdir)

    # Now start to render file by file
    print("Rendering files started")
    env = Environment(loader = FileSystemLoader(template_dir))
    for file in files:
        template = env.get_template(file.replace(template_dir, ''))
        rendered = template.render(variables) 
        with open(file.replace(template_dir, build_dir), 'w') as newfile:
            newfile.write(rendered)
            print("Rendering file %s" % newfile.name)
    print("Rendering files finished")
    
    print("Templar finished!")
    return



if __name__ == "__main__":
    main()