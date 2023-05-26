# DataDoctor[Beta]

DataDoctor is a Python package for data cleaning and preprocessing. It provides various methods to treat common issues in data such as missing values, duplicate records, inconsistent data formats, outliers, inconsistent naming conventions, data entry errors, and more. The package uses popular libraries such as pandas, numpy, scikit-learn, fuzzywuzzy, and chardet.

[![Python Version](https://img.shields.io/badge/python-3.6%20%7C%203.7%20%7C%203.8%20%7C%203.9-blue)](https://www.python.org/downloads/)

## Built With

- pandas
- numpy
- scikit-learn
- fuzzywuzzy
- python-Levenshtein
- chardet

## Prerequisites

- Python 3.6 or higher

## Getting Started

Follow these instructions to get started with DataDoctor.

## Installation

```
pip install DataDoctor
```
or
```
!pip install DataDoctor
```

## Usage

### Import the DataDoctor package
```
from data_doctor import DataDoctor
```

### Create an instance of DataDoctor
```
doctor = DataDoctor()
```
### Load your data in .CSV format
```
data = Your_Data.csv
```

### Treat the data
```
doctor.load_data(data)
doctor.treat_missing_data()
doctor.treat_duplicate_records()
doctor.treat_inconsistent_data_formats()
doctor.treat_inaccurate_data_entries()
doctor.treat_outliers()
doctor.treat_inconsistent_naming_conventions()
doctor.treat_data_entry_errors()
doctor.treat_inconsistent_units_of_measurement()
doctor.treat_incorrect_data_types()
doctor.treat_invalid_values()
doctor.treat_inconsistent_or_conflicting_values()
doctor.treat_encoding_errors()
doctor.treat_inconsistent_date_and_time_formats()
doctor.treat_inconsistent_variable_names()
doctor.treat_inconsistent_capitalization_or_punctuation()
doctor.treat_spelling_or_typographical_errors()
```

### Generate a report
```
doctor.generate_report()
```

## Features

- Missing data treatment
- Duplicate records treatment
- Inconsistent data formats treatment
- Inaccurate data entries treatment
- Outliers treatment
- Inconsistent naming conventions treatment
- Data entry errors treatment
- Inconsistent units of measurement treatment
- Incorrect data types treatment
- Invalid values treatment
- Inconsistent or conflicting values treatment
- Encoding errors treatment
- Inconsistent date and time formats treatment
- Inconsistent variable names treatment
- Inconsistent capitalization or punctuation treatment
- Spelling or typographical errors treatment

## Algorithm

The DataDoctor package uses a combination of techniques to clean and preprocess data. These techniques include iterative imputation, simple imputation, isolation forest, fuzzy matching, and others. Each technique serves a specific purpose in the data cleaning and preprocessing process.

Iterative imputation is a method for handling missing data by modeling each missing value as a function of other variables in the data. Simple imputation is another method for handling missing data by replacing missing values with a single estimated value.

Isolation forest is an algorithm for detecting anomalies in data. It works by building an ensemble of isolation trees to isolate anomalies from the rest of the data.

Fuzzy matching is a technique for finding matches between strings that are not exactly the same but are similar. It can be used to identify and link records that refer to the same entity but have variations in spelling or formatting.

By using these techniques together, the DataDoctor package can effectively clean and preprocess data to improve its quality and usability.

## Feedback

I welcome feedback, bug reports, and feature requests. Please submit them to the Issue Tracker.

## Contribution

Contributions are welcome! Read the [Contribution Guidelines](CONTRIBUTING.md) for more information.

## Author

- Aryan Bajaj

## License

This project is licensed under the [MIT License](https://github.com/Aryan-Bajaj/DataDoctor/blob/main/LICENSE.md).
