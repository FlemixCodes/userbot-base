from vkbottle import ABCRule
from vkbottle.user import Message


class FromMe(ABCRule):
    async def check(self, message: Message) -> bool:
        return message.out == 1
