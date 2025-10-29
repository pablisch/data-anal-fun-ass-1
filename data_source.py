import pandas as pd

def get_data_frame():
    df = pd.read_csv('data/customerChurnData.csv')
    return df