import pandas as pd


def dashboard_score(df):

    score = 100

    if df.isnull().sum().sum() > 0:
        score -= 10

    if df.duplicated().sum() > 0:
        score -= 10

    if len(df) < 100:
        score -= 20

    return max(score, 0)