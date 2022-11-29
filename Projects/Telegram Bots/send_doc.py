import telepot
import asyncio
import telepot.aio
from telepot.aio.loop import MessageLoop
import config
from telepot.namedtuple import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, ForceReply
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton
from telepot.namedtuple import InlineQueryResultArticle, InlineQueryResultPhoto, InputTextMessageContent


async def handel(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    command = msg

    print(content_type, chat_type, chat_id)
    print('Got command: %s' % command)

    if command == '/start':
        await bot.sendMessage(chat_id, "Now please send your phone number!")
        markup = ReplyKeyboardMarkup(keyboard=[
            [dict(text='Phone', request_contact=True), KeyboardButton(text='Location', request_location=True)],
        ])
        await bot.sendMessage(chat_id, 'Thank you!', reply_markup=markup)

    if command == 'ok' or 'Ok' or 'OK':
        await  bot.sendMessage(chat_id, "Hi there. Now I will send you the pdf below ...")
        await bot.sendDocument(chat_id, document=open('Grading.pdf', 'rb'))

    elif command == 'thank you' or 'thanks' or 'thanks bro' or 'thank you bro':
        await  bot.sendMessage(chat_id, "Welcome :)")

        # await bot.sendMessage(chat_id, "You said '{}'".format(command))


TOKEN = ''

bot = telepot.aio.Bot(TOKEN)
loop = asyncio.get_event_loop()

loop.create_task(MessageLoop(bot, handel).run_forever())
# also we may use bot.message_loop(handle)

print("Listening ...")

# keep the program running
loop.run_forever()
