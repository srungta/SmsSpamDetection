from os import makedirs, path
import pandas as pd

def read_csv_from_file(filepath):
    data = pd.read_csv(filepath,encoding = 'utf8')
    return data

def write_to_csv(dataframe, filepath):
    dataframe.to_csv(filepath)

def ensure_path_exists(directory_path):
    if path.exists(directory_path):
        return
    makedirs(directory_path)
