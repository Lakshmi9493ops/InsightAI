import pandas as pd


def remove_duplicates(df):
    """
    Remove duplicate rows.
    """
    before = len(df)
    df = df.drop_duplicates()
    after = len(df)

    return df, before - after


def remove_missing_values(df):
    """
    Remove rows containing missing values.
    """
    before = len(df)
    df = df.dropna()
    after = len(df)

    return df, before - after


def fill_missing_values(df, method):
    """
    Fill missing values.
    """

    temp_df = df.copy()

    numeric_columns = temp_df.select_dtypes(include="number").columns

    if method == "Mean":

        for col in numeric_columns:
            temp_df[col] = temp_df[col].fillna(
                temp_df[col].mean()
            )

    elif method == "Median":

        for col in numeric_columns:
            temp_df[col] = temp_df[col].fillna(
                temp_df[col].median()
            )

    elif method == "Mode":

        for col in temp_df.columns:

            mode = temp_df[col].mode()

            if not mode.empty:
                temp_df[col] = temp_df[col].fillna(mode[0])

    return temp_df