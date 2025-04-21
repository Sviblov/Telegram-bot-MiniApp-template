from typing import Optional

from sqlalchemy import select, delete, update
from sqlalchemy.dialects.postgresql import insert

from infrastructure.database.models import User,supported_language
from infrastructure.database.models.payment import Invoice
from infrastructure.database.repo.base import BaseRepo


class UserRepo(BaseRepo):
    async def get_or_create_user(
        self,
        user_id: int,
        full_name: str,
        language: Optional[str] = None,
        username: Optional[str] = None,
    ):
        """
        Creates or updates a new user in the database and returns the user object.
        :param user_id: The user's ID.
        :param full_name: The user's full name.
        :param language: The user's language.
        :param username: The user's username. It's an optional parameter.
        :return: User object, None if there was an error while making a transaction.
        """
        
        # Ensure language defaults to 'en' if None is passed
        language = language or "en"

        insert_stmt = (
            insert(User)
            .values(
                user_id=user_id,
                username=username,
                full_name=full_name,
                language=language,
            )
            .on_conflict_do_update(
                index_elements=[User.user_id],
                set_=dict(
                    username=username,
                    full_name=full_name,
                ),
            )
            .returning(User)
        )
        result = await self.session.execute(insert_stmt)

        await self.session.commit()
        return result.scalar_one()



    async def get_user(self, user_id: int):
        """
        Retrieves a user from the database by user_id.
        :param user_id: The user's ID.
        :return: User object, None if not found.
        """
        select_stmt = (
            select(User)
            .where(User.user_id == user_id)
        )
        result = await self.session.execute(select_stmt)

        return result.scalar_one_or_none()
    
    async def deleteUser(self, user_id: int):
        """
        Deletes a user and all related records from the database.
        :param user_id: The user's ID.
        :return: True if the user and related records were deleted, False otherwise.
        """
        # First, delete related records in the invoices table
        delete_invoices = delete(Invoice).where(Invoice.user_id == user_id)
        await self.session.execute(delete_invoices)

        # Then, delete the user
        delete_user = delete(User).where(User.user_id == user_id)
        result = await self.session.execute(delete_user)

        await self.session.commit()
        return result.rowcount > 0