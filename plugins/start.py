from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("Channel", url="https://t.me/ML_BotUpdates")],
        [InlineKeyboardButton(
            "Report Bugs 😊", url="https://t.me/ML_SupportGroup")]
    ])
    
    welcomed = f"Hey <b>{message.from_user.first_name}</b>\n a Simple YouTube Downloader Bot that can:
  ➠ Download YouTube videos
  ➠ Download audio from YouTube videos

NB:  Bot may slow ,so wait 5 - 10 second to bot respond....
please dont spam with links.../help for More info"
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagation
