import plotly.express as px


def top_customers(df):

    if "customer_name" not in df.columns:
        return None

    if "sales" not in df.columns:
        return None

    summary = (
        df.groupby("customer_name", as_index=False)
        .agg({"sales": "sum"})
        .sort_values("sales", ascending=False)
        .head(10)
    )

    fig = px.bar(
        summary,
        x="customer_name",
        y="sales",
        color="sales",
        text_auto=".2s",
        title="Top 10 Customers"
    )

    fig.update_layout(
        template="plotly_white",
        xaxis_title="Customer",
        yaxis_title="Sales",
        xaxis_tickangle=-45,
        height=600
    )

    return fig