import pandas as pd


def detect_sales_outliers(df):

    if "sales" not in df.columns:
        return pd.DataFrame()

    q1 = df["sales"].quantile(0.25)
    q3 = df["sales"].quantile(0.75)

    iqr = q3 - q1

    lower = q1 - 1.5 * iqr
    upper = q3 + 1.5 * iqr

    outliers = df[
        (df["sales"] < lower) |
        (df["sales"] > upper)
    ]

    return outliers