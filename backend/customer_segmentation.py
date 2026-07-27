import pandas as pd
from sklearn.cluster import KMeans
import plotly.express as px


def customer_segmentation(df):

    required = ["customer_name", "sales"]

    for col in required:
        if col not in df.columns:
            return None

    temp = df.copy()

    temp["sales"] = pd.to_numeric(
        temp["sales"],
        errors="coerce"
    )

    temp = temp.dropna()

    summary = (
        temp.groupby("customer_name", as_index=False)
        ["sales"]
        .sum()
    )

    model = KMeans(
        n_clusters=3,
        random_state=42
    )

    summary["Cluster"] = model.fit_predict(
        summary[["sales"]]
    )

    fig = px.scatter(
        summary,
        x="customer_name",
        y="sales",
        color="Cluster",
        title="Customer Segmentation"
    )

    fig.update_layout(
        template="plotly_white",
        xaxis_title="Customer",
        yaxis_title="Sales",
        height=600
    )

    return fig