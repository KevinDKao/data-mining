# Import required libraries
import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta

# Set the stock symbol (ticker)
ticker = "AAPL"  # Example using Apple stock

# Create a Ticker object
stock = yf.Ticker(ticker)

# Get basic stock info
info = stock.info
print(f"Company Name: {info['longName']}")
print(f"Current Price: ${info['currentPrice']}")

# Download historical data (last 1 year)
end_date = datetime.now()
start_date = end_date - timedelta(days=365)
hist_data = stock.history(start=start_date, end=end_date)

# Save historical data to CSV
hist_data.to_csv(f"{ticker}_historical_data.csv")

# Get company financials
balance_sheet = stock.balance_sheet
income_stmt = stock.income_stmt
cash_flow = stock.cashflow

# Save financial statements to Excel
with pd.ExcelWriter(f"{ticker}_financials.xlsx") as writer:
    balance_sheet.to_excel(writer, sheet_name='Balance Sheet')
    income_stmt.to_excel(writer, sheet_name='Income Statement')
    cash_flow.to_excel(writer, sheet_name='Cash Flow')

# Get additional information
print("\nDividend Data:")
print(stock.dividends)

print("\nSplit Data:")
print(stock.splits)

# Get institutional holders
print("\nMajor Holders:")
print(stock.major_holders)

# Get news
print("\nRecent News:")
news = stock.news
for item in news[:5]:  # Show last 5 news items
    print(f"Title: {item['title']}")
    print(f"Link: {item['link']}")
    print("---")

# Get recommendations
print("\nAnalyst Recommendations:")
print(stock.recommendations)

# Get options data
expirations = stock.options  # Get available expiration dates
if len(expirations) > 0:
    # Get options chain for the nearest expiration
    opt = stock.option_chain(expirations[0])
    
    # Save calls and puts to CSV
    opt.calls.to_csv(f"{ticker}_calls.csv")
    opt.puts.to_csv(f"{ticker}_puts.csv")