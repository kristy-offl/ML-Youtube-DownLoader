from pyrogram import Client, Filters


@Client.on_message(Filters.command(["help"]))
async def start(client, message):
    helptxt = f"Send Youtube Link🔗. Wait For Some Sec🥺. Next Select The Desired Quality 👻"
    await message.reply_text(helptxt)
