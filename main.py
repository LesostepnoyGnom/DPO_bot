# -*- coding: utf-8 -*-
"""
Created on Fri May 12 11:50:20 2023

@author: 1618047
"""

import telebot
from telebot import types

bot = telebot.TeleBot('6135866200:AAFphz7aOXAVGHyLm9Tugpic76kaqqGIcqU')

def get_img(message):
    bot.send_message(message.from_user.id, 'Изображение получено')

def send(message):
    bot.send_message(message.from_user.id, 'Изображение получено')

@bot.message_handler(commands = ['start'])
def main(message):
    
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton(text='Внести информацию', callback_data='get_inf')
    btn2 = types.InlineKeyboardButton(text='Help', callback_data='help')
    
    markup.add(btn1)
    markup.add(btn2)
    
    bot.send_message(message.from_user.id, f'Здравствуйте, {message.from_user.first_name}', reply_markup = markup)
    
@bot.message_handler(commands = ['help'])
def fhelp(message):
    bot.send_message(message.from_user.id, '<b>Help</b> <em><u>information</u></em>', parse_mode=('html'))
    
@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    
    if callback.data == 'get_inf':
        bot.send_message(callback.message.chat.id, 'Отправьте адрес')
        bot.register_next_step_handler(callback.message, adres)
    elif callback.data == 'help':
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton(text='Посмотреть список запрашиваемой информации', callback_data='list')
        btn2 = types.InlineKeyboardButton(text='Другое', callback_data='other')
        
        markup.add(btn1)
        markup.add(btn2)
        
        bot.send_message(callback.message.chat.id, 'Что вас интересует?', reply_markup = markup)
        
    elif callback.data == 'list':
        bot.send_message(callback.message.chat.id, '1) Адресс объекта\n'
                                                   '2) Фото оборудования\n'
                                                   '3) Информационная табличка оборудования\n'
                                                   '4) Наpвание оборудования\n'
                                                   '5) Производитель\n'
                                                   '6) Наличие гарантии\n'
                                                   '7) Контакты гарантийного центра\n'
                                                   '8) Дата последнего ТО\n'
                                                   '9) Время работы оборудования в сутки\n'
                                                   '10) Дата введения в эксплуатацию\n'
                                                   '11) Напряжение питания\n'
                                                   '12) Потребление электроэнергии в кВт/ч')
    
def adres(message):
    adres = message.text.strip()
    bot.register_next_step_handler(message, photo)
    bot.send_message(message.chat.id, 'Отправьте фото аппаратуры')
def photo(message):
    photo = message.text.strip()
    bot.register_next_step_handler(message, table)
    bot.send_message(message.chat.id, 'Отправьте фото информационной таблички')
def table(message):
    table = message.text.strip()
    bot.register_next_step_handler(message, name)
    bot.send_message(message.chat.id, 'Напишите название оборудования')
def name(message):
    name = message.text.strip()
    bot.register_next_step_handler(message, proiz)
    bot.send_message(message.chat.id, 'Напишите производителя оборудования')
def proiz(message):
    proiz = message.text.strip()
    bot.register_next_step_handler(message, garant)
    bot.send_message(message.chat.id, 'Находится ли оборудование на гарантии')
def garant(message):
    garant = message.text.strip()
    bot.register_next_step_handler(message, finish)
    bot.send_message(message.chat.id, 'Отправьте фото информационной таблички')
def finish(message):
    bot.send_message(message.chat.id, 'Пожалуйста, проверьте введённые данные\n'
                                      '1) Адресс объекта - '+adres+'\n'
                                      '2) Фото оборудования - '+photo+'\n'
                                      '3) Информационная табличка оборудования - '+table+'\n'
                                      '4) Название оборудования - '+name+'\n'
                                      '5) Производитель - '+proiz+'\n'
                                      '6) Наличие гарантии - '+garant+'\n'
                                      '7) Контакты гарантийного центра - \n'
                                      '8) Дата последнего ТО\n'
                                      '9) Время работы оборудования в сутки\n'
                                      '10) Дата введения в эксплуатацию\n'
                                      '11) Напряжение питания\n'
                                      '12) Потребление электроэнергии в кВт/ч')
bot.polling(non_stop=True)