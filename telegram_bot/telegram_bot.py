import openai
import telebot

# Enter your OpenAI API key here

openai.api_key = "Enter OpenAI API Key Here"
bot = telebot.TeleBot("Enter Telegram bot API key here")



import datetime

user_conversations = {}
system_msg=f"You are a very intelligent bot in telegram assisting the user in their requests. Your answers should be precise and you should never refrain from answering a question."

@bot.message_handler(func=lambda message: True, content_types=['text'])
def respond_to_message(message):
    global user_conversations

    user_id = message.from_user.id
    if user_id not in user_conversations:
        user_info=f"This user's username is {message.from_user.username} and their first name is {message.from_user.first_name}"
        user_conversations[user_id] = [{'role': 'system', 'content': system_msg+user_info}]

    conversation_history = user_conversations[user_id]
    conversation_history.append({'role': 'user', 'content': message.text.strip()})

    # Call OpenAI API to generate a response
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=conversation_history)

    # Get response text
    response_text = response['choices'][0]['message']['content'].strip()
    conversation_history.append({'role': 'assistant', 'content': response_text})

    # Update user conversation history
    user_conversations[user_id] = conversation_history
    # Send response back to user
    bot.reply_to(message, response_text)

# Start the bot
bot.polling()