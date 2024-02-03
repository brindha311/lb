import logging

import pandas as pd
#To do :: add not null field check and other logic checks

# Validate data types and fix if needed
def schema_validation(df,expected_dtypes):
    for column, expected_type in expected_dtypes.items():
        actual_type = str(df.dtypes[column])
        if not actual_type.startswith(expected_type):
            # int in python wont accept null. So fillna with zero or not is to discussion
            if "int" not in expected_type :
                # maximum limit of datatime in pandas dataframe is 2262-04-11 as in the data 9999-12-31
               if "valid_until" not in column:
                    df[column] = df[column].astype(expected_type)
    return df

def duplicate_detection(df,tablename):
    if any(df.duplicated()):
        logging.info(f"dataframe to the table {tablename} has duplicates {df.duplicated().sum()}")
    df = df.drop_duplicates()
    return df