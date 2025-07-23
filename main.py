import requests
import time

# ==== CONFIG ====
BOT_TOKEN = "YOUR_TOKEN_HERE"
CHAT_ID = "ID_HERE"
TARGET_PRICE = 97  # Change this to the price you want alert for
COIN_ID = "litecoin"  # Options: bitcoin, ethereum, litecoin, etc.
CURRENCY = "usd"
CHECK_INTERVAL = 60  # in seconds

# ==== FUNCTION ====
def get_price():
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={COIN_ID}&vs_currencies={CURRENCY}"
    response = requests.get(url)
    data = response.json()
    return data[COIN_ID][CURRENCY]

def send_alert(price):
    text = f"🚨 Alert! {COIN_ID.capitalize()} price is now ${price}"
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": text}
    requests.post(url, data=data)

# ==== LOOP ====
print("🔄 Bot is running...")
while True:
    try:
        price = get_price()
        print(f"{COIN_ID} = ${price}")
        if price >= TARGET_PRICE:
            send_alert(price)
            print("✅ Alert sent!")
            break  # stop after first alert
        time.sleep(CHECK_INTERVAL)
    except Exception as e:
        print("Error:", e)
        time.sleep(10)
