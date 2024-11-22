import telebot
from telebot import types

token=''
my_chat_id= 640692142
bot=telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start_messages(message):
    first_name=message.chat.first_name
    Keyboard=types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    button_shop=types.KeyboardButton(text="Каталог")
    button_own=types.KeyboardButton(text='Своя модель')
    button_info=types.KeyboardButton(text='Канал')
    cart=types.KeyboardButton(text='Корзина')
    Keyboard.add(button_shop, button_own, button_info, cart)
    bot.send_message(message.chat.id,f'удалил', reply_markup=Keyboard)

def info_func(message):
    Keyboard=types.InlineKeyboardMarkup()
    url_button=types.InlineKeyboardButton(text='Перейти в канал', url='удалил')
    go_back=types.KeyboardButton(text="Главное меню")
    cart=types.KeyboardButton(text='Корзина')
    Keyboard.add(url_button, go_back, cart)
    bot.send_message(message.chat.id, 'Не забудь подписаться!', reply_markup=Keyboard)

def send_request(message):
    mes=f'Новая заявка: {message.text}'
    bot.send_message(my_chat_id,mes)
    bot.send_message(message.chat.id, 'Ваш запрос обрабатывается')

@bot.message_handler(commands=['Каталог'])
def send_servive(message):
    Keyboard=types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    button_fan=types.KeyboardButton(text="Фэнтези")
    button_animal=types.KeyboardButton(text="Звери")
    cart=types.KeyboardButton(text='Корзина')
    go_back=types.KeyboardButton(text="Главное меню")
    Keyboard.add(button_fan, button_animal, go_back, cart)
    bot.send_message(message.chat.id,'Выбирай не стесняйся', reply_markup=Keyboard)

@bot.message_handler(commands=['Фэнтези'])
def send_all_picture_fantasy(message):
    bard = open(r'C:\Users\Леонид\Desktop\bot\bard.jpg', 'rb')
    bot.send_photo(message.chat.id, photo=bard, caption='Енот бард')
    savager = open(r"C:\Users\Леонид\Desktop\bot\large_display_Savager.jpg", 'rb')
    bot.send_photo(message.chat.id, photo=savager, caption='Медведь с шипами')
    Shadhavar= open(r"C:\Users\Леонид\Desktop\bot\large_display_Shadhavar.JPG", 'rb')
    bot.send_photo(message.chat.id, photo=Shadhavar, caption='Зомби единорог')
    Serpopard= open(r"C:\Users\Леонид\Desktop\bot\Serpopard.jpg", 'rb')
    bot.send_photo(message.chat.id, photo=Serpopard, caption='Серопад')
    dragon= open(r"C:\Users\Леонид\Desktop\bot\дракон.jpg", 'rb')
    bot.send_photo(message.chat.id, photo=dragon, caption='Дракон')
    mimic_three= open(r"C:\Users\Леонид\Desktop\bot\елка мимик.jpg", 'rb')
    bot.send_photo(message.chat.id, photo=mimic_three, caption='Новогодняя елка мимик')
    three= open(r"C:\Users\Леонид\Desktop\bot\елка.jpg", 'rb')
    bot.send_photo(message.chat.id, photo=three, caption='Новгодняя елка')
    cactus= open(r"C:\Users\Леонид\Desktop\bot\кактус.jpg", 'rb')
    bot.send_photo(message.chat.id, photo=cactus, caption='Плотоядный кактус')
    kitsune= open(r"C:\Users\Леонид\Desktop\bot\китсуне.jpg", 'rb')
    bot.send_photo(message.chat.id, photo=kitsune, caption='Кицунэ')
    korgi= open(r"C:\Users\Леонид\Desktop\bot\корги.jpg", 'rb')
    bot.send_photo(message.chat.id, photo=korgi, caption='Боевой корги')
    cat_mage= open(r"C:\Users\Леонид\Desktop\bot\кот маг.jpg", 'rb')
    bot.send_photo(message.chat.id, photo=cat_mage, caption='Магический кот')
    bear= open(r"C:\Users\Леонид\Desktop\bot\медведь.jpg", 'rb')
    bot.send_photo(message.chat.id, photo=bear, caption='Медведь с седлом')
    tedy= open(r"C:\Users\Леонид\Desktop\bot\мишка.jpg", 'rb')
    bot.send_photo(message.chat.id, photo=tedy, caption='Мишка Теди')
    tedy_mimic= open(r"C:\Users\Леонид\Desktop\bot\мишка мимик.jpg", 'rb')
    bot.send_photo(message.chat.id, photo=tedy_mimic, caption='Мишка Теди Мимик')
    hell_pug= open(r"C:\Users\Леонид\Desktop\bot\мопс без седла.jpg", 'rb')
    bot.send_photo(message.chat.id, photo=hell_pug, caption='Адский мопс')
    hell_pug_2= open(r"C:\Users\Леонид\Desktop\bot\мопс с седлом.jpg", 'rb')
    bot.send_photo(message.chat.id, photo=hell_pug_2, caption='Адский мопс с седлом')
    walrus= open(r"C:\Users\Леонид\Desktop\bot\морж с седлом.jpg", 'rb')
    bot.send_photo(message.chat.id, photo=walrus, caption='Морж с седлом')
    pitbull_2= open(r"C:\Users\Леонид\Desktop\bot\питбуль с упряжкой.jpg", 'rb')
    bot.send_photo(message.chat.id, photo=pitbull_2, caption='Питбуль с седлом')
    hell_hound= open(r"C:\Users\Леонид\Desktop\bot\псинка.JPG", 'rb')
    bot.send_photo(message.chat.id, photo=hell_hound, caption='Адская гончая')
    horned_toad= open(r"C:\Users\Леонид\Desktop\bot\рогатный-жаб.jpg", 'rb')
    bot.send_photo(message.chat.id, photo=horned_toad, caption='Рогатая жаба')
    stegosaurus= open(r"C:\Users\Леонид\Desktop\bot\стегозавр.JPG", 'rb')
    bot.send_photo(message.chat.id, photo=stegosaurus, caption='Стегозавр')
    hell_dog= open(r"C:\Users\Леонид\Desktop\bot\странный пес.JPG", 'rb')
    bot.send_photo(message.chat.id, photo=hell_dog, caption='Адский пес')
    fat_dragon= open(r"C:\Users\Леонид\Desktop\bot\толстый дракон.JPG", 'rb')
    bot.send_photo(message.chat.id, photo=fat_dragon, caption='Упитанный дракон')
    hell_cat= open(r"C:\Users\Леонид\Desktop\bot\херовый кот.JPG", 'rb')
    bot.send_photo(message.chat.id, photo=hell_cat, caption='Адский кот')
    chimera= open(r"C:\Users\Леонид\Desktop\bot\химера.jpg", 'rb')
    bot.send_photo(message.chat.id, photo=chimera, caption='Химера')
    cat_king= open(r"C:\Users\Леонид\Desktop\bot\кот король.png", 'rb')
    bot.send_photo(message.chat.id, photo=cat_king, caption='Кот король')
    csen= open(r"C:\Users\Леонид\Desktop\bot\горшок ксеноморф.jpg", 'rb')
    bot.send_photo(message.chat.id, photo=csen, caption='Горшок ксеноморф')


