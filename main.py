import os
import requests
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.dispatcher.filters import Command


# Replace with your Telegram bot token (you'll set this as an environment variable)
TELEGRAM_API_TOKEN = os.getenv("7663557065:AAHjhf-lA5xyGaOYxW5YvUV41C9RecIpba4")

# Free GPT API URL (you can change this to any API you prefer for improving scripts)
GPT_API_URL = "https://api.openai.com/v1/completions"  # Use a real API here, like OpenAI API

# Initialize bot and dispatcher
bot = Bot(token=TELEGRAM_API_TOKEN)
dp = Dispatcher()

# Start command handler
@dp.message(Command("start"))
async def start_command(message: Message):
    await message.answer("🚀 Send me your Instagram script, and I'll help improve its storytelling!")

# Script improvement handler
@dp.message()
async def improve_script(message: Message):
    user_script = message.text

    # Sending a request to a free GPT API for script improvement (replace with real API)
    headers = {
        "Authorization": f"Bearer {os.getenv('GPT_API_KEY')}",
        "Content-Type": "application/json"
    }
    
    data = {
        "model": "text-davinci-003",  # You can use any GPT-3 model
        "prompt": f"Improve this script for Instagram reels storytelling:\n\n{user_script}",
        "max_tokens": 250,
    }
    
    response = requests.post(GPT_API_URL, json=data, headers=headers)
    
    if response.status_code == 200:
        improved_script = response.json().get("choices", [{}])[0].get("text", "Sorry, I couldn't improve that.")
        await message.answer(f"✨ Improved Script:\n\n{improved_script}")
    else:
        await message.answer("⚠️ Error generating response. Try again later.")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
