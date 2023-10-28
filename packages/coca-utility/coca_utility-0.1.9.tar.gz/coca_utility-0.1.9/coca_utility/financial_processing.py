import pandas as pd
import numpy as np
import joblib
import statsmodels.api as sml
import enum


class BarKind(enum.Enum):
    VOLUME = enum.auto()
    DOLLAR = enum.auto()
    CUSUM = enum.auto()


class _SymmetryCuSumFilter:
    def __init__(self, thresh: int):
        self.sPos, self.sNeg = 0, 0
        self.thresh = thresh
        self.group = 0

    def proc(self, x: int | float):
        self.sPos, self.sNeg = max(0, self.sPos + x), min(0, self.sNeg + x)
        if self.sNeg < -self.thresh:
            self.sNeg = 0
            self.group += 1
        elif self.sPos > self.thresh:
            self.sPos = 0
            self.group += 1
        return self.group


def createBar(
    df: pd.DataFrame,
    col_value: str,
    col_volume: str,
    kind: BarKind,
    thresh=100,
) -> pd.DataFrame:
    df_ = df.copy()
    df_.sort_index(inplace=True)

    if kind == BarKind.VOLUME:
        df_["group"] = df_[col_volume].cumsum() // thresh
    elif kind == BarKind.DOLLAR:
        df_["group"] = (df_[col_value] * df_[col_volume]).cumsum() // thresh
    elif kind == BarKind.CUSUM:
        filter = _SymmetryCuSumFilter(thresh)
        df_["group"] = df_["diff"].apply(filter.proc)
    else:
        return df_
    return (
        df_[[col_value, col_volume, "group"]]
        .groupby("group")
        .apply(
            lambda df__: pd.Series(
                {
                    "timestamp": df__.index[-1],
                    "Open": df__[col_value].iloc[0],
                    "High": df__[col_value].max(),
                    "Low": df__[col_value].min(),
                    "Close": df__[col_value].iloc[-1],
                    "Volume": df__[col_volume].sum(),
                }
            )
        )
        .set_index("timestamp")
    )


def fracDiff(
    df: pd.DataFrame, d: float, thres=1e-5, is_FFD=True
) -> pd.DataFrame:
    def _getWeights(size):
        w = [1.0]
        for k in range(1, size):
            w.append(-w[-1] * (d - k + 1) / k)
        if is_FFD:
            w = np.where(np.abs(w) < thres, 0, w)
        return np.array(w[::-1])

    df_ = df.copy().ffill().dropna()
    w = _getWeights(df_.shape[0])
    if is_FFD:
        start = np.count_nonzero(w) - 1
    else:
        w_cs = np.cumsum(abs(w))
        w_cs /= w_cs[-1]
        start = df_[w_cs > thres].shape[0]

    return df_.apply(
        lambda series: pd.Series(
            data=[
                np.dot(w[-(i + 1) :], series[: (i + 1)])
                for i in range(start, series.shape[0])
            ],
            index=series.index[start:],
        )
    )


class ParallelExecutor:
    def __init__(self, n_atom, data):
        self.n_atom = n_atom
        self.data = data

    def execute(self, thresh, n_batch=1, n_jobs=-1):
        parts = self.createPartition(self.n_atom, thresh * n_batch)
        return joblib.Parallel(n_jobs=n_jobs)(
            joblib.delayed(self.execFunc)(
                self.data, i_start=parts[i - 1], i_end=parts[i]
            )
            for i in range(1, len(parts))
        )

    def execFunc(self, data, i_start, i_end):
        raise NotImplementedError

    def createPartition(self, n_atom, thresh):
        return ParallelExecutor.linParts(n_atom, thresh)

    @staticmethod
    def linParts(n_atom, thresh):
        parts = np.linspace(0, n_atom, min(thresh, n_atom) + 1)
        parts = np.ceil(parts).astype(int)
        return parts

    @staticmethod
    def nestedParts(n_atom, thresh, is_upper_triangle=False):
        parts, n_thread_ = [0], min(thresh, n_atom)
        for num in range(n_thread_):
            part = 1 + 4 * (
                parts[-1] ** 2
                + parts[-1]
                + n_atom * (n_atom + 1.0) / n_thread_
            )
            part = (-1 + part**0.5) / 2.0
            parts.append(part)
        parts = np.round(parts).astype(int)
        if is_upper_triangle:
            parts = np.cumsum(np.diff(parts)[::-1])
            parts = np.append(np.array([0]), parts)
        return parts


def _tValLinR(series: pd.Series):
    x = np.ones((series.shape[0], 2))
    x[:, 1] = np.arange(series.shape[0])
    return sml.OLS(series, x).fit()


def getBinsFromTrend(
    series: pd.Series, hrzns: range, n_jobs=-1, verbose=0, p_thres=0.01
) -> pd.DataFrame:
    def func(series_: pd.Series):
        if len(series_) < max(hrzns):
            return
        dic = {"t_end": [], "t_val": [], "p_val": []}
        for hrzn in hrzns:
            t_end = series_.index[hrzn - 1]
            ols = _tValLinR(series_.loc[:t_end])
            dic["t_end"].append(t_end)
            dic["t_val"].append(ols.tvalues["x1"])
            dic["p_val"].append(ols.pvalues["x1"])
        df = pd.DataFrame(dic)
        df = df[df.t_val.abs() == df.t_val.abs().max()]
        df["t_start"] = series_.index[0]
        df["bin"] = (
            np.sign(df.t_val.values[0]) if df.p_val.values[0] < p_thres else 0,
        )
        return df.set_index("t_start", drop=True)

    return pd.concat(
        joblib.Parallel(n_jobs=n_jobs, verbose=verbose)(
            joblib.delayed(func)(series_)
            for series_ in series.rolling(max(hrzns))
        )  # type: ignore
    )  # type: ignore
