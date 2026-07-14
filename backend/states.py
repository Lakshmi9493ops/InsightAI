import plotly.express as px


def top_states(df):

    if "state" not in df.columns:
        return None

    if "sales" not in df.columns:
        return None

    summary = (
        df.groupby("state", as_index=False)["sales"]
        .sum()
        .sort_values("sales", ascending=False)
        .head(10)
    )

    fig = px.bar(
        summary,
        x="state",
        y="sales",
        color="sales",
        title="Top 10 States"
    )

    fig.update_layout(
        template="plotly_white"
    )

    return fig