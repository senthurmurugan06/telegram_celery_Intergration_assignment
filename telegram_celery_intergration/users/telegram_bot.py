import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
from django.conf import settings
from .models import User

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    telegram_username = user.username
    if telegram_username:
        # Save the Telegram username to the database
        User.objects.update_or_create(
            telegram_username=telegram_username,
            defaults={'telegram_username': telegram_username}
        )
        await update.message.reply_text(f"Hello {telegram_username}! Your Telegram username has been saved.")
    else:
        await update.message.reply_text("Please set a username in your Telegram settings and try again.")

def run_bot():
    token = os.getenv('TELEGRAM_BOT_TOKEN')
    if not token:
        raise ValueError("TELEGRAM_BOT_TOKEN environment variable is not set!")
    
    print(f"Starting bot with token: {token[:10]}...")  # Only print first 10 chars for security
    application = Application.builder().token(token).build()
    application.add_handler(CommandHandler("start", start))
    print("Bot is running...")
    
    # Use the correct polling method
    application.run_polling(allowed_updates=Update.ALL_TYPES) 