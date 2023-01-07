import logging

from aiogram import Bot, Dispatcher, executor, types
import requests
from bs4 import BeautifulSoup



API_TOKEN = '5535857653:AAHpC1EiseEdUdBzwtzSmj3bqLmX_pIHdkk'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


amazon = "https://www.google.com/search?q=AMZN+action&rlz=1C5CHFA_enUS1034US1034&oq=AMZN+action&aqs=chrome..69i57j0i19i22i30l9.182j0j4&sourceid=chrome&ie=UTF-8"
google = "https://www.google.com/search?q=GOOGL&rlz=1C5CHFA_enUS1034US1034&oq=GOOGL&aqs=chrome..69i57j35i39j0i512l4j69i60l2.170j0j9&sourceid=chrome&ie=UTF-8"

response_amazon = requests.get(amazon).text
response_google = requests.get(google).text
soup_amazon = BeautifulSoup(response_amazon, "html.parser")
soup_google = BeautifulSoup(response_google, "html.parser")

googl = (soup_google.text.split('Stock Price')[1].split(' ')[0])
amzn = (soup_amazon.text.split('Stock Price')[1].split(' ')[0])


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply(f"AMZN - {amzn}\nGOOGL - {googl}")



@dp.message_handler()
async def echo(message: types.Message):
    # old style:
    # await bot.send_message(message.chat.id, message.text)

    await message.answer(message.text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

