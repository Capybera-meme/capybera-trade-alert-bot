import os
import requests
from flask import Flask

app = Flask(__name__)

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL = "@CAPYBERA_Official"


def send_telegram_message(message):
    if not BOT_TOKEN:
        return {"ok": False, "error": "BOT_TOKEN is not configured"}

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    response = requests.post(
        url,
        data={
            "chat_id": CHANNEL,
            "text": message,
            "parse_mode": "HTML",
            "disable_web_page_preview": True
        },
        timeout=20
    )

    return response.json()


@app.route("/")
def home():
    return "CAPYBERA TRADE ALERT is running."


@app.route("/demo/buy")
def demo_buy():
    message = """🟢 <b>CAPYBERA BUY — DEMO</b>

💰 Amount: 0.50 SOL
💵 Value: $95.20
🪙 Tokens: 1,500,000 CAPYBERA
👛 Wallet: 7xK...9Pq
📈 Price: $0.0000634

⚠️ <b>DEMO ALERT</b> — Not a real blockchain transaction."""

    result = send_telegram_message(message)

    if result.get("ok"):
        return "Demo BUY alert sent successfully."

    return f"Telegram error: {result}", 500


@app.route("/demo/sell")
def demo_sell():
    message = """🔴 <b>CAPYBERA SELL — DEMO</b>

💰 Amount: 0.25 SOL
💵 Value: $47.60
🪙 Tokens: 750,000 CAPYBERA
👛 Wallet: 9Ab...3Xy
📉 Price: $0.0000634

⚠️ <b>DEMO ALERT</b> — Not a real blockchain transaction."""

    result = send_telegram_message(message)

    if result.get("ok"):
        return "Demo SELL alert sent successfully."

    return f"Telegram error: {result}", 500


if __name__ == "__main__":
    port = int(os.getenv("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
