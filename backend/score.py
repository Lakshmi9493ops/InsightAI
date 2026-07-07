def dashboard_score(df):

    score = 100

    if df.isnull().sum().sum() > 0:
        score -= 20

    if df.duplicated().sum() > 0:
        score -= 20

    return score