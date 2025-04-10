
from aiogram.types import  InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardButton
from aiogram.types.web_app_info import WebAppInfo
import logging

from infrastructure.database.models import button
from typing import List

def getButton(button: button):
        
        if button.web_app_link:
            webapp = WebAppInfo(
            url=button.web_app_link
            )
            return InlineKeyboardButton(
                text=button.button_text,
                web_app=webapp
            )
        else:
            return InlineKeyboardButton(
                text=button.button_text,
                callback_data=button.callback_data
            )

def StandardMenu(ButtonsData: List[button]):

    keyboard = InlineKeyboardBuilder()
    for button in ButtonsData:
        newbutton = getButton(button)
        keyboard.row(newbutton)

    return keyboard.as_markup()