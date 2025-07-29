from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_message:
        await update.effective_message.reply_text("✅ Bot aktif! Sinyal sistemi hazır 🚀")

if __name__ == '__main__':
    app = ApplicationBuilder().token("8455466930:AAED97pwYbBvuBzUkd1oyYQYk7-ZA_yIT28").build()
    app.add_handler(CommandHandler("start", start))
    print("🚀 Bot başlatıldı. Telegram üzerinden /start yazarak test edebilirsin.")
    app.run_polling()
