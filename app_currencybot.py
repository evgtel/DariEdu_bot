import telebot
from config import TOKEN, currency
from extensions import APIException, CryptoConverter

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])
def handle_start_help(message):
    bot.reply_to(message, "Для укажите валюту в формате\nВалюта1 Валюта2 Количество\nСписок валют - /values")

@bot.message_handler(commands=['values'])
def handle_values(message):
    currency_list = '\n'.join(currency)
    bot.reply_to(message, f"Список доступных валют:\n{currency_list}")

@bot.message_handler()
def function_name(message):
    try:
        convert_str = message.text.split(' ')  # ft_key, tt_key, amount

        if len(convert_str) != 3:
            raise APIException("Ошибка: параметров должно быть 3.")

        from_key, to_key, amount = convert_str
        total_base = CryptoConverter.get_price(from_key, to_key, amount)
    except APIException as e:
        bot.reply_to(message, f'Ошибка пользователя.\n{e}')
    except Exception as e:
        bot.reply_to(message, f'Ошибка программы.\n{e}')
    else:
        bot.reply_to(message, f"Цена {amount} {from_key} в {to_key} - {total_base}")


bot.polling(none_stop=True)

