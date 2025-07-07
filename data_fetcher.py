import yfinance as yf
import requests
from bs4 import BeautifulSoup

def get_current_price(symbol):
    data = yf.Ticker(symbol).history(period="1d")
    return round(data['Close'].iloc[-1], 2)

def get_rsi(symbol, period=14):
    data = yf.Ticker(symbol).history(period="1mo", interval="1d")
    delta = data['Close'].diff()
    gain = delta.where(delta > 0, 0).rolling(period).mean()
    loss = -delta.where(delta < 0, 0).rolling(period).mean()
    rs = gain / loss
    rsi = 100 - (100 / (1 + rs))
    return round(rsi.iloc[-1], 2)

def get_yahoo_news(symbol):
    url = f"https://finance.yahoo.com/quote/{symbol}?p={symbol}"
    response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
    soup = BeautifulSoup(response.text, "html.parser")
    news_items = soup.find_all("h3")
    return [item.text for item in news_items][:3]
