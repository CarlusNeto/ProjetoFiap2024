import pandas as pd

def load_data(file_path):
    """
    Carrega os dados de um arquivo CSV.
    """
    return pd.read_csv(file_path)

def preprocess_data(df):
    """
    Realiza pré-processamento básico nos dados.
    """
    # Implementar lógica de pré-processamento aqui
    return df