from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from datetime import datetime

TOKEN = "8667830292:AAFULxi6gqcjoHF3p5dTLZLGmY-LjGYI7Zk"

aniversarios = {}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Olá! Sou seu assistente de lembretes 😄"
    )

async def aniversario(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        nome = context.args[0]
        data = context.args[1]

        aniversarios[nome] = data

        await update.message.reply_text(
            f"Aniversário de {nome} salvo para {data} 🎉"
        )

    except:
        await update.message.reply_text(
            "Use:\n/aniversario Nome DD/MM"
        )

async def listar(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not aniversarios:
        await update.message.reply_text("Nenhum aniversário salvo.")
        return

    mensagem = "📅 Aniversários:\n\n"

    for nome, data in aniversarios.items():
        mensagem += f"{nome} - {data}\n"

    await update.message.reply_text(mensagem)

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("aniversario", aniversario))
app.add_handler(CommandHandler("listar", listar))

print("Bot rodando...")
app.run_polling()
