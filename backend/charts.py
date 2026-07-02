import pandas as pd
import plotly.express as px


def sales_by_category(df):

    # Check required columns
    if "category" not in df.columns or "sales" not in df.columns:
        return None

    # Convert sales to numeric
    temp_df = df.copy()
    temp_df["sales"] = pd.to_numeric(temp_df["sales"], errors="coerce")

    # Remove invalid values
    temp_df = temp_df.dropna(subset=["sales"])

    # Group by category
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
        height=500,
        showlegend=False,
        xaxis_title="Category",
        yaxis_title="Total Sales"
    )

    return fig