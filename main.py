from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    ContextTypes,
    MessageHandler,
    filters,
)

BAD_WORDS = [
    "씨발",
    "병신",
    "좆",
    "미친",
    "개새끼"
]

async def detect_badword(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message or not update.message.text:
        return

    text = update.message.text.lower()

    if any(word in text for word in BAD_WORDS):
        await update.message.reply_text(
            f"⚠️ 욕설 감지됨\n\n{text}"
        )

def main():
    app = ApplicationBuilder().token(
        "8417386403:AAEqhnrxIX95pFAU9k-qene9Aw2wAPG_mjU"
    ).build()

    app.add_handler(
        MessageHandler(filters.TEXT & ~filters.COMMAND, detect_badword)
    )

    print("🤖 Telegram bot running...")
    app.run_polling()

if __name__ == "__main__":
    main()
