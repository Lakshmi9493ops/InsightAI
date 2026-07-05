import pandas as pd
import plotly.express as px


def top_products(df):

    if "product_name" not in df.columns:
        return None

    if "sales" not in df.columns:
        return None

    temp_df = df.copy()

    temp_df["sales"] = pd.to_numeric(
        temp_df["sales"],
        errors="coerce"
    )

    summary = (
        temp_df.groupby("product_name", as_index=False)["sales"]
        .sum()
        .sort_values(
            by="sales",
            ascending=False
        )
        .head(10)
    )

    fig = px.bar(
        summary,
        x="sales",
        y="product_name",
        orientation="h",
        title="Top 10 Products by Sales"
    )

    fig.update_layout(
        template="plotly_white",
        height=600
    )

    return fig