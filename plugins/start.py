from modules.config import (
    START_PIC, 
    BOT_USERNAME,
    SUPPORT_GROUP,
    OWNER_USERNAME,
    UPDATES_CHANNEL,
)
from modules.helpers.filters import command
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message



@Client.on_message(
    command(["start", f"start@{BOT_USERNAME}"]) & filters.private & ~filters.edited
)
async def start_private(client: Client, message: Message):
 await message.reply_photo(
        photo=f"{START_PIC}",
        caption=f"""**๐ฅ ๐๐๐ฅ๐ฅ๐จ, ๐ ๐๐ฆ ๐๐ฎ๐ฉ๐๐ซ๐๐๐ฌ๐ญ ๐๐ข๐ ๐ก ๐๐ฎ๐๐ฅ๐ข๐ญ๐ฒ
๐๐จ ๐๐๐  ๐๐ ๐๐ฎ๐ฌ๐ข๐ ๐๐ฅ๐๐ฒ๐๐ซ ๐๐จ๐ญ ๐ ๐๐ฎ๐ฌ๐ญ ๐๐๐ ๐๐ ยป ๐๐จ ๐๐จ๐ฎ๐ซ ๐๐ซ๐จ๐ฎ๐ฉ ๐๐ง๐
๐๐ง๐ฃ๐จ๐ฒ ๐๐ฎ๐ฉ๐๐ซ ๐๐ฎ๐๐ฅ๐ข๐ญ๐ฒ โฅ๏ธ๐๐ฎ๐ฌ๐ข๐.**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "โ ๐๐๐ ๐๐ ๐๐จ ๐๐จ๐ฎ๐ซ ๐๐ซ๐จ๐ฎ๐ฉ โ",
                        url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                    )
                ],
                [
                    InlineKeyboardButton("โจ๐๐๐๐ฉ๐'๐ฑ๐๐ฅ", url=f"https://t.me/{OWNER_USERNAME}"),
                    InlineKeyboardButton("๐ค ๐ฟ๐ฉ๐๐๐๐๐๐ฉ๐'๐ฑ๐ ๐ฅ", url=f"https://t.me/MAGNESIUM_XD"),
                ],
                [
                    InlineKeyboardButton(
                        "๐ป๐๐๐๐๐๐๐โข๐ถ๐ป๐ด๐๐", url=f"{SUPPORT_GROUP}"
                    ),
                    InlineKeyboardButton(
                        "๐ฅ๐๐๐ฟ๐ผ๐๐ฉ๐โข๐พ๐๐ผ๐๐๐ฉ๐๐ก", url=f"{UPDATES_CHANNEL}"
                    ),
                ],
            ]
        ),
    )


