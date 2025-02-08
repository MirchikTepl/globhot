import telebot
from bot_logic import gen_pass, gen_temp, gen_problem, gen_zasyxa, gen_gryaz, gen_elektro, flip_coin  # Импортируем функции из bot_logic

# Замени 'TOKEN' на токен твоего бота
bot = telebot.TeleBot("7675329100:AAEzb-xLY45VwVQ0P1jOMvZeHFrnQLd1ROg")

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я твой Telegram бот. Напиши команду /hello, /bye, /pass, /problem ")

@bot.message_handler(commands=['hello'])
def send_hello(message):
    bot.reply_to(message, "Привет! Давай поговорим о глоб.потеплении: Нажмите на проблему:   /Elektro,    /Gryaz,    /Zasyxa")

@bot.message_handler(commands=['bye'])
def send_bye(message):
    bot.reply_to(message, "Пока! Удачи!")

@bot.message_handler(commands=['pass'])
def send_password(message):
    password = gen_pass(10)  # Устанавливаем длину пароля, например, 10 символов
    bot.reply_to(message, f"Вот твой сгенерированный пароль: {password}")

@bot.message_handler(commands=['problem'])
def send_emodji(message):
    problem = gen_problem()
    bot.reply_to(message, f"Нажмите на проблему:    /Перегрузка электричества,    /Загрязнения,    /Засуха")

@bot.message_handler(commands=['Засуха'])
def send_emodji(message):
    zasyxa = gen_zasyxa()
    bot.reply_to(message, f"Если в вашем регионе преобладал и преобладает сухой климат, то всё стабильно, но если у вас должна преобладать влага, а сейчас засуха, то ситуация критическая. Глоб.потепление уже у вас, дабы не ухудшить ситуацию читайте остальные проблемы тут /problem. Больше инфы тут: https://www.un.org/ru/global-issues/climate-change")

@bot.message_handler(commands=['Перегрузка электричества'])
def send_emodji(message):
    elektro = gen_elektro()
    bot.reply_to(message, f"Если в важем окружении замечено большое потребление энергии, то рекомендую попросить (хотя бы) знакомых и близких потреблять меньше энергии, т.к. черезмерное потребление эллектричества приводить не только к поломке станций, но и к глоб.потеплению. Больше инфы тут: https://www.un.org/ru/global-issues/climate-change")

@bot.message_handler(commands=['Загрязнения'])
def send_emodji(message):
    problem = gen_problem()
    bot.reply_to(message, f"Если в вашем регионе обнаружена экологическая проблема, свящанная с загрязнением улиц, воды и т.д., то это очень плохо. Рекомендовано пожаловаться в правительство и немедленно устранить проблему, которая в дальнейшем приведёт к глоб.потеплению. Больше инфы тут: https://www.un.org/ru/global-issues/climate-change")

@bot.message_handler(commands=['coin'])
def send_coin(message):
    coin = flip_coin()
    bot.reply_to(message, f"Монетка выпала так: {coin}")

# Запускаем бота
bot.polling()
