import pandas as pd
import plotly.express as px


# ---------------------------------------------------
# Sales by Category
# ---------------------------------------------------

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
        text_auto=".2s",
        title="Sales by Category"
    )

    fig.update_layout(
        template="plotly_white",
        showlegend=False,
        height=500,
        xaxis_title="Category",
        yaxis_title="Total Sales"
    )

    fig.update_traces(textposition="outside")

    return fig


# ---------------------------------------------------
# Sales by Region
# ---------------------------------------------------

def sales_by_region(df):

    if "region" not in df.columns or "sales" not in df.columns:
        return None

    temp_df = df.copy()

    temp_df["sales"] = pd.to_numeric(
        temp_df["sales"],
        errors="coerce"
    )

    temp_df = temp_df.dropna(subset=["sales"])

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
        text_auto=".2s",
        title="Sales by Region"
    )

    fig.update_layout(
        template="plotly_white",
        showlegend=False,
        height=500,
        xaxis_title="Region",
        yaxis_title="Total Sales"
    )

    fig.update_traces(textposition="outside")

    return fig


# ---------------------------------------------------
# Monthly Sales Trend
# ---------------------------------------------------

def monthly_sales_trend(df):

    if "order_date" not in df.columns or "sales" not in df.columns:
        return None

    temp_df = df.copy()

    temp_df["order_date"] = pd.to_datetime(
        temp_df["order_date"],
        errors="coerce"
    )

    temp_df["sales"] = pd.to_numeric(
        temp_df["sales"],
        errors="coerce"
    )

    temp_df = temp_df.dropna(
        subset=["order_date", "sales"]
    )

    temp_df["Month"] = temp_df["order_date"].dt.to_period("M")

    summary = (
        temp_df.groupby("Month", as_index=False)["sales"]
        .sum()
        .sort_values("Month")
    )

    summary["Month"] = summary["Month"].astype(str)

    fig = px.line(
        summary,
        x="Month",
        y="sales",
        markers=True,
        title="Monthly Sales Trend"
    )

    fig.update_layout(
        template="plotly_white",
        height=500,
        xaxis_title="Month",
        yaxis_title="Sales"
    )

    return fig


# ---------------------------------------------------
# Profit by Category
# ---------------------------------------------------

def profit_by_category(df):

    if "category" not in df.columns or "profit" not in df.columns:
        return None

    temp_df = df.copy()

    temp_df["profit"] = pd.to_numeric(
        temp_df["profit"],
        errors="coerce"
    )

    temp_df = temp_df.dropna(subset=["profit"])

    summary = (
        temp_df.groupby("category", as_index=False)["profit"]
        .sum()
        .sort_values(by="profit", ascending=False)
    )

    fig = px.bar(
        summary,
        x="category",
        y="profit",
        color="category",
        text_auto=".2s",
        title="Profit by Category"
    )

    fig.update_layout(
        template="plotly_white",
        showlegend=False,
        height=500,
        xaxis_title="Category",
        yaxis_title="Total Profit"
    )

    fig.update_traces(textposition="outside")

    return fig