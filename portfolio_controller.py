from portfolio_model import PortfolioModel
from portfolio_view import PortfolioView

class PortfolioController:
    def __init__(self):
        self.model = PortfolioModel()
        self.view = PortfolioView()

    def add_asset(self, ticker, sector, asset_class, quantity, purchase_price):
        self.model.add_asset(ticker, sector, asset_class, quantity, purchase_price)

    def view_portfolio(self):
        total_value, portfolio_data = self.model.get_portfolio_value()
        self.view.display_portfolio(self.model.data, portfolio_data)

    def asset_weights(self):
        weights = self.model.get_weights()
        self.view.display_weights(weights)

    def rebalancing_suggestions(self):
        weights = self.model.get_weights()
        self.view.display_rebalancing(weights)

    def plot_price(self, tickers):
        self.view.plot_prices(tickers)

    def dividends(self):
        data = self.model.get_dividends()
        self.view.display_dividends(data)

    def risk_metrics(self):
        mean, std = self.model.get_risk_metrics()
        self.view.display_risk_metrics(mean, std)

    def sector_allocation(self):
        sector_data = self.model.get_sector_allocation()
        self.view.plot_sector_allocation(sector_data)

    def simulate(self):
        sims = self.model.simulate_portfolio()
        self.view.plot_simulation(sims)
