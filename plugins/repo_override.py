from pyrogram import filters
from pyrogram.types import Message
from StrangerMusic import app  # agar app ka naam alag ho to bata

@app.on_message(filters.command("repo"))
async def repo_override(_, message: Message):
    await message.reply_text(
        "🚫 Repo command disabled.\n\n"
        "This bot is private.\n"
        "No public repository available."
    )
