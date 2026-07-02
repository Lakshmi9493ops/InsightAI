import pandas as pd


def remove_duplicates(df):
    """
    Remove duplicate rows from the dataset.
    Returns:
        cleaned_df, duplicates_removed
    """

    duplicates_before = df.duplicated().sum()

    cleaned_df = df.drop_duplicates()

    return cleaned_df, duplicates_before