from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from WOODStream.config import Telegram

class LANG(object):

    START_TEXT = """
<b>👋 ʜᴇʏ, </b>{}\n 
<b>ɪ'ᴍ ᴛᴇʟᴇɢʀᴀᴍ ғɪʟᴇ sᴛʀᴇᴀᴍ ʙᴏᴛ ᴀs ᴡᴇʟʟ ᴀs ᴅɪʀᴇᴄᴛ ʟɪɴᴋ ɢᴇɴᴇʀᴀᴛᴏʀ ʙᴏᴛ</b>\n
<b>ᴡᴏʀᴋɪɴɢ ᴏɴ ᴄʜᴀɴɴᴇʟs ᴀɴᴅ ᴘʀɪᴠᴀᴛᴇ ᴄʜᴀᴛ</b>"""

    HELP_TEXT = """
<b>- ᴀᴅᴅ ᴍᴇ ᴀs ᴀɴ ᴀᴅᴍɪɴ ᴏɴ ᴛʜᴇ ᴄʜᴀɴɴᴇʟ</b>
<b>- sᴇɴᴅ ᴍᴇ ᴀɴʏ ғɪʟᴇ</b>
<b>- ɪ'ʟʟ ᴘʀᴏᴠɪᴅᴇ sᴛʀᴇᴀᴍᴀʙʟᴇ ʟɪɴᴋ</b>\n
<b>🔞 ᴀᴅᴜʟᴛ ᴄᴏɴᴛᴇɴᴛ sᴛʀɪᴄᴛʟʏ ᴘʀᴏʜɪʙɪᴛᴇᴅ.</b>"""

    ABOUT_TEXT = """
<b>⚜ ᴍʏ ɴᴀᴍᴇ : {}</b>\n
<b>✦ ᴠᴇʀsɪᴏɴ : {}</b>
<b>✦ ᴏᴡɴᴇʀ : <a href='https://telegram.me/svnig7'>❖ sᴠɴ ❖ ™</a></b>\n
"""

    STREAM_TEXT = """
<b>ғɪʟᴇ ɴᴀᴍᴇ :</b> <code>{}</code>\n
<b>ғɪʟᴇ sɪᴢᴇ :</b> <code>{}</code>\n
<b>ᴅᴏᴡɴʟᴏᴀᴅ ʟɪɴᴋ :</b> <code>{}</code>\n
<b>sᴛʀᴇᴀᴍ ʟɪɴᴋ :</b> <code>{}</code>\n
<b>ғɪʟᴇ ʟɪɴᴋ :</b> <code>{}</code>\n"""

    STREAM_TEXT_X = """
<b>ғɪʟᴇ ɴᴀᴍᴇ :</b> <b>{}</b>\n
<b>ғɪʟᴇ sɪᴢᴇ :</b> <code>{}</code>\n
<b>ᴅᴏᴡɴʟᴏᴀᴅ ʟɪɴᴋ :</b> <code>{}</code>\n
<b>ғɪʟᴇ ʟɪɴᴋ :</b> <code>{}</code>\n"""


    BAN_TEXT = "sᴏʀʀʏ sɪʀ, ʏᴏᴜ ᴀʀᴇ ʙᴀɴɴᴇᴅ ᴛᴏ ᴜsᴇ ᴍᴇ\n\n**[ ᴄᴏɴᴛᴀᴄᴛ ᴅᴇᴠ ](tg://user?id={}) ᴛʜᴇʏ ᴡɪʟʟ ʜᴇʟᴘ ʏᴏᴜ**"


class BUTTON(object):
    START_BUTTONS = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton('ʜᴇʟᴘ', callback_data='help'),
            InlineKeyboardButton('ᴀʙᴏᴜᴛ', callback_data='about'),
            InlineKeyboardButton('ᴄʟᴏsᴇ', callback_data='close')
        ],
            [InlineKeyboardButton("ᴜᴘᴅᴀᴛᴇ ᴄʜᴀɴɴᴇʟ", url=f'https://t.me/{Telegram.UPDATES_CHANNEL}')]
        ]
    )
    HELP_BUTTONS = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton('ʜᴏᴍᴇ', callback_data='home'),
            InlineKeyboardButton('ᴀʙᴏᴜᴛ', callback_data='about'),
            InlineKeyboardButton('ᴄʟᴏsᴇ', callback_data='close'),
        ],
            [InlineKeyboardButton("ᴜᴘᴅᴀᴛᴇ ᴄʜᴀɴɴᴇʟ", url=f'https://t.me/{Telegram.UPDATES_CHANNEL}')]
        ]
    )
    ABOUT_BUTTONS = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton('ʜᴏᴍᴇ', callback_data='home'),
            InlineKeyboardButton('ʜᴇʟᴘ', callback_data='help'),
            InlineKeyboardButton('ᴄʟᴏsᴇ', callback_data='close'),
        ],
            [InlineKeyboardButton("ᴜᴘᴅᴀᴛᴇ ᴄʜᴀɴɴᴇʟ", url=f'https://t.me/{Telegram.UPDATES_CHANNEL}')]
        ]
    )
