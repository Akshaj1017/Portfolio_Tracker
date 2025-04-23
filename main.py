from portfolio_controller import PortfolioController

def main():
    controller = PortfolioController()
    menu = [
        "Add Asset",
        "View Portfolio",
        "Asset Weights",
        "Rebalancing Suggestions",
        "Plot Price History",
        "Track Dividends",
        "Risk Metrics",
        "Sector Allocation",
        "Simulate Portfolio (15 Years)",
        "Exit"
    ]

    while True:
        print("\nTotal Portfolio Value: ${:.2f}".format(controller.model.get_portfolio_value()[0]))
        for i, item in enumerate(menu, 1):
            print(f"{i}. {item}")
        choice = input("Enter your choice: ")

        if choice == "1":
            ticker = input("Enter Ticker Symbol: ")
            sector = input("Enter Sector: ")
            asset_class = input("Enter Asset Class: ")
            quantity = int(input("Enter Quantity: "))
            price = float(input("Enter Purchase Price: "))
            controller.add_asset(ticker, sector, asset_class, quantity, price)
        elif choice == "2":
            controller.view_portfolio()
        elif choice == "3":
            controller.asset_weights()
        elif choice == "4":
            controller.rebalancing_suggestions()
        elif choice == "5":
            tickers = input("Enter ticker symbols (comma separated): ").split(",")
            controller.plot_price(tickers)
        elif choice == "6":
            controller.dividends()
        elif choice == "7":
            controller.risk_metrics()
        elif choice == "8":
            controller.sector_allocation()
        elif choice == "9":
            controller.simulate()
        elif choice == "10":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
