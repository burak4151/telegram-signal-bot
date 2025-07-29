from telegram.ext import ApplicationBuilder, CommandHandler
from telegram import Update
from telegram.ext import ContextTypes

import os

TOKEN = os.environ.get("8455466930:AAED97pwYbBvuBzUkd1oyYQYk7-ZA_yIT28")  # Environment'ten al

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🟢 Bot aktif!")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))

app.run_polling()


