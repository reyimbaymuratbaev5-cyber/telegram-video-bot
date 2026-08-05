import json
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters

TOKEN = "BOT_TOKENINGIZ"

with open("codes.json", "r") as f:
    CODES = json.load(f)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🎬 Video olish uchun kodni yuboring.")

async def check_code(update: Update, context: ContextTypes.DEFAULT_TYPE):
    code = update.message.text.strip()

    if code in CODES:
        await update.message.reply_video(CODES[code])
    else:
        await update.message.reply_text("❌ Kod noto'g'ri.")

app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, check_code))

app.run_polling()
