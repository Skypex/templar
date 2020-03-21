# Templar

Templar is a tool to compile a source directory into a destination directory using Jinja template language.

A possible use case could be that you have to compile some default configuration over and over again.
With Templar, you could create the configuration once and fill it afterwards with variables.git

## Installation

Setup a virtual environment and install the required packages via [pip](https://pip.pypa.io/en/stable/).

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Usage

```python
python templar/main.py
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[GPL-3.0](https://choosealicense.com/licenses/gpl-3.0/)
