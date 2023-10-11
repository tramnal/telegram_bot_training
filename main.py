from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message
from dotenv import dotenv_values

BOT_TOKEN = dotenv_values('.env')['TOKEN']

# Creating Bot and Dispatcher objects
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


# This handler will trigger command "/start"
@dp.message(Command(commands=['start']))
async def process_start_command(message: Message):
    await message.answer('Привет!\nМеня зовут Эхо-бот!\nНапиши мне что-нибудь')


# This handler will trigger command '/help'
@dp.message(Command(commands=['help']))
async def process_help_command(message: Message):
    await message.answer(
        'Напиши мне что-нибудь, и в ответ '
        'я пришлю тебе твое сообщение'
    )


# This handler will trigger any messages, except for the "/start" and "/help" commands
@dp.message()
async def send_echo(message: Message):
    await message.reply(text=message.text)


if __name__ == '__main__':
    dp.run_polling(bot)
