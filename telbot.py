import random
import time
import telebot

bot = telebot.TeleBot('5647135917:AAEQQlyHm63cwX62hrC6u-QGg-EHeXkATxI')

word = ['пидор','бот']
first = (['Иди ка в хуй нарядись, ',
         'И нахуй ты вообще родился, ',
         'А ты хорош, но я все равно твою мать ебал... '])
second = ['21', '22', '23']
third = ['31', '32', '33']

@bot.message_handler(commands=['start',]) 
def start(message):
    if message.from_user.first_name == 'Михаил':
        return bot.send_message(message.chat.id, 'привет пирожочек =)')
    else:
        mess = f'Привет, {message.from_user.first_name}'
        return bot.send_message(message.chat.id, mess)


@bot.message_handler(commands=['debug'])
def start(message):
    mess = f'Хуй тебе, а не отладка, {message.from_user.first_name}' 
    bot.send_message(message.chat.id, mess)


@bot.message_handler(commands=['help'])
def start(message):
    mess = f'Сорян, но тебе я не помогу, {message.from_user.first_name}' 
    bot.send_message(message.chat.id, mess)
    time.sleep(random.randint(2, 5))
    mess = f'Да я рофлю, вот мои команды:'
    bot.send_message(message.chat.id, mess)


@bot.message_handler(content_types=['text'])
def get_text_message(message):
    mess = message.text.lower()
    if 'пидор' in mess.split() and ('бот,' in mess.split() or 'бот' in mess.split()):
        return bot.send_message(message.chat.id, f'{random.choice(first)}{message.from_user.first_name}')

    if 'бот' in mess.split():
        return bot.send_message(message.chat.id, f'Мне пока нечего на это ответить, {message.from_user.first_name}')

#msg = random.choice(first) + ' ' + random.choice(second) + ' ' + random.choice(third)

bot.polling(none_stop=True)
