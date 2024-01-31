from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message

from config import OWNER_ID


def filter(cmd: str):
    return filters.private & filters.incoming & filters.command(cmd)

@Client.on_message(filter("start"))
async def start(bot: Client, msg: Message):
    me2 = (await bot.get_me()).mention
    await bot.send_message(
        chat_id=msg.chat.id,
        text=f"""𝖧𝐞𝐲 {msg.from_user.mention},

𝖨 𝖠𝐦 {me2},
𝖳𝖱𝖴𝖲𝖳𝖤𝖣 𝖲𝖳𝖱𝖨𝖭𝖦 𝖦𝖤𝖭𝖤𝖱𝖠𝖳𝖮𝖱 𝖡𝖮𝖳.
𝖥𝖴𝖫𝖫𝖸 𝖲𝖠𝖥𝖤 & 𝖲𝖤𝖢𝖴𝖱𝖤.
𝖭𝖮  𝖤𝖱𝖱𝖮𝖱.

𝖬𝐚𝐝𝐞 𝖡𝐲  : [𝖳𝖤𝖠𝖬 𝖣𝖠𝖷𝖷](tg://user?id={OWNER_ID}) !""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(text="𝖦𝖤𝖭𝖤𝖱𝖠𝖳𝖤 𝖲𝖳𝖱𝖨𝖭𝖦", callback_data="generate")
                ],
                [
                    InlineKeyboardButton(" 𝖲𝐮𝐩𝐩𝐨𝐫𝐭", url="https://t.me/AllPremiumCc"),
                    InlineKeyboardButton("𝖮𝐟𝐟𝐢𝐜𝐞", url="https://t.me/ALLTYPECC")
                ]
            ]
        ),
        disable_web_page_preview=True,
    )
