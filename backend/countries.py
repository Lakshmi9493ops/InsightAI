import pandas as pd
import plotly.express as px


def top_countries(df):

    if "country" not in df.columns:
        return None

    if "sales" not in df.columns:
        return None

    temp = df.copy()

    temp["sales"] = pd.to_numeric(
        temp["sales"],
        errors="coerce"
    )

    temp = temp.dropna(subset=["sales"])

    summary = (
        temp.groupby("country", as_index=False)["sales"]
        .sum()
        .sort_values("sales", ascending=False)
        .head(10)
    )

    fig = px.bar(
        summary,
        x="sales",
        y="country",
        orientation="h",
        color="sales",
        title="Top 10 Countries"
    )

    fig.update_layout(
        template="plotly_white",
        height=550,
        yaxis={"categoryorder":"total ascending"}
    )

    return fig