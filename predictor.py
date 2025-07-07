import sqlite3
from data_fetcher import get_current_price, get_rsi, get_yahoo_news
from finbert_model import analyze_sentiment
from learn_logic import get_current_thresholds, record_trade

def generate_trade_signal(symbol):
    price = get_current_price(symbol)
    rsi = get_rsi(symbol)
    news = get_yahoo_news(symbol)
    sentiment = analyze_sentiment(" ".join(news))

    thresholds = get_current_thresholds()  # from DB

    if rsi < thresholds['rsi_buy'] and sentiment > thresholds['sentiment_buy']:
        entry = price
        exit_price = round(entry * thresholds['profit_target'], 2)

        # Record this signal to DB
        record_trade(symbol, entry, exit_price, sentiment, rsi, "BUY")

        return {
            "Stock": symbol,
            "Current Price": price,
            "Entry Price": entry,
            "Estimated Exit": exit_price,
            "Time Frame": "Swing (2–4 days)"
        }

    return None
