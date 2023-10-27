import pandas as pd
from statsmodels.tsa.seasonal import seasonal_decompose

from .indicators import Indicators


class TechnicalIndicators(Indicators):
    def __init__(self, history):
        super().__init__(history)

    @property
    def df(self):
        return self.history.df

    @property
    def series_indicators(self):
        return self.history.indicators.series

    def sharpe_ratio(self, periods=252, risk_free_rate=0.05):
        returns = self.series_indicators.log_change()
        daily_risk_free = (1 + risk_free_rate) ** (1 / periods) - 1

        excess_returns = returns - daily_risk_free

        return excess_returns.mean() / excess_returns.std()

    def rsi(self, window=252):
        delta = self.df.diff()

        gain = delta.where(delta > 0, 0).fillna(0)
        loss = -delta.where(delta < 0, 0).fillna(0)

        avg_gain = gain.rolling(window=window, min_periods=1).mean()
        avg_loss = loss.rolling(window=window, min_periods=1).mean()

        rs = avg_gain / avg_loss

        return 100 - (100 / (1 + rs))

    def beta(self) -> pd.Series:
        returns = self.series_indicators.log_change().dropna()

        betas = {}

        for asset in returns.columns:
            market_returns = returns.drop(columns=[asset]).mean(axis=1)

            asset_returns = returns[asset]

            covariance = asset_returns.cov(market_returns)
            market_variance = market_returns.var()

            beta = covariance / market_variance
            betas[asset] = beta

        return pd.Series(betas)

    def drawdown(self):
        return self.df / self.df.cummax() - 1

    def autocorrelation(self, lag=15) -> pd.Series:
        returns = self.series_indicators.log_change()
        acorr = returns.apply(lambda col: col.autocorr(lag=lag))

        return acorr

    def seasonal_decompose(self, period=252):
        result = seasonal_decompose(self.df, model="multiplicative", period=period)
        return result.trend, result.seasonal, result.resid

    def adtv(self, window=20,column="Volume"):
        return self.df[column].rolling(window=window).mean()
