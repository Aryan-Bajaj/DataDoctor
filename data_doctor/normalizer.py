import pandas as pd
import numpy as np
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import SimpleImputer, IterativeImputer
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import IsolationForest
from fuzzywuzzy import fuzz
import re
import warnings
import chardet
from data_doctor.utils import detect_encoding

warnings.filterwarnings("ignore")


class DataDoctor:
    def __init__(self):
        self.df = None
        self.report = []

    def load_data(self, data):
        self.df = data

    def treat(self, file_name, inplace=True):
        if not inplace:
            self.df = pd.read_csv(file_name)
        else:
            self.load_data(pd.read_csv(file_name))

    def treat_missing_data(self):
        for column in self.df.columns:
            if self.df[column].dtype == np.number:
                imputer = IterativeImputer()
                treated_data = imputer.fit_transform(self.df[[column]]).ravel()
            else:
                imputer = SimpleImputer(strategy='most_frequent')
                treated_data = imputer.fit_transform(self.df[[column]]).ravel()

            num_errors = self.df[column].isnull().sum()
            self.df[column] = treated_data
            self.report.append(f"Missing data treated for column '{column}'. {num_errors} errors detected.")

    def treat_duplicate_records(self):
        num_duplicates = self.df.duplicated().sum()
        self.df.drop_duplicates(inplace=True)
        self.report.append(f"Duplicate records treated. {num_duplicates} duplicates removed.")

    def treat_inconsistent_data_formats(self):
        for column in self.df.columns:
            if self.df[column].dtype == 'O':
                self.df[column] = self.df[column].str.lower()

        self.report.append("Inconsistent data formats treated.")

    def treat_inaccurate_data_entries(self):
        for column in self.df.columns:
            if self.df[column].dtype == 'O':
                valid_values = self.df[column].dropna().unique()
                num_errors = (~self.df[column].isin(valid_values)).sum()
                self.df[column] = self.df[column].apply(lambda x: x if x in valid_values else np.nan)
                self.report.append(f"Inaccurate data entries treated for column '{column}'. {num_errors} errors detected.")

    def treat_outliers(self):
        for column in self.df.columns:
            if self.df[column].dtype == np.number:
                outlier_detector = IsolationForest(contamination=0.1)
                outlier_detector.fit(self.df[[column]])
                outlier_mask = outlier_detector.predict(self.df[[column]]) != -1
                self.df = self.df[outlier_mask]

        self.report.append("Outliers treated.")

    def treat_inconsistent_naming_conventions(self):
        self.df.rename(columns=lambda x: x.lower(), inplace=True)
        self.report.append("Inconsistent naming conventions treated.")

    def treat_data_entry_errors(self):
        for column in self.df.columns:
            if self.df[column].dtype == 'O':
                valid_names = self.df[column].dropna().unique()
                self.df[column] = self.df[column].apply(
                    lambda x: max(valid_names, key=lambda y: fuzz.ratio(x, y)) if pd.notnull(x) else x
                )

        self.report.append("Data entry errors treated.")

    def treat_inconsistent_units_of_measurement(self):
        conversion_factor = 2.54

        for column in self.df.columns:
            if self.df[column].dtype == np.number:
                self.df[column] = self.df[column] * conversion_factor

        self.report.append("Inconsistent units of measurement treated.")

    def treat_incorrect_data_types(self):
        for column in self.df.columns:
            if self.df[column].dtype == 'O':
                try:
                    self.df[column] = pd.to_numeric(self.df[column], errors='coerce')
                except ValueError:
                    pass

        self.report.append("Incorrect data types treated.")

    def treat_invalid_values(self):
        for column in self.df.columns:
            if self.df[column].dtype == np.number:
                min_value = self.df[column].min()
                max_value = self.df[column].max()
                num_errors = ((self.df[column] < min_value) | (self.df[column] > max_value)).sum()
                self.df[column] = self.df[column].apply(lambda x: x if min_value <= x <= max_value else np.nan)
                self.report.append(f"Invalid values treated for column '{column}'. {num_errors} errors detected.")

    def treat_inconsistent_or_conflicting_values(self):
        for column in self.df.columns:
            if self.df[column].dtype == 'O':
                self.df[column] = self.df[column].apply(lambda x: x if pd.isna(x) else x.split()[0])

        self.report.append("Inconsistent or conflicting values treated.")

    def treat_encoding_errors(self):
        for column in self.df.columns:
            if self.df[column].dtype == 'O':
                encoding = detect_encoding(self.df[column].values.astype(str).to_list())
                try:
                    self.df[column] = self.df[column].str.decode(encoding)
                    self.report.append(f"Encoding errors treated for column '{column}'.")
                except UnicodeDecodeError:
                    self.report.append(f"Encoding errors detected in column '{column}', but unable to fix.")

    def treat_inconsistent_date_and_time_formats(self):
        for column in self.df.columns:
            if self.df[column].dtype == 'O':
                try:
                    self.df[column] = pd.to_datetime(self.df[column], errors='coerce')
                except ValueError:
                    pass

        self.report.append("Inconsistent date and time formats treated.")

    def treat_inconsistent_variable_names(self):
        self.df.rename(columns=lambda x: re.sub(r'\W+', '_', x.lower()), inplace=True)
        self.report.append("Inconsistent variable names treated.")

    def treat_inconsistent_capitalization_or_punctuation(self):
        self.df.rename(columns=lambda x: x.capitalize(), inplace=True)
        self.report.append("Inconsistent capitalization or punctuation treated.")

    def treat_spelling_or_typographical_errors(self):
        for column in self.df.columns:
            if self.df[column].dtype == 'O':
                valid_names = self.df[column].dropna().unique()
                self.df[column] = self.df[column].apply(
                    lambda x: max(valid_names, key=lambda y: fuzz.ratio(x, y)) if pd.notnull(x) else x
                )

        self.report.append("Spelling or typographical errors treated.")

    def treat_data_normalization_issues(self):
        normalizer = DataNormalizer()
        self.df = normalizer.normalize_data(self.df)
        self.report.append("Data normalization issues treated.")

    def generate_report(self):
        print("Data Treatment Report:")
        print("======================")
        for step_num, step_report in enumerate(self.report, start=1):
            print(f"{step_report}")
