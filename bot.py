print('0%')
import config
print('7%')
import telebot
print('14%')
import random
print('21%')
import sys
print('28%')
import random
print('35%')
import os
print('42%')
import time
print('49%')
import requests
print('56%')
import re
print('63%')
import os.path
print('70%')
import subprocess
print('77%')
from telegram.ext import Updater
print('84%')
from telegram.ext import InlineQueryHandler
print('94%')
from telegram.ext import CommandHandler
print('100%')

bot = telebot.TeleBot(config.token)

zi = os.path.exists('img.zip')

if zi == True:
	subprocess.Popen(['python', 'unziper.py'])
else:
	pass

@bot.message_handler(commands = ['id', 'chat'])
def id(message):
        bot.send_message(message.chat.id, message.chat.id)
        print(message.chat.id)

@bot.message_handler(commands = ['img'])
def anime(message):
	path = os.path.exists('img')
	if path == True:
		l = os.listdir('img')
		score = 0
		for i in l:
			score += 1
		r = random.randint(1, score)
		bot.send_photo(message.chat.id, open('img/{0}'.format(l[r]), 'rb'))
	else:
		pass

def get_url_dog():
    contents = requests.get('https://random.dog/woof.json').json()
    url = contents['url']
    return url

@bot.message_handler(commands = ['start'])
def start(message):
	bot.send_message(message.chat.id, config.start_mess)

@bot.message_handler(commands = ['help'])
def help(message):
	bot.send_message(message.chat.id, config.help_mess)

@bot.message_handler(commands = ['dog'])
def dog(message):
    url = get_url_dog()
    bot.send_photo(message.chat.id, photo = url)

@bot.message_handler(content_types = ['text'])
def repeat_all_messages(message):
	name = message.from_user.first_name
	bot.send_message(config.chat, '{0} : {1}'.format(name, message.text)) # if you want the bot to send all messages a certain chat.

def main():
    updater = Updater(bot)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('dog',dog))
    updater.start_polling()
    updater.idle()

print('Done')

if __name__ == '__main__':
     bot.polling(none_stop = True)
     main()
