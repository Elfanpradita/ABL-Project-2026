from aiogram import Router
from aiogram.types import Message
from app.services.api_client import get_status

router = Router()

@router.message()
async def handle(message: Message):
    text = message.text

    if text == "/start":
        await message.answer(
            "🤖 Server Monitoring Bot\n\n"
            "Commands:\n"
            "/status\n/cpu\n/ram\n/disk\n/uptime\n/ping"
        )

    elif text == "/ping":
        await message.answer("🏓 Pong!")

    elif text in ["/status", "/cpu", "/ram", "/disk", "/uptime"]:
        data = await get_status()

        if text == "/status":
            msg = (
                f"🖥 Server Status\n"
                f"CPU: {data['cpu']}%\n"
                f"RAM: {data['ram']}%\n"
                f"Disk: {data['disk']}%\n"
            )

        elif text == "/cpu":
            msg = f"🔥 CPU Usage: {data['cpu']}%"

        elif text == "/ram":
            msg = f"💾 RAM Usage: {data['ram']}%"

        elif text == "/disk":
            msg = f"📀 Disk Usage: {data['disk']}%"

        elif text == "/uptime":
            msg = f"⏱ Uptime: {data['uptime']}"

        await message.answer(msg)