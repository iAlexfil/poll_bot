from aiogram.filters import Filter
from aiogram.types import Message


class TextFilter(Filter):
    def __init__(self, my_text: str) -> None:
        self.my_text = my_text

    async def __call__(self, message: Message) -> bool:
        return message.text == self.my_text


class LowerTextFilter(TextFilter):
    def __init__(self, my_text):
        super().__init__(my_text)

    async def __call__(self, message: Message) -> bool:
        return str(message.text).lower() == self.my_text.lower()
