from aiogram import Bot, Dispatcher, F
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


# This handler will trigger when sending a photo to the bot
@dp.message(F.photo)
async def send_photo_echo(message: Message):
    await message.reply_photo(message.photo[0].file_id)


# This handler will trigger when sending stickers to the bot
@dp.message(F.sticker)
async def send_sticker_echo(message: Message):
    await message.reply_sticker(message.sticker.file_id)


# This handler will trigger when sending an animation to the bot
@dp.message(F.animation)
async def send_animation_echo(message: Message):
    await message.reply_animation(message.animation.file_id)


# This handler will trigger when sending voice messages to the bot
@dp.message(F.voice)
async def send_voice_echo(message: Message):
    await message.reply_voice(message.voice.file_id)


# This handler will trigger when sending videos to the bot
@dp.message(F.video)
async def send_video_echo(message: Message):
    await message.reply_video(message.video.file_id)


# This handler will trigger when sending audios to the bot
@dp.message(F.audio)
async def send_audio_echo(message: Message):
    await message.reply_audio(message.audio.file_id)


# This handler will trigger when sending documents to the bot
@dp.message(F.document)
async def send_document_echo(message: Message):
    await message.reply_document(message.document.file_id)


# This handler will trigger when sending location to the bot
@dp.message(F.location)
async def send_location_echo(message: Message):
    await message.reply_location(message.location.latitude, message.location.longitude)


# This handler will trigger any text messages, except for the "/start" and "/help" commands
@dp.message()
async def send_echo(message: Message):
    await message.reply(text=message.text)


if __name__ == '__main__':
    dp.run_polling(bot)
