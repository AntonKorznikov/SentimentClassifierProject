import telebot
import torch
import os
from transformers import RobertaTokenizer, RobertaForSequenceClassification
from mongo_db import MongoDB
from dotenv import load_dotenv

from predict_label import Classifier

load_dotenv()


bot = telebot.TeleBot(os.environ["API_TOKEN"])
MONGO_URI = "mongodb://mongo:27017/"
DB_NAME = "telegram_bot"
COLLECTION_NAME = "messages"

classifier = Classifier()
mongo_db = MongoDB(MONGO_URI, DB_NAME, COLLECTION_NAME)


@bot.message_handler(commands=["send_offense"])
def send_offense(message):
    user_id = message.from_user.id

    offense = mongo_db.collection.find_one({"user_id": user_id})

    if offense:
        verdict = offense.get("verdict", "No verdict found.")
        user_message = offense.get("message", "No message found.")
        response = f"Your last offense:\nMessage: {user_message}\nVerdict: {verdict}"
    else:
        response = "No offense record found for you."
    bot.reply_to(message, response)


# Handler for receiving ALL messages
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    user_id = message.from_user.id
    user_message = message.text
    print(user_message)

    is_hate_speech = classifier.encode_and_classify([user_message])
    print(is_hate_speech)
    verdict = "Hate Speech Detected" if is_hate_speech else "Not Hate Speech"
    bot.reply_to(message, verdict)
    log_entry = {"user_id": user_id, "message": user_message, "verdict": verdict}
    # TODO: insertion doesn't work
    mongo_db.collection.insert_one(log_entry)

    print(f"Logged: {log_entry}")


bot.polling()
