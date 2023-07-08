from typing import Union

from pyrogram import filters, types
from pyrogram.types import InlineKeyboardMarkup, Message

import config
from config import BANNED_USERS
from strings import get_command, get_string, managements
from AarohiX import app
from AarohiX.misc import SUDOERS
from AarohiX.utils import management_pannel
from AarohiX.utils.database import get_lang, is_commanddelete_on
from AarohiX.utils.decorators.language import (LanguageStart,
                                                  languageCB)
from AarohiX.utils.inline.management import (management_back_markup,
                                          private_management_panel)

### Command
MANAGEMENT_COMMAND = get_command("MANAGEMENT_COMMAND")


@app.on_message(
    filters.command(MANAGEMENT_COMMAND)
    & filters.private
    & ~filters.edited
    & ~BANNED_USERS
)
@app.on_callback_query(
    filters.regex("settings_back_helper") & ~BANNED_USERS
)
async def helper_private(
    client: app, update: Union[types.Message, types.CallbackQuery]
):
    is_callback = isinstance(update, types.CallbackQuery)
    if is_callback:
        try:
            await update.answer()
        except:
            pass
        chat_id = update.message.chat.id
        language = await get_lang(chat_id)
        _ = get_string(language)
        keyboard = management_pannel(_, True)
        if update.message.photo:
            await update.edit_message_text(
                _["management_1"].format(config.SUPPORT_HEHE), reply_markup=keyboard
            )
        else:
            await update.edit_message_text(
                _["management_1"].format(config.SUPPORT_HEHE), reply_markup=keyboard
            )
    else:
        chat_id = update.chat.id
        if await is_commanddelete_on(update.chat.id):
            try:
                await update.delete()
            except:
                pass
        language = await get_lang(chat_id)
        _ = get_string(language)
        keyboard = management_pannel(_)
        await update.reply_sticker("CAACAgUAAxkBAAIjVmKPYTFByKZlCo9d8mUv8QVAJEw7AAL9BQACiy14VGoQxOCDfE1KJAQ")
        await update.reply_photo(
            photo=config.START_IMG_URL,
            caption=_["management_1"].format(config.SUPPORT_HEHE), reply_markup=keyboard)


@app.on_message(
    filters.command(MANAGEMENT_COMMAND)
    & filters.group
    & ~filters.edited
    & ~BANNED_USERS
)
@LanguageStart
async def management_com_group(client, message: Message, _):
    keyboard = private_management_panel(_)
    await message.reply_photo(
        photo=config.START_IMG_URL,
        caption=_["management_2"], reply_markup=InlineKeyboardMarkup(keyboard)
    )


@app.on_callback_query(filters.regex("management_callback") & ~BANNED_USERS)
@languageCB
async def helper_cb(client, CallbackQuery, _):
    callback_data = CallbackQuery.data.strip()
    cb = callback_data.split(None, 1)[1]
    keyboard = management_back_markup(_)
            return await CallbackQuery.answer()
    try:
        await CallbackQuery.answer()
    except:
        pass
    if cb == "hb1":
        await CallbackQuery.edit_message_text(
            managements.MANAGEMENT_1, reply_markup=keyboard
        )
    elif cb == "hb2":
        await CallbackQuery.edit_message_text(
            managements.MANAGEMENT_2, reply_markup=keyboard
        )
    elif cb == "hb3":
        await CallbackQuery.edit_message_text(
            managements.MANAGEMENT_3, reply_markup=keyboard
        )
    elif cb == "hb4":
        await CallbackQuery.edit_message_text(
            managements.MANAGEMENT_4, reply_markup=keyboard
        )
    elif cb == "hb5":
        await CallbackQuery.edit_message_text(
            managements.MANAGEMENT_5, reply_markup=keyboard
        )
    elif cb == "hb6":
        await CallbackQuery.edit_message_text(
            managements.MANAGEMENT_6, reply_markup=keyboard
        )
    elif cb == "hb7":
        await CallbackQuery.edit_message_text(
            managements.MANAGEMENT_7, reply_markup=keyboard
        )
    elif cb == "hb8":
        await CallbackQuery.edit_message_text(
            managements.MANAGEMENT_8, reply_markup=keyboard
    elif cb == "hb9":
         await CallbackQuery.edit_message_text(
             managements.MANAGEMENT_9, reply_markup=keyboard    
        )
    elif cb == "hb10":
        await CallbackQuery.edit_message_text(
            managements.MANAGEMENT_10, reply_markup=keyboard
        )
    elif cb == "hb11":
        await CallbackQuery.edit_message_text(
            managements.MANAGEMENT_11, reply_markup=keyboard
        )
    elif cb == "hb12":
        await CallbackQuery.edit_message_text(
            managements.MANAGEMENT_12, reply_markup=keyboard
        )
    elif cb == "hb13":
        await CallbackQuery.edit_message_text(
            managements.MANAGEMENT_13, reply_markup=keyboard
        )
