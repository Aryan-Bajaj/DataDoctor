import pandas as pd
import numpy as np
import unittest
from data_doctor.normalizer import DataDoctor
from data_doctor.utils import detect_encoding

class TestDataDoctor(unittest.TestCase):

    def setUp(self):
        self.data_doctor = DataDoctor()

    def test_treat_missing_data(self):
        
        df = pd.DataFrame({'A': [1, 2, np.nan, 4, 5],
                           'B': [np.nan, 2, 3, np.nan, 5],
                           'C': [1, np.nan, 3, 4, 5]})
        self.data_doctor.load_data(df)

        self.data_doctor.treat_missing_data()

        
        expected_df = pd.DataFrame({'A': [1, 2, 3, 4, 5],
                                    'B': [2, 2, 3, 4, 5],
                                    'C': [1, 2, 3, 4, 5]})
        pd.testing.assert_frame_equal(self.data_doctor.df, expected_df)

    

if __name__ == '__main__':
    unittest.main()