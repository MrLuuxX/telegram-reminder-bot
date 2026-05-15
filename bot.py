import os
from threading import Thread
from flask import Flask
from telegram.ext import Application, CommandHandler

TOKEN = os.getenv("BOT_TOKEN")

# ===== FLASK =====
app_web = Flask(__name__)

@app_web.route("/")
def home():
    return "Bot online!"

def run_web():
    port = int(os.environ.get("PORT", 10000))
    app_web.run(host="0.0.0.0", port=port)

# ===== TELEGRAM =====
async def start(update, context):
    await update.message.reply_text("Bot funcionando 😄")

telegram_app = Application.builder().token(TOKEN).build()

telegram_app.add_handler(CommandHandler("start", start))

# ===== START =====
if __name__ == "__main__":
    Thread(target=run_web).start()

    print("Bot iniciado...")
    telegram_app.run_polling()
