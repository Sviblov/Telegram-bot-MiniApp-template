
from aiogram.types import  InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardButton
from aiogram.types.web_app_info import WebAppInfo
import logging

from infrastructure.database.models import button
from typing import List

def getButton(button: button):
        

        if button.type == 'webapp':
            webapp = WebAppInfo(
            url=button.data
            )
            return InlineKeyboardButton(
                text=button.button_text,
                web_app=webapp
            )
        elif button.type == 'url':
            return InlineKeyboardButton(
                text=button.button_text,
                url=button.data
            )
        elif button.type=='callback':
            return InlineKeyboardButton(
                text=button.button_text,
                callback_data=button.data
            )
        elif button.type=='invoice':
            return InlineKeyboardButton(
                text=button.button_text,
            )
        
def StandardMenu(ButtonsData: List[button]):

    keyboard = InlineKeyboardBuilder()
    for button in ButtonsData:
        newbutton = getButton(button)
        keyboard.row(newbutton)

    return keyboard.as_markup()