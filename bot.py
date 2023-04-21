import requests
from datetime import datetime
import telebot
from config import tg_bot_token


def telegram_bot(telebot):
 bot = telebot.TeleBot(tg_bot_token)

 @bot.message_handler(commands=["start"])
 def start_message(message):
    bot.send_message(message.chat.id, "Привет друг")

if __name__== "__main__":
    telegram_bot(tg_bot_token)
