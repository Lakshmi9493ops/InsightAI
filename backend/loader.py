import pandas as pd


def load_dataset(uploaded_file):
    """
    Load CSV or Excel dataset.
    """

    if uploaded_file.name.endswith(".csv"):
        return pd.read_csv(uploaded_file)

    return pd.read_excel(uploaded_file)