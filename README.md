# Prettify JSON

Cкрипт, который на вход принимает  файл с произвольными данными в формате JSON и выводит его содержимое в консоль в удобном для чтения виде: добавляет переносы строк, отступы слева и пробелы.

# Quickstart

[TODO]

Example of script launch on Linux, Python 3.5:

```bash

$ python pprint_json.py <name of file>  # possibly requires call of python3 executive instead of just python
{
	"type": "Feature",
	"geometry": {
		"coordinates": [
			37.61230620948003,
			55.73473489837388
		],
		"type": "Point"
	},
	"properties": {
		"ReleaseNumber": 2,
		"RowId": "9d238393-552d-4ab9-ae1b-12f69e54c83d",
		"DatasetId": 1854,
		},
		"VersionNumber": 1
	}
}

```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
