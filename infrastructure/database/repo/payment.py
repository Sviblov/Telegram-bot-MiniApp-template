import logging
from typing import Optional


from sqlalchemy import select, update
from sqlalchemy.dialects.postgresql import insert

from infrastructure.database.models import Invoice
from infrastructure.database.repo.base import BaseRepo
from datetime import datetime




logger = logging.getLogger('invoice_repo')

class PaymentRepo(BaseRepo):
    async def createInvoice(
        self,
        user_id: int,
        amount: int
    ):
        """
        Creates or updates a new user in the database and returns the user object.
        :param user_id: The user's ID.
        :param full_name: The user's full name.
        :param language: The user's language.
        :param username: The user's username. It's an optional parameter.
        :return: User object, None if there was an error while making a transaction.
        """

        insert_stmt = (
            insert(Invoice)
            .values(
                user_id=user_id,
                amount=amount,
                created_at=datetime.now()
            )
            .returning(Invoice)
        )
        result = await self.session.execute(insert_stmt)

        await self.session.commit()
        return result.scalar_one()


    async def getInvoice(
            self,
            invoice_id: int
    ):
        """
        Creates or updates a new user in the database and returns the user object.
        :param user_id: The user's ID.
        :param full_name: The user's full name.
        :param language: The user's language.
        :param username: The user's username. It's an optional parameter.
        :return: User object, None if there was an error while making a transaction.
        """

        stmt = select(Invoice).where(Invoice.invoice_id == invoice_id)
        result = await self.session.execute(stmt)
        return result.scalar_one()

    async def payInvoice(
            self,
            invoice_id: int,
            payment_reference: str
    ):
        """
        Creates or updates a new user in the database and returns the user object.
        :param user_id: The user's ID.
        :param full_name: The user's full name.
        :param language: The user's language.
        :param username: The user's username. It's an optional parameter.
        :return: User object, None if there was an error while making a transaction.
        """

        stmt = (
            update(Invoice)
            .where(
                Invoice.invoice_id == invoice_id
                )
            .values(
                paid=True,
                paid_at=datetime.now(),
                payment_reference_id=payment_reference
            ).returning(Invoice)
        )
    
        result = await self.session.execute(stmt)
        await self.session.commit()
        return result.scalar_one()