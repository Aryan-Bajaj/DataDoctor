# DataDoctor[Beta]

`DataDoctor()` is a Python package for data cleaning and preprocessing. It provides various methods to treat common issues in data such as missing values, duplicate records, inconsistent data formats, outliers, inconsistent naming conventions, data entry errors, and more. The package uses popular libraries such as `pandas`, `numpy`, `scikit-learn`, `fuzzywuzzy`, and `chardet`.

[![Python Version](https://img.shields.io/badge/python-3.6%20%7C%203.7%20%7C%203.8%20%7C%203.9-blue)](https://www.python.org/downloads/)

## Index
- [Built With](https://github.com/Aryan-Bajaj/DataDoctor/tree/main#built-with)
- [Prerequisites](https://github.com/Aryan-Bajaj/DataDoctor/tree/main#prerequisites)
- [Features](https://github.com/Aryan-Bajaj/DataDoctor/tree/main#features)
- [Getting Started](https://github.com/Aryan-Bajaj/DataDoctor/tree/main#getting-started)
- [Installation](https://github.com/Aryan-Bajaj/DataDoctor/tree/main#installation)
- [Usage](https://github.com/Aryan-Bajaj/DataDoctor/tree/main#usage)
- [Treat the data (Codes & Explanations)](https://github.com/Aryan-Bajaj/DataDoctor/tree/main#treat-the-data)
- [Algorithm](https://github.com/Aryan-Bajaj/DataDoctor/tree/main#algorithm)
- [Feedback](https://github.com/Aryan-Bajaj/DataDoctor/tree/main#feedback)
- [Contribution](https://github.com/Aryan-Bajaj/DataDoctor/tree/main#contribution)
- [Author](https://github.com/Aryan-Bajaj/DataDoctor/tree/main#author)
- [License](https://github.com/Aryan-Bajaj/DataDoctor/tree/main#license)

## Built With

- `pandas` - It is a Python library for **data analysis and manipulation**  that provides fast, flexible, and expressive data structures such as DataFrame and Series.
- `numpy` - It is a Python library for **scientific computing** that adds support for large, multi-dimensional arrays, matrices and high-level mathematical functions to operate on these arrays.
- `scikit-learn` - It is a Python library for **machine learning** that provides simple and efficient tools for data mining and data analysis, such as classification, regression, clustering, dimensionality reduction, etc.
- `fuzzywuzzy` - It is a Python library for **fuzzy string matching** that uses the Levenshtein distance to calculate the similarity between two strings.
- `python-Levenshtein` - It is a Python extension module that provides fast computation of **Levenshtein distance** and string operations based on it.
- `chardet` - It is a Python library that can automatically detect the **character encoding** of a text file or a byte string.

## Prerequisites

- Python 3.6 or higher

## Features

- [Missing data treatment](https://github.com/Aryan-Bajaj/DataDoctor/tree/main#--treatment-of-missing-data)
- [Duplicate records treatment](https://github.com/Aryan-Bajaj/DataDoctor/tree/main#--treatment-of-duplicate-records)
- [Inconsistent data formats treatment](https://github.com/Aryan-Bajaj/DataDoctor/tree/main#--treatment-of-inconsistent-data-formats)
- [Inaccurate data entries treatment](https://github.com/Aryan-Bajaj/DataDoctor/tree/main#--treatment-of-inaccurate-data-entries)
- [Outliers treatment](https://github.com/Aryan-Bajaj/DataDoctor/tree/main#--treatment-of-outliers)
- [Inconsistent naming conventions treatment](https://github.com/Aryan-Bajaj/DataDoctor/tree/main#--treatment-of-inconsistent-naming-conventions)
- [Data entry errors treatment](https://github.com/Aryan-Bajaj/DataDoctor/tree/main#--treatment-of-data-entry-errors)
- [Inconsistent units of measurement treatment](https://github.com/Aryan-Bajaj/DataDoctor/tree/main#--treatment-of-inconsistent-units-of-measurement)
- [Incorrect data types treatment](https://github.com/Aryan-Bajaj/DataDoctor/tree/main#--treatment-of-incorrect-data-types)
- [Invalid values treatment](https://github.com/Aryan-Bajaj/DataDoctor/tree/main#--treatment-of-invalid-values)
- [Inconsistent or conflicting values treatment](https://github.com/Aryan-Bajaj/DataDoctor/tree/main#--treatment-of-inconsistent-or-conflicting-values)
- [Encoding errors treatment](https://github.com/Aryan-Bajaj/DataDoctor/tree/main#--treatment-of-encoding-errors)
- [Inconsistent date and time formats treatment](https://github.com/Aryan-Bajaj/DataDoctor/tree/main#--treatment-of-inconsistent-date-and-time-formats)
- [Inconsistent variable names treatment](https://github.com/Aryan-Bajaj/DataDoctor/tree/main#--treatment-of-inconsistent-variable-names)
- [Inconsistent capitalization or punctuation treatment](https://github.com/Aryan-Bajaj/DataDoctor/tree/main#--treatment-of-inconsistent-capitalization-or-punctuation)
- [Spelling or typographical errors treatment](https://github.com/Aryan-Bajaj/DataDoctor/tree/main#--treatment-of-spelling-or-typographical-errors)
- [Report Generation](https://github.com/Aryan-Bajaj/DataDoctor/tree/main#generate-a-report)

## Getting Started

Follow the below instructions to get started with `DataDoctor()`.

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

## Codes & Explanations

The `DataDoctor()` class provides a variety of methods for treating common data issues. These methods include:

1. [`treat_missing_data()`](https://github.com/Aryan-Bajaj/DataDoctor/tree/main#--treatment-of-missing-data): treats missing data in the loaded dataset by applying an imputation technique based on the data type of each column.
2. [`treat_duplicate_records()`](https://github.com/Aryan-Bajaj/DataDoctor/tree/main#--treatment-of-duplicate-records): treats duplicate records in the loaded dataset by removing them.
3. [`treat_inconsistent_data_formats()`](https://github.com/Aryan-Bajaj/DataDoctor/tree/main#--treatment-of-inconsistent-data-formats): treats inconsistent data formats in the loaded data by converting all values in string columns to lowercase.
4. [`treat_inaccurate_data_entries()`](https://github.com/Aryan-Bajaj/DataDoctor/tree/main#--treatment-of-inaccurate-data-entries): treats inaccurate data entries in string columns of the loaded data by replacing them with the most frequent value in the column.
5. [`treat_outliers()`](https://github.com/Aryan-Bajaj/DataDoctor/tree/main#--treatment-of-outliers): treats outliers in numerical columns of the loaded data by removing them using the Isolation Forest algorithm.
6. [`treat_inconsistent_naming_conventions()`](https://github.com/Aryan-Bajaj/DataDoctor/tree/main#--treatment-of-inconsistent-naming-conventions): treats inconsistent naming conventions in the loaded data by converting all column names to lowercase.
7. [`treat_data_entry_errors()`](https://github.com/Aryan-Bajaj/DataDoctor/tree/main#--treatment-of-data-entry-errors): treats data entry errors in string columns of the loaded data by replacing incorrect or similar-but-incorrect entries with the most similar valid value.
8. [`treat_inconsistent_units_of_measurement()`](https://github.com/Aryan-Bajaj/DataDoctor/tree/main#--treatment-of-inconsistent-units-of-measurement): treats inconsistent units of measurement in numerical columns of the loaded data by converting the values to a consistent unit of measurement.
9. [`treat_incorrect_data_types()`](https://github.com/Aryan-Bajaj/DataDoctor/tree/main#--treatment-of-incorrect-data-types): treats incorrect data types in the loaded data by converting string columns that should contain numeric data to their appropriate numeric data type.
10. [`treat_invalid_values()`](https://github.com/Aryan-Bajaj/DataDoctor/tree/main#--treatment-of-invalid-values): treats invalid values in numerical columns of a dataset by replacing them with np.nan (a missing value indicator).
11. [`treat_inconsistent_or_conflicting_values()`](https://github.com/Aryan-Bajaj/DataDoctor/tree/main#--treatment-of-inconsistent-or-conflicting-values): treats inconsistent or conflicting values in string columns of the loaded data by resolving cases where there are conflicting values within the same entry or inconsistent values across different entries in a column.
12. [`treat_encoding_errors()`](https://github.com/Aryan-Bajaj/DataDoctor/tree/main#--treatment-of-encoding-errors): treats encoding errors in string columns of the loaded dataset by determining the encoding of each string column and then decoding the values using the detected encoding.
13. [`treat_inconsistent_date_and_time_formats()`](https://github.com/Aryan-Bajaj/DataDoctor/tree/main#--treatment-of-inconsistent-date-and-time-formats): treats inconsistent date and time formats in string columns of a dataset by converting the values to a consistent date and time format.
14. [`treat_inconsistent_variable_names()`](https://github.com/Aryan-Bajaj/DataDoctor/tree/main#--treatment-of-inconsistent-variable-names): treats inconsistent variable names in the loaded data by replacing non-word characters with underscores and converting them to lowercase.
15. [`treat_inconsistent_capitalization_or_punctuation()`](https://github.com/Aryan-Bajaj/DataDoctor/tree/main#--treatment-of-inconsistent-capitalization-or-punctuation): treats inconsistent capitalization or punctuation in column names within the loaded dataset by replacing non-word characters with underscores and converting them to lowercase.
16. [`treat_spelling_or_typographical_errors()`](https://github.com/Aryan-Bajaj/DataDoctor/tree/main#--treatment-of-spelling-or-typographical-errors): treats spelling or typographical errors in string columns of the loaded data by replacing incorrect or misspelled values with the most similar valid value from a given set of valid names.
17. [`generate_report()`](https://github.com/Aryan-Bajaj/DataDoctor/tree/main#generate-a-report): It generates a report that provides information about the data treatment steps performed on the loaded data. It gives an overview of the issues addressed and the changes made to the data.

Each method has its own advantages and benefits in improving data quality and consistency. The `DataDoctor` class offers a comprehensive toolkit for data treatment and cleaning.

### - Loading the Data into the `DataDoctor()` Class:

The `load_data()` method is a part of the DataDoctor class. It is used to load data into the `DataDoctor()` object. Here's an overview of its meaning, advantages, and why you would use it:

The `load_data()` method allows you to provide data to the `DataDoctor()` object for further data treatment and analysis. It initialises the dataframe attribute of the `DataDoctor()` object with the provided data.

The below code helps you to perform the above-explained function:
```
doctor.load_data(data)
```

Advantages:

- Seamless Integration - The load_data method seamlessly integrates with the other methods in the `DataDoctor()` class, allowing you to perform a variety of data treatments and analyses on the loaded data.
- Flexibility - You can load data from various sources such as files, databases, or in-memory data structures, enabling you to work with data from different contexts.
- Efficiency - By loading data into the DataDoctor object, you can perform multiple data treatments and analyses without the need for repetitive data loading or passing the data to individual manual methods.

### - Treatment of Missing Data:

The `treat_missing_data()` method is used to treat missing data in the loaded dataset. It handles missing values by applying an imputation technique based on the data type of each column. For numerical columns, it uses the IterativeImputer class to estimate missing values based on other features. For non-numerical columns, it uses the SimpleImputer class with the 'most_frequent' strategy to replace missing values with the most frequent value in the column.

The below code helps you to perform the above-explained function:
```
doctor.treat_missing_data()
```

Advantages:

- Completing missing data - Missing data can be problematic for data analysis and modelling. By treating missing data, you can ensure that your dataset is complete and ready for further analysis.
- Retaining valuable information - The imputation techniques used in this method estimate missing values based on the available data, allowing you to retain valuable information that would have been lost if you simply removed rows with missing values.
- Preserving the structure of the dataset - By replacing missing values with estimated values, the overall structure of the dataset is maintained, which can be crucial for maintaining relationships between variables.

Why use this feature from `DataDoctor()`:

- Ensure data completeness - Missing data can introduce bias and affect the accuracy of your analysis. This method helps handle missing values and ensures your dataset is complete.
- Maintain data integrity - Instead of discarding rows with missing values, treating missing data allows you to retain the maximum amount of information from your dataset, improving the accuracy of your analysis.
- Prepare data for further analysis - By imputing missing values, you can create a more robust dataset that is suitable for various analysis tasks such as machine learning, statistical modelling, or exploratory data analysis.

### - Treatment of Duplicate Records:

The `treat_duplicate_records()` method is part of the `DataDoctor()` class and is used to treat duplicate records in the loaded dataset. Duplicate records refer to dataset rows with identical values across all columns. These duplicates can occur due to various reasons such as data entry errors, system issues, or merging datasets.

The below code helps you to perform the above-explained function:
```
doctor.treat_duplicate_records()
```

Advantages:

- Data Quality Improvement - Duplicate records can introduce bias and inaccuracies in data analysis and modeling. By removing duplicate records, the data quality is improved, leading to more reliable and accurate results.
= Data Consistency - Duplicate records can cause inconsistencies in the dataset, affecting the integrity and coherence of the data. By treating duplicate records, the dataset becomes more consistent and suitable for analysis.
- Efficient Data Analysis - Duplicate records can skew statistical measures, affect aggregations, and unnecessarily increase the computational load. Removing duplicates ensures that data analysis is based on the correct and representative data points, leading to more efficient and meaningful results.
- Error Identification - The number of duplicate records treated is reported, providing valuable insights into the quality of the dataset. This information can help identify potential issues in data collection, integration, or storage processes.

Why use this feature from `DataDoctor()`:

The `treat_duplicate_records()` method from `DataDoctor()` provides a convenient and automated way to handle duplicate records in a dataset. It saves time and effort compared to manually identifying and removing duplicates. By using this feature, you can ensure data quality, consistency, and accuracy, leading to more reliable analysis and decision-making based on clean and unique data.

Note: It's important to consider the context and nature of the dataset before applying this method. In some cases, duplicate records may be intentional and hold important information. Therefore, it's recommended to review the data and consult domain experts if necessary before treating duplicates.

### - Treatment of Inconsistent Data Formats:

This method is part of the `DataDoctor()` class and is used to treat inconsistent data formats in the loaded data. It performs the following operations:

- It iterates over each column in the data.
- If the column's data type is an object (string), it converts all values in that column to lowercase using the `str.lower()` method. This ensures consistent capitalisation for all string values within the column.
- The method adds a report entry indicating that inconsistent data formats have been treated.

Inconsistent data formats can pose challenges when working with data analysis and processing tasks. Inconsistent capitalization within string values can lead to difficulties in searching, grouping, and analyzing data. By applying the `treat_inconsistent_data_formats()` method, you can achieve a consistent format for all string values within the dataset by converting them to lowercase. This enhances data consistency, simplifies data manipulation, and enables accurate comparison and analysis of string values.

The below code helps you to perform the above explained function:
```
doctor.treat_inconsistent_data_formats()
```

Advantages and Benefits:

- Consistency - This method ensures a consistent data format for all string values within the dataset by converting them to lowercase. It helps avoid inconsistencies caused by variations in capitalization, leading to improved data quality and reliability.
- Ease of Comparison - Having consistent data formats simplifies comparison operations on string values. With all values converted to lowercase, you can perform case-insensitive comparisons and operations, allowing for more accurate and efficient data analysis.
- Data Manipulation - The consistent formatting provided by this method simplifies data manipulation tasks. You can easily filter, group, aggregate, and transform string values, knowing that they adhere to a standardised format.
- Enhanced Data Understanding - By normalising the data formats, it becomes easier to understand and interpret the dataset. Inconsistent capitalisation can make it challenging to identify unique values or detect patterns, but with a consistent format, you can gain clearer insights from the data.
- Compatibility - The consistent data format achieved through this method ensures compatibility with other data processing operations and algorithms. It eliminates potential issues caused by variations in capitalisation when integrating or merging datasets.

Why use This Feature from `DataDoctor()`:

The `treat_inconsistent_data_formats()` method is a valuable feature provided by the `DataDoctor()` class. Using this feature, you can easily address inconsistent capitalisation within string values, improving data quality, consistency, and ease of analysis. It helps you overcome common challenges associated with inconsistent data formats and ensures compatibility with various data processing tasks. Incorporating this feature as part of your data treatment workflow can significantly enhance the reliability and usability of your dataset.

 ### - Treatment of Inaccurate Data Entries:

This method is part of the DataDoctor class and is used to treat inaccurate data entries in string columns of the loaded data. It identifies valid values for each string column and replaces any entries that do not match the valid values with np.nan.

Inaccurate data entries refer to values in a string column that does not correspond to valid or expected values. These can occur due to various reasons such as human error during data entry or inconsistencies in the data source. `The treat_inaccurate_data_entries()` method aims to address this issue by identifying inaccurate entries and replacing them with missing values (np.nan).

The below code helps you to perform the above-explained function:
```
doctor.treat_inaccurate_data_entries()
```

Advantages and Benefits:

- Data Accuracy - By treating inaccurate data entries, this method helps improve the accuracy and integrity of the dataset. It ensures that the values in string columns align with the expected valid values, reducing the presence of incorrect or erroneous entries.
- Consistency - The method promotes consistency in the dataset by enforcing valid values for string columns. It ensures that the data adheres to predefined rules or standards, making it easier to work with and reducing potential errors caused by inconsistent or conflicting values.
- Data Analysis and Modeling - By cleaning inaccurate data entries, the method enhances the quality of data used for analysis and modeling tasks. More accurate and reliable data leads to better insights, decision-making, and model performance.

Why use This Feature from `DataDoctor()`:

While the `treat_inaccurate_data_entries()` method is effective in treating inaccurate data entries, it relies on the assumption that there are predefined valid values for each string column. If valid values are not known or cannot be determined, alternative data treatment approaches may be necessary.

It's important to review the generated report after applying this method to identify the number of errors detected and the columns affected. This information helps in understanding the impact of the treatment and the quality of the dataset.

Example:

Suppose you have a dataset containing a "Gender" column with entries such as "M", "Male", "F", "Female", and some inaccurate entries like "Man" and "Fem". Calling `treat_inaccurate_data_entries()` on this dataset will identify these inaccurate entries and replace them with np.nan, resulting in a more consistent representation of gender information.

### - Treatment of Outliers:

The `treat_outliers()` method is a feature provided by the `DataDoctor()` class to treat outliers in numerical columns of the loaded data. Outliers are data points that significantly deviate from the normal range of values in a dataset and can distort the analysis or modelling process. This method utilises the Isolation Forest algorithm to detect and remove outliers from the data.

The below code helps you to perform the above-explained function:
```
doctor.treat_outliers()
```

Advantages:

- Improved Data Quality - Outliers can introduce biases and distort statistical measures. By treating outliers, the `treat_outliers()` method helps improve the data's quality and reliability, leading to more accurate analysis and modelling.
- Enhanced Data Understanding - Outliers often represent data points that are unusual or unexpected. By identifying and removing outliers, you gain a deeper understanding of the central tendencies and patterns within the dataset, allowing for better insights and decision-making.
- Robust Modelling - Outliers can significantly impact statistical models, leading to poor model performance or biased results. By treating outliers, the `treat_outliers()` method helps in building more robust and reliable models that generalise well to unseen data.
- Preservation of Data Distribution - The Isolation Forest algorithm used in this method is effective at identifying outliers while preserving the underlying distribution of the data. This ensures that the data structure and patterns remain intact after outlier treatment.

Why use this Feature from `DataDoctor()`:

The `treat_outliers()` method provides a convenient way to handle outliers within numerical columns of a dataset. Outliers can be detrimental to the accuracy and reliability of data analysis and modelling tasks. By using this feature from `DataDoctor()`, you can easily detect and remove outliers, ensuring that your data is clean, representative, and suitable for further analysis or modelling purposes. The method's integration within the `DataDoctor()` class allows for a comprehensive and systematic treatment of various data issues, providing a streamlined workflow for data preprocessing and quality improvement.

### - Treatment of Inconsistent Naming Conventions:

This method is a part of the `DataDoctor()` class and is used to treat inconsistent naming conventions in the loaded dataset. It ensures that all column names are in a consistent format by converting them to lowercase.

Inconsistent naming conventions refer to variations in the capitalisation or formatting of column names within the dataset. For example, some column names may be written in uppercase, some in lowercase, and some may contain special characters or spaces. Such inconsistencies can make it difficult to work with the data and can lead to errors in data analysis and processing.

The `treat_inconsistent_naming_conventions()` method addresses this issue by standardising the column names to a consistent format, which converts them to lowercase. This ensures uniformity and makes referring to and manipulating the columns in subsequent data operations easier.

The below code helps you to perform the above-explained function:
```
doctor.treat_inconsistent_naming_conventions()
```

Advantages:

- Consistency - Standardising the column names to a consistent format improves the overall consistency of the dataset. It eliminates confusion caused by different capitalisations or formatting variations, allowing for easier interpretation and analysis of the data.
- Ease of Access - Using lowercase column names simplifies accessing and referencing columns in the dataset. It reduces the chances of typos or case-sensitive errors when querying or manipulating the data.
- Compatibility - Standardised column names enhance compatibility with other software tools and programming languages. Many programming languages and libraries prefer lowercase naming conventions, so converting column names to lowercase increases interoperability.
- Code Readability - Lowercase column names tend to be more readable in code and improve code clarity. Consistent naming conventions make it easier for other programmers or team members to understand and collaborate on the codebase.

Why use this feature from `DataDoctor()`:

The `treat_inconsistent_naming_conventions()` feature from DataDoctor is beneficial in data preprocessing and data cleaning tasks. By applying this method, you can ensure that your dataset has consistent and standardised column names, which is essential for maintaining data quality and enabling smooth data analysis and manipulation.

Using this feature helps to eliminate potential naming-related issues, reduces the likelihood of errors caused by inconsistent naming conventions, and enhances the overall quality and usability of the dataset. It promotes good data hygiene practices and prepares the dataset for further analysis, modelling, or integration with other data systems.

### - Treatment of Data Entry Errors:

The `treat_data_entry_errors()` method is a feature provided by the `DataDoctor()` class that helps in treating data entry errors in string columns of a given dataset. This method is designed to identify and correct inaccurate or misspelled entries in the data.

Data entry errors can occur when human input or data collection processes result in inconsistencies or inaccuracies in the recorded data. Such errors can include misspellings, typos, or variations in naming conventions. The `treat_data_entry_errors()` method aims to identify and rectify these errors by comparing the entries with a set of valid values and replacing incorrect or similar-but-incorrect entries with the most similar valid value.

The below code helps you to perform the above-explained function:
```
doctor.treat_data_entry_errors()
```

Advantages:

The treat_data_entry_errors() method offers several advantages in the data treatment process:
- Error Detection - The method can identify inaccurate or misspelled entries by comparing data entries with a set of valid values.
- Data Consistency - By replacing incorrect or similar-but-incorrect entries with the most similar valid value, the method improves the consistency and accuracy of the data.
- Automated Correction - The method leverages the fuzzy matching algorithm to automatically correct data entry errors without manual intervention, saving time and effort in the data treatment process.
- Flexible Application - The method is designed to work specifically with string columns, making it suitable for datasets that involve textual data or categorical variables.
- Customizability - The method can be easily customised or extended to incorporate domain-specific valid values or specific data entry error patterns.

Why use this feature from `DataDoctor()`:

The `treat_data_entry_errors()` feature from `DataDoctor()` is beneficial in scenarios where the dataset contains string columns with potential data entry errors. By utilising this feature, you can:

- Improve Data Quality - By automatically correcting inaccurate or misspelled entries, the feature enhances the overall quality and integrity of the dataset.

- Increase Data Consistency - Inconsistencies in data entries can hinder analysis and modelling tasks. The feature helps to standardise and harmonise the data by replacing incorrect entries with the most similar valid values.

- Save Manual Effort - Correcting data entry errors manually can be time-consuming and error-prone. The feature automates the error correction process, reducing the need for manual intervention and saving valuable time and effort.

- Enhance Data Analysis - Accurate and consistent data allows for more reliable analysis, modelling, and decision-making. By using the `treat_data_entry_errors()` feature, you can ensure the reliability of the data and derive more accurate insights from the dataset.

### - Treatment of Inconsistent Units Of Measurement:

This method is part of the `DataDoctor()` class and is used to treat inconsistent units of measurement in numerical columns of the loaded data. It performs a conversion of the values in the numerical columns to a consistent unit of measurement.

In many datasets, numerical columns may contain values measured in different units, leading to inconsistencies and hindering accurate analysis or modelling. The `treat_inconsistent_units_of_measurement()` method addresses this issue by applying a conversion factor to the numerical values, ensuring that they are consistent and comparable.

The below code helps you to perform the above-explained function:
```
doctor.treat_inconsistent_units_of_measurement()
```

Advantage:

Treating inconsistent units of measurement is important because it brings uniformity to the data, allowing for meaningful comparisons and analysis. By applying a conversion factor, this method ensures that all numerical values in the dataset are expressed in a single unit, making it easier to interpret and analyse the data.

Why use this feature from `DataDoctor()`:

Using the `treat_inconsistent_units_of_measurement()` feature from the `DataDoctor()` class provides several benefits:

- Data Consistency - Inconsistent units of measurement can introduce errors and inconsistencies in the dataset. This feature helps maintain data consistency by converting all numerical values to a standardized unit.
- Comparability - By converting all numerical values to a consistent unit, this feature enables proper comparison and analysis of the data. It ensures that the values are on the same scale, allowing for meaningful insights and conclusions.
- Simplified Analysis - When the dataset contains values measured in different units, it becomes challenging to perform calculations or statistical operations accurately. By treating inconsistent units, this feature simplifies data analysis tasks by ensuring that all values are in the same unit.
- Ease of Interpretation - Inconsistent units of measurement can make it difficult to interpret the data correctly. By converting values to a common unit, this feature enhances the interpretability of the dataset, making it easier to understand and draw insights from.

### - Treatment of Incorrect Data Types:

The `treat_incorrect_data_types()` method in the `DataDoctor()` class is used to treat incorrect data types in the loaded data. It is designed to handle situations where columns that should contain numeric data are mistakenly encoded as string data. By identifying such columns and converting their values to numeric data, this method helps ensure the data is in the appropriate format for further analysis or processing.

Incorrect data types can occur due to various reasons, such as data entry errors or formatting issues during data collection. When numeric values are stored as strings, it can lead to incorrect calculations, inaccurate analysis, or unexpected errors in subsequent data operations. The t`reat_incorrect_data_types()` method helps resolve these issues by attempting to convert string columns to their appropriate numeric data type.

The below code helps you to perform the above-explained function:
```
doctor.treat_incorrect_data_types()
```

Advantages:

- Consistency and Accuracy - By converting columns with numeric data from string to numeric data types, the method promotes data consistency and accuracy throughout the dataset. It ensures that the data is correctly interpreted and processed for numerical operations, statistical analysis, or machine learning tasks.
- Preventing Errors - Treating incorrect data types helps prevent potential errors that may arise from using inappropriate data types. It reduces the risk of unexpected behaviour or inconsistencies when performing calculations or applying mathematical operations on the data.
- Simplified Data Handling - By correctly assigning the appropriate data types, it simplifies data handling and facilitates downstream operations. It allows for seamless integration with libraries and algorithms that expect specific data types, enhancing compatibility and ease of use.

Why use this feature from `DataDoctor()`:

The treat_incorrect_data_types() feature from DataDoctor offers an automated and systematic approach to address the issue of incorrect data types in a dataset. By utilising this feature, you can benefit from the following:

- Efficiency - The method handles the conversion of data types in a single step, avoiding the need for manual data type identification and conversion.
- Scalability - It can be applied to datasets of varying sizes, accommodating both small and large-scale data processing requirements.
- Consistency across Columns - The method operates across all columns, consistently identifying and converting inappropriate data types throughout the dataset. This ensures uniformity and avoids inconsistencies in data types across different columns.
- Integration with Data Treatment Workflow - The treat_incorrect_data_types() method is part of the broader set of data treatment functionalities provided by the DataDoctor class. It can be seamlessly integrated into your data preprocessing pipeline alongside other data treatment methods, enabling comprehensive and systematic data cleaning and preparation.

### - Treatment of Invalid Values:

The `treat_invalid_values(`) method is a feature the `DataDoctor()` class provides in the code. This method is used to treat invalid values in numerical columns of a dataset. 

The method `treat_invalid_values()` addresses the issue of invalid values present in numerical columns of the dataset. Invalid values are values that fall outside the expected range or are not meaningful in the context of the data. These values can be problematic as they can introduce errors and inconsistencies in the analysis or modelling process. This method aims to identify and handle such invalid values effectively.

The below code helps you to perform the above-explained function:
```
doctor.treat_invalid_values()
```

Advantages:

- Data Integrity - By treating invalid values, the method helps improve the dataset's integrity by removing or replacing values that are outside the expected range. This ensures that the data used for analysis or modelling is reliable and accurate.
- Improved Analysis - Handling invalid values allows for more meaningful and accurate analysis. By replacing invalid values with np.nan (a missing value indicator), the method ensures that these values do not skew statistical calculations or produce misleading results.
- Data Consistency - Treating invalid values helps maintain dataset consistency. By identifying and addressing outliers or values that don't adhere to the data's expected range, the method contributes to a more consistent and reliable dataset.
- Preprocessing for Machine Learning - Invalid values can be problematic when training machine learning models. By treating these values, the method prepares the data for machine learning algorithms, ensuring that the models receive valid input and preventing potential errors during the training or prediction phase.

Why use this feature from `DataDoctor()`:

The `treat_invalid_values()` feature from the `DataDoctor()` class offers a convenient and reliable way to handle invalid values in numerical columns. By utilising this feature, you can:

- Improve the quality and reliability of your data by identifying and addressing invalid values.
- Ensure that your analysis or modelling results are not influenced by outliers or values that don't conform to the expected range.
- Prepare your data for machine learning tasks by treating invalid values that can hinder the performance of your models.

### - Treatment of Inconsistent or Conflicting Values:

The `treat_inconsistent_or_conflicting_values()` method is a part of the `DataDoctor()` class and is used to treat inconsistent or conflicting values in string columns of the loaded data. It identifies and resolves cases where there are conflicting values within the same entry or inconsistent values across different entries in a column.

The below code helps you to perform the above-explained function:
```
doctor.treat_inconsistent_or_conflicting_values()
```

Advantage:

- Ensures data consistency - Inconsistent or conflicting values in a column can lead to data quality issues and inconsistencies. This method ensures that values within a column are consistent and free from conflicts, providing more reliable and accurate data.
- Improved data analysis - Consistent values enable better analysis and interpretation of the data. You can avoid skewed insights or incorrect conclusions based on conflicting values by resolving inconsistencies.
- Enhanced data integration - When merging or integrating data from different sources, inconsistent or conflicting values can cause challenges. This method helps align values across different entries, making the integration process smoother and more reliable.

Why use this feature from `DataDoctor()`:

- Inconsistent or conflicting values in string columns are common data quality issues that can affect data analysis, modelling, and decision-making processes. This feature from DataDoctor provides an automated way to address and resolve such issues, saving significant time and effort compared to manual data cleaning.
- The method intelligently identifies and resolves inconsistencies or conflicts in values by extracting the first part of each entry and discarding the rest, which is helpful when dealing with data where inconsistent or conflicting values might appear due to different formats or interpretations.
- This feature ensures that your data is clean, standardised, and ready for further analysis or processing, leading to more accurate and reliable results.

### - Treatment of Encoding Errors:

The `treat_encoding_errors()` method in the `DataDoctor()` class is designed to handle encoding errors in string columns of the loaded dataset. Encoding errors can occur when the encoding of the data does not match the expected encoding, leading to decoding issues and incorrect representation of characters.

The `treat_encoding_errors()` method detects and addresses encoding errors by attempting to determine the encoding of each string column and then decoding the values using the detected encoding. This method ensures that the data is properly decoded and represented by fixing encoding errors, preventing issues such as garbled text or incorrect characters.

The below code helps you to perform the above-explained function:
```
doctor.treat_encoding_errors()
```

Advantage:

The `treat_encoding_errors()` method offers several advantages:

- Data Consistency - Encoding errors can introduce inconsistencies and inaccuracies in the data. By treating encoding errors, this method helps ensure data consistency and reliability.
- Proper Analysis - Correctly decoding the data is crucial for performing accurate analysis and extracting meaningful insights. Treating encoding errors allows for proper analysis and interpretation of the data.
- Enhanced Data Quality - Fixing encoding errors improves the overall quality of the dataset by eliminating data artifacts caused by incorrect encoding.

Why use this feature from `DataDoctor()`:

Using the `treat_encoding_errors()` feature from `DataDoctor()` is beneficial in scenarios where you encounter encoding errors in your dataset. By employing this feature, you can address and fix encoding issues, resulting in clean, correctly encoded data that is ready for further analysis or processing.

### - Treatment of Inconsistent Date and Time Formats:

The `treat_inconsistent_date_and_time_formats()` method is a feature provided by the `DataDoctor()` class from the `data_doctor` module. It is designed to address inconsistent date and time formats in string columns of a dataset. This method performs data treatment by attempting to convert the values in these columns to a consistent date and time format.

In datasets that contain date and time information, it is common to encounter variations in the format of these values. This inconsistency can arise due to differences in data entry practices or data sources. The `treat_inconsistent_date_and_time_formats()` method aims to standardize the date and time formats across the dataset, ensuring consistency and facilitating data analysis and processing.

The below code helps you to perform the above explained function:
```
doctor.treat_inconsistent_date_and_time_formats()
```

Advantages:

The advantages of using the `treat_inconsistent_date_and_time_formats()` method include:

- Consistency - By converting all date and time values to a consistent format, this method ensures that the dataset has uniformity in representing dates and times. This simplifies data manipulation and analysis tasks.
- Data Integrity - Inconsistent date and time formats can introduce errors and inaccuracies in the dataset. The method improves data integrity and reliability by treating these inconsistencies, reducing the risk of incorrect analyses or interpretations.
- Compatibility - Many data analysis and visualisation tools expect date and time values to be in specific formats. By standardising the formats, the treated dataset becomes more compatible with a wide range of tools and libraries, making it easier to perform further analysis or visualisation tasks.

Why use this feature from `DataDoctor()`:

The `DataDoctor()` class and its associated methods, including `treat_inconsistent_date_and_time_formats()`, provide a comprehensive data treatment and cleaning toolkit. By using this feature, you can address inconsistencies in date and time formats in a dataset, ensuring data quality and preparing the dataset for downstream analysis. This method eliminates the need for manual and error-prone data formatting, as it automates the process of converting inconsistent date and time values to a standardised format.

By utilizing the `treat_inconsistent_date_and_time_formats()` method from `DataDoctor()`, you can save time and effort in preprocessing and cleansing your data, allowing you to focus more on extracting meaningful insights and making informed decisions based on the treated dataset.

### - Treatment of Inconsistent Variable Names:

The `treat_inconsistent_variable_names()` method is a feature provided by the `DataDoctor()` class. It is used to treat inconsistent variable names in the loaded data. This method ensures that variable names are consistent, following a specific format, by replacing non-word characters with underscores and converting them to lowercase.

Inconsistent variable names refer to the situation where the names of variables (columns) in a dataset have different capitalisations, contain special characters, or have inconsistent word separators. For example, a dataset may have variables named "Age", "gender", and "Income(in USD)". Inconsistent variable names can make data analysis and modelling tasks more challenging and error-prone. The `treat_inconsistent_variable_names()` method aims to standardise and clean up the variable names to improve data consistency and ease further data processing.

The below code helps you to perform the above-explained function:
```
doctor.treat_inconsistent_variable_names()
```

Advantages:

- Consistency - The method helps in maintaining consistency by standardising the variable names. It ensures that variables follow a specific naming convention, reducing ambiguity and improving understanding.
- Readability - By converting variable names to lowercase and replacing non-word characters with underscores, the method improves the readability of the dataset. Uniform variable names make it easier to identify and reference specific variables in the data.
- Data Analysis - Consistent variable names facilitate data analysis tasks such as filtering, sorting, and grouping. With standardized names, you can easily reference and manipulate variables, simplifying the analysis process.
- Compatibility - Many data analysis libraries and tools expect variables to follow specific naming conventions. By treating inconsistent variable names, you ensure compatibility with various analysis tools and frameworks, allowing seamless integration into data analysis workflows.

Why use this feature from `DataDoctor()`:

The `treat_inconsistent_variable_names()` feature provided by the `DataDoctor()` class offers several benefits for data preprocessing and analysis:

- Data Consistency - Inconsistent variable names can introduce inconsistencies and errors in data analysis workflows. By using this feature, you can ensure that all variable names follow a standardized format, reducing potential confusion and improving the overall quality and consistency of the data.
- Easier Data Exploration - Consistent variable names make it easier to explore and understand the dataset. With standardized names, you can quickly identify and refer to specific variables, facilitating data exploration, visualization, and querying tasks.
- Simplified Data Integration - When working with multiple datasets or merging data from different sources, having consistent variable names is crucial. This feature helps harmonize variable names across datasets, enabling seamless data integration and reducing the need for manual data transformations.
- Enhanced Model Development - In machine learning and statistical modeling, standardized variable names can improve the interpretability and reproducibility of models. Clear and consistent variable names contribute to better feature selection, model building, and model evaluation processes.

### - Treatment of Inconsistent Capitalization or Punctuation:

The `treat_inconsistent_capitalization_or_punctuation()` method is a part of the `DataDoctor()` class in the `data_doctor module`. This method is designed to treat inconsistent capitalisation or punctuation in column names within the loaded dataset.

Inconsistent capitalisation or punctuation in column names refers to situations where column names are not consistently formatted in terms of capitalisation (e.g., a mix of uppercase and lowercase letters) or punctuation (e.g., inconsistent use of underscores or hyphens). Inconsistent formatting can make it difficult to work with the dataset and can lead to errors when performing data analysis or modelling tasks.

The below code helps you to perform the above-explained function:
```
doctor.treat_inconsistent_capitalization_or_punctuation()
```

Advantages:

Treating inconsistent capitalisation or punctuation in column names has several advantages:

- Standardisation - By applying consistent capitalisation rules and punctuation conventions to column names, the dataset becomes more standardised and easier to understand.
- Improved Readability - Consistent capitalisation and punctuation make column names more readable and intuitive, leading to a better comprehension of the dataset's structure.
- Compatibility - Standardised column names are more compatible with various data analysis and modelling tools, as they often rely on standardised naming conventions.
- Data Integrity - Correcting inconsistent capitalisation or punctuation reduces the risk of creating duplicate columns or referencing the wrong column during data processing.

Why use this feature from `DataDoctor()`:

The `treat_inconsistent_capitalization_or_punctuation()` method provides an automated way to address inconsistent capitalisation or punctuation in column names. By using this feature, you can ensure that your dataset's column names adhere to consistent formatting standards, improving data quality and facilitating further data analysis and modelling tasks.

Example Result:

Suppose we have a dataset with the following inconsistent column names:

- "Name"
- "AGE"
- "City_Of_Origin"
- "income"
- "No_of_Children"

After applying the `treat_inconsistent_capitalization_or_punctuation()` method, the column names would be standardised to:

- "Name"
- "Age"
- "City_Of_Origin"
- "Income"
- "No_Of_Children"

This standardisation helps create a more consistent and readable dataset, making it easier to work with the data and avoid potential issues due to inconsistent naming conventions.

### - Treatment of Spelling or Typographical Errors:

The `treat_spelling_or_typographical_errors()` method in the `DataDoctor()` class is designed to address spelling or typographical errors in string columns of the loaded data. It applies a correction mechanism to replace incorrect or misspelled values with the most similar valid value from a given set of valid names.

Spelling or typographical errors in data can lead to inconsistencies and inaccuracies in analysis and modelling tasks. This method helps to standardise the values in string columns by identifying and replacing incorrect or misspelled entries with the most similar valid value. By correcting these errors, the method improves the quality and reliability of the data.

The below code helps you to perform the above-explained function:
```
doctor.treat_spelling_or_typographical_errors()
```

Advantages:

- Data Consistency - The method ensures that similar values are represented uniformly, reducing variations due to spelling or typographical mistakes.
- Data Accuracy - By replacing incorrect or misspelled values with the most similar valid value, the method improves the accuracy of the data.
- Standardization - It helps to standardize the values in string columns, making them more consistent and facilitating data analysis and comparisons.

Why use this feature from `DataDoctor()`:

Using the `treat_spelling_or_typographical_errors()` feature from `DataDoctor()` can provide several benefits:

- Data Quality Improvement - By correcting spelling or typographical errors, the feature enhances the quality of the data, making it more reliable for further analysis and decision-making.
- Time-saving - Manually identifying and correcting spelling errors in large datasets can be time-consuming. This feature automates the process, saving time and effort.
- Increased Consistency - Standardising the values in string columns ensures consistency across the dataset, making it easier to merge, analyze, and visualize the data.
- Better Analysis and Insights - Correcting spelling errors improves the accuracy of the data, leading to more reliable analysis results and insights.
- Data Integration - When combining multiple datasets, the feature helps to align and match values by correcting misspelled entries, ensuring accurate data integration.

It is important to note that the correction mechanism used in this method relies on fuzzy matching algorithms to find the most similar valid value. While it can significantly improve the accuracy of data, manual review and verification may still be necessary in certain cases to ensure the correctness and relevance of the corrections.

Once the `treat_spelling_or_typographical_errors()` method is executed, it will process the loaded data, identify misspelled or incorrect values in string columns, and replace them with the most similar valid value. The changes will be applied to the dataframe attribute of the `DataDoctor()` object.

### Generate a report

The `generate_report()` method in the `DataDoctor()` class is used to generate a report summarizing the data treatment steps that have been applied to the loaded data. It prints the report to the console. Here's an explanation of this method:

The `generate_report()` method generates a report that provides information about the data treatment steps performed on the loaded data. It gives an overview of the issues addressed and the changes made to the data.

The below code helps you to perform the above-explained function:
```
doctor.generate_report()
```

Advantage:

The `generate_report()` method provides a concise summary of the data treatment process. It helps users understand the transformations applied to the data, identifies any issues or errors that were encountered, and provides transparency in the data treatment workflow. This report can be useful for auditing purposes, sharing information with stakeholders, or documenting the data treatment process.

Why to use this feature from `DataDoctor()`:

The `generate_report()` feature from the DataDoctor class is beneficial because it allows users to quickly obtain an overview of the data treatment steps that have been applied. It provides a comprehensive summary of the actions taken to clean and preprocess the data, making it easier to understand the transformations made and the resulting data quality improvements. This report can be used to communicate the data treatment process to other team members, ensure reproducibility, and track the progress of data cleaning efforts.

Results:

When you call the `generate_report()` method, it will print the data treatment report to the console. The report will contain a header indicating that it is the "Data Treatment Report," followed by a separator line. Each step of the data treatment process will be listed, along with relevant information and statistics about the treatment performed. 

The output will look similar to the following:
```
Data Treatment Report:
======================
Missing data treated for column 'Column1'. 10 errors detected.
Duplicate records treated. 5 duplicates removed.
Inconsistent data formats treated.
Inaccurate data entries treated for column 'Column2'. 3 errors detected.
Outliers treated.
```

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
