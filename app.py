import streamlit as st
import pandas as pd

from backend.loader import load_dataset
from backend.cleaning import (
    remove_duplicates,
    remove_missing_values
)
from backend.summary import dataset_summary
from backend.charts import sales_by_category
from backend.kpi import calculate_kpis

# ---------------------------------------------------
# PAGE CONFIGURATION
# ---------------------------------------------------

st.set_page_config(
    page_title="InsightAI",
    page_icon="📊",
    layout="wide"
)

# ---------------------------------------------------
# SIDEBAR
# ---------------------------------------------------

st.sidebar.title("📊 InsightAI")
st.sidebar.success("Navigation")

# ---------------------------------------------------
# TITLE
# ---------------------------------------------------

st.title("📊 InsightAI")

st.markdown("""
## AI-Powered Business Data Analyst

Upload a business dataset and analyze it instantly.

Current Features

- Upload CSV & Excel
- Executive KPI Dashboard
- Remove duplicate rows
- Remove missing values
- Dataset Summary
- Interactive Charts
""")

# ---------------------------------------------------
# FILE UPLOAD
# ---------------------------------------------------

uploaded_file = st.file_uploader(
    "📂 Upload CSV or Excel",
    type=["csv", "xlsx"]
)

# ---------------------------------------------------
# MAIN
# ---------------------------------------------------

if uploaded_file is not None:

    df = load_dataset(uploaded_file)

    # --------------------------
    # Cleaning
    # --------------------------

    st.subheader("🧹 Data Cleaning")

    remove_dup = st.checkbox("Remove Duplicate Rows")

    remove_missing = st.checkbox(
        "Remove Rows with Missing Values"
    )

    if remove_dup:
        df, duplicates = remove_duplicates(df)
        st.success(
            f"Removed {duplicates} duplicate rows."
        )

    if remove_missing:
        df, missing = remove_missing_values(df)
        st.success(
            f"Removed {missing} rows with missing values."
        )

    # --------------------------
    # KPI Dashboard
    # --------------------------

    kpi = calculate_kpis(df)

    st.subheader("📊 Executive Dashboard")

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
            "📦 Orders",
            kpi["orders"]
        )

    with c4:
        st.metric(
            "🌍 Countries",
            kpi["countries"]
        )

    # --------------------------
    # Dataset Summary
    # --------------------------

    summary = dataset_summary(df)

    st.subheader("📑 Dataset Summary")

    s1, s2, s3, s4, s5 = st.columns(5)

    s1.metric("Rows", summary["rows"])
    s2.metric("Columns", summary["columns"])
    s3.metric("Numeric", summary["numeric"])
    s4.metric("Text", summary["text"])
    s5.metric("Date", summary["date"])

    # --------------------------
    # Chart
    # --------------------------

    st.subheader("📊 Sales by Category")

    fig = sales_by_category(df)

    if fig is not None:
        st.plotly_chart(
            fig,
            use_container_width=True
        )

    # --------------------------
    # Preview
    # --------------------------

    with st.expander(
        "📄 Dataset Preview",
        expanded=True
    ):
        st.dataframe(df.head())

    # --------------------------
    # Information
    # --------------------------

    with st.expander(
        "ℹ Dataset Information"
    ):

        info = pd.DataFrame({
            "Column": df.columns,
            "Datatype": df.dtypes.astype(str)
        })

        st.dataframe(info)

    # --------------------------
    # Missing Values
    # --------------------------

    with st.expander(
        "❗ Missing Values"
    ):

        missing = pd.DataFrame({
            "Column": df.columns,
            "Missing": df.isnull().sum().values
        })

        st.dataframe(missing)