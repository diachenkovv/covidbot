import COVID19Py
import telebot
from telebot import types
import os
from dotenv import load_dotenv
load_dotenv()

covid19 = COVID19Py.COVID19()
bot = telebot.TeleBot(os.getenv('TOKEN'))


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn1 = types.KeyboardButton('В усьому світі')
    btn2 = types.KeyboardButton('Україна')
    btn3 = types.KeyboardButton('Італія')
    btn4 = types.KeyboardButton('Китай')
    markup.add(btn1, btn2, btn3, btn4)
    send_message = f"<b>Вітаю, {message.from_user.first_name}!</b>\nЩоб дізнати останні дані щодо COVID-19 напишіть " \
        f"назва країни, наприклад: США, Україна i так далі"
    bot.send_message(message.chat.id, send_message,
                     parse_mode='html', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def mess(message):
    final_message = ""
    get_message_bot = message.text.strip().lower()
    if get_message_bot == "сша":
        location = covid19.getLocationByCountryCode("US")
    elif get_message_bot == "україна":
        location = covid19.getLocationByCountryCode("UA")
    elif get_message_bot == "росія":
        location = covid19.getLocationByCountryCode("RU")
    elif get_message_bot == "білорусь":
        location = covid19.getLocationByCountryCode("BY")
    elif get_message_bot == "італія":
        location = covid19.getLocationByCountryCode("IT")
    elif get_message_bot == "франція":
        location = covid19.getLocationByCountryCode("FR")
    elif get_message_bot == "німеччина":
        location = covid19.getLocationByCountryCode("DE")
    elif get_message_bot == "японія":
        location = covid19.getLocationByCountryCode("JP")
    elif get_message_bot == "китай":
        location = covid19.getLocationByCountryCode("CN")
    else:
        location = covid19.getLatest()
    final_message = f"<u>Дані з усього світу:</u>\n<b>Захворіло: </b>{location['confirmed']:,}\n<b>Померло: </b>{location['deaths']:,}"

    if final_message == "":
        date = location[0]['last_updated'].split("T")
        time = date[1].split(".")
        final_message = f"<u>Дані по країні:</u>\nНаселення: {location[0]['country_population']:,}\n" \
            f"Останнє оновлення: {date[0]} {time[0]}\nОстанні дані:\n<b>" \
            f"Захворіло: </b>{location[0]['latest']['confirmed']:,}\n<b>Померло: </b>" \
            f"{location[0]['latest']['deaths']:,}"

        bot.send_message(message.chat.id, final_message, parse_mode='html')


bot.polling(none_stop=True)
# latest = covid19.getLatest()
# location = covid19.getLocationByCountryCode("UA")

# print(latest)
