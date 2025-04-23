import pandas as pd
import yfinance as yf
import numpy as np

class PortfolioModel:
    def __init__(self):
        self.filename = "portfolio.csv"
        try:
            self.data = pd.read_csv(self.filename)
        except FileNotFoundError:
            self.data = pd.DataFrame(columns=["Ticker", "Sector", "Asset Class", "Quantity", "Purchase Price"])

    def save_data(self):
        self.data.to_csv(self.filename, index=False)

    def add_asset(self, ticker, sector, asset_class, quantity, purchase_price):
        new_row = pd.DataFrame([[ticker.upper(), sector.upper(), asset_class.upper(), quantity, purchase_price]],
                               columns=["Ticker", "Sector", "Asset Class", "Quantity", "Purchase Price"])
        self.data = pd.concat([self.data, new_row], ignore_index=True)
        self.save_data()

    def get_portfolio_value(self):
        total_value = 0
        portfolio_data = []
        for _, row in self.data.iterrows():
            stock = yf.Ticker(row["Ticker"])
            current_price = stock.history(period="1d")["Close"].iloc[-1]
            transaction_value = row["Quantity"] * row["Purchase Price"]
            current_value = row["Quantity"] * current_price
            total_value += current_value
            portfolio_data.append([row["Ticker"], row["Quantity"], row["Purchase Price"], transaction_value, current_price, current_value])

        return total_value, portfolio_data

    def get_weights(self):
        values = []
        tickers = []
        for _, row in self.data.iterrows():
            stock = yf.Ticker(row["Ticker"])
            current_price = stock.history(period="1d")["Close"].iloc[-1]
            values.append(row["Quantity"] * current_price)
            tickers.append(row["Ticker"])
        total = sum(values)
        return dict(zip(tickers, [round((v / total) * 100, 2) for v in values]))

    def get_sector_allocation(self):
        allocation = self.data.groupby("Sector").apply(
            lambda x: sum([
                yf.Ticker(row["Ticker"]).history(period="1d")["Close"].iloc[-1] * row["Quantity"]
                for _, row in x.iterrows()
            ])
        )
        return allocation / allocation.sum()

    def get_dividends(self):
        dividend_data = {}
        for ticker in self.data["Ticker"].unique():
            stock = yf.Ticker(ticker)
            dividends = stock.dividends
            dividend_data[ticker] = dividends
        return dividend_data

    def get_risk_metrics(self):
        tickers = self.data["Ticker"].unique()
        prices = pd.DataFrame()

        for ticker in tickers:
            stock = yf.Ticker(ticker)
            hist = stock.history(period="1y")["Close"]
            prices[ticker] = hist

        returns = prices.pct_change().dropna()
        mean_returns = returns.mean()
        std_returns = returns.std()

        return mean_returns, std_returns

    def simulate_portfolio(self, years=15, n_simulations=100000):
        tickers = self.data["Ticker"].unique()
        weights = self.get_weights()
        weights_vector = np.array([weights[t] / 100 for t in tickers])

        prices = pd.DataFrame()
        for ticker in tickers:
            prices[ticker] = yf.Ticker(ticker).history(period="1y")["Close"]

        returns = prices.pct_change().dropna()
        mean_returns = returns.mean().values
        cov_matrix = returns.cov().values

        initial_value = self.get_portfolio_value()[0]
        simulations = np.zeros((years * 252, n_simulations))

        for i in range(n_simulations):
            daily_returns = np.random.multivariate_normal(mean_returns, cov_matrix, years * 252)
            portfolio_returns = daily_returns @ weights_vector
            portfolio_values = initial_value * (1 + portfolio_returns).cumprod()
            simulations[:, i] = portfolio_values

        return simulations
