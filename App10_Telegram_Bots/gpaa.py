import telepot
import asyncio
import telepot.aio
import urllib.request, urllib.error
from bs4 import BeautifulSoup
from telepot.aio.loop import MessageLoop
from telepot.namedtuple import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, ForceReply
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton
from telepot.namedtuple import InlineQueryResultArticle, InlineQueryResultPhoto, InputTextMessageContent
import config

whitelist = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ 0123456789')

async def on_chat_message(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print('Chat:', content_type, chat_type, chat_id)

    if content_type != 'text':
        return

    command = msg['text'][-1:].lower()

    markup = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton (text = 'Channel status', callback_data='press')],
    ])

    try:
        sauce = urllib.request.urlopen('https://www.youtube.com/user/'+msg['text']+'/about').read()
       # 'content_channel = sauce.content' if we will use sauce = requests.get(...) without read() in the end

        soup = BeautifulSoup(sauce, 'html.parser')
        # searching for necessary data
        for item in soup.find_all('span', 'about-stat'):
            answer = ''.join(filter(whitelist.__contains__, item.text)) + "\n"
            # it is validation we can put await 'bot.sendMessage(chat_id, item.text)' instead if we do not use 'answer'
            await bot.sendMessage(chat_id, answer)

    except urllib.error.HTTPError as err:
        if err.code == 404:
            await bot.sendMessage(chat_id, "Cannot find such channel! ")

    # await bot.sendMessage(chat_id, "Please reply the inline key! Force reply! ", reply_markup=markup)

async def on_callback_query(msg):
    query_id, from_id, data = telepot.glance(msg, flavor='callback_query')
    print('Callback query:', query_id, from_id, data)

    await bot.answerCallbackQuery(query_id, text='Callback is on the screen')


# main part
TOKEN = config.TOKEN

bot = telepot.aio.Bot(TOKEN)
loop = asyncio.get_event_loop()

loop.create_task(MessageLoop(bot, {'chat': on_chat_message,
                                   'callback_query': on_callback_query}).run_forever())

# also we may use bot.message_loop(handle)

print("Listening ...")

# keep the program running
loop.run_forever()
