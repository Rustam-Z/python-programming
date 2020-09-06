import time
import telepot
import config
import asyncio
import telepot.aio
from telepot.aio.loop import MessageLoop
from telepot.namedtuple import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, ForceReply
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton
from telepot.namedtuple import InlineQueryResultArticle, InlineQueryResultPhoto, InputTextMessageContent

message_with_inline_keyboard = None

async def on_chat_message(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print('Chat:', content_type, chat_type, chat_id)

    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [dict(text='IUT website', url='https://inha.uz/')],
        [InlineKeyboardButton(text='Calculus', callback_data='calculus_pressed')],
        [InlineKeyboardButton(text = 'OOP2', callback_data='oop2_pressed')],
        ])

    global message_with_inline_keyboard
    message_with_inline_keyboard = await bot.sendMessage(chat_id, 'Please insert your marks', reply_markup=keyboard)

async def on_callback_query(msg):
    query_id, from_id, query_data = telepot.glance(msg, flavor='callback_query')
    print('Callback Query:', query_id, from_id, query_data)

    if query_data == 'calculus_pressed':
        # markup = ReplyKeyboardMarkup(keyboard=[
        #     ['Plain text', KeyboardButton(text='Text only')],
        #     [dict(text='Phone', request_contact=True), KeyboardButton(text='Location', request_location=True)],
        # ])
        # await bot.sendMessage(query_id, 'Custom keyboard with various buttons', reply_markup=markup)
        await bot.answerCallbackQuery(query_id, text='Got your Calculus score')
    elif query_data == 'oop_pressed':
        # markup = ReplyKeyboardMarkup(keyboard=[
        #     ['Plain text', KeyboardButton(text='Text only')],
        #     [dict(text='Phone', request_contact=True), KeyboardButton(text='Location', request_location=True)],
        # ])
        # await bot.sendMessage(query_id, 'Custom keyboard with various buttons', reply_markup=markup)
        await bot.answerCallbackQuery(query_id, text='Got your OOP score')

TOKEN = config.TOKEN  # get token from command-line

bot = telepot.aio.Bot(TOKEN)
answerer = telepot.aio.helper.Answerer(bot)

loop = asyncio.get_event_loop()
loop.create_task(MessageLoop(bot, {'chat': on_chat_message,
                                   'callback_query': on_callback_query,}).run_forever())

print('Listening ...')

loop.run_forever()