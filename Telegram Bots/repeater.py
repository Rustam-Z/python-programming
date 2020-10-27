import telepot
import time
import telepot.aio
from telepot.loop import MessageLoop
#
def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    command = msg['text']

    print(content_type, chat_type, chat_id)
    print('Got command: %s' % command)

    if content_type == 'text':
        bot.sendMessage(chat_id, "Ты сказал '{}'".format(command))

TOKEN = '1295279684:AAGKfm8kGIqS6q1r2vCbUpozfDoX-TlvDHY'

bot = telepot.Bot(TOKEN)

MessageLoop(bot, handle).run_as_thread()
# also we may use bot.message_loop(handle)

print("Listening ...")

# keep the program running
while 1:
    time.sleep(10)
