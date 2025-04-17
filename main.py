import logging
import os
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

API_TOKEN = os.getenv("BOT_TOKEN")

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def send_welcome(message: types.Message):
    await message.reply("Ты запустил JustFuckDoIt_bot. Вставай, работай над собой и не ной!")

@dp.message_handler()
async def echo(message: types.Message):
    await message.reply("Делай, бл*ть! Хватит тянуть. Всё ради Инны, детей и новой жизни!")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
