import logging
import telegram
import random
from telegram.ext import Updater, CommandHandler

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

logger = logging.getLogger(__name__)
bot = telegram.Bot(token='2133753651:AAHtA4_kqPvdx_6vdImHTpW4s-s24x4RSik')

def start(update, context):
    chat_id = update.message.chat.id
    bot.sendMessage(chat_id, 'Hello! You can know which Jedi you are by sending /who to me! :-)')

def error(update, context):
    logger.warning('%s caused error (%s)', update, context.error)

def JediCheck(update, context):
    chatId = update.message.chat.id
    dict1 = {"A": "You are Anakin Skywalker! Rudest to enemies, nicest to friends. Best pilot in your village.", 
    "Y": "Yoda, you are! Litte grumpy Shrek. Sometimes can do something cool.", 
    "M": "You are Mace Windu! No shit for nothing, badass motherducker. Maybe villian.", 
    "O": "You are Obi-Wan Kenobi! Follow rules and don't want any chaos, wise and funny guy.",
    "D": "You are Sifo-Dyas! No one cares about you, just the guy, that did something cool :/.",
    "U":"You are Luminara Unduli! Someone considers you nice, but you're more rough.",
    "T":"You are Ahsoka Tano! Despite every troubles in your life, you're still coming through with joy.",
    "L":"You are Luke Skywalker! A good feller with purest heart, sees good in everyone, everybody likes you.",
    "K":"You are Ki-Adi-Mundi! Nasty selfish duck."}
    
    items_list = list(dict1.items())
    item = random.choice(items_list)
    letter = item[0]
    discr = item[1]
        
    bot.sendPhoto(chat_id = chatId, photo=open('%s.jpg' % letter, 'rb'), caption=discr)

def main():
   
    updater = Updater('2133753651:AAHtA4_kqPvdx_6vdImHTpW4s-s24x4RSik', use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('who', JediCheck))
    dp.add_error_handler(error)
    updater.start_polling()
    updater.idle()
    

if __name__ == '__main__':
    main()