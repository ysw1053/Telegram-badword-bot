from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    ContextTypes,
    MessageHandler,
    filters,
)

# 네가 미리 정한 욕설 리스트
BAD_WORDS = [
    "씨발",
    "병신",
    "좆",
    "미친",
    "개새끼"
]

async def detect_badword(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # 메시지 없으면 무시 (사진 등)
    if not update.message or not update.message.text:
        return

    text = update.message.text.lower()

    # 욕설 감지
    if any(word in text for word in BAD_WORDS):
        await update.message.reply_text(
            f"⚠️ 욕설 감지됨\n\n{text}"
        )
    # 욕설 없으면 아무 반응도 안 함

def main():
    app = ApplicationBuilder().token(
        "여기에_네_텔레그램_BOT_TOKEN"
    ).build()

    # 모든 일반 텍스트 메시지 감지
    app.add_handler(
        MessageHandler(filters.TEXT & ~filters.COMMAND, detect_badword)
    )

    print("🤖 Clean Keyboard Telegram Bot 실행 중...")
    app.run_polling()

if __name__ == "__main__":
    main()
