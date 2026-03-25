import requests
import os
from flask import Flask

app = Flask(__name__)

TOKEN = os.environ.get("BOT_TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")

@app.route("/")
def home():
    return "VN30 BOT RUNNING"

def send_signal(msg):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    data = {
        "chat_id": CHAT_ID,
        "text": msg
    }
    requests.post(url, data=data)

send_signal("✅ BOT VN30 đã hoạt động")
