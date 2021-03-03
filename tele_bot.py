import telebot
from Config import exchanger, TOKEN
from extensions import Converter, ConvertionException

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start','help'])
def help(message: telebot.types.Message):
    text = 'Данный бот предназначен для конвертации валют:\n' \
'Для правильной работы с ботом, необходимо дать 3 параметра:\n' \
'Первая валюта, из которой мы хотим конвертировать\n' \
'Вторая валюта, в которую мы хотим конвертировать\n' \
'сумму перевода\n' \
'Для ознакомления с доступными валютами. /values'
    bot.reply_to(message, text)



@bot.message_handler(commands=['values', 'Values'])
def values(message: telebot.types.Message):
    text = "Доступные валюты:\n"
    text += "\n".join(f'{i+1} {key}' for i, key in enumerate(exchanger.keys()))
    bot.reply_to(message,text)

@bot.message_handler(content_types=['text'])
def convert(message: telebot.types.Message):
    try:
        textmessage = message.text.split(" ")

        if len(textmessage) != 3:
            raise ConvertionException("слишком много параметров!")

        quote, base, amount = textmessage
        total_base = Converter.convert(quote, base, amount)

    except ConvertionException as e:
        bot.reply_to(message, f'Ошибка пользователя. \n {e}')

    except Exception as e:
        bot.reply_to(message, f'Не удалось обратотать команду \n {e}')
    else:
        text = f'Цена {amount} {quote} в {base} - {total_base}'
        bot.send_message(message.chat.id, text)

bot.polling(none_stop=True)
