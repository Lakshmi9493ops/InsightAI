import pandas as pd
import plotly.express as px


def top_customers(df):

    if "customer_name" not in df.columns:
        return None

    if "sales" not in df.columns:
        return None

    temp = df.copy()

    temp["sales"] = pd.to_numeric(
        temp["sales"],
        errors="coerce"
    )

    temp = temp.dropna(subset=["sales"])

    summary = (
        temp.groupby("customer_name", as_index=False)["sales"]
        .sum()
        .sort_values("sales", ascending=False)
        .head(10)
    )

    fig = px.bar(
        summary,
        x="sales",
        y="customer_name",
        orientation="h",
        color="sales"
    )

    fig.update_layout(
        template="plotly_white",
        height=550
    )

    return fig