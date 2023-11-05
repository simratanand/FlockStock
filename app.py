from flask import Flask, request, render_template
import subprocess

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        ticker = request.form['ticker']
        results = get_stock_info(ticker)
        return render_template('results.html', results=results)
    return render_template('index.html')

def get_stock_info(ticker):
    commands = [
        f"get_stock_price {ticker}",
        f"calculate_SMA {ticker} 20",
        f"calculate_EMA {ticker} 20",
        f"calculate_RSI {ticker}",
        f"calculate_MACD {ticker}"
    ]
    results = []

    for command in commands:
        process = subprocess.Popen(["python", "main.py"], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        output, _ = process.communicate(input=command)
        results.append(output)

    return results

if __name__ == '__main__':
    app.run(debug=True)

