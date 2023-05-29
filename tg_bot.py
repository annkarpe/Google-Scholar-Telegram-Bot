import telebot
from telebot import types
from gs_parser import parse_article_info
from credentials import bot_token


bot = telebot.TeleBot(bot_token)


@bot.message_handler(commands=['start'])
def greet(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    btn_add = types.KeyboardButton('/add_search')
    btn_remove = types.KeyboardButton('/remove_search')
    btn_help = types.KeyboardButton('/help')
    markup.add(btn_add, btn_remove, btn_help)

    bot.send_message(message.chat.id, 'Hello! '
            'My purpose is to continuously send you new articles '
            'from Google Scholar based on your interests. '
            'For more information type /help', reply_markup=markup)


@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, 'no help, haha')


@bot.message_handler(commands=['add_search'], content_types=['text'])
def search(message):
    bot.send_message(message.chat.id, 'Enter your query')
    bot.register_next_step_handler(message, process_search_query)


def process_search_query(message):
    query = message.text
    response = parse_article_info(query)
    for name, url in response:
        bot.send_message(message.chat.id, name)
        bot.send_message(message.chat.id, url)


#your query is added, you'll receive new articles when they appear. 
#get last articles on given topic (max 10)

bot.polling()