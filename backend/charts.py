import pandas as pd
import plotly.express as px


def sales_by_category(df):

    if "category" not in df.columns or "sales" not in df.columns:
        return None

    temp_df = df.copy()

    temp_df["sales"] = pd.to_numeric(
        temp_df["sales"],
        errors="coerce"
    )

    temp_df = temp_df.dropna(subset=["sales"])

    summary = (
        temp_df.groupby("category", as_index=False)["sales"]
        .sum()
        .sort_values(by="sales", ascending=False)
    )

    fig = px.bar(
        summary,
        x="category",
        y="sales",
        color="category",
        title="Sales by Category"
    )

    fig.update_layout(
        template="plotly_white",
        showlegend=False,
        height=500
    )

    return fig


def sales_by_region(df):

    if "region" not in df.columns or "sales" not in df.columns:
        return None

    temp_df = df.copy()

    temp_df["sales"] = pd.to_numeric(
        temp_df["sales"],
        errors="coerce"
    )

    summary = (
        temp_df.groupby("region", as_index=False)["sales"]
        .sum()
        .sort_values(by="sales", ascending=False)
    )

    fig = px.bar(
        summary,
        x="region",
        y="sales",
        color="region",
        title="Sales by Region"
    )

    fig.update_layout(
        template="plotly_white",
        showlegend=False,
        height=500
    )

    return fig