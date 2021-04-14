from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("Channel", url="https://t.me/ML_BotUpdates")],
        [InlineKeyboardButton(
            "Report Bugs 😊", url="https://t.me/ML_SupportGroup")]
    ])
    welcomed = f"**Hey [{}](tg://user?id={})</b>\n/help for More info"
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagation
