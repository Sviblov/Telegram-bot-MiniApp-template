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

from tgbot.keyboards.inline import StandardMenu
from tgbot.services.services import send_invoice
from tgbot.states import UserStates



user_callbacks_router = Router()
logger = logging.getLogger(__name__)
@user_callbacks_router.callback_query(F.data.in_({"start"}), StateFilter(UserStates.counter))
async def user_start(callback: CallbackQuery, state: FSMContext, repo: RequestsRepo, bot: Bot, user: User):
    await callback.answer()
    data= await state.get_data()
    counter=data['counter']
    replyText=await repo.interface.get_MessageText('welcome_not_admin')
    replyTextFormatted = replyText.format(user.full_name, counter)
    replyButtons= await repo.interface.get_ButtonLables('welcome_not_admin')
    replyMarkup=StandardMenu(replyButtons)
    await bot.send_message(user.user_id, replyTextFormatted, reply_markup=replyMarkup)

@user_callbacks_router.callback_query(F.data.in_({"plusCounter","minusCounter"}), StateFilter(UserStates.counter))
async def updateCounter(callback: CallbackQuery, state: FSMContext, repo: RequestsRepo, bot: Bot, user: User):
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

@user_callbacks_router.callback_query(F.data.in_({"createInvoice"}), StateFilter(UserStates.counter))
async def createInvoice(callback: CallbackQuery, state: FSMContext, repo: RequestsRepo, bot: Bot, user: User):
    await callback.answer()
    
    #TODO: сделать чтобы инвойс был на значение счетчика
    data = await state.get_data()
    counter = data['counter']
    if counter>0:
        amount = counter
        invoice = await repo.payment.createInvoice(user.user_id, amount)
        replyText=await repo.interface.get_MessageText('invoice_text')
        invoiceTitle = await repo.interface.get_MessageText('invoice_title')
        
        invoice = await send_invoice(bot, callback.message.chat.id, replyText,invoiceTitle, amount, str(invoice.invoice_id))
        
        
    else:
       
        replyText=await repo.interface.get_MessageText('negative_counter')
        replyButtons= await repo.interface.get_ButtonLables('negative_counter')
        replyMarkup=StandardMenu(replyButtons)
        await bot.send_message(user.user_id, replyText, reply_markup=replyMarkup)

    