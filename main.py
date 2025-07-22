from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from game import LudoGame

games = {}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🎲 Welcome to Telegram Ludo!\n/startgame to begin.")

async def start_game(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    games[chat_id] = LudoGame(chat_id)
    await update.message.reply_text("✅ New Ludo game created. Players can now /join")

async def join(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    user = update.effective_user.first_name
    game = games.get(chat_id) or LudoGame(chat_id)
    msg = game.add_player(user)
    games[chat_id] = game
    await update.message.reply_text(msg)

async def roll(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    game = games.get(chat_id) or LudoGame(chat_id)
    result = game.roll_dice()
    games[chat_id] = game
    await update.message.reply_text(result)

app = ApplicationBuilder().token("7882173382:AAGFqT3FNolrkIHmn83uG2CsFDS1bDgBZ-s").build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("startgame", start_game))
app.add_handler(CommandHandler("join", join))
app.add_handler(CommandHandler("roll", roll))
app.run_polling()
