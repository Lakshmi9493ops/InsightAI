import pandas as pd


def strongest_correlations(df):

    numeric = df.select_dtypes(include="number")

    corr = numeric.corr()

    pairs = (
        corr.unstack()
        .reset_index()
    )

    pairs.columns = [
        "Column1",
        "Column2",
        "Correlation"
    ]

    pairs = pairs[
        pairs["Column1"] != pairs["Column2"]
    ]

    pairs["Correlation"] = pairs["Correlation"].abs()

    pairs = (
        pairs.sort_values(
            "Correlation",
            ascending=False
        )
        .drop_duplicates("Correlation")
        .head(10)
    )

    return pairs