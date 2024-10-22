import telebot
import torch
import os
from transformers import RobertaTokenizer, RobertaForSequenceClassification
from mongo_db import MongoDB
from dotenv import load_dotenv

from predict_label import Classifier

load_dotenv()

# Initialize the Telegram bot with your token
bot = telebot.TeleBot(os.environ["API_TOKEN"])
# MONGO_URI = "mongodb://localhost:27017/"  # Replace with your MongoDB URI if needed
# DB_NAME = "telegram_bot"  # Database name
# COLLECTION_NAME = "messages"  # Collection name

# Load RoBERTa model and tokenizer (pretrained for binary classification like hate speech detection)
classifier = Classifier()
# Initialize MongoDB
# mongo_db = MongoDB(MONGO_URI, DB_NAME, COLLECTION_NAME)


# Handler for receiving messages
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    user_id = message.from_user.id
    user_message = message.text
    print(user_message)

    # Run model inference
    is_hate_speech = classifier.encode_and_classify([user_message])

    # Prepare verdict message
    print(is_hate_speech)
    verdict = "Hate Speech Detected" if is_hate_speech else "Not Hate Speech"
    bot.reply_to(message, verdict)

    # # Save the data to MongoDB
    # log_entry = {"user_id": user_id, "message": user_message, "verdict": verdict}
    # collection.insert_one(log_entry)  # Insert the log into the MongoDB collection

    # print(f"Logged: {log_entry}")  # Optionally log to console


# Start polling (bot will listen for new messages)
bot.polling()
