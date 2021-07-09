from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton



@Client.on_message(
    filters.command("start")
    & filters.private
    & ~ filters.edited
)
async def start_(client: Client, message: Message):
    await message.reply_sticker("CAACAgEAAxkBAAEJbcdgfc0EbBXPwD9Xy4Rl7UDsqcruzQACeQIAAqcI6Uf9k-kK7H0fxR8E")
    await message.reply_text(
        f"""<b>Hey {format(
        message.from_user.mention)}! Hii
I am powerful VC music Bot..🔥
I can play songs in your group's VC 😉

To listen songs also add @DANISHMUSICBOT to your group..

And don't forgot to promote me with all rights..😉
Otherwise I can't play songs..🙄

Use the buttons below to know more about me..🔥
 </b>""",
      
       
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Music World 🌍", url="https://t.me/wearefriendscircle",
                    )
                ],
                [
                    InlineKeyboardButton(
                        "Official Clan 🔥", url="https://t.me/weopsecretfighters"
                    ),
                    InlineKeyboardButton(
                        "My Creator 😎", url="https://t.me/idanishbaba"
                    ),
                    InlineKeyboardButton(
                        "⚔️ Commands", url="https://telegra.ph/MusicBot-Robot-MusicBot-Robo-03-14"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "➕ Add To Your Group ➕", url="https://t.me/danishbabamusic2_bot?startgroup=true"
                    )
                ]
            ]
        )
    )

@Client.on_message(
    filters.command("start")
    & filters.group
    & ~ filters.edited
)
async def start(client: Client, message: Message):
    await message.reply_text(
        "💁🏻‍♂️ Do you want to search for a YouTube video?",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "✅ Yes", switch_inline_query_current_chat=""
                    ),
                    InlineKeyboardButton(
                        "No ❌", callback_data="close"
                    )
                ]
            ]
        )
    )
