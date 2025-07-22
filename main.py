from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from ludo.game import LudoGame

games = {}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🎲 Welcome to Telegram Ludo!\n/startgame to begin.")

async def start_game(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    games[chat_id] = LudoGame()
    await update.message.reply_text("✅ New Ludo game created. Players can now /join")

async def join(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    user = update.effective_user.first_name
    if chat_id in games:
        msg = games[chat_id].add_player(user)
        await update.message.reply_text(msg)
    else:
        await update.message.reply_text("No active game. Use /startgame.")

async def roll(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    if chat_id in games:
        result = games[chat_id].roll_dice()
        await update.message.reply_text(result)
    else:
        await update.message.reply_text("Start a game first with /startgame.")

app = ApplicationBuilder().token("YOUR_TOKEN_HERE").build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("startgame", start_game))
app.add_handler(CommandHandler("join", join))
app.add_handler(CommandHandler("roll", roll))
app.run_polling()
