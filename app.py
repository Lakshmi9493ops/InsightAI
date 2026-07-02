import streamlit as st
import pandas as pd
from backend.loader import load_dataset
from backend.cleaning import remove_duplicates

# -------------------------------
# Page Configuration
# -------------------------------
st.set_page_config(
    page_title="InsightAI",
    page_icon="📊",
    layout="wide"
)

# -------------------------------
# Sidebar
# -------------------------------
st.sidebar.title("📊 InsightAI")
st.sidebar.success("Navigation")

# -------------------------------
# Main Page
# -------------------------------
st.title("📊 InsightAI")

st.markdown("""
### AI-Powered Business Data Analyst

Welcome!

This application helps you:

- 📂 Upload CSV or Excel files
- 🧹 Clean business data
- 📈 Analyze trends
- 📊 Create interactive dashboards
- 🤖 Generate AI-powered business insights
- 📄 Download reports

---
""")
# -------------------------------
# Upload Dataset
# -------------------------------

# -------------------------------
# Upload Dataset
# -------------------------------


uploaded_file = st.file_uploader(
    "📂 Upload a CSV or Excel file",
    type=["csv", "xlsx"]
)

if uploaded_file is not None:

    # -------------------------------
    # Data Cleaning Options
    # -------------------------------
    st.subheader("🧹 Data Cleaning Options")

    remove_dup = st.checkbox("Remove Duplicate Rows")

    # -------------------------------
    # Load Dataset
    # -------------------------------
    df = load_dataset(uploaded_file)

    # -------------------------------
    # Remove Duplicates (Optional)
    # -------------------------------
    duplicates_removed = 0

    if remove_dup:
        df, duplicates_removed = remove_duplicates(df)
        st.info(f"🧹 Duplicate rows removed: {duplicates_removed}")

    # -------------------------------
    # Success Message
    # -------------------------------
    st.success(f"✅ {uploaded_file.name} uploaded successfully!")

    # -------------------------------
    # Dataset Preview
    # -------------------------------
    with st.expander("📄 Dataset Preview", expanded=True):
        st.dataframe(df.head())

    # -------------------------------
    # Dataset Shape
    # -------------------------------
    rows, columns = df.shape

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Rows", rows)

    with col2:
        st.metric("Columns", columns)

    # -------------------------------
    # Dataset Information
    # -------------------------------
    with st.expander("ℹ️ Dataset Information"):

        info_df = pd.DataFrame({
            "Column Name": df.columns,
            "Data Type": df.dtypes.astype(str)
        })

        st.dataframe(info_df)

    # -------------------------------
    # Missing Values
    # -------------------------------
    with st.expander("❗ Missing Values"):

        missing = df.isnull().sum()

        missing_df = pd.DataFrame({
            "Column": missing.index,
            "Missing Values": missing.values
        })

        st.dataframe(missing_df)