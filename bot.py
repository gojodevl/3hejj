from rubpy.bot import BotClient, filters
from rubpy.bot.models import Update


TOKEN = "BIBIAE0UGUKKYHUSAHIYNBOTPRIHTDKXXZYXRURWGLAIHDYVFZOMGRGWVHUVVMJY"


app = BotClient(
    token=TOKEN
)


print("ID BOT STARTED 🚀")


@app.on_update(filters.private)
async def get_id(client: BotClient, update: Update):

    user_id = update.new_message.sender_id

    print("USER ID:", user_id)

    await update.reply(
        f"👤 شناسه شما:\n\n{user_id}"
    )


app.run()