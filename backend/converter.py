import pandas as pd


def convert_numeric(df, column):

    temp_df = df.copy()

    temp_df[column] = pd.to_numeric(
        temp_df[column],
        errors="coerce"
    )

    return temp_df