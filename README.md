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

Here’s the section you asked for, converted into markdown format:

```markdown
### Step 1: Clone the Repository

First, clone the repository to your local machine using the following command:

```bash
git clone https://github.com/yourusername/portfolio-management-system.git
```

This will create a local copy of the repository. After cloning, navigate to the project directory:

```bash
cd portfolio-management-system
```

### Step 2: Install the Required Dependencies

The project requires several Python libraries to run correctly. These dependencies are listed in the `requirements.txt` file. To install them, run the following command:

```bash
pip install -r requirements.txt
```

This will automatically install all the necessary libraries for the application.

### Step 3: Run the Application

Once the dependencies are installed, you can start the application by running the following command:

```bash
python main.py
```

This will launch the program, and you will be presented with a menu of options to interact with the Portfolio Management System.

### Step 4: Interact with the Application

After running the application, you will be presented with a menu offering different functionalities. You can:

- **Add Asset**: Add new assets to your portfolio.
- **View Portfolio**: View a summary of all your portfolio assets, including transaction values, current prices, and overall portfolio value.
- **Track Dividends**: View the dividends of the assets in your portfolio.
- **Asset Weights**: View the relative weights of each asset in your portfolio.
- **Rebalancing Suggestions**: Get recommendations on how to rebalance your portfolio.
- **Sector Allocation Visualization**: Visualize your portfolio's sector allocation for better diversification insights.
- **Simulate Portfolio**: Run Monte Carlo simulations to predict the future performance of your portfolio over the next 15 years under different risk scenarios.
```
