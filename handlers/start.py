from loader import dp,bot
from aiogram import types
from utils import database
from keyboards import menu_keyboard, social_check_keyboard,language_keyboard
from base_lang import reg_lang,cheack_lang
content_channel = '-1001589342789'

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    text = f'''Выберите язык бота / Select the language of the bot'''
    await message.answer(text, reply_markup= language_keyboard.keyboard)

@dp.callback_query_handler(text='ru')
async def palka_payment(callback: types.CallbackQuery):
    reg_lang(chat_id=callback.message.chat.id,lang='ru')
    text = f'''👋 Привет, {callback.message.chat.first_name}\n\n<b>Этот бот может найти приватные фотографии девушек, анализируя их профили во всех социальных сетях и в слитых базах данных 😏\n\n</b>🔎 Отправьте боту ссылку на страничку ВКонтакте или Instagram, или отправьте номер телефона (What\'s App/Viber/Telegram)  🔞👇'''
    if not database.user_exists(callback.message.from_user.id):
        database.create_user(callback.message.from_user.id, callback.message.from_user.username)
        if callback.message.get_args() != '':
            if database.user_exists(callback.message.get_args()):
                database.update_user(callback.message.from_user.id, 'invited_by', callback.message.get_args())
        await callback.message.answer_photo('https://sun1-95.userapi.com/impg/X3WP4VJR6QgTVolvcfobfgYM5tPU0opNeP7M9A/bLPaeXcs89Y.jpg?size=1280x1280&quality=96&sign=bf858645ce1d4ee9bd6d838d00c23095&type=album', text, reply_markup=menu_keyboard.keyboard)
        await callback.message.answer('🔥 Выбери, где будем искать', reply_markup=social_check_keyboard.keyboard)
    else:
        await callback.message.answer_photo('https://sun1-95.userapi.com/impg/X3WP4VJR6QgTVolvcfobfgYM5tPU0opNeP7M9A/bLPaeXcs89Y.jpg?size=1280x1280&quality=96&sign=bf858645ce1d4ee9bd6d838d00c23095&type=album', text, reply_markup=menu_keyboard.keyboard)
        await callback.message.answer('🔥 Выбери, где будем искать', reply_markup=social_check_keyboard.keyboard)


@dp.callback_query_handler(text='eng')
async def palka_payment(callback: types.CallbackQuery):
    reg_lang(chat_id=callback.message.chat.id, lang='eng')
    text = f'''👋 Hello, {callback.message.chat.first_name}\n\n<b>This bot can find private photos of girls by analyzing their profiles in all social networks and in merged databases. 😏\n\n</b>🔎Send the bot a link to the Instagram page, or send the phone number (What's App/Viber/Telegram)🔞👇'''
    if not database.user_exists(callback.message.from_user.id):
        database.create_user(callback.message.from_user.id, callback.message.from_user.username)
        if callback.message.get_args() != '':
            if database.user_exists(callback.message.get_args()):
                database.update_user(callback.message.from_user.id, 'invited_by', callback.message.get_args())
        await bot.copy_message(caption = text,chat_id=callback.message.chat.id, message_id=15, from_chat_id=content_channel,reply_markup=menu_keyboard.keyboard_eng)
        await callback.message.answer('🔥 Choose where we will look', reply_markup=social_check_keyboard.keyboard_eng)
    else:
        await bot.copy_message(caption = text,chat_id=callback.message.chat.id, message_id=15, from_chat_id=content_channel,reply_markup=menu_keyboard.keyboard_eng)
        await callback.message.answer('🔥 Choose where we will look', reply_markup=social_check_keyboard.keyboard_eng)