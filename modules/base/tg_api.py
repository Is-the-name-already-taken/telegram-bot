from telegram import (
    Update,
    BotCommand,
    ReplyKeyboardMarkup,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)
from telegram.ext import ContextTypes


class Bot:
    def __init__(self, db):
        self.db = db

    async def set_commands(self, app):
        await app.bot.set_my_commands([BotCommand("start", "Start")])
        return

    async def start_cmd(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        await context.bot.send_message(chat_id=update.effective_chat.id, text="Hello")
        return

    async def delete_this_cmd(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        await context.bot.send_message(
            chat_id=update.effective_chat.id, text="This command will be deleted"
        )
        await update.message.delete()
        return

    async def reply(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        text = update.message.text
        await update.message.reply_text(f"You said: {text}")
        return

    async def keyboard_cmd(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        keyboard = [["/start", "Show Recent Data"], ["Delete Data"]]
        reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
        await update.message.reply_text(
            "Please choose an option:", reply_markup=reply_markup
        )
        return

    async def inkeyboard_cmd(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        keyboard = [
            [
                InlineKeyboardButton("Fetch Data", callback_data="fetch"),
                InlineKeyboardButton("Help", callback_data="help"),
            ],
            [InlineKeyboardButton("Go to Google", url="https://google.com")],
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await update.message.reply_text("Select an action:", reply_markup=reply_markup)
        return

    async def button_callback(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        query = update.callback_query
        await query.answer()

        if query.data == "fetch":
            await query.edit_message_text(text="Fetching data...")
        elif query.data == "help":
            await query.edit_message_text(text="Help section")
        return
    
    async def h_cmd(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        msg = update.message.text
        if " " in msg:
            command_part, body = msg.split(maxsplit=1)
        else:
            body = ""
        
        args = body.split("\n")
        for a in args:
            self.db.insert_h_data(a)
            
        await context.bot.send_message(chat_id=update.effective_chat.id, text="Data inserted.")
        return

    async def hl_cmd(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        h_list = self.db.fetch_all_h_data()
        h_list = str(h_list)
        await context.bot.send_message(chat_id=update.effective_chat.id, text=h_list)
        return