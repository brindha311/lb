import pandas as pd
import os
import shutil


def read_csv_file_to_dataframe(src_path):
    # Read CSV file into a DataFrame
    df = pd.read_csv(src_path, delimiter=";", header=0)
    return df



def move_file_after_processed(src_file_path,destination_file_path):
    # move csv file after processed
    shutil.move(src_file_path, destination_file_path)


def load_dataframe_to_csv(df,load_path):
    df.to_csv(load_path, index=False)

