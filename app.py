from flask import Flask, request
import requests
import os

app = Flask(__name__)

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

@app.route("/")
def home():
    return "server dang chay"

@app.route("/webhook", methods=["GET","POST"])
def webhook():
    signal = request.args.get("signal")
    price = request.args.get("price")
    time = request.args.get("time")

    text = f"🚨 TIN HIEU VN30 🚨\nLenh: {signal}\nGia: {price}\nTime: {time}"

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    requests.post(url, data={"chat_id": CHAT_ID, "text": text})

    return "ok"

if __name__ == "__main__":
    app.run()
