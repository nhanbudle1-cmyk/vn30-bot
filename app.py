from flask import Flask, request
import requests
import os

app = Flask(__name__)

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

@app.route("/")
def home():
    return "server dang chay"

@app.route("/webhook", methods=["GET", "POST"])
def webhook():
    if request.method == "POST":
        data = request.get_json(silent=True) or {}
        signal = data.get("signal", "N/A")
        price = data.get("price", "N/A")
        time = data.get("time", "N/A")
    else:
        signal = request.args.get("signal", "N/A")
        price = request.args.get("price", "N/A")
        time = request.args.get("time", "N/A")

    text = f"🚨 TIN HIEU VN30 🚨\nLenh: {signal}\nGia: {price}\nTime: {time}"

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    r = requests.post(url, data={"chat_id": CHAT_ID, "text": text})

    return f"ok - {r.status_code}"

if __name__ == "__main__":
    app.run()
