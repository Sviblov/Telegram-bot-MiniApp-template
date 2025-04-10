import logging
from typing import Optional


from sqlalchemy import select
from sqlalchemy.dialects.postgresql import insert

from infrastructure.database.models import message, button, supported_language

from infrastructure.database.repo.base import BaseRepo
from infrastructure.database.repo.users import UserRepo
from aiogram.types import Message

logger = logging.getLogger('interface')

class InterfaceRepo(BaseRepo):

    async def get_MessageText(
        self,
        key: str,
        language: str = 'ru'
    ):
        
       
        select_data = (
            select(message).where(
                message.key==key
                # message.language==language
                )
        )
        
        row: message = await self.session.scalar(select_data)
        
        return row.message
        

    async def get_ButtonLables(
        self,
        menu_key: str,
        language: str = 'ru'
    ):
       
        select_data = (
            select(button).where(
                button.menu_key==menu_key
                # button.language==lang_to_use
                ).order_by(button.order)
        )

        
        
        rows = await self.session.execute(select_data)
        rows_scalar = rows.scalars().all()
        if len(rows_scalar) > 0:
            return rows_scalar
        else: 
            logger.warn(f"No Russian buttons defined when queryng standard button: {menu_key}")
            
            return None