# библиотеки, которые загружаем из вне
import telebot
TOKEN = '6498939874:AAFrB4CCO4Rt8oSteQjn9DcqP2sBJUmCYXI'


from telebot import TeleBot, types
import random


bot = TeleBot(token='6498939874:AAFrB4CCO4Rt8oSteQjn9DcqP2sBJUmCYXI', parse_mode='html') # создание бота

#библиотека с сериалами по жанрам:
western_list = ["Дэдвуд (2004 – 2006) -\n#вестерн #драма #криминал\nhttps://www.kinopoisk.ru/series/255671/","Забытые Богом (2017) -\n#вестерн #драма \nhttps://www.kinopoisk.ru/series/979311/","Джо Пикетт (2021) -\n#вестерн #криминал \nhttps://www.kinopoisk.ru/series/4438738/"]
biopic_list = ["Спартак: Кровь и песок (2010 – 2013) -\n#боевик #драма #мелодрама #приключения #биография\nhttps://www.kinopoisk.ru/series/469619/","Великая (2020 – 2021) -\n#комедия #биография #история\nhttps://www.kinopoisk.ru/series/666955/","Гений (2017 – ...) -\n#драма #биография #история\nhttps://https://www.kinopoisk.ru/series/975848/"]
historical_list = ["Викинги (сериал 2013 – 2020) -\n#история #драма #боевик #мелодрама #приключения #военный\nhttps://www.kinopoisk.ru/series/682255/","Последнее королевство (2015 – 2022) -\n#история #драма #боевик\nhttps://www.kinopoisk.ru/series/863829/","Пустая корона (2012 – 2016) -\n#история #драма #военный\nhttps://www.kinopoisk.ru/series/692830/"]
military_list = ["Братья по оружию (2001) -\n#военный #боевик #драма #история\nhttps://www.kinopoisk.ru/series/94249/", "Тихий океан (2010) -\n#военный #боевик #драма #история\nhttps://www.kinopoisk.ru/series/426030/","Поколение убийц (2008) -\n#драма #военный\nhttps://www.kinopoisk.ru/series/414891/"]
melodrama_list = ["Сексуальное просвещение (2019 – 2023) -\n#мелодрама #драма #комедия\nhttps://www.kinopoisk.ru/series/1147693/", "Реванш (2011 – 2015) -\n#мелодрама #триллер #драма #детектив\nhttps://www.kinopoisk.ru/series/582476/", "Великолепный век (2011 – 2014) -\n#мелодрама #история #военный #биография\nhttps://www.kinopoisk.ru/series/610422/"]
cartoon_list = ["Любовь. Смерть. Роботы (2019 – ...) -\n#мультфильм #фантастика #комедия #боевик #ужасы\nhttps://www.kinopoisk.ru/series/1228254/", "Киберпанк: Бегущие по краю (2022) -\n#аниме #мультфильм #фантастика #боевик\nhttps://www.kinopoisk.ru/series/2000102/", "Непобедимый (2021 – ...) -\n#мультфильм #фантастика #фэнтези\nhttps://www.kinopoisk.ru/series/1171895/","Южный Парк (1997 – ...) -\n#мультфильм #комедия\nhttps://www.kinopoisk.ru/series/161252/"]
science_fiction_list = ["Черное зеркало (2011 – ...) -\n #фантастика #триллер #драма #детектив #ужасы\nhttps://www.kinopoisk.ru/series/655800/", "Мир Дикого Запада (2016 – 2022) -\n #фантастика #драма #детектив\nhttps://www.kinopoisk.ru/series/195523/","Пацаны (2019 – ...) -\n #фантастика #боевик #драма #комедия #криминал\nhttps://www.kinopoisk.ru/series/195523/"]
horror_list = ["Американская история ужасов (2011 – ...) -\n#ужасы #фантастика #триллер #драма\nhttps://www.kinopoisk.ru/series/589167/","Очень странные дела (2016 – ...) -\n #ужасы #фантастика #фэнтези #триллер\nhttps://www.kinopoisk.ru/series/915196/", "Эш против Зловещих мертвецов (2015 – 2018) -\n#ужасы #комедия #фэнтези #боевик\nhttps://www.kinopoisk.ru/series/855898/", "Призрак дома на холме (2018) -\n#драма #ужасы\nhttps://www.kinopoisk.ru/series/1044279/"]
comedy_list = ["Голяк (2019 – ...) -\n#комедия #криминал\nhttps://www.kinopoisk.ru/series/1236393/","Чудотворцы (2019 – ...) -\n#комедия #фэнтези\nhttps://www.kinopoisk.ru/series/1111018/","Кобра Кай (2018 – 2023)-\n#комедия #спорт #боевик\nhttps://www.kinopoisk.ru/series/1047617/", "Офис (2005 – 2013) -\n#комедия\nhttps://www.kinopoisk.ru/series/253245/"]
action_list = ["Банши (2013 – 2016) -\n #боевик #триллер #драма #криминал\nhttps://www.kinopoisk.ru/series/696973/","Побег (2005 – 2017) -\n #боевик #триллер #драма #криминал #детектив\nhttps://www.kinopoisk.ru/series/258048/", "Игра престолов (2011 – 2019) -\n #фэнтези #драма #боевик #мелодрама #приключения\nhttps://www.kinopoisk.ru/series/464963/", "Бумажный дом (2017 – 2021) -\n #боевик #триллер #драма #криминал #детектив\nhttps://www.kinopoisk.ru/series/1046206/"]
thriller_list = ["Декстер (2006-2013) -\n#триллер #драма #криминал #детектив #мелодрама\nhttps://https://www.kinopoisk.ru/series/277537/","Озарк (2017 – 2022) -\n#триллер #драма #криминал\nhttps://www.kinopoisk.ru/series/1045553/","Острые предметы (2018) -\n#триллер #драма #криминал #детектив\nhttps://www.kinopoisk.ru/series/737644/","Святилище (2019) -\n#триллер #детектив\nhttps://www.kinopoisk.ru/series/1174264//"]
drama_list = ["Слово пацана. Кровь на асфальте (2023) -\n#драма #криминал\nhttps://https://https://www.kinopoisk.ru/series/5304403/","Во все тяжкие (2008 – 2013) - -\n#криминал #драма #триллер\nhttps://www.kinopoisk.ru/series/404900/", "Чернобыль (2019) -\n #драма #история\nhttps://https://www.kinopoisk.ru/series/1227803/","Эйфория (2019 – ...) -\n#драма\nhttps://https://www.kinopoisk.ru/series/1178445/"]

