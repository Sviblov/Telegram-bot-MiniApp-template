from aiogram import Router, F

from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from aiogram.types.successful_payment import SuccessfulPayment
from aiogram import types

from tgbot.services.processPayment import processPayment
from tgbot.services.mainMenu import sendMainMenu
import logging



from aiogram import Bot

from infrastructure.database.repo.requests import RequestsRepo
from infrastructure.database.models.users import User





payment_router = Router()
logger = logging.getLogger(__name__)



@payment_router.pre_checkout_query(lambda query: True)
async def precheckout_query(pre_checkout: types.PreCheckoutQuery, state: FSMContext, repo: RequestsRepo, bot: Bot):
    await bot.answer_pre_checkout_query(pre_checkout.id, ok=True)
    

    logger.info(f"Precheckout. User: {pre_checkout.from_user}, Amount: {pre_checkout.total_amount}")


@payment_router.message(F.successful_payment)
async def successful_payment(message: Message, state: FSMContext, repo: RequestsRepo, bot: Bot, user: User):
    
    paymentInfo: SuccessfulPayment = message.successful_payment
    invoiceId = paymentInfo.invoice_payload
    transactionReference = paymentInfo.telegram_payment_charge_id
    
    #process payment
    invoice = await repo.payment.payInvoice(int(invoiceId), transactionReference)

    #Issue subscription
    # Here insert what you would like to do after the payment is successful
    await processPayment(repo, invoice, bot=bot, user=user)
    
    
    logging.info(f'Payment successfull: sending message to user. User: {user.full_name}, Amount: {message.successful_payment.total_amount // 100}')
    
    #await bot.refund_star_payment(user.user_id, transactionReference)
