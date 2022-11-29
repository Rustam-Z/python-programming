from nltk.chat.eliza import eliza_chatbot
import telepot
import asyncio
import telepot.aio
from telepot.aio.loop import MessageLoop
import config


async def hande(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    command = msg['text']

    print(content_type, chat_type, chat_id)
    print('Got command: %s' % command)

    if content_type == 'text':
        if command == "/start":
            await bot.sendMessage(chat_id, "Hello, do you need any help?")
        else:
            await bot.sendMessage(chat_id, eliza_chatbot.respond(command))


# put the token inside
TOKEN = ''

bot = telepot.aio.Bot(TOKEN)
loop = asyncio.get_event_loop()

loop.create_task(MessageLoop(bot, hande).run_forever())
# also we may use bot.message_loop(handle)

print("Listening ...")

# keep the program running
loop.run_forever()
