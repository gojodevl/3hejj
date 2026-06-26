from rubika import Bot
from config import TOKEN


bot = Bot(token=TOKEN)


@bot.on_message()
def message(update):

    uid = update.message.author_guid
    text = update.message.text

    bot.send_message(
        uid,
        f"""
👤 اطلاعات شما:

ID:
{uid}

پیام شما:
{text}
"""
    )


print("ID BOT STARTED")

bot.run()
