from vkbottle import API
from vkbottle.user import User, run_multibot
from vkbottle.http import AiohttpClient

from bot.config import TOKEN, TOKENS
from bot.commands import labelers


def start_bot() -> None:
    """Запуск бота"""
    user = User(token=TOKEN)
    for labeler in labelers:
        user.labeler.load(labeler)

    user.run_forever()


def start_multibot() -> None:
    """Запуск мультибота"""
    apis = []
    for token in TOKENS:
        apis.append(API(token=token, client=AiohttpClient()))

    user = User()
    for labeler in labelers:
        user.labeler.load(labeler)

    run_multibot(user, apis)
