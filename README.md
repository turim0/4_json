# Prettify JSON

A script that accepts a data file in JSON format and outputs it to the console in an easy-to-read format: adds line breaks, left indents and spaces.

# Quickstart

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
