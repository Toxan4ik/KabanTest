from os import system

system("pip install numpy, openai, bs4")
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from openai import AsyncClient

from bs4 import BeautifulSoup
import requests

import random

bot = Bot(token="7783613623:AAHHSWVi7HlB6PhX2rEmJeFNCZKMXO7UJGI") # кабан 7746997930:AAGisN5ApKcZV53BbDXya2an0Jn9OKCJOFE   погода 7783613623:AAHHSWVi7HlB6PhX2rEmJeFNCZKMXO7UJGI
dp = Dispatcher()

@dp.message(Command("casino"))
async def casino_command(message: types.Message):
	casino_message = await message.reply_dice(emoji="🎰")
	await asyncio.sleep(1.5)
	await message.reply(text="Ваш выигрыш "+message.from_user.first_name)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())


