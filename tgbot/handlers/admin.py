from aiogram import Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from tgbot.filters.admin import AdminFilter
from tgbot.states import UserStates

from aiogram import Bot

from infrastructure.database.repo.requests import RequestsRepo
from infrastructure.database.models.users import User

from tgbot.services.services import send_message, delete_message

from tgbot.keyboards.inline import StandardMenu
from tgbot.services.services  import putUserToDefault


admin_router = Router()
admin_router.message.filter(AdminFilter())


@admin_router.message(CommandStart())
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



@admin_router.message(Command("delete"))
async def user_start(message: Message, state: FSMContext, repo: RequestsRepo, bot: Bot, user: User):
    
    await putUserToDefault(user,repo,bot,state)