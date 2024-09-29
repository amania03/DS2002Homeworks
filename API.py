import os
import requests
import pandas as pd
import matplotlib.pyplot as plt

# API key
API_KEY = "mykey"

# Function to fetch stock data for a given ticker symbol
def fetch_stock_data(ticker):
    try:
        api_url = f"https://yfapi.net/v6/finance/quote?symbols={ticker}"
        headers = {
            'x-api-key': API_KEY
        }
        response = requests.get(api_url, headers=headers)
        response.raise_for_status()
        data = response.json()

        if data and 'quoteResponse' in data and data['quoteResponse']['result']:
            stock_info = data['quoteResponse']['result'][0]
            return {
                "Ticker": stock_info.get("symbol", "N/A"),
                "Full Name": stock_info.get("longName", "N/A"),
                "Current Price": stock_info.get("regularMarketPrice", "N/A"),
                "Target Mean Price": stock_info.get("targetMeanPrice", "N/A"),
                "52 Week High": stock_info.get("fiftyTwoWeekHigh", "N/A"),
                "52 Week Low": stock_info.get("fiftyTwoWeekLow", "N/A")
            }
        else:
            print("No data found for this stock.")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data for {ticker}: {e}")
        return None

# Function to fetch top 5 trending stocks in the US
def fetch_trending_stocks():
    try:
        api_url = "https://yfapi.net/v1/finance/trending/US"
        headers = {
            'x-api-key': API_KEY
        }
        response = requests.get(api_url, headers=headers)
        response.raise_for_status()
        data = response.json()

        if data and 'finance' in data and data['finance']['result']:
            trending = data['finance']['result'][0]['quotes'][:5]  # Get top 5 trending stocks
            trending_stocks = []

            for stock in trending:
                ticker = stock.get('symbol', 'N/A')
                short_name = fetch_stock_detail(ticker)  # Fetch detailed info for trending stock
                trending_stocks.append({"Ticker": ticker, "Name": short_name})

            return trending_stocks
        else:
            print("No trending stocks data found")
            return []
    except requests.exceptions.RequestException as e:
        print(f"Error fetching trending stocks: {e}")
        return []

# Fetch stock details for a given ticker symbol
def fetch_stock_detail(ticker):
    try:
        api_url = f"https://yfapi.net/v6/finance/quote?symbols={ticker}"
        headers = {
            'x-api-key': API_KEY
        }
        response = requests.get(api_url, headers=headers)
        response.raise_for_status()
        data = response.json()

        if data and 'quoteResponse' in data and data['quoteResponse']['result']:
            return data['quoteResponse']['result'][0].get('shortName', 'N/A')
        else:
            return 'N/A'
    except requests.exceptions.RequestException as e:
        print(f"Error fetching details for {ticker}: {e}")
        return 'N/A'

# Function to fetch historical stock prices for the past 5 days
def fetch_historical_prices(ticker):
    try:
        api_url = f"https://yfapi.net/v8/finance/chart/{ticker}?range=5d&interval=1d"
        headers = {
            'x-api-key': API_KEY
        }
        response = requests.get(api_url, headers=headers)
        response.raise_for_status()
        data = response.json()

        if data and 'chart' in data and data['chart']['result']:
            timestamps = data['chart']['result'][0]['timestamp']
            prices = data['chart']['result'][0]['indicators']['quote'][0]['high']
            return timestamps, prices
        else:
            print("No historical data found.")
            return None, None
    except requests.exceptions.RequestException as e:
        print(f"Error fetching historical data for {ticker}: {e}")
        return None, None

# Main function to run the program
def main():
    # Get user input for the stock ticker
    ticker = input("Enter the ticker symbol of the stock: ").upper()

    # Fetch stock data
    stock_data = fetch_stock_data(ticker)

    if stock_data:
        # Display stock information
        print("\nStock Information:")
        for key, value in stock_data.items():
            print(f"{key}: {value}")

        # Save data to a CSV file
        df = pd.DataFrame([stock_data])
        df.to_csv(f"{ticker}_stock_data.csv", index=False)
        print(f"\nStock data saved to {ticker}_stock_data.csv")

        # Display top 5 trending stocks
        print("\nTop 5 Trending Stocks in the US:")
        trending_stocks = fetch_trending_stocks()
        for i, stock in enumerate(trending_stocks, start=1):
            print(f"{i}. {stock['Ticker']} - {stock['Name']}")

        # Bonus: Plot historical stock prices
        timestamps, prices = fetch_historical_prices(ticker)
        if timestamps and prices:
            dates = pd.to_datetime(timestamps, unit='s')
            plt.figure(figsize=(10, 6))
            plt.plot(dates, prices, marker='o', color='blue', linestyle='-', label='High Price')
            plt.title(f'Historical High Prices of {ticker} Over the Past 5 Days')
            plt.xlabel('Date')
            plt.ylabel('High Price (USD)')
            plt.xticks(rotation=45)
            plt.legend()
            plt.tight_layout()
            plt.show()
    else:
        print("Failed to retrieve stock data. Please check the ticker symbol and try again.")

if __name__ == "__main__":
    main()

#I used OpenAI and Stackoverflow to help with this assignment 