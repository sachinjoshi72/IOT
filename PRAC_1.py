import telepot
token = '1338830968:AAGR_T7QS6CQ-fCl90rZSFvvEbIF18Eqdz8'
TelegramBot = telepot.Bot(token)
print (TelegramBot.getMe())
def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print(content_type, chat_type, chat_id)

    if content_type == 'text':
        TelegramBot.sendMessage(chat_id, "You said '{}'".format(msg["text"]))


TelegramBot.message_loop(handle)
