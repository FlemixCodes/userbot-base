from vkbottle.user import UserLabeler, Message

from bot.config import EMOJI
from bot.rules import FromMe
from bot.utils import get_user_id_reply

labeler = UserLabeler()
labeler.vbml_ignore_case = True
labeler.auto_rules = [FromMe()]


@labeler.message(text=["!айди", "!id"])
async def get_id_handler(message: Message):
    user_id = get_user_id_reply(message)
    await message.answer(f"{EMOJI['user']} Айди пользователя: {user_id}")
