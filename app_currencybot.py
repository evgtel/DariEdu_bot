import telebot
from telebot import types
from config import TOKEN, currency
from extensions import APIException, CryptoConverter

bot = telebot.TeleBot(TOKEN)




@bot.message_handler(commands=['start'])
def start(message: telebot.types.Message):
    text = 'Hi! Я Бот-конвертер валют.  \nПоказать справку /help'
    bot.reply_to(message, text)

@bot.message_handler(commands=['help'])
def handle_start_help(message):
    bot.reply_to(message, "Для конвертации валют\nвведите через пробел:\n "
                            "<Валюта1> <Валюта2> <Количество>\nСписок валют - /values\nПример:\nдоллар рубль 5")

@bot.message_handler(commands=['values'])
def handle_values(message):
    currency_list = '\n'.join(currency)
    bot.reply_to(message, f"Список доступных валют:\n{currency_list}")



@bot.message_handler(commands=['button'])
def button_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Кнопка")
    markup.add(item1)
    bot.send_message(message.chat.id, 'Выберите что вам надо', reply_markup=markup)


@bot.message_handler(content_types='text')
def message_reply(message):
    if message.text=="Кнопка":
        fr = message.from_user.id
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1=types.KeyboardButton("Кнопка 2")
        item2 = types.KeyboardButton("Кнопка 3")
        markup.add(item1,item2)
        bot.send_message(message.chat.id,f'User_id:{fr}',reply_markup=markup)
    elif message.text=="Кнопка 2":
        bot.send_message(message.chat.id,'Спасибо за прочтение статьи!')


@bot.message_handler()
def function_name(message):
    try:
        convert_str=[]
        pr_str = message.text.split(' ')
        for ss in pr_str:
            if ss != '':
                convert_str.append(ss)
        if len(convert_str) != 3:
            raise APIException("Ошибка: параметров должно быть 3.")

        base, quote, amount = convert_str
        total_base = CryptoConverter.get_price(base, quote, amount)
    except APIException as e:
        bot.reply_to(message, f'Ошибка пользователя.\n{e}')
    except Exception as e:
        bot.reply_to(message, f'Ошибка программы.\n{e}')
    else:
        bot.reply_to(message, f"Цена {amount} {base} - {total_base} {quote}")


bot.polling(none_stop=True)

