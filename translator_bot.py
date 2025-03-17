import telebot
import os
from dotenv import load_dotenv
from googletrans import Translator
import logging

translator = Translator()

load_dotenv()

# Replace 'YOUR_TELEGRAM_BOT_TOKEN' with your actual bot token
BOT_TOKEN = os.environ.get(
    "TELEGRAM_BOT_TOKEN"
)  # Using os.environ is recommended for security

if not BOT_TOKEN:
    print("Error: TELEGRAM_BOT_TOKEN environment variable not set.")
    exit(1)

bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(func=lambda message: True)  # React to all messages
def handle_all_messages(message):
    """
    Handles all incoming messages and replies with a simple acknowledgement.
    """
    try:
        chat_id = message.chat.id
        user_id = message.from_user.id
        username = (
            message.from_user.username or message.from_user.first_name or "unknown"
        )  # handle possible cases of no username.
        message_text = (
            message.text or message.caption or "No text"
        )  # handle cases of photo/video messages

        logging.warning(
            f"Received message from {username} ({user_id}) in chat {chat_id}: {message_text}"
        )  # logging

        result = translator.detect(message_text)
        logging.warning(result)

        # Respond to the message
        if result.lang == "uk":
            text = translator.translate(
                message_text, src='uk', dest='zh-CN'
            ).text
            bot.reply_to(message, f"{username}说了:\n{text}")

    except Exception as e:
        print(f"Error handling message: {e}")


if __name__ == "__main__":
    print("Bot started, listening for messages...")
    bot.infinity_polling()
