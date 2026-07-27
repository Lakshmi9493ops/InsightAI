import pandas as pd
import plotly.express as px
from sklearn.cluster import KMeans


def product_segmentation(df):

    if "product_name" not in df.columns or "sales" not in df.columns:
        return None

    temp = df.copy()

    temp["sales"] = pd.to_numeric(
        temp["sales"],
        errors="coerce"
    )

    temp = temp.dropna(subset=["sales"])

    summary = (
        temp.groupby("product_name", as_index=False)["sales"]
        .sum()
        .sort_values("sales", ascending=False)
    )

    model = KMeans(
        n_clusters=3,
        random_state=42,
        n_init=10
    )

    summary["Cluster"] = model.fit_predict(
        summary[["sales"]]
    )

    fig = px.scatter(
        summary,
        x="product_name",
        y="sales",
        color="Cluster",
        hover_name="product_name",
        title="📦 Product Segmentation"
    )

    fig.update_layout(
        template="plotly_white",
        height=600
    )

    return fig