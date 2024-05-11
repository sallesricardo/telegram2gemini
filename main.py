import numpy as np
import pandas as pd

import google.generativeai as genai

import telebot

from settings import GOOGLE_API_KEY, TELEGRAM_TOKEN

genai.configure(api_key=GOOGLE_API_KEY)

for m in genai.list_models():
  if 'embedContent' in m.supported_generation_methods:
    print(m.name)

bot = telebot.TeleBot(TELEGRAM_TOKEN)

@bot.message_handler(commands=['start'])
def send_wellcome(message):
    bot.reply_to(message, "Seja bem vindo(a)!")


bot.infinity_polling()

