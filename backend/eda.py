import pandas as pd
import plotly.express as px

def numerical_summary(df):

    numeric_df = df.select_dtypes(include="number")

    return numeric_df.describe().T

def correlation_heatmap(df):

    numeric_df = df.select_dtypes(include="number")

    if numeric_df.shape[1] < 2:
        return None

    corr = numeric_df.corr()

    fig = px.imshow(
        corr,
        text_auto=".2f",
        color_continuous_scale="RdBu_r",
        title="Correlation Heatmap"
    )

    return fig
def histogram(df, column):

    import plotly.express as px

    fig = px.histogram(
        df,
        x=column,
        title=f"{column} Distribution"
    )

    return fig