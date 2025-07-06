import requests

TOKEN = "8136421090:AAFrb8RI6BQ2tH49YXX_5S32_W0yWfT04Cg"
CHAT_ID = "570096331"

def send_message(text):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": text}
    try:
        res = requests.post(url, json=payload)
        print("✅ پیام ارسال شد:", res.text)
    except Exception as e:
        print("❌ خطا در ارسال پیام:", e)

if __name__ == "__main__":
    send_message("🚀 تست موفق Railway")