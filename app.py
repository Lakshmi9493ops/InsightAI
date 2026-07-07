import streamlit as st
import pandas as pd

# Backend Modules
from backend.loader import load_dataset
from backend.cleaning import (
    remove_duplicates,
    remove_missing_values,
    fill_missing_values
)
from backend.eda import (
    numerical_summary,
    correlation_heatmap
)
from backend.converter import convert_numeric
from backend.exporter import convert_to_csv
from backend.summary import dataset_summary
from backend.kpi import calculate_kpis
from backend.charts import (
    sales_by_category,
    sales_by_region,
    monthly_sales_trend,
    profit_by_category
)
from backend.products import top_products

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

page = st.sidebar.radio(
    "Go To",
    [
        "Dashboard",
        "Dataset"
    ]
)

# ---------------------------------------------------
# MAIN TITLE
# ---------------------------------------------------

st.title("📊 InsightAI")

st.markdown("""
## AI-Powered Business Data Analyst

Upload a business dataset and analyze it instantly.

### Current Features

- 📂 Upload CSV & Excel
- 📊 Executive KPI Dashboard
- 🧹 Remove Duplicate Rows
- ❗ Remove Missing Values
- 📈 Interactive Business Charts
- 📋 Dataset Summary
- 👀 Dataset Preview
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

    # --------------------------
    # Load Dataset
    # --------------------------
    df = load_dataset(uploaded_file)

    # --------------------------
    # Sidebar Filters
    # --------------------------
    st.sidebar.header("📌 Dashboard Filters")

    # Region Filter
    selected_region = "All"

    if "region" in df.columns:

        regions = sorted(df["region"].dropna().unique())

        selected_region = st.sidebar.selectbox(
            "🌍 Select Region",
            ["All"] + regions
        )

        if selected_region != "All":
            df = df[df["region"] == selected_region]

    # Category Filter
    selected_category = "All"

    if "category" in df.columns:

        categories = sorted(df["category"].dropna().unique())

        selected_category = st.sidebar.selectbox(
            "📦 Select Category",
            ["All"] + categories
        )

        if selected_category != "All":
            df = df[df["category"] == selected_category]

    
    # --------------------------
    # Data Cleaning
    # --------------------------

    st.subheader("🧹 Data Cleaning")

    # Cleaning Options
    remove_dup = st.checkbox("Remove Duplicate Rows")

    remove_missing = st.checkbox(
        "Remove Rows with Missing Values"
    )

    fill_method = st.selectbox(
        "Fill Missing Values",
        [
            "None",
            "Mean",
            "Median",
            "Mode"
        ]
    )

    # --------------------------
    # Apply Cleaning
    # --------------------------

    if remove_dup:

        df, duplicates = remove_duplicates(df)

        st.success(
            f"✅ Removed {duplicates} duplicate rows."
        )

    if remove_missing:

        df, missing = remove_missing_values(df)

        st.success(
            f"✅ Removed {missing} rows with missing values."
        )

    if fill_method != "None":

        df = fill_missing_values(
            df,
            fill_method
        )

        st.success(
            f"✅ Missing values filled using {fill_method}."
        )

# --------------------------
# Data Type Conversion
# --------------------------

    st.subheader("🔄 Data Type Conversion")

    column = st.selectbox(
        "Select Column",
        df.columns
    )

    if st.button("Convert Selected Column to Numeric"):

        df = convert_numeric(
            df,
            column
        )

        st.success(
            f"✅ '{column}' converted to numeric."
        )
    # --------------------------
    # KPI Dashboard
    # --------------------------

        # --------------------------
    # Executive Dashboard
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

    st.divider()

    # --------------------------
    # Sales by Category
    # --------------------------

    st.subheader("📊 Sales by Category")

    fig = sales_by_category(df)

    if fig is not None:
        st.plotly_chart(
            fig,
            use_container_width=True
        )

    # --------------------------
    # Sales by Region
    # --------------------------

    st.subheader("🌍 Sales by Region")

    fig = sales_by_region(df)

    if fig is not None:
        st.plotly_chart(
            fig,
            use_container_width=True
        )

    # --------------------------
    # Top 10 Products
    # --------------------------

    st.subheader("🏆 Top 10 Products")

    fig = top_products(df)

    if fig is not None:
        st.plotly_chart(
            fig,
            use_container_width=True
        )

    # --------------------------
    # Monthly Sales Trend
    # --------------------------

    st.subheader("📈 Monthly Sales Trend")

    fig = monthly_sales_trend(df)

    if fig is not None:
        st.plotly_chart(
            fig,
            use_container_width=True
        )

    # --------------------------
    # Profit by Category
    # --------------------------

    st.subheader("💰 Profit by Category")

    fig = profit_by_category(df)

    if fig is not None:
        st.plotly_chart(
            fig,
            use_container_width=True
        )

    st.divider()

    # --------------------------
    # Dataset Preview
    # --------------------------

    with st.expander(
        "📄 Dataset Preview",
        expanded=True
    ):
        st.dataframe(df.head())

    # --------------------------
    # Dataset Information
    # --------------------------

    with st.expander("ℹ️ Dataset Information"):

        info = pd.DataFrame({
            "Column": df.columns,
            "Datatype": df.dtypes.astype(str)
        })

        st.dataframe(info)
    
    # --------------------------
    # Missing Values
    # --------------------------

    with st.expander("❗ Missing Values"):

        missing_df = pd.DataFrame({
            "Column": df.columns,
            "Missing Values": df.isnull().sum().values,
            "Missing (%)": (
                df.isnull().sum() / len(df) * 100
            ).round(2).values
        })

        st.dataframe(
            missing_df,
            use_container_width=True
        )
    # --------------------------
    # Download Cleaned Dataset
    # --------------------------

    st.subheader("📥 Download Cleaned Dataset")

    csv = convert_to_csv(df)

    st.download_button(
        label="⬇ Download Cleaned CSV",
        data=csv,
        file_name="cleaned_dataset.csv",
        mime="text/csv"
    ) 
    st.subheader("📊 Numerical Summary")

    summary_df = numerical_summary(df)

    st.dataframe(summary_df) 
    st.subheader("🔥 Correlation Heatmap")

    fig = correlation_heatmap(df)

    if fig is not None:
        st.plotly_chart(
            fig,
            use_container_width=True
        ) 
    st.subheader("📈 Distribution Analysis")

    numeric_columns = df.select_dtypes(include="number").columns.tolist()

    if numeric_columns:

        selected_column = st.selectbox(
            "Select Numeric Column",
            numeric_columns
        )

    from backend.eda import histogram

    fig = histogram(df, selected_column)

    st.plotly_chart(
        fig,
        use_container_width=True
    )