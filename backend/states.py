import pandas as pd
import plotly.express as px


def top_states(df):

    if "state" not in df.columns:
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
        temp.groupby("state", as_index=False)["sales"]
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
        template="plotly_white",
        showlegend=False,
        height=500
    )

    return fig