import numpy as np
import pandas as pd
import statsmodels.api as sm
from statsmodels.tsa.stattools import adfuller
from scipy.stats import shapiro

class StatTests:
    def __init__(self, series) -> None:
        # Initiate series, check type and generate returns
        self.series = series
        assert type(self.series) == pd.core.series.Series, f"Pandas Series must be passed, insted got {type(self.series)}"
        self.returns = series.pct_change(1).dropna()

    def print_report(self):
        # Prints out a complete report on TS properties.
        print("=====================================================")
        print("STATISTICAL TESTS REPORT\n")
        print("TIME SERIES STATIONARITY:")
        self.timeseries_stationarity()
        print("\nRETURNS STATIONARITY:")
        self.returns_stationarity()
        print('\nRETURNS NORMALITY:')
        self.returns_normality()
        print('\nVOLATILITY CLUSTERING:')
        self.volatility_clustering()
        print('\nAUTOCCORELATION OF RETURNS:')
        self.returns_autocorrelation()
        print("=====================================================")

    def timeseries_stationarity(self, alpha = 0.05):
        # Returns true if returns are stationary
        print(f"Augmented DF test for stationarity, alpha = {alpha}")
        p = adfuller(self.series)[1]
        print(f"p = {p:1.3f}")
        if p <= alpha:
            print("Time series IS stationary")
            return True
        else:
            print("Time series IS NOT stationary")
            return False

    def returns_stationarity(self, alpha = 0.05):
        # Returns true if returns are stationary
        print(f"Augmented DF test for stationarity, alpha = {alpha}")
        p = adfuller(self.returns)[1]
        print(f"p = {p:1.3f}")
        if p <= alpha:
            print("The returns ARE stationary")
            return True
        else:
            print("The returns ARE NOT stationary")
            return False


    def returns_normality(self, alpha=0.05):
        # Returns true if returns are normally distributed
        print(f'Shapiro normality test, alpha = {alpha}')
        stat, p = shapiro(self.returns)
        print(f"p = {p:1.3f}")
        if p <= alpha:
            print("The returns ARE NOT normally distributed")
            return False
        else:
            print("The returns ARE normally distributed")
            return True

    def volatility_clustering(self, alpha = 0.05):
        # Returns true if volatility clustering occurs
        print(f"Ljung-Box test for autocorrelation test, alpha = {alpha}")
        abs_ret = self.returns.abs()
        p = sm.stats.acorr_ljungbox(abs_ret, lags=[1]).iloc[0,1]
        print(f"p = {p:1.3f}")
        if p <= alpha:
            print("Volatility clustering IS present")
            return True
        else:
            print("Volatility clustering IS NOT present")
            return False

    def returns_autocorrelation(self, alpha = 0.05):
        # Returns true if returns are autocorrelated
        print(f"Ljung-Box test for autocorrelation test, alpha = {alpha}")
        p = sm.stats.acorr_ljungbox(self.returns, lags=[1]).iloc[0,1]
        print(f"p = {p:1.3f}")
        if p <= alpha:
            print("The returns ARE autocorrelated")
            return True
        else:
            print("The returns ARE NOT autocorrelated")
            return False