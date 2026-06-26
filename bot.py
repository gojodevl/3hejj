from rubpy import Bot
from config import TOKEN

bot = Bot(token=TOKEN)

print("ID BOT STARTED 🚀")

@bot.on_message()
def handler(message):

    user_id = message.author_guid
    text = message.text

    # فقط برای تست
    print("MESSAGE:", text)
    print("USER ID:", user_id)

    bot.send_message(
        user_id,
        f"👤 آیدی شما:\n{user_id}"
    )

bot.run()