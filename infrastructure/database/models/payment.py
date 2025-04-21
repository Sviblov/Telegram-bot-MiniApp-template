from typing import Optional

from sqlalchemy import TIMESTAMP, ForeignKey, String, func
from sqlalchemy import text, BIGINT, Boolean, true, false
from sqlalchemy.dialects.postgresql import TEXT
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from datetime import datetime

from .base import Base


class Invoice(Base):
    __tablename__ = "invoices"
    invoice_id: Mapped[int] = mapped_column(BIGINT, primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.user_id"))
    amount: Mapped[int] = mapped_column(BIGINT)
    created_at: Mapped[datetime] = mapped_column(TIMESTAMP, server_default=func.now())
    paid: Mapped[bool] = mapped_column(Boolean, server_default=false())
    paid_at: Mapped[datetime] = mapped_column(TIMESTAMP, nullable=True)
    payment_reference_id: Mapped[str] = mapped_column(String(256), nullable=True)

    def __repr__(self):
        return f"<Invoice {self.invoice_id} {self.user_id} {self.amount}>"

