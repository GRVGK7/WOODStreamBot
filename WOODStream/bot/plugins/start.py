import logging
import math
from WOODStream import __version__
from WOODStream.bot import WOODStream
from WOODStream.server.exceptions import FIleNotFound
from WOODStream.utils.bot_utils import gen_linkx, verify_user
from WOODStream.config import Telegram
from WOODStream.utils.database import Database
from WOODStream.utils.translation import LANG, BUTTON
from pyrogram import filters, Client
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.enums.parse_mode import ParseMode
import asyncio

db = Database(Telegram.DATABASE_URL, Telegram.SESSION_NAME)

@WOODStream.on_message(filters.command('start') & filters.private)
async def start(bot: Client, message: Message):
    if not await verify_user(bot, message):
        return
    usr_cmd = message.text.split("_")[-1]

    if usr_cmd == "/start":
        if Telegram.START_PIC:
            await message.reply_photo(
                photo=Telegram.START_PIC,
                caption=LANG.START_TEXT.format(message.from_user.mention, WOODStream.username),
                parse_mode=ParseMode.HTML,
                reply_markup=BUTTON.START_BUTTONS
            )
        else:
            await message.reply_text(
                text=LANG.START_TEXT.format(message.from_user.mention, WOODStream.username),
                parse_mode=ParseMode.HTML,
                disable_web_page_preview=True,
                reply_markup=BUTTON.START_BUTTONS
            )
    else:
        if "stream_" in message.text:
            try:
                file_check = await db.get_file(usr_cmd)
                file_id = str(file_check['_id'])
                if file_id == usr_cmd:
                    reply_markup, stream_text = await gen_linkx(m=message, _id=file_id,
                                                                name=[WOODStream.username, WOODStream.fname])
                    await message.reply_text(
                        text=stream_text,
                        parse_mode=ParseMode.HTML,
                        disable_web_page_preview=True,
                        reply_markup=reply_markup,
                        quote=True
                    )

            except FIleNotFound as e:
                await message.reply_text("**ғɪʟᴇ ɴᴏᴛ ғᴏᴜɴᴅ**")
            except Exception as e:
                await message.reply_text("sᴏᴍᴇᴛʜɪɴɢ ᴡᴇɴᴛ ᴡʀᴏɴɢ")
                logging.error(e)

        elif "file_" in message.text:
            try:
                file_check = await db.get_file(usr_cmd)
                db_id = str(file_check['_id'])
                file_id = file_check['file_id']
                file_name = file_check['file_name']
                if db_id == usr_cmd:
                    filex = await message.reply_cached_media(file_id=file_id, caption=f'**{file_name}**')
                    await asyncio.sleep(3600)
                    try:
                        await filex.delete()
                        await message.delete()
                    except Exception:
                        pass

            except FIleNotFound as e:
                await message.reply_text("**ғɪʟᴇ ɴᴏᴛ ғᴏᴜɴᴅ**")
            except Exception as e:
                await message.reply_text("sᴏᴍᴇᴛʜɪɴɢ ᴡᴇɴᴛ ᴡʀᴏɴɢ")
                logging.error(e)

        else:
            await message.reply_text(f"**ɪɴᴠᴀʟɪᴅ ᴄᴏᴍᴍᴀɴᴅ**")

@WOODStream.on_message(filters.private & filters.command(["about"]))
async def start(bot, message):
    if not await verify_user(bot, message):
        return
    if Telegram.START_PIC:
        await message.reply_photo(
            photo=Telegram.START_PIC,
            caption=LANG.ABOUT_TEXT.format(WOODStream.fname, __version__),
            parse_mode=ParseMode.HTML,
            reply_markup=BUTTON.ABOUT_BUTTONS
        )
    else:
        await message.reply_text(
            text=LANG.ABOUT_TEXT.format(WOODStream.fname, __version__),
            disable_web_page_preview=True,
            reply_markup=BUTTON.ABOUT_BUTTONS
        )

@WOODStream.on_message((filters.command('help')) & filters.private)
async def help_handler(bot, message):
    if not await verify_user(bot, message):
        return
    if Telegram.START_PIC:
        await message.reply_photo(
            photo=Telegram.START_PIC,
            caption=LANG.HELP_TEXT.format(Telegram.OWNER_ID),
            parse_mode=ParseMode.HTML,
            reply_markup=BUTTON.HELP_BUTTONS
        )
    else:
        await message.reply_text(
            text=LANG.HELP_TEXT.format(Telegram.OWNER_ID),
            parse_mode=ParseMode.HTML,
            disable_web_page_preview=True,
            reply_markup=BUTTON.HELP_BUTTONS
        )

# ---------------------------------------------------------------------------------------------------

@WOODStream.on_message(filters.command('files') & filters.private)
async def my_files(bot: Client, message: Message):
    if not await verify_user(bot, message):
        return
    user_files, total_files = await db.find_files(message.from_user.id, [1, 10])

    file_list = []
    async for x in user_files:
        file_list.append([InlineKeyboardButton(x["file_name"], callback_data=f"myfile_{x['_id']}_{1}")])
    if total_files > 10:
        file_list.append(
            [
                InlineKeyboardButton("◄", callback_data="N/A"),
                InlineKeyboardButton(f"1/{math.ceil(total_files / 10)}", callback_data="N/A"),
                InlineKeyboardButton("►", callback_data="userfiles_2")
            ],
        )
    if not file_list:
        file_list.append(
            [InlineKeyboardButton("ᴇᴍᴘᴛʏ", callback_data="N/A")],
        )
    file_list.append([InlineKeyboardButton("ᴄʟᴏsᴇ", callback_data="close")])
    await message.reply_photo(photo=Telegram.FILE_PIC,
                              caption="ᴛᴏᴛᴀʟ ғɪʟᴇs : {}".format(total_files),
                              reply_markup=InlineKeyboardMarkup(file_list))


