import os 
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ApplicationBuilder,CommandHandler,ContextTypes

load_dotenv()
TOKEN = os.getenv("TELEGRAM_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Fala! Bem Vindo à Barbearia.")

async def servico (update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Corte - R$ 30\nBarba - 50  ")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start)) 
app.add_handler(CommandHandler("servico", servico))
app.run_polling ()

