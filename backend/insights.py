import pandas as pd


def business_insights(df):

    insights = []

    temp = df.copy()

    if "sales" in temp.columns:

        temp["sales"] = pd.to_numeric(
            temp["sales"],
            errors="coerce"
        )

        total_sales = temp["sales"].sum()

        insights.append(
            f"💰 Total Sales: ${total_sales:,.2f}"
        )

    if "profit" in temp.columns:

        temp["profit"] = pd.to_numeric(
            temp["profit"],
            errors="coerce"
        )

        total_profit = temp["profit"].sum()

        insights.append(
            f"📈 Total Profit: ${total_profit:,.2f}"
        )

    if "category" in temp.columns:

        best = (
            temp.groupby("category")["sales"]
            .sum()
            .idxmax()
        )

        insights.append(
            f"🏆 Best Category: {best}"
        )

    return insights