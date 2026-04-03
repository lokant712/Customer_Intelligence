import os
import logging
import asyncio
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters
from search import semantic_search
from llm import summarize

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Sends a welcome message when the command /start is issued."""
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Hello! I'm your Customer Intelligence Bot. Ask me anything about customer feedback!"
    )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handles incoming text messages."""
    query = update.message.text
    print(f"Received message: {query}")
    
    if not query or len(query.split()) < 3:
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="Please ask a more descriptive question (at least 3 words)."
        )
        return

    # Notify user that processing is happening
    processing_msg = await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="SEARCHING AND ANALYZING..."
    )

    try:
        # Run synchronous blocking functions in a separate thread to avoid blocking the async loop
        loop = asyncio.get_running_loop()
        
        # 1. Retrieve context
        # semantic_search is synchronous, so we run it in an executor
        search_results = await loop.run_in_executor(None, semantic_search, query)
        
        # 2. Generate answer
        # summarize is synchronous, so we run it in an executor
        answer = await loop.run_in_executor(None, summarize, search_results, query)
        
        # 3. Send response
        await context.bot.delete_message(
            chat_id=update.effective_chat.id, 
            message_id=processing_msg.message_id
        )
        
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=answer
        )

    except Exception as e:
        logging.error(f"Error handling message: {e}")
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=f"Error: {str(e)}"
        )


async def ping(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Simple ping command to check if bot is responsive."""
    print("Received /ping command")
    await context.bot.send_message(chat_id=update.effective_chat.id, text="pong")

def main():
    """Starts the bot."""
    token = os.getenv("TELEGRAM_BOT_TOKEN")
    if not token:
        print("Error: TELEGRAM_BOT_TOKEN environment variable not set.")
        return

    application = ApplicationBuilder().token(token).build()
    
    start_handler = CommandHandler('start', start)
    ping_handler = CommandHandler('ping', ping)
    message_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), handle_message)
    
    application.add_handler(start_handler)
    application.add_handler(ping_handler)
    application.add_handler(message_handler)
    
    print("Bot is polling...")
    application.run_polling()

if __name__ == '__main__':
    main()
