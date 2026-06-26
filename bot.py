import requests
import time

from config import TOKEN


API_URL = "https://botapi.rubika.ir/v3"


def send_message(chat_id, text):

    requests.post(
        API_URL + "/sendMessage",
        json={
            "token": TOKEN,
            "chat_id": chat_id,
            "text": text
        }
    )


def get_updates(offset):

    r = requests.post(
        API_URL + "/getUpdates",
        json={
            "token": TOKEN,
            "offset": offset
        }
    )

    return r.json()



offset = 0

print("ID BOT STARTED")


while True:

    try:

        data = get_updates(offset)


        if "result" in data:

            for update in data["result"]:

                offset = update["update_id"] + 1


                msg = update["message"]

                user_id = msg["from"]["id"]


                send_message(
                    user_id,
                    f"👤 آیدی شما:\n\n{user_id}"
                )


        time.sleep(2)


    except Exception as e:
        print(e)
        time.sleep(3)