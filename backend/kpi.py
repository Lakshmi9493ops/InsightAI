import pandas as pd


def calculate_kpis(df):
    """
    Calculate executive KPI values.
    """

    total_sales = 0
    total_profit = 0
    total_orders = 0
    total_countries = 0

    # Total Sales
    if "sales" in df.columns:
        total_sales = pd.to_numeric(
            df["sales"],
            errors="coerce"
        ).sum()

    # Total Profit
    if "profit" in df.columns:
        total_profit = pd.to_numeric(
            df["profit"],
            errors="coerce"
        ).sum()

    # Total Orders
    if "order_id" in df.columns:
        total_orders = df["order_id"].nunique()

    # Total Countries
    if "country" in df.columns:
        total_countries = df["country"].nunique()

    return {
        "sales": total_sales,
        "profit": total_profit,
        "orders": total_orders,
        "countries": total_countries
    }