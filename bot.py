import config
import telebot
import random
import sys, random, os, time
from telegram.ext import Updater, InlineQueryHandler, CommandHandler
import requests
import re

start_mess = '🧭/help -- none\n🐕/dog -- sends a photo of a dog\n🎌/anime -- sends a picture in anime styles'
help_mess = 'I can not help you'

bot = telebot.TeleBot(config.token)



@bot.message_handler(commands = ['anime'])
def anime(message):
	l = os.listdir('img')
	score = 0
	for i in l:
		score += 1
	r = random.randint(1, score)
	addres = str(r) + '.png'
	bot.send_photo(message.chat.id, open(r'img\{0}'.format(addres), 'rb'))

def get_url_dog():
    contents = requests.get('https://random.dog/woof.json').json()
    url = contents['url']
    return url

@bot.message_handler(commands = ['start'])
def start(message):
	bot.send_message(message.chat.id, start_mess)
	# print(message.chat.id)

@bot.message_handler(commands = ['help'])
def help(message):
	bot.send_message(message.chat.id, help_mess)

@bot.message_handler(commands = ['dog'])
def dog(message):
    url = get_url_dog()
    chat_id = message.chat.id
    bot.send_photo(chat_id=chat_id, photo=url)

@bot.message_handler(content_types = ["text"])
def repeat_all_messages(message):
	text = ''
	for x in message.text:
		if True:
			text += x
	print(text)
	bot.send_message(config.chat, text)

def main():
    updater = Updater(bot)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('dog',dog))
    updater.start_polling()
    updater.idle()

print('done')

if __name__ == '__main__':
     bot.polling(none_stop = True)
     main()
