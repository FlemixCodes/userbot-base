from vkbottle.user import UserLabeler, Message

from bot.config import EMOJI
from bot.utils import get_pingtime
from bot.rules import FromMe

labeler = UserLabeler()
labeler.vbml_ignore_case = True
labeler.auto_rules = [FromMe()]


@labeler.message(text=["!пинг", "!ping"])
async def ping_handler(message: Message):
    pingtime = get_pingtime(message.date)
    
    await message.answer(
        f"{EMOJI['ok']} Понг!\n" \
        f"{EMOJI['watch']} Время ответа: {pingtime}с."
    )
