import pandas as pd
from statsmodels.tsa import stattools


def adfuller(series: pd.Series) -> dict:
    return dict(
        zip(
            ("adf", "pvalue", "usedlag", "nobs", "critical values", "icbest"),
            stattools.adfuller(series),
        )
    )
