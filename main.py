import os
import requests

TOKEN = os.getenv("TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

def send_message(text):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": text
    }
    try:
        res = requests.post(url, json=payload)
        print("✅ پیام ارسال شد:", res.text)
    except Exception as e:
        print("❌ خطا در ارسال پیام:", e)

if __name__ == "__main__":
    send_message("📡 سیگنال تست از ربات Railway 🚀")
