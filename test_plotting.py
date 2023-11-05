from main import plot_stock_price

# Replace 'AAPL' with a valid stock ticker symbol
ticker = 'AAPL'
image_path = plot_stock_price(ticker)
print(f"Plot saved at {image_path}")
