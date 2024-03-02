#  python function to read excel data
import pandas as pd

def get_assets_from_excel(filename : str)->list:

    df = pd.read_excel(filename)

    assets_list = df['Sigla'].tolist()

    return assets_list