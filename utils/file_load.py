import pandas
import re

def load_data_list(file_path):
    df = pandas.read_excel(file_path).head()
    return df.values.tolist()

def load_dict_list(file_path):
    df = pandas.read_excel(file_path).head()
    return df.to_dict(orient='records')