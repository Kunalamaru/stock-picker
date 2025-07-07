import streamlit as st
from predictor import generate_trade_signal
from streamlit_autorefresh import st_autorefresh

# 🔁 Auto-refresh every 5 minutes (300,000 ms)
st_autorefresh(interval=300000, key="refresh")

st.set_page_config(page_title="📈 Smart Trade App", layout="centered")
st.title("📌 Trade Ideas (Auto-Learning)")

stocks = ["INFY.NS", "RELIANCE.NS", "TCS.NS", "ICICIBANK.NS"]
results = []

for symbol in stocks:
    signal = generate_trade_signal(symbol)
    if signal:
        results.append(signal)

if results:
    st.write("### 📊 Best Entry Opportunities")
    st.table(results)
else:
    st.warning("No good setups found right now.")
