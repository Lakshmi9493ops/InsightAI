def remove_duplicates(df):
    """
    Remove duplicate rows.
    """
    duplicates = df.duplicated().sum()
    df = df.drop_duplicates()
    return df, duplicates


def remove_missing_values(df):
    """
    Remove rows containing missing values.
    """
    missing_rows = df.isnull().any(axis=1).sum()
    df = df.dropna()
    return df, missing_rows