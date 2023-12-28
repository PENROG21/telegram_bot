from bs4 import BeautifulSoup
import telebot
import urllib.request
from telebot import types

bot = telebot.TeleBot("5929718382:AAFZXsV2YldpqY7KCW4bbwyorLwfWHZiIo0")


@bot.message_handler(commands=['start'])
def start_message(message):
    markup = types.ReplyKeyboardMarkup()
    asd1 = markup.add(types.InlineKeyboardButton("rfpl"))
    asd2 = markup.add(types.InlineKeyboardButton("epl󠁧󠁢󠁥󠁮󠁧󠁿󠁧󠁢󠁥󠁮󠁧"))
    asd3 = markup.add(types.InlineKeyboardButton("seria-a󠁧󠁢󠁥󠁮󠁧󠁿󠁧󠁢󠁥󠁮󠁧"))
    bot.send_message(message.chat.id, 'Введите название чемпионата на английском', reply_markup=markup)


@bot.message_handler(func=lambda message: True)
def handle_message2(message):
    try:
        championship_table = message.text
        url = f'https://www.sports.ru/{championship_table}/table/'

        def parse(html):
            soup = BeautifulSoup(html, 'html.parser')
            teams = []

            for row in soup.select('tbody > tr'):
                cols = row.find_all('td')
                team = {
                    'Место': cols[0].text,
                    'Команда': cols[1].text,
                    'Матчи': cols[8].text
                }
                teams.append(team)

            return teams

        with urllib.request.urlopen(url) as rs:
            html = rs.read()

        teams = parse(html)

        info = ''
        for team in teams:
            info += f"{team['Место']})Команда:{team['Команда']},очков:{team['Матчи']}\n"

        bot.send_message(message.chat.id, info)

    except Exception as e:
        bot.reply_to(message, f"Ошибка: {e}")


bot.polling(none_stop=True)