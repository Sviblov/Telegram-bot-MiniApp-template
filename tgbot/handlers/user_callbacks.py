from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.types import CallbackQuery, ForceReply
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
import logging
import os
from datetime import datetime, time

from aiogram import Bot

from infrastructure.database.repo.requests import RequestsRepo
from infrastructure.database.models.users import User

from ..states import UserStates



user_callbacks_router = Router()
logger = logging.getLogger(__name__)

@user_callbacks_router.callback_query(F.data.in_({"plusCounter","minusCounter"}), StateFilter(UserStates.counter))
async def start_test(callback: CallbackQuery, state: FSMContext, repo: RequestsRepo, bot: Bot, user: User):
    await callback.answer()
   
    data = await state.get_data()
    counter = data['counter']
    if callback.data == "plusCounter":
        counter += 1
    elif callback.data == "minusCounter":
        counter -= 1

    data['counter'] = counter
    await state.set_data(data)
    
    replyText=await repo.interface.get_MessageText('welcome_not_admin')
    replyTextFormatted = replyText.format(user.full_name, data['counter'])
    await callback.message.edit_text(replyTextFormatted, reply_markup=callback.message.reply_markup)    

