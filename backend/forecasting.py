import pandas as pd
from sklearn.linear_model import LinearRegression
import plotly.express as px


def sales_forecast(df):

    if "year" not in df.columns or "sales" not in df.columns:
        return None

    data = (
        df.groupby("year", as_index=False)["sales"]
        .sum()
        .sort_values("year")
    )

    X = data[["year"]]
    y = data["sales"]

    model = LinearRegression()
    model.fit(X, y)

    next_year = data["year"].max() + 1
    prediction = model.predict([[next_year]])[0]

    future = pd.DataFrame({
        "year": [next_year],
        "sales": [prediction]
    })

    chart = pd.concat([data, future])

    fig = px.line(
        chart,
        x="year",
        y="sales",
        markers=True,
        title="Sales Forecast"
    )

    return fig