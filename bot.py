import requests
import time

TOKEN = "BIBIAE0UGUKKYHUSAHIYNBOTPRIHTDKXXZYXRURWGLAIHDYVFZOMGRGWVHUVVMJY"
API = "https://botapi.rubika.ir/v3"

offset = 0

print("ID BOT STARTED 🚀")


def get_updates(offset):
    try:
        r = requests.post(API + "/getUpdates", json={
            "token": TOKEN,
            "offset": offset
        }, timeout=10)

        return r.json()

    except Exception as e:
        print("GET_UPDATES_ERROR:", e)
        return {}


def send_message(chat_id, text):
    try:
        requests.post(API + "/sendMessage", json={
            "token": TOKEN,
            "chat_id": chat_id,
            "text": text
        }, timeout=10)

    except Exception as e:
        print("SEND_ERROR:", e)


while True:
    data = get_updates(offset)

    if not data or "result" not in data:
        time.sleep(2)
        continue

    for update in data["result"]:
        offset = update["update_id"] + 1

        try:
            msg = update.get("message", {})
            user_id = msg.get("from", {}).get("id")

            if not user_id:
                continue

            print("USER:", user_id)

            send_message(
                user_id,
                f"👤 آیدی شما:\n{user_id}"
            )

        except Exception as e:
            print("PARSE_ERROR:", e)

    time.sleep(1)