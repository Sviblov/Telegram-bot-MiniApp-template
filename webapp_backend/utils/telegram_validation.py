import hmac
import hashlib
from urllib.parse import parse_qsl
from pydantic import BaseModel

class InitData(BaseModel):
    init_data: str

def validate_telegram_init_data(init_data: str, bot_token: str) -> bool:
    """
    Проверяет подлинность данных Telegram WebApp.

    :param init_data: Строка данных, переданная Telegram WebApp.
    :param bot_token: Токен вашего Telegram-бота.
    :return: True, если данные подлинные, иначе False.
    """
    # Парсим init_data в словарь
    parsed_data = dict(parse_qsl(init_data, keep_blank_values=True))
    received_hash = parsed_data.pop("hash", None)

    if not received_hash:
        return False

    # Формируем строку для проверки данных
    data_check_string = "\n".join(f"{k}={v}" for k, v in sorted(parsed_data.items()))

    # Создаем секретный ключ
    secret_key = hmac.new(b"WebAppData", bot_token.encode(), hashlib.sha256).digest()

    # Вычисляем хэш
    hmac_hash = hmac.new(secret_key, data_check_string.encode(), hashlib.sha256).hexdigest()

    # Сравниваем вычисленный хэш с полученным
    return hmac.compare_digest(hmac_hash, received_hash)

