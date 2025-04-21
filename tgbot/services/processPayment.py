
from aiogram import Bot
from infrastructure.database.repo.requests import RequestsRepo
from infrastructure.database.models.users import User
from infrastructure.database.models.payment import Invoice 

from tgbot.services.services import send_message
from typing import Union

from tgbot.keyboards.inline import StandardMenu

async def processPayment(
    repo: RequestsRepo,
    invoice: Invoice,
    bot: Bot,
    user: User,
):
    """
    Process payment
    """
    amount=invoice.amount
    messageText = await repo.interface.get_MessageText('payment_success')
    messageTextFormatted = messageText.format(amount)
    messageButtons = await repo.interface.get_ButtonLables('payment_success')
    messageMarkup = StandardMenu(messageButtons)

    
    await send_message(
        bot=bot,
        user_id=user.user_id,
        text=messageTextFormatted,
        reply_markup=messageMarkup,
        repo=repo,
    )
    
