from typing import Optional

from sqlalchemy import String
from sqlalchemy import text, BIGINT, Boolean, true, false
from sqlalchemy.dialects.postgresql import TEXT
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from aiogram.types import InlineKeyboardButton
from .base import Base, TimestampMixin, TableNameMixin


class message(Base):
    """
    This class represents a Standard Message in the application.
    """
    __tablename__ = "interface_messages"
    key: Mapped[str]  = mapped_column(String(32), primary_key=True, autoincrement=False)
    language: Mapped[str] = mapped_column(String(10),primary_key=True, server_default=text("'en'"))
    message: Mapped[str]  = mapped_column(TEXT)
    comment: Mapped[str]  = mapped_column(String(256))


    def __repr__(self):
        return f"<StandardMessage {self.key} {self.language}>"
    

class button(Base):
    
    """
    This class represents a Standard Button in the application.
    """
    __tablename__ = "interface_buttons"
    key: Mapped[str]  = mapped_column(String(32), primary_key=True, autoincrement=False)
    menu_key: Mapped[str]  = mapped_column(String(32),primary_key=True, autoincrement=False)
    language: Mapped[str] = mapped_column(String(10), primary_key=True, server_default=text("'en'"))
    button_text: Mapped[str]  = mapped_column(String(256))
    callback_data: Mapped[str]  = mapped_column(String(32))
    web_app_link: Mapped[str]  = mapped_column(String(256), nullable=True)
    order: Mapped[int]  = mapped_column(BIGINT, server_default=text("0"))
    comment: Mapped[str]  = mapped_column(String(256))


    def __repr__(self):
        return f"<StandardButton {self.key} {self.language}>"
    

            
    

class supported_language(Base):
    """
    This class represents a Standard Message in the application.
    """
    __tablename__ = "interface_supported_languages"
    lang_id: Mapped[int] = mapped_column(BIGINT, primary_key=True, autoincrement=True)
    language: Mapped[str] = mapped_column(String(2), server_default=text("'en'"))
    language_full: Mapped[str]  = mapped_column(String(15))
    is_default: Mapped[bool] = mapped_column(Boolean, server_default=false())
    


    def __repr__(self):
        return f"<{self.language} language>"