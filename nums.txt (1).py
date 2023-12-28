import telebot
import folium

# Создаем объект бота
bot = telebot.TeleBot('Token')

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Привет! Я могу создать карту с помощью библиотеки folium. Введи широту и долготу:")

@bot.message_handler(func=lambda message: True)
def create_map(message):
    try:
        lat, lon = map(float, message.text.split())
        map2 = folium.Map(location=[lat, lon])
        map2.save('map.html')  # Сохраняем карту в формате html
        with open('map.html', 'rb') as f:
            bot.send_document(message.chat.id, f)
    except Exception as e:
        bot.reply_to(message, f"Произошла ошибка при создании карты. Проверь правильность введенных координат. {e}")

# Запускаем бота
bot.polling(none_stop=True)