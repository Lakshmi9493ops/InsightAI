def dataset_report(df):

    report = {}

    report["Rows"] = len(df)

    report["Columns"] = len(df.columns)

    report["Missing"] = df.isnull().sum().sum()

    report["Duplicates"] = df.duplicated().sum()

    report["Memory"] = round(
        df.memory_usage().sum()/1024,
        2
    )

    return report