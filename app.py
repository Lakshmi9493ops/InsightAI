import streamlit as st
import pandas as pd

# ==============================
# Backend Imports
# ==============================

from backend.loader import load_dataset
from backend.customer_segmentation import customer_segmentation

from backend.cleaning import (
    remove_duplicates,
    remove_missing_values,
    fill_missing_values
)
from backend.correlation_insights import strongest_correlations
from backend.converter import convert_numeric
from backend.report import dataset_report
from backend.summary import dataset_summary

from backend.kpi import calculate_kpis

from backend.exporter import convert_to_csv

from backend.eda import (
    numerical_summary,
    correlation_heatmap,
    histogram
)

from backend.charts import (
    sales_by_category,
    sales_by_region,
    monthly_sales_trend,
    profit_by_category,
    sales_by_segment,
    sales_by_market,
    sales_by_year,
    sales_by_ship_mode,
    sales_by_priority
)
from backend.product_segmentation import product_segmentation
from backend.products import top_products
from backend.customers import top_customers
from backend.states import top_states
from backend.countries import top_countries
from backend.score import dashboard_score
from backend.insights import business_insights
from backend.forecasting import sales_forecast
from backend.anomaly import detect_sales_outliers

from backend.ml_sales_prediction import (
    train_sales_model,
    predict_sales
)

# ==============================
# Page Configuration
# ==============================

st.set_page_config(
    page_title="InsightAI",
    page_icon="📊",
    layout="wide"
)

# ==============================
# Sidebar
# ==============================

st.sidebar.title("📊 InsightAI")

page = st.sidebar.radio(
    "Navigation",
    [
        "Dashboard",
        "Analytics",
        "Machine Learning",
        "Dataset"
    ]
)

# ==============================
# Title
# ==============================

st.title("📊 InsightAI")

st.caption("AI-Powered Business Analytics Platform")

st.divider()

# ==============================
# Upload File
# ==============================

uploaded_file = st.file_uploader(
    "📂 Upload CSV or Excel",
    type=["csv", "xlsx"]
)

# ==============================
# Stop if no file uploaded
# ==============================

if uploaded_file is None:

    st.info("👆 Please upload a CSV or Excel file to continue.")

    st.stop()

# ==============================
# Load Dataset
# ==============================

df = load_dataset(uploaded_file)

# ==============================
# Sidebar Filters
# ==============================

st.sidebar.header("Dashboard Filters")

if "region" in df.columns:

    regions = sorted(df["region"].dropna().unique())

    selected_region = st.sidebar.selectbox(
        "Region",
        ["All"] + regions
    )

    if selected_region != "All":
        df = df[df["region"] == selected_region]

if "category" in df.columns:

    categories = sorted(df["category"].dropna().unique())

    selected_category = st.sidebar.selectbox(
        "Category",
        ["All"] + categories
    )

    if selected_category != "All":
        df = df[df["category"] == selected_category]

# ==============================
# Data Cleaning
# ==============================

st.subheader("🧹 Data Cleaning")

c1, c2, c3 = st.columns(3)

with c1:
    remove_dup = st.checkbox("Remove Duplicates")

with c2:
    remove_null = st.checkbox("Remove Missing Values")

with c3:
    fill_method = st.selectbox(
        "Fill Missing Values",
        ["None", "Mean", "Median", "Mode"]
    )

if remove_dup:
    df, _ = remove_duplicates(df)

if remove_null:
    df, _ = remove_missing_values(df)

if fill_method != "None":
    df = fill_missing_values(df, fill_method)

# ==============================
# Convert Column
# ==============================

st.subheader("🔄 Convert Column to Numeric")

selected_column = st.selectbox(
    "Select Column",
    df.columns
)

if st.button("Convert"):

    df = convert_numeric(
        df,
        selected_column
    )

    st.success(f"{selected_column} converted successfully.")
# =====================================================
# Executive Dashboard
# =====================================================

st.divider()

st.header("📊 Executive Dashboard")

kpi = calculate_kpis(df)

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.metric(
        "💰 Total Sales",
        f"${kpi['sales']:,.2f}"
    )

with c2:
    st.metric(
        "📈 Total Profit",
        f"${kpi['profit']:,.2f}"
    )

with c3:
    st.metric(
        "📦 Total Orders",
        kpi["orders"]
    )

with c4:
    st.metric(
        "🌍 Countries",
        kpi["countries"]
    )

# =====================================================
# Business Health Score
# =====================================================

st.divider()

score = dashboard_score(df)

st.subheader("⭐ Business Health Score")

st.metric(
    "Overall Dashboard Score",
    f"{score}/100"
)

# =====================================================
# Dataset Summary
# =====================================================

summary = dataset_summary(df)

st.divider()

st.subheader("📑 Dataset Summary")

s1, s2, s3, s4, s5 = st.columns(5)

with s1:
    st.metric("Rows", summary["rows"])

with s2:
    st.metric("Columns", summary["columns"])

with s3:
    st.metric("Numeric", summary["numeric"])

with s4:
    st.metric("Text", summary["text"])

with s5:
    st.metric("Date", summary["date"])

# =====================================================
# Business Charts
# =====================================================

st.divider()

st.header("📈 Business Analytics Dashboard")

charts = [

    ("📦 Sales by Category", sales_by_category),

    ("🌍 Sales by Region", sales_by_region),

    ("📈 Monthly Sales Trend", monthly_sales_trend),

    ("💰 Profit by Category", profit_by_category),

    ("🏆 Top Products", top_products),

    ("👥 Top Customers", top_customers),

    ("🥧 Sales by Segment", sales_by_segment),

    ("🌎 Sales by Market", sales_by_market),

    ("📅 Sales by Year", sales_by_year),

    ("🚚 Sales by Ship Mode", sales_by_ship_mode),

    ("⭐ Sales by Order Priority", sales_by_priority),

    ("🏆 Top States", top_states),

    ("🌍 Top Countries", top_countries)

]

for title, chart_function in charts:

    st.subheader(title)

    fig = chart_function(df)

    if fig is not None:

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    else:

        st.info(
            f"{title} cannot be displayed for this dataset."
        )

# =====================================================
# AI Business Insights
# =====================================================

st.divider()

st.header("🤖 AI Business Insights")

insights = business_insights(df)

if insights:

    for item in insights:

        st.success(item)

else:

    st.info("No insights available.")
st.subheader("👥 Customer Segmentation")

fig = customer_segmentation(df)

if fig is not None:
    st.plotly_chart(
        fig,
        use_container_width=True
    )
st.subheader("📦 Product Segmentation")

fig = product_segmentation(df)

if fig is not None:
    st.plotly_chart(
        fig,
        use_container_width=True
    )
st.subheader("🔗 Strongest Correlations")

corr_df = strongest_correlations(df)

st.dataframe(
    corr_df,
    use_container_width=True
)
st.subheader("📄 Dataset Report")

report = dataset_report(df)

st.json(report)