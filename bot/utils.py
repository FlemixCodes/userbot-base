import time

from vkbottle.user import Message


def get_pingtime(date: int) -> float:
    """Получить время ответа"""
    pingtime = abs(round(time.time() - date, 3))
    return pingtime


def get_user_id_reply(message: Message) -> int | None:
    """Получить айди пользователя из пересланного сообщения"""
    if message.reply_message:
        return message.reply_message.from_id
