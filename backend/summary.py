import pandas as pd


def dataset_summary(df):

    rows, columns = df.shape

    numeric_columns = len(df.select_dtypes(include="number").columns)

    text_columns = len(df.select_dtypes(include="object").columns)

    date_columns = len(df.select_dtypes(include="datetime").columns)

    return {
        "rows": rows,
        "columns": columns,
        "numeric": numeric_columns,
        "text": text_columns,
        "date": date_columns
    }