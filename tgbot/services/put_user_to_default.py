from aiogram.fsm.context import FSMContext
from ..services.services import delete_message

from infrastructure.database.models import message as logmessage
from infrastructure.database.repo.requests import RequestsRepo

async def putUserToDefault(user, repo: RequestsRepo, bot, state: FSMContext):
    #deleting messages
    allMessages = await repo.log_message.get_messages(user.user_id)
    
    for message in allMessages:
        await delete_message(bot, message[0],message[1])
        
    #deleting from logs
    await repo.log_message.delete_messages(user.user_id)


    await state.set_data(None)
    await state.set_state(None)