@bot.message_handler(commands=['Звери'])
def send_all_picture_animal(message):
    wolf= open(r"C:\Users\Леонид\Desktop\bot\волк.JPG", 'rb')
    bot.send_photo(message.chat.id, photo=wolf, caption='Волк')
    hound= open(r"C:\Users\Леонид\Desktop\bot\гончая.jpg", 'rb')
    bot.send_photo(message.chat.id, photo=hound, caption='Гончая')
    egypt_cat= open(r"C:\Users\Леонид\Desktop\bot\египетский кот.JPG", 'rb')
    bot.send_photo(message.chat.id, photo=egypt_cat, caption='Египетский кот')
    cat= open(r"C:\Users\Леонид\Desktop\bot\кот кверху животом.jpg", 'rb')
    bot.send_photo(message.chat.id, photo=cat, caption='Кот животом к верху')
    lion= open(r"C:\Users\Леонид\Desktop\bot\лев.jpg", 'rb')
    bot.send_photo(message.chat.id, photo=lion, caption='Лев')
    walrus_2= open(r"C:\Users\Леонид\Desktop\bot\морж.jpg", 'rb')
    bot.send_photo(message.chat.id, photo=walrus_2, caption='Морж')
    elk= open(r"C:\Users\Леонид\Desktop\bot\олень.jpg", 'rb')
    bot.send_photo(message.chat.id, photo=elk, caption='Олень')
    dog= open(r"C:\Users\Леонид\Desktop\bot\песель.jpg", 'rb')
    bot.send_photo(message.chat.id, photo=dog, caption='Песель')
    pitbull= open(r"C:\Users\Леонид\Desktop\bot\питбуль.jpg", 'rb')
    bot.send_photo(message.chat.id, photo=pitbull, caption='Питбуль')
    lynx= open(r"C:\Users\Леонид\Desktop\bot\рысь.jpg", 'rb')
    bot.send_photo(message.chat.id, photo=lynx, caption='Рысь')
    cat_sphynx= open(r"C:\Users\Леонид\Desktop\bot\сфинкс.jpg", 'rb')
    bot.send_photo(message.chat.id, photo=cat_sphynx, caption='Кот сфинкс')

#@bot.message_handler(commands=['Корзина'])
#def sell(message):



@bot.message_handler(content_types=['text'])
def repeat_all_messages(message):
    if message.text.lower() == 'канал':
        info_func(message)
    if message.text.lower() == 'своя модель':
        bot.send_message(message.chat.id, 'Как можно точнее опишите, какую вы хотите фигурку или оаставьте на нее ссылку. Так же оставьте ваш номер телефона или ник, для обратной свзяи')
        bot.send_photo(message.chat.id)
        bot.register_next_step_handler(message,send_request)
    if message.text.lower() == 'каталог':
        send_servive(message)
    if message.text.lower() == 'фэнтези':
        send_all_picture_fantasy(message)
    if message.text.lower() == 'звери':
        send_all_picture_animal(message)
    if message.text.lower()=='главное меню':
        first_name=message.chat.first_name
        Keyboard=types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
        button_shop=types.KeyboardButton(text="Каталог")
        button_own=types.KeyboardButton(text='Своя модель')
        button_info=types.KeyboardButton(text='Канал')
        cart=types.KeyboardButton(text='Корзина')
        Keyboard.add(button_shop, button_own, button_info, cart)
        bot.send_message(message.chat.id,f'удалил', reply_markup=Keyboard)
        
        


if __name__=='__main__':
    bot.infinity_polling()

