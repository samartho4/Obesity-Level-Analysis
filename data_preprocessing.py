
import pandas as pd

def import_data(file_path):
    data = pd.read_csv(file_path)
    return data

def clean_data(df):
    df = df.applymap(lambda x: x.strip("b'").strip("'") if isinstance(x, str) else x)
    df = df.drop_duplicates()
    df.fillna(method='ffill', inplace=True)
    return df
