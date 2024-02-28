from vkbottle import PhotoMessageUploader
from vkbottle.user import UserLabeler, Message

from bot.config import EMOJI
from bot.rules import FromMe

labeler = UserLabeler()
labeler.vbml_ignore_case = True
labeler.auto_rules = [FromMe()]


@labeler.message(text=["!картинка", "!picture"])
async def get_picture_handler(message: Message):
    photo_uploader = PhotoMessageUploader(message.ctx_api)
    photo = await photo_uploader.upload("bot/assets/images/image.jpeg")
    
    await message.answer(f"{EMOJI['image']} Ваша картинка", attachment=photo)
