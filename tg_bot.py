import telebot;
from telebot import types 

bot = telebot.TeleBot('6553183721:AAEI1gBIZohSD0F2wwUg95j-eaujiLaqUKE');

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Понедельник")
    btn2 = types.KeyboardButton("Вторник")
    btn3 = types.KeyboardButton("Среда")
    btn4 = types.KeyboardButton("Четверг")
    btn5 = types.KeyboardButton("Пятница")
    btn6 = types.KeyboardButton("Суббота")
    markup.add(btn1, btn2,btn3,btn4,btn5,btn6)
    bot.send_message(message.chat.id, text="Привет, {0.first_name}! Я бот-распиание, выбери день недели".format(message.from_user), reply_markup=markup)


@bot.message_handler(content_types=['text'])
def func(message):
    if(message.text == "Понедельник"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Чётная")
        btn2 = types.KeyboardButton("Нечётная")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn1, btn2,back)
        bot.send_message(message.chat.id, text="Какая сейчас неделя?", reply_markup=markup)

    elif(message.text == "Чётная"):
        bot.send_message(message.chat.id, text="8:30 - 9:55 Основы российской государственности (лекц) \n10:05 - 11:30 Технологии и методы программирование (лекц) \n11:40 - 13:05 Математика (пр) \n13:45 - 15:10 Информационные технологии (пр)")
    
    elif message.text == "Нечётная":
        bot.send_message(message.chat.id, text="8:30 - 9:55 Основы российской государственности (лекц) \n10:05 - 11:30 Технологии и методы программирование (лекц) \n11:40 - 13:05 Технологии и методы (лаб) \n13:45 - 15:10 Информационные технологии (пр)")

    elif (message.text == "Вернуться в главное меню"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Понедельник")
        btn2 = types.KeyboardButton("Вторник")
        btn3 = types.KeyboardButton("Среда")
        btn4 = types.KeyboardButton("Четверг")
        btn5 = types.KeyboardButton("Пятница")
        btn6 = types.KeyboardButton("Суббота")
        markup.add(btn1, btn2,btn3,btn4,btn5,btn6)
        bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup)  
    elif(message.text == "Вторник"):
        bot.send_message(message.chat.id, text="11:40 - 13:05 История России (лекц)\n13:45 - 15:10 Математика (лекц)  \n15:20 - 16:45 Математика (пр)\n16:55 - 18:20 Основы российской государственности (пр)")
    elif(message.text == "Среда"):
        bot.send_message(message.chat.id, text="13:45 - 15:10 Информационные технологии (пр)  \n15:20 - 16:45 Технологии и методы программирования (пр)\n16:55 - 18:20 История России (пр)")
    elif(message.text == "Четверг"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Чётная")
        btn2 = types.KeyboardButton("Нечётная")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn1, btn2,back)
        bot.send_message(message.chat.id, text="Какая сейчас неделя?", reply_markup=markup)
        
    elif(message.text == "Чётная"):
        bot.send_message(message.chat.id, text="11:40 - 13:05 Физика (лекц) \n13:45 - 15:10 Физика (лаба) \n15:20 - 16:45 Русский язык (пр) ")
    
    elif message.text == "Нечётная":
        bot.send_message(message.chat.id, text="11:40 - 13:05 Русский язык (лекц) \n13:45 - 15:10 Физика (пр) \n15:20 - 16:45 Русский язык (пр) ")
    
    elif (message.text == "Вернуться в главное меню"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Понедельник")
        btn2 = types.KeyboardButton("Вторник")
        btn3 = types.KeyboardButton("Среда")
        btn4 = types.KeyboardButton("Четверг")
        btn5 = types.KeyboardButton("Пятница")
        btn6 = types.KeyboardButton("Суббота")
        markup.add(btn1, btn2,btn3,btn4,btn5,btn6)
        bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup)
    
    elif(message.text == "Пятница"):
        bot.send_message(message.chat.id, text="13:45 - 15:10 Иностранный язык (пр)  \n15:20 - 16:45 Физкультура (пр)")
    elif(message.text == "Суббота"):
        bot.send_message(message.chat.id, text="8:30 - 9:55 Математическая логика (пр) \n10:05 - 11:30 Математическая логика (лекц)")
if __name__ == '__main__':
    bot.polling(none_stop=True)
