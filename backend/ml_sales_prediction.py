import pandas as pd

from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score


def train_sales_model(df):

    required = [
        "quantity",
        "discount",
        "profit",
        "sales"
    ]

    for col in required:
        if col not in df.columns:
            return None, None

    temp = df.copy()

    for col in required:
        temp[col] = pd.to_numeric(
            temp[col],
            errors="coerce"
        )

    temp = temp.dropna()

    X = temp[
        [
            "quantity",
            "discount",
            "profit"
        ]
    ]

    y = temp["sales"]

    model = LinearRegression()

    model.fit(X, y)

    predictions = model.predict(X)

    score = r2_score(y, predictions)

    return model, score


def predict_sales(model, quantity, discount, profit):

    prediction = model.predict(
        [[
            quantity,
            discount,
            profit
        ]]
    )

    return round(float(prediction[0]), 2)