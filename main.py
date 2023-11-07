from typing import Final
from telegram import Update
from telegram.ext import Application,CommandHandler,MessageHandler,filters,ContextTypes


TOKEN: Final= '6962733431:AAG3inP9FRqRej68Mtc3yGSLxcFrB_t2e6I'
BOT_USERNAME: Final='@cntrl_skj_bot'

# Commands
async def start_command(update: Update, Context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hello!! welcome to skynet-git.')

async def help_command(update: Update, Context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hello!! for help contact SKJ-git.')

async def custom_command(update: Update, Context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hello!! this is a custom command for skynet-git.')

# Responses

def  handle_response(text: str) -> str:
    processed: str = text.lower()
    if 'hello' in processed:
        return 'Hey there!'
    if 'how are u' in processed:
        return 'how are u!'
    if 'what is ur name' in processed:
        return 'controllerbot-skynet!'
    if 'menu' in processed:
        return 'here is the menu!'
    
    return 'I do not understand..' 

async def handle_msg(update: Update, context: ContextTypes.DEFAULT_TYPE):
    Message_type: str = update.message.chat.type
    text: str = update.message.text

    print(f'User({update.message.chat.id}) in {Message_type} :"{text}"')

    response: str = handle_response(text)

    print('Bot: ',response)

    await update.message.reply_text(response)

async def error(update: Update, Context: ContextTypes.DEFAULT_TYPE):
    print(f'update {update} caused err {Context.error}')
    
if __name__ == "__main__":
    print('starting program/bot')
    app = Application.builder().token(TOKEN).build()

    #commands
    app.add_handler(CommandHandler('start',start_command))
    app.add_handler(CommandHandler('help',help_command))
    app.add_handler(CommandHandler('custom',custom_command))

    #messgaes 
    app.add_handler(MessageHandler(filters.TEXT,handle_msg))

    #errors
    app.add_error_handler(error)

    #poll the bot
    print('polling')
    app.run_polling(poll_interval=3)



