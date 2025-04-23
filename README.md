# Portfolio Management System

This is a portfolio management system built to track assets, view portfolio performance, monitor dividends, and visualize sector allocation. The system allows you to simulate future portfolio performance using Monte Carlo simulations, helping to assess the impact of risk and uncertainty over time.

## Features

The system includes the following functionalities:

1. **Add Asset**: Add new assets to your portfolio by specifying the ticker symbol, sector, asset class, quantity, and purchase price.
2. **View Portfolio**: View a detailed summary of all the assets in your portfolio, including the current price, quantity, and transaction value.
3. **Track Dividends**: Track the dividends of the assets in your portfolio and get an overview of all dividend payments.
4. **Asset Weights**: View the relative weights of each asset in your portfolio.
5. **Rebalancing Suggestions**: Get suggestions for portfolio rebalancing based on the current asset distribution.
6. **Sector Allocation Visualization**: Visualize the sector allocation of your portfolio, helping you assess the diversification of your investments.
7. **Plot Price History**: Plot the historical price data for selected assets to analyze trends over time.
8. **Simulate Portfolio**: Perform a Monte Carlo simulation over the next 15 years to simulate your portfolio's future performance, assuming 100,000 simulated paths, to demonstrate the impact of risk and uncertainty.

## Libraries Used

This project uses several libraries for functionality and visualization. The key libraries used in this project include:

- `yfinance`: For fetching stock data and historical prices.
- `pandas`: For data manipulation and handling portfolio data.
- `matplotlib`: For visualizing sector allocations and portfolio performance.
- `numpy`: For numerical operations, especially in simulations.
- `scipy`: For statistical analysis and some simulation processes.

## Installation

Follow these steps to set up the project locally:

### Step 1: Clone the repository

Clone this repository to your local machine:

```bash
git clone https://github.com/yourusername/portfolio-management-system.git
cd portfolio-management-system

