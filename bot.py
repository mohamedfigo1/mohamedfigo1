import logging
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters

logging.basicConfig(level=logging.INFO)

MAIN_MENU = [
    ['📊 تابع أرباحك', '📌 الشروط والحد الأدنى'],
    ['💬 الدعم والسحب']
]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    reply_markup = ReplyKeyboardMarkup(MAIN_MENU, resize_keyboard=True)
    await update.message.reply_text(
        "أهلاً بك في بوت المهام! 👋\nاختر من القائمة أدناه:",
        reply_markup=reply_markup
    )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == '📊 تابع أرباحك':
        user_balance = 0.00 
        await update.message.reply_text(f"📊 حسابك الشخصي:\n\n💰 رصيدك الحالي: {user_balance} جنيه\n\n✅ يتم تحديث الرصيد فور قبول المهام.")

    elif text == '📌 الشروط والحد الأدنى':
        await update.message.reply_text("📌 الشروط والحد الأدنى للسحب:\n\n1. الحد الأدنى للسحب هو ($500/10£) .\n2. المراجعة تتم يدوياً لمنع التلاعب.")

    elif text == '💬 الدعم والسحب':
        await update.message.reply_text("🔒 طلب السحب:\n\nيتم فتح خيار السحب تلقائياً عند وصول رصيدك إلى الحد الأدنى ($500/10£).")

if name == 'main':
    TOKEN = "8898733113:AAH4qLA0xZPCUwu0GsT3aRSoriji3QIaRYo"
    
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    
    app.run_polling()