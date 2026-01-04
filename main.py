from telegram.ext import ApplicationBuilder, MessageHandler, filters, CallbackQueryHandler
from telegram.ext._handlers.commandhandler import CommandHandler

import modules
import traceback

def main():
    db = modules.DB()
    db.h_init_db()
    bot = modules.Bot(db)
    
    user_filter = filters.User(user_id=modules.ALLOWED_USERS)
    
    app = ApplicationBuilder().token(modules.TOKEN).post_init(bot.set_commands).build()
    
    app.add_handler(CommandHandler("start", bot.start_cmd, filters=user_filter))
    app.add_handler(CommandHandler("k", bot.keyboard_cmd, filters=user_filter))
    app.add_handler(CommandHandler("ik", bot.inkeyboard_cmd, filters=user_filter))
    app.add_handler(CommandHandler("delete_this", bot.delete_this_cmd, filters=user_filter))
    
    app.add_handler(CommandHandler("h", bot.h_cmd, filters=user_filter))
    app.add_handler(CommandHandler("hl", bot.hl_cmd, filters=user_filter))
    
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND & user_filter, bot.reply))
    
    app.add_handler(CallbackQueryHandler(bot.button_callback))
    

    print("Bot is running...")

    try:
        app.run_polling()
    except Exception as e:
        traceback.print_exc()


if __name__ == "__main__":
    main()
