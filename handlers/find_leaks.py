from loader import dp,bot
from aiogram import types
from keyboards import social_check_keyboard,menu_keyboard,language_keyboard
from base_lang import cheack_lang
content_channel = '-1001589342789'

@dp.message_handler(text='🔍 Найти сливы 🔍')
async def find_leaks(message: types.Message):
    text=f'''👋 Привет, {message.from_user.full_name}\n\n<b>Этот бот может найти приватные фотографии девушек, анализируя их профили во всех социальных сетях и в слитых базах данных 😏</b>\n\n🔎 Отправьте боту ссылку на страничку ВКонтакте или Instagram, или отправьте номер телефона (What\'s App/Viber/Telegram)  🔞👇'''
    await message.answer_photo('https://sun1-95.userapi.com/impg/X3WP4VJR6QgTVolvcfobfgYM5tPU0opNeP7M9A/bLPaeXcs89Y.jpg?size=1280x1280&quality=96&sign=bf858645ce1d4ee9bd6d838d00c23095&type=album', text)
    await message.answer('🔥 Выбери, где будем искать', reply_markup=social_check_keyboard.keyboard)

@dp.message_handler(text='🔍 Find nudes 🔍')
async def find_leaks_eng(message: types.Message):
    text = f'''👋 Hello, {message.from_user.full_name}\n\n<b>This bot can find private photos of girls by analyzing their profiles in all social networks and in merged databases. 😏\n\n</b>🔎Send the bot a link to the Instagram page, or send the phone number (What's App/Viber/Telegram)🔞👇'''
    await bot.copy_message(caption=text, chat_id=message.chat.id, message_id=15, from_chat_id=content_channel,reply_markup=menu_keyboard.keyboard_eng)
    await message.answer('🔥 Choose where we will look', reply_markup=social_check_keyboard.keyboard_eng)

@dp.message_handler(text='Bot language / Язык бота')
async def lag_eng(message: types.Message):
    text = f'''Выберите язык бота / Select the language of the bot'''
    await message.answer(text, reply_markup=language_keyboard.keyboard)


@dp.callback_query_handler(text='instagram')
async def inst(callback: types.CallbackQuery):
    await callback.message.edit_text('<b>Отправте ссылку на профиль instagram</b>\n\nПримеры:\nhttps://www.instagram.com/karna.val/\ninstagram.com/samoylovaoxana/', reply_markup=social_check_keyboard.back_keyboard)

@dp.callback_query_handler(text='instagram_eng')
async def inst(callback: types.CallbackQuery):
    await callback.message.edit_text('<b>Send a link to your instagram profile</b>\n\nExamples:\nhttps://www.instagram.com/jenselter/\ninstagram.com/anacheri/', reply_markup=social_check_keyboard.back_keyboard_eng)


@dp.callback_query_handler(text='vk')
async def inst(callback: types.CallbackQuery):
    await callback.message.edit_text('<b>Отправте ссылку на профиль ВКонтакте</b>\n\nПримеры:\nhttps://vk.com/id494445129\nvk.com/id173811890', reply_markup=social_check_keyboard.back_keyboard)

@dp.callback_query_handler(text='phone_number')
async def inst(callback: types.CallbackQuery):
    if cheack_lang(chat_id= callback.message.chat.id) == 'ru':
        await callback.message.edit_text('<b>Отправте номер телефона, начинающийся с +</b>\n\n+7...\n+3...', reply_markup=social_check_keyboard.back_keyboard)
    else:
        await callback.message.edit_text('<b>Send a phone number starting with +</b>\n\n+1...\n+2...', reply_markup=social_check_keyboard.back_keyboard_eng)

@dp.callback_query_handler(text='tiktok')
async def inst(callback: types.CallbackQuery):
    await callback.message.edit_text('<b>Отправте никнейм пользователя</b>\n\nПримеры:\n@karinakross\n@buzova86', reply_markup=social_check_keyboard.back_keyboard)

@dp.callback_query_handler(text='social_back')
async def back(callback: types.CallbackQuery):
    if cheack_lang(chat_id=callback.message.chat.id) == 'ru':
        await callback.message.delete()
        await callback.message.answer('🔥 Выбери, где будем искать', reply_markup=social_check_keyboard.keyboard)
    else:
        await callback.message.delete()
        await callback.message.answer('🔥 Choose where we will look', reply_markup=social_check_keyboard.keyboard_eng)