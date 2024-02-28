import time

from vkbottle import API, VKAPIError
from vkbottle.user import Message


def get_pingtime(date: int) -> float:
    """Получить время ответа"""
    pingtime = abs(round(time.time() - date, 3))
    return pingtime


def get_user_id_reply(message: Message) -> int | None:
    """Получить айди пользователя из пересланного сообщения"""
    if message.reply_message:
        return message.reply_message.from_id


async def check_token_valid(api: API) -> bool:
    """Проверить access_token на валидность через объект API"""
    try:
        await api.account.get_profile_info()
        return True
    except VKAPIError[5]:
        return False
