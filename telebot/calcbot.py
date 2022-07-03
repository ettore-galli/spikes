#!/usr/bin/python

# This is a simple echo bot using the decorator mechanism.
# It echoes any incoming text messages.

import telebot

API_TOKEN = "5537796647:AAFjMM0EGifw8s-Eyxh1rGDWNxWEr1bOF_M"

bot = telebot.TeleBot(API_TOKEN)


# Handle '/start' and '/help'
@bot.message_handler(commands=["help", "start"])
def send_welcome(message):
    bot.reply_to(
        message,
        """\
Supercalc bot
""",
    )


def process_message(message: str) -> str:
    return f"--> {message}"


# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, process_message(message.text))


def main_bot():
    bot.infinity_polling()


if __name__ == "__main__":
    main_bot()
