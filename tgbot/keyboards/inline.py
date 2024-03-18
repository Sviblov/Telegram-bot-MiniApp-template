
from aiogram.types import  InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardButton

from infrastructure.database.models import button
from typing import List



def StandardMenu(ButtonsData: List[button]):

    keyboard = InlineKeyboardBuilder()
    for button in ButtonsData:
        newbutton = InlineKeyboardButton(
            text=button.button_text,
            callback_data=button.callback_data
            )
        keyboard.row(newbutton)

    return keyboard.as_markup()