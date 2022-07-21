from distutils.log import INFO
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler

TOKEN='5506412234:AAF-0_PQLOQkpwb-Ry-LBK_FiDtxPOYWfUU'

logging.basicConfig(
  format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
  level = logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
  await context.bot.send_message(chat_id=update.effective_chat.id, text='Olá, logo teremos informações')

async def crash(update: Update, context: ContextTypes.DEFAULT_TYPE):
  await context.bot.send_message(chat_id=update.effective_chat.id, text='Aqui te darei informação sobre o game crash')

if __name__ == '__main__':
  apllication = ApplicationBuilder().token(TOKEN).build()

  start_handler = CommandHandler('start', start)
  crash_handler = CommandHandler('crash', crash)
  apllication.add_handler(start_handler)

  apllication.run_polling()