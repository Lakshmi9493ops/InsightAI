import streamlit as st
import pandas as pd

from backend.loader import load_dataset
from backend.cleaning import remove_duplicates, remove_missing_values
from backend.summary import dataset_summary

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
# MAIN PAGE
# ---------------------------------------------------
st.title("📊 InsightAI")

st.markdown("""
## AI-Powered Business Data Analyst

Welcome to **InsightAI**.

Upload your business dataset and let InsightAI help you analyze it.

### Current Features

- 📂 Upload CSV & Excel
- 🧹 Remove duplicate rows
- 📊 Dataset summary
- 👀 Dataset preview
- ℹ Dataset information
- ❗ Missing value analysis

---
""")

# ---------------------------------------------------
# FILE UPLOADER
# ---------------------------------------------------
uploaded_file = st.file_uploader(
    "📂 Upload a CSV or Excel file",
    type=["csv", "xlsx"]
)

# ---------------------------------------------------
# IF FILE IS UPLOADED
# ---------------------------------------------------
if uploaded_file is not None:

    # Load Dataset
    df = load_dataset(uploaded_file)

    # -----------------------------
    # Data Cleaning
    # -----------------------------
    st.subheader("🧹 Data Cleaning")

    remove_dup = st.checkbox("Remove Duplicate Rows")
    remove_missing = st.checkbox("Remove Rows with Missing Values")

    duplicates_removed = 0

    if remove_dup:
        df, duplicates_removed = remove_duplicates(df)
        st.info(f"🧹 Duplicate rows removed: {duplicates_removed}")
    missing_removed = 0

    if remove_missing:
        df, missing_removed = remove_missing_values(df)
        st.info(f"🧹 Rows removed because of missing values: {missing_removed}")

    # -----------------------------
    # Dataset Summary
    # -----------------------------
    summary = dataset_summary(df)

    st.success(f"✅ {uploaded_file.name} uploaded successfully!")

    st.subheader("📊 Dataset Summary")

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.metric("Rows", summary["rows"])

    with col2:
        st.metric("Columns", summary["columns"])

    with col3:
        st.metric("Numeric Columns", summary["numeric"])

    with col4:
        st.metric("Text Columns", summary["text"])

    with col5:
        st.metric("Date Columns", summary["date"])

    # -----------------------------
    # Dataset Preview
    # -----------------------------
    with st.expander("📄 Dataset Preview", expanded=True):
        st.dataframe(df.head())

    # -----------------------------
    # Dataset Information
    # -----------------------------
    with st.expander("ℹ Dataset Information"):

        info_df = pd.DataFrame({
            "Column Name": df.columns,
            "Data Type": df.dtypes.astype(str)
        })

        st.dataframe(info_df)

    # -----------------------------
    # Missing Values
    # -----------------------------
    with st.expander("❗ Missing Values"):

        missing_df = pd.DataFrame({
            "Column": df.columns,
            "Missing Values": df.isnull().sum().values
        })

        st.dataframe(missing_df)