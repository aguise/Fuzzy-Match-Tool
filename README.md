# Fuzzy-Match-Tool
A matching tool that utilizes fuzzy-matching algorithms to take in raw data inputs and outputs standardized ISO-Codes into an Excel file for access

## Getting Started
These instructions will help you run the following project and produce a list of standardized ISO codes for your raw data input

### Prerequisites
This project includes some external Python libraries that will need to be installed in order to run the project successfully

```
pip install fuzzywuzzy
pip install xlwt
```

## Installing 
Simply clone the repository into a folder on your local project directory
```
git clone https://github.com/aguise/Fuzzy-Match-Tool.git
```

## Running the Project
The following command line script successfully runs this project. Command line arguments include inputting what type of ISO code data is being matched, and then CSV files for the raw data input and what the standardadize format for this data.
```
python main.py [type of data] [raw_data_file] [standard_data_file]
```

### Example
```
python main.py "currencies" currnecy_input.csv currency_output.csv
```

## Built With
* [fuzzywuzzy](https://pypi.org/project/fuzzywuzzy/) - Fuzzy string matching library utilizing Levenshtein Distance
* [xlwt](https://pypi.org/project/xlwt/) - Python library that helps generate spreadsheet files

## Authors
* **Andrew (Mac) Guise** - [aguise](https://github.com/aguise)
* **Nicholas Rucker** - [nicholasrucker](https://github.com/nicholasrucker)
* **Amruta Rao** - [amurao1998](https://github.com/amurao1998)

