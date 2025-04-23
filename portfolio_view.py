import matplotlib.pyplot as plt
import pandas as pd

class PortfolioView:
    def display_portfolio(self, data, portfolio_data):
        print("\nPortfolio:")
        print(f"{'Ticker':<10}{'Quantity':<10}{'Purchase Price':<15}{'Transaction Value':<20}{'Current Price':<15}{'Current Value':<15}")
        for item in portfolio_data:
            print(f"{item[0]:<10}{item[1]:<10}{item[2]:<15}${item[3]:<20.2f}${item[4]:<15.2f}${item[5]:<15.2f}")

    def display_weights(self, weights):
        print("\nAsset Weights (%):")
        for ticker, weight in weights.items():
            print(f"{ticker}: {weight:.2f}%")

    def display_risk_metrics(self, means, stds):
        print("\nExpected Annual Return and Risk (Volatility):")
        for ticker in means.index:
            print(f"{ticker} -> Mean: {means[ticker]*100:.2f}%, Std Dev: {stds[ticker]*100:.2f}%")

    def display_dividends(self, dividend_data):
        for ticker, dividends in dividend_data.items():
            print(f"\nDividends for {ticker}:")
            print(dividends.tail(10))

    def display_rebalancing(self, weights):
        equal_weight = 100 / len(weights)
        print("\nRebalancing Suggestions:")
        for ticker, weight in weights.items():
            diff = equal_weight - weight
            action = "Buy" if diff > 0 else "Sell"
            print(f"{action} {ticker}: {abs(diff):.2f}%")

    def plot_prices(self, tickers):
        import yfinance as yf
        for ticker in tickers:
            stock = yf.Ticker(ticker.upper())
            hist = stock.history(period="1y")["Close"]
            hist.plot(label=ticker.upper())
        plt.title("Price History (1 Year)")
        plt.xlabel("Date")
        plt.ylabel("Price")
        plt.legend()
        plt.tight_layout()
        plt.show()

    def plot_sector_allocation(self, sector_data):
        sector_data.plot(kind="pie", autopct="%1.1f%%", title="Sector Allocation", ylabel="")
        plt.tight_layout()
        plt.show()

    def plot_simulation(self, simulations):
        plt.figure(figsize=(10, 6))
        plt.plot(simulations[:, :100], color='blue', alpha=0.1)
        plt.title("Monte Carlo Portfolio Simulation (15 Years)")
        plt.xlabel("Days")
        plt.ylabel("Portfolio Value")
        plt.tight_layout()
        plt.show()
