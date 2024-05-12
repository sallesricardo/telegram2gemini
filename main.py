import numpy as np
import pandas as pd

import google.generativeai as genai

import telebot

from settings import GOOGLE_API_KEY, TELEGRAM_TOKEN

genai.configure(api_key=GOOGLE_API_KEY)

available_models = []
for m in genai.list_models():
    if 'generateContent' in m.supported_generation_methods:
        available_models.append(m.name.split('/')[-1])

model_name = 'gemini-1.0-pro'

generation_config = {
  "candidate_count": 1,
  "temperature": 0.5,
}

safety_settings={
    'HATE': 'BLOCK_NONE',
    'HARASSMENT': 'BLOCK_NONE',
    'SEXUAL' : 'BLOCK_NONE',
    'DANGEROUS' : 'BLOCK_NONE'
    }

def get_model(model, config, safety):
    return  genai.GenerativeModel(model_name=model,
                                  generation_config=config,
                                  safety_settings=safety)

model = get_model(model_name, generation_config, safety_settings)

bot = telebot.TeleBot(TELEGRAM_TOKEN)

@bot.message_handler(commands=['start'])
def send_wellcome(message):
    bot.reply_to(message, "Seja bem vindo(a)!")

@bot.message_handler(commands=['getModels'])
def send_models_list(message):
    bot.reply_to(message, '\n'.join(available_models))

@bot.message_handler(commands=['config'])
def set_configs(message):
    global model_name
    global generation_config
    global safety_settings

    reload_model = False
    error_msg = ''
    param_to_change = [
        'model',
        'temperature',
        'safety',
        'help'
    ]
    params = message.text.split(' ')
    if (params[1].lower() == param_to_change[0]) and params[2] in available_models:

        model_name = params[2]
    elif (params[1].lower() == param_to_change[1]):
        try:
            generation_config['temperature'] = float(params[2])
            reload_model = True
        except:
            error_msg = 'Parametro deve ser um número de 0 a 1'

    if reload_model:
        model = get_model(model_name, generation_config, safety_settings)
        bot.reply_to(message, f'{params[1]} Configurado!')
    else:
        bot.reply_to(message, f'{params[1]} não reconhecido! {error_msg}')

@bot.message_handler(func=lambda message: True)
def get_gemini_answer(message):
    print(message)
    print(message.content_type)
    if (message.content_type == 'text'):
        response = model.generate_content(message.text)
        bot.reply_to(message, response.text)
    else:
        print(message)
        bot.reply_to(message, 'Tipo de mensagem ainda não tratado')


bot.infinity_polling()


