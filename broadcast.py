#Made by a reference with https://github.com/PaulSonOfLars/tgbot/blob/0ece72778b7772725ab214fe0929daaa2fc7d2d1/tg_bot/modules/users.py#L51
import telegram
from telegram import Update, Bot ,TelegramError
import pymongo
from time import sleep

myclient = pymongo.MongoClient()
database = myclient['users']
collection = database["user"]

botOwnerID = '1520625615' # Replace thiswith your user id
def broadcast(update , context ):
    chat_id = update.message.chat_id
    fname = update.effective_message
    
    #extracting chatid from database
    if chat_id == botOwnerID:
        chat = (collection.find({}, {'userid': 1, '_id': 0}))
        chats = [sub['userid'] for sub in chat]
        failed = 0
        
        for chat in chats:
          try:
              context.bot.copy_message(chat_id=chat,
                               from_chat_id=update.message.reply_to_message.chat.id,
                               message_id=update.message.reply_to_message.message_id)
              sleep(0.1)
              
          except TelegramError:
                failed += 1
                LOGGER.warning("Couldn't send broadcast to %s, group name %s", chat)

        update.message.reply_text("Broadcast complete. {} users failed to receive the message, probably due to being kicked.".format(failed))
    
    else:
        bot.send_message(chat_id=botOwnerID, text="Someone tried to access broadcast command"
                                                  "\nUser Info :"
                                                  f"User Id = {chat_id}"
                                                  f"First name = {fname}"
                                                  f"Message = {update.message.reply_to_message.text}")
