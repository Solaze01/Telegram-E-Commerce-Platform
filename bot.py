from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.utils import executor
from config import BOT_TOKEN
from services.catalog import get_catalog

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'catalog'])
async def show_catalog(message: Message):
    catalog = get_catalog()
    await message.answer(catalog)

if __name__ == "__main__":
    executor.start_polling(dp)
