import json
import threading
import time
import requests
import websocket

TOKEN = "BIBIAE0UGUKKYHUSAHIYNBOTPRIHTDKXXZYXRURWGLAIHDYVFZOMGRGWVHUVVMJY"

WS_URL = "wss://botws.rubika.ir/websocket"  # WebSocket endpoint (ممکنه بسته به اکانت تغییر کنه)
API_URL = "https://botapi.rubika.ir/v3"


print("ID BOT STARTED 🚀")


def send_message(chat_id, text):
    try:
        requests.post(
            API_URL + "/sendMessage",
            json={
                "token": TOKEN,
                "chat_id": chat_id,
                "text": text
            },
            timeout=10
        )
    except Exception as e:
        print("SEND ERROR:", e)


def on_message(ws, message):
    try:
        data = json.loads(message)

        print("RAW:", data)

        msg = data.get("message", {})
        user_id = msg.get("from", {}).get("id") or msg.get("author_guid")

        if not user_id:
            return

        print("USER ID:", user_id)

        send_message(user_id, f"👤 آیدی شما:\n{user_id}")

    except Exception as e:
        print("PARSE ERROR:", e)


def on_error(ws, error):
    print("WS ERROR:", error)


def on_close(ws, close_status_code, close_msg):
    print("WS CLOSED - reconnecting in 3s...")
    time.sleep(3)
    start_ws()


def on_open(ws):
    print("WS CONNECTED")

    # authenticate (بسته به API ممکنه متفاوت باشه)
    auth_payload = {
        "type": "auth",
        "token": TOKEN
    }

    ws.send(json.dumps(auth_payload))


def start_ws():
    ws = websocket.WebSocketApp(
        WS_URL,
        on_message=on_message,
        on_error=on_error,
        on_close=on_close,
        on_open=on_open
    )

    ws.run_forever()


start_ws()