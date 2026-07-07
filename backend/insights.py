def business_insights(df):

    insights = []

    if "sales" in df.columns:
        insights.append(
            f"Total Sales: ${df['sales'].sum():,.2f}"
        )

    if "profit" in df.columns:
        insights.append(
            f"Total Profit: ${df['profit'].sum():,.2f}"
        )

    if "category" in df.columns:

        top = (
            df.groupby("category")["sales"]
            .sum()
            .idxmax()
        )

        insights.append(
            f"Highest Sales Category: {top}"
        )

    return insights