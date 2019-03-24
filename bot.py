import config
import telebot
import random
import sys, random, os, time
from telegram.ext import Updater, InlineQueryHandler, CommandHandler
import requests
import re
import os.path
import subprocess

bot = telebot.TeleBot(config.token)

#chat = '' # here you need to enter the chat ID in which the bot will write.

zi = os.path.exists('img.zip')

if zi == True:
	subprocess.Popen(['python', 'unziper.py'])
else:
	pass

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

@bot.message_handler(commands = [config.key])
def id(message):
	f = open('id.txt', 'w')
	f.write(str(message.chat.id))
	f.close()
	print(message.chat.id)

di = os.path.exists('id.txt')
if di == True:
	f = open('id.txt')		
	chat = f.read()
	f.close()
else:
	pass
	
@bot.message_handler(commands = ['start'])
def start(message):
	bot.send_message(message.chat.id, config.start_mess)
	# print(message.chat.id)

@bot.message_handler(commands = ['help'])
def help(message):
	bot.send_message(message.chat.id, config.help_mess)

@bot.message_handler(commands = ['dog'])
def dog(message):
    url = get_url_dog()
    chat.id = message.chat.id
    bot.send_photo(message.chat.id, photo = url)

@bot.message_handler(content_types = ['text'])
def repeat_all_messages(message):
	 bot.send_message(chat, message.text) # if you want the bot to send all messages a certain chat.

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
