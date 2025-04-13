from aiogram import Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

from aiogram.fsm.context import FSMContext

from aiogram import Bot

from infrastructure.database.repo.requests import RequestsRepo
from infrastructure.database.models.users import User

from tgbot.services.services import send_message, delete_message
from tgbot.services.put_user_to_default import putUserToDefault

from tgbot.keyboards.inline import StandardMenu

from tgbot.states import UserStates


user_messages_router = Router()


@user_messages_router.message(CommandStart())
async def user_start(message: Message, state: FSMContext, repo: RequestsRepo, bot: Bot, user: User):
    
    currentState = await state.get_state()
    if currentState == UserStates.counter:
        data= await state.get_data()
    else:  
        data= {
            'counter': 0
        }
        await state.set_data(data)

    
    await state.set_state(UserStates.counter)
    replyText=await repo.interface.get_MessageText('welcome_not_admin')
    replyTextFormatted = replyText.format(user.full_name, data['counter'])
    replyButtons= await repo.interface.get_ButtonLables('welcome_not_admin')
    replyMarkup=StandardMenu(replyButtons)
    
    await send_message(bot, user.user_id, replyTextFormatted, reply_markup=replyMarkup, repo = repo)



@user_messages_router.message(Command("delete"))
async def user_start(message: Message, state: FSMContext, repo: RequestsRepo, bot: Bot, user: User):
    
    await putUserToDefault(user,repo,bot,state)
