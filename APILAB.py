# Using API Calls in Python with JSON and DataFrames - University Data Example

# Step 1: Making the API Call to Fetch University Data
import requests
import json
import pandas as pd
import matplotlib.pyplot as plt
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# API endpoint for fetching universities
url = "http://universities.hipolabs.com/search?country=United%20States"

# Make the GET request
response = requests.get(url)

# Check the status code
if response.status_code == 200:
    print("API request successful!")
else:
    print(f"Failed to retrieve data: {response.status_code}")

# Step 2: Parsing the JSON Response
# Parse the JSON response
university_data = response.json()

# Pretty-print the first university
print(json.dumps(university_data[0], indent=2))

# Step 3: Converting the JSON Data to a DataFrame
# Convert JSON data to a DataFrame
df = pd.DataFrame(university_data)

# Display the first few rows of the DataFrame
print(df.head())

# Step 4: Basic Data Analysis
# Count the number of universities by state
state_counts = df['state-province'].value_counts()
print(state_counts)

# Step 5: Data Visualization
# Plot the number of universities per state
state_counts.plot(kind='bar', figsize=(10, 6))
plt.title("Number of Universities per State")
plt.xlabel("State")
plt.ylabel("Number of Universities")
plt.show()

# Step 6: Extending to Multiple Countries
countries = ["United States", "Canada", "Australia", "United Kingdom"]
university_list = []

for country in countries:
    response = requests.get(f"http://universities.hipolabs.com/search?country={country}")
    data = response.json()

    for uni in data:
        uni['country'] = country
        university_list.append(uni)

# Convert to DataFrame
df_universities = pd.DataFrame(university_list)

# Display the first few rows
print(df_universities.head())

# Step 7: Visualizing University Counts by Country
# Count the number of universities per country
country_counts = df_universities['country'].value_counts()

# Plot the data
country_counts.plot(kind='bar', figsize=(10, 6))
plt.title("Number of Universities per Country")
plt.xlabel("Country")
plt.ylabel("Number of Universities")
plt.show()

# Customizing the Workshop - Fetching Stock Data from Finance API
# Get stock symbols from the user
stocks = input("Enter a list of stock symbols separated by commas (e.g., AAPL, GOOG, TSLA): ")
stock_list = [stock.strip() for stock in stocks.split(",")]

print("The Stocks we will research are: " + ", ".join(stock_list))

# Retrieve the API key from environment variable
apikey = os.getenv("API_KEY")

# API endpoint for stock quotes
url = "https://yfapi.net/v6/finance/quote"

# Prepare a list to store stock data
stock_data = []

# Loop through each stock symbol and fetch data
for stock in stock_list:
    querystring = {"symbols": stock}

    headers = {
        'x-api-key': apikey  # Trying to store my API key in an enviornment variable for privacy protection
    }

    response = requests.get(url, headers=headers, params=querystring)

    # Check if the response is successful
    if response.status_code == 200:
        stock_json = response.json()
        # Check if we received a valid result
        if stock_json['quoteResponse']['result']:
            stock_info = stock_json['quoteResponse']['result'][0]
            company_name = stock_info["longName"]
            market_price = stock_info["regularMarketPrice"]
            stock_data.append({'Company': company_name, 'Price': market_price})
            print(f"{company_name} Price: ${market_price}")
        else:
            print(f"No data found for {stock}")
    else:
        print(f"Failed to retrieve data for {stock}: {response.status_code}")

# Convert the collected stock data to a DataFrame for further analysis or visualization
df_stocks = pd.DataFrame(stock_data)

# Display the DataFrame
print("\nStock Data:")
print(df_stocks)
