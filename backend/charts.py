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
        .sort_values("profit", ascending=False)
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
        yaxis_title="Profit"
    )

    fig.update_traces(textposition="outside")

    return fig


# ---------------------------------------------------
# Sales by Segment
# ---------------------------------------------------

def sales_by_segment(df):

    if "segment" not in df.columns or "sales" not in df.columns:
        return None

    temp_df = df.copy()

    temp_df["sales"] = pd.to_numeric(
        temp_df["sales"],
        errors="coerce"
    )

    temp_df = temp_df.dropna(subset=["sales"])

    summary = (
        temp_df.groupby("segment", as_index=False)["sales"]
        .sum()
    )

    fig = px.pie(
        summary,
        names="segment",
        values="sales",
        hole=0.45,
        title="Sales by Segment"
    )

    fig.update_layout(
        template="plotly_white",
        height=500
    )

    return fig


# ---------------------------------------------------
# Sales by Market
# ---------------------------------------------------

def sales_by_market(df):

    if "market" not in df.columns or "sales" not in df.columns:
        return None

    temp_df = df.copy()

    temp_df["sales"] = pd.to_numeric(
        temp_df["sales"],
        errors="coerce"
    )

    temp_df = temp_df.dropna(subset=["sales"])

    summary = (
        temp_df.groupby("market", as_index=False)["sales"]
        .sum()
        .sort_values("sales", ascending=False)
    )

    fig = px.bar(
        summary,
        x="market",
        y="sales",
        color="market",
        text_auto=".2s",
        title="Sales by Market"
    )

    fig.update_layout(
        template="plotly_white",
        showlegend=False,
        height=500
    )

    fig.update_traces(textposition="outside")

    return fig


# ---------------------------------------------------
# Sales by Year
# ---------------------------------------------------

def sales_by_year(df):

    if "year" not in df.columns or "sales" not in df.columns:
        return None

    temp_df = df.copy()

    temp_df["sales"] = pd.to_numeric(
        temp_df["sales"],
        errors="coerce"
    )

    temp_df = temp_df.dropna(subset=["sales"])

    summary = (
        temp_df.groupby("year", as_index=False)["sales"]
        .sum()
        .sort_values("year")
    )

    fig = px.line(
        summary,
        x="year",
        y="sales",
        markers=True,
        title="Yearly Sales"
    )

    fig.update_layout(
        template="plotly_white",
        height=500,
        xaxis_title="Year",
        yaxis_title="Sales"
    )

    return fig


# ---------------------------------------------------
# Sales by Ship Mode
# ---------------------------------------------------

def sales_by_ship_mode(df):

    if "ship_mode" not in df.columns or "sales" not in df.columns:
        return None

    temp_df = df.copy()

    temp_df["sales"] = pd.to_numeric(
        temp_df["sales"],
        errors="coerce"
    )

    temp_df = temp_df.dropna(subset=["sales"])

    summary = (
        temp_df.groupby("ship_mode", as_index=False)["sales"]
        .sum()
        .sort_values("sales", ascending=False)
    )

    fig = px.bar(
        summary,
        x="ship_mode",
        y="sales",
        color="ship_mode",
        text_auto=".2s",
        title="Sales by Ship Mode"
    )

    fig.update_layout(
        template="plotly_white",
        showlegend=False,
        height=500
    )

    fig.update_traces(textposition="outside")

    return fig


# ---------------------------------------------------
# Sales by Order Priority
# ---------------------------------------------------

def sales_by_priority(df):

    if "order_priority" not in df.columns or "sales" not in df.columns:
        return None

    temp_df = df.copy()

    temp_df["sales"] = pd.to_numeric(
        temp_df["sales"],
        errors="coerce"
    )

    temp_df = temp_df.dropna(subset=["sales"])

    summary = (
        temp_df.groupby("order_priority", as_index=False)["sales"]
        .sum()
    )

    fig = px.pie(
        summary,
        names="order_priority",
        values="sales",
        hole=0.45,
        title="Sales by Order Priority"
    )

    fig.update_layout(
        template="plotly_white",
        height=500
    )

    return fig


# ---------------------------------------------------
# Top 10 States
# ---------------------------------------------------

def sales_by_state(df):

    if "state" not in df.columns or "sales" not in df.columns:
        return None

    temp_df = df.copy()

    temp_df["sales"] = pd.to_numeric(
        temp_df["sales"],
        errors="coerce"
    )

    temp_df = temp_df.dropna(subset=["sales"])

    summary = (
        temp_df.groupby("state", as_index=False)["sales"]
        .sum()
        .sort_values("sales", ascending=False)
        .head(10)
    )

    fig = px.bar(
        summary,
        x="state",
        y="sales",
        color="sales",
        text_auto=".2s",
        title="Top 10 States"
    )

    fig.update_layout(
        template="plotly_white",
        showlegend=False,
        height=500
    )

    fig.update_traces(textposition="outside")

    return fig


# ---------------------------------------------------
# Top 10 Countries
# ---------------------------------------------------

def sales_by_country(df):

    if "country" not in df.columns or "sales" not in df.columns:
        return None

    temp_df = df.copy()

    temp_df["sales"] = pd.to_numeric(
        temp_df["sales"],
        errors="coerce"
    )

    temp_df = temp_df.dropna(subset=["sales"])

    summary = (
        temp_df.groupby("country", as_index=False)["sales"]
        .sum()
        .sort_values("sales", ascending=False)
        .head(10)
    )

    fig = px.bar(
        summary,
        x="country",
        y="sales",
        color="sales",
        text_auto=".2s",
        title="Top 10 Countries"
    )

    fig.update_layout(
        template="plotly_white",
        showlegend=False,
        height=500
    )

    fig.update_traces(textposition="outside")

    return fig