# обработчик команды '/start'
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Вестерн🔫")
    btn2 = types.KeyboardButton("Биография📖")
    btn3 = types.KeyboardButton("Исторический🎎")
    btn4 = types.KeyboardButton("Военный🎖")
    btn5 = types.KeyboardButton("Драма💔")
    btn6 = types.KeyboardButton("Мелодрама❤️‍🩹")
    btn7 = types.KeyboardButton("Комедия😁")
    btn8 = types.KeyboardButton("Мультфильм🐣")
    btn9 = types.KeyboardButton("Фантастика🌌")
    btn10 = types.KeyboardButton("Триллер👀") 
    btn11 = types.KeyboardButton("Ужасы😱")
    btn12 = types.KeyboardButton("Боевик🥷")
    markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, btn10, btn11, btn12)
    bot.send_message(message.chat.id, text="Привет, {0.first_name}! Давай залипать в Netflix и чилить? Не забудь взять попкорн🍿\nВыбор жанра за Тобой😉".format(message.from_user), reply_markup=markup)
    bot.send_video(message.chat.id, 'https://gifdb.com/images/high/eating-popcorn-and-watching-tv-e96tbw0ss6kpinm8.gif', None, 'Text')

# обработчик всех остальных сообщений    
@bot.message_handler(content_types=['text'])
def func(message):
    if(message.text == "Вестерн🔫"):
     bot.send_message(message.chat.id,"Твой выбор на сегодня:\n\n{0}".format(random.choice(western_list)))
     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
     btn1 = types.KeyboardButton("Да, спасибо за рекомендацию!🤩")
     btn2 = types.KeyboardButton("Давай другой Вестерн🔫")
     btn3 = types.KeyboardButton("Выбрать другой жанр🧐")
     markup.add(btn1, btn2, btn3)
     bot.send_message(message.chat.id,text="Ну что, выбор очевиден?☺️", reply_markup=markup)

    elif(message.text == "Давай другой Вестерн🔫"):
      bot.send_message(message.chat.id,"Твой выбор на сегодня:\n\n{0}".format(random.choice(western_list)))
      bot.send_message(message.chat.id,text="А если этот?👉🏻👈🏻")

    elif(message.text == "Биография📖"):
     bot.send_message(message.chat.id,"Твой выбор на сегодня:\n\n{0}".format(random.choice(biopic_list)))
     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
     btn1 = types.KeyboardButton("Да, спасибо за рекомендацию!🤩")
     btn2 = types.KeyboardButton("Давай другой Байопик📖")
     btn3 = types.KeyboardButton("Выбрать другой жанр🧐")
     markup.add(btn1, btn2, btn3)
     bot.send_message(message.chat.id,text="Ну что, выбор очевиден?☺️", reply_markup=markup)

    elif message.text == "Давай другой Байопик📖":
      bot.send_message(message.chat.id,"Твой выбор на сегодня:\n\n{0}".format(random.choice(biopic_list)))
      bot.send_message(message.chat.id,text="А если этот?👉🏻👈🏻")

    elif(message.text == "Исторический🎎"):
     bot.send_message(message.chat.id,"Твой выбор на сегодня:\n\n{0}".format(random.choice(historical_list)))
     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
     btn1 = types.KeyboardButton("Да, спасибо за рекомендацию!🤩")
     btn2 = types.KeyboardButton("Давай другую Историю🎎")
     btn3 = types.KeyboardButton("Выбрать другой жанр🧐")
     markup.add(btn1, btn2, btn3)
     bot.send_message(message.chat.id,text="Ну что, выбор очевиден?☺️", reply_markup=markup)

    elif message.text == "Давай другую Историю🎎":
      bot.send_message(message.chat.id,"Твой выбор на сегодня:\n\n{0}".format(random.choice(historical_list)))
      bot.send_message(message.chat.id,text="А если этот?👉🏻👈🏻")

    elif(message.text == "Военный🎖"):
     bot.send_message(message.chat.id,"Твой выбор на сегодня:\n\n{0}".format(random.choice(military_list)))
     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
     btn1 = types.KeyboardButton("Да, спасибо за рекомендацию!🤩")
     btn2 = types.KeyboardButton("Давай другой Военный🎖")
     btn3 = types.KeyboardButton("Выбрать другой жанр🧐")
     markup.add(btn1, btn2, btn3)
     bot.send_message(message.chat.id,text="Ну что, выбор очевиден?☺️", reply_markup=markup)

    elif message.text == "Давай другой Военный🎖":
      bot.send_message(message.chat.id,"Твой выбор на сегодня:\n\n{0}".format(random.choice(military_list)))
      bot.send_message(message.chat.id,text="А если этот?👉🏻👈🏻")

    elif(message.text == "Драма💔"):
     bot.send_message(message.chat.id,"Твой выбор на сегодня:\n\n{0}".format(random.choice(drama_list)))
     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
     btn1 = types.KeyboardButton("Да, спасибо за рекомендацию!🤩")
     btn2 = types.KeyboardButton("Давай другую Драму💔")
     btn3 = types.KeyboardButton("Выбрать другой жанр🧐")
     markup.add(btn1, btn2, btn3)
     bot.send_message(message.chat.id,text="Ну что, выбор очевиден?☺️", reply_markup=markup)

    elif message.text == "Давай другую Драму💔":
      bot.send_message(message.chat.id,"Твой выбор на сегодня:\n\n{0}".format(random.choice(drama_list)))
      bot.send_message(message.chat.id,text="А если этот?👉🏻👈🏻")

    elif(message.text == "Мелодрама❤️‍🩹"):
     bot.send_message(message.chat.id,"Твой выбор на сегодня:\n\n{0}".format(random.choice(melodrama_list)))
     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
     btn1 = types.KeyboardButton("Да, спасибо за рекомендацию!🤩")
     btn2 = types.KeyboardButton("Давай другую Мелодраму❤️‍🩹")
     btn3 = types.KeyboardButton("Выбрать другой жанр🧐")
     markup.add(btn1, btn2, btn3)
     bot.send_message(message.chat.id,text="Ну что, выбор очевиден?☺️", reply_markup=markup)

    elif message.text == "Давай другую Мелодраму❤️‍🩹":
      bot.send_message(message.chat.id,"Твой выбор на сегодня:\n\n{0}".format(random.choice(melodrama_list)))
      bot.send_message(message.chat.id,text="А если этот?👉🏻👈🏻")

    elif(message.text == "Комедия😁"):
     bot.send_message(message.chat.id,"Твой выбор на сегодня:\n\n{0}".format(random.choice(comedy_list)))
     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
     btn1 = types.KeyboardButton("Да, спасибо за рекомендацию!🤩")
     btn2 = types.KeyboardButton("Давай другую Комедию😁")
     btn3 = types.KeyboardButton("Выбрать другой жанр🧐")
     markup.add(btn1, btn2, btn3)
     bot.send_message(message.chat.id,text="Ну что, выбор очевиден?☺️", reply_markup=markup)

    elif message.text == "Давай другую Комедию😁":
      bot.send_message(message.chat.id,"Твой выбор на сегодня:\n\n{0}".format(random.choice(comedy_list)))
      bot.send_message(message.chat.id,text="А если этот?👉🏻👈🏻")

    elif(message.text == "Мультфильм🐣"):
     bot.send_message(message.chat.id,"Твой выбор на сегодня:\n\n{0}".format(random.choice(cartoon_list)))
     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
     btn1 = types.KeyboardButton("Да, спасибо за рекомендацию!🤩")
     btn2 = types.KeyboardButton("Давай другой Мультфильм🐣")
     btn3 = types.KeyboardButton("Выбрать другой жанр🧐")
     markup.add(btn1, btn2, btn3)
     bot.send_message(message.chat.id,text="Ну что, выбор очевиден?☺️", reply_markup=markup)

    elif message.text == "Давай другой Мультфильм🐣":
      bot.send_message(message.chat.id,"Твой выбор на сегодня:\n\n{0}".format(random.choice(cartoon_list)))
      bot.send_message(message.chat.id,text="А если этот?👉🏻👈🏻")

    elif(message.text == "Фантастика🌌"):
     bot.send_message(message.chat.id,"Твой выбор на сегодня:\n\n{0}".format(random.choice(science_fiction_list)))
     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
     btn1 = types.KeyboardButton("Да, спасибо за рекомендацию!🤩")
     btn2 = types.KeyboardButton("Давай другую Фантастику🌌")
     btn3 = types.KeyboardButton("Выбрать другой жанр🧐")
     markup.add(btn1, btn2, btn3)
     bot.send_message(message.chat.id,text="Ну что, выбор очевиден?☺️", reply_markup=markup)

    elif message.text == "Давай другую Фантастику🌌":
      bot.send_message(message.chat.id,"Твой выбор на сегодня:\n\n{0}".format(random.choice(science_fiction_list)))
      bot.send_message(message.chat.id,text="А если этот?👉🏻👈🏻")

    elif(message.text == "Триллер👀"):
     bot.send_message(message.chat.id,"Твой выбор на сегодня:\n\n{0}".format(random.choice(thriller_list)))
     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
     btn1 = types.KeyboardButton("Да, спасибо за рекомендацию!🤩")
     btn2 = types.KeyboardButton("Давай другой Триллер👀")
     btn3 = types.KeyboardButton("Выбрать другой жанр🧐")
     markup.add(btn1, btn2, btn3)
     bot.send_message(message.chat.id,text="Ну что, выбор очевиден?☺️", reply_markup=markup)

    elif message.text == "Давай другой Триллер👀":
      bot.send_message(message.chat.id,"Твой выбор на сегодня:\n\n{0}".format(random.choice(thriller_list)))
      bot.send_message(message.chat.id,text="А если этот?👉🏻👈🏻")

    elif(message.text == "Ужасы😱"):
     bot.send_message(message.chat.id,"Твой выбор на сегодня:\n\n{0}".format(random.choice(horror_list)))
     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
     btn1 = types.KeyboardButton("Да, спасибо за рекомендацию!🤩")
     btn2 = types.KeyboardButton("Давай другие Ужасы😱")
     btn3 = types.KeyboardButton("Выбрать другой жанр🧐")
     markup.add(btn1, btn2, btn3)
     bot.send_message(message.chat.id,text="Ну что, выбор очевиден?☺️", reply_markup=markup)

    elif message.text == "Давай другие Ужасы😱":
      bot.send_message(message.chat.id,"Твой выбор на сегодня:\n\n{0}".format(random.choice(horror_list)))
      bot.send_message(message.chat.id,text="А если этот?👉🏻👈🏻")

    elif(message.text == "Боевик🥷"):
     bot.send_message(message.chat.id,"Твой выбор на сегодня:\n\n{0}".format(random.choice(action_list)))
     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
     btn1 = types.KeyboardButton("Да, спасибо за рекомендацию!🤩")
     btn2 = types.KeyboardButton("Давай другой Боевик🥷")
     btn3 = types.KeyboardButton("Выбрать другой жанр🧐")
     markup.add(btn1, btn2, btn3)
     bot.send_message(message.chat.id,text="Ну что, выбор очевиден?☺️", reply_markup=markup)

    elif message.text == "Давай другой Боевик🥷":
      bot.send_message(message.chat.id,"Твой выбор на сегодня:\n\n{0}".format(random.choice(action_list)))
      bot.send_message(message.chat.id,text="А если этот?👉🏻👈🏻")
    
    elif(message.text == "Да, спасибо за рекомендацию!🤩"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("/start")
        markup.add(btn1)
        bot.send_message(message.chat.id,text="Обращайся!😇", reply_markup=markup)
        bot.send_video(message.chat.id, 'https://gifdb.com/images/high/wayne-campbell-thanks-bsldt49mptpa3yez.gif', None, 'Text')
    
    elif (message.text == "Выбрать другой жанр🧐"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Вестерн🔫")
        btn2 = types.KeyboardButton("Биография📖")
        btn3 = types.KeyboardButton("Исторический🎎")
        btn4 = types.KeyboardButton("Военный🎖")
        btn5 = types.KeyboardButton("Драма💔")
        btn6 = types.KeyboardButton("Мелодрама❤️‍🩹")
        btn7 = types.KeyboardButton("Комедия😁")
        btn8 = types.KeyboardButton("Мультфильм🐣")
        btn9 = types.KeyboardButton("Фантастика🌌")
        btn10 = types.KeyboardButton("Триллер👀")
        btn11 = types.KeyboardButton("Ужасы😱")
        btn12 = types.KeyboardButton("Боевик🥷")
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, btn10, btn11, btn12)
        bot.send_message(message.chat.id, text="Вы вернулись в главное меню😉", reply_markup=markup)
    else:
        bot.send_message(message.chat.id, text="Не понимаю тебя😟")


# главная функция программы
def main():
    # запускаем нашего бота
    bot.infinity_polling()


if __name__ == '__main__':
    main()
