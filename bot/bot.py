from vkbottle import API
from vkbottle.user import User, run_multibot
from vkbottle.http import AiohttpClient

from bot.config import TOKEN, TOKENS
from bot.commands import labelers
from bot.utils import check_token_valid


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
        api = API(token=token, client=AiohttpClient())
        if check_token_valid(api):
            apis.append(api)

    user = User()
    for labeler in labelers:
        user.labeler.load(labeler)

    run_multibot(user, apis)
