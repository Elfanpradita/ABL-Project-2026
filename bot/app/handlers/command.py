from aiogram import Router
from aiogram.types import Message
from bot.app.services.api_client import get_status

router = Router()

@router.message()
async def handle(message: Message):
    if message.text == "/status":
        data = await get_status()

        text = (
            f"🖥 Server Status\n"
            f"CPU: {data['cpu']}%\n"
            f"RAM: {data['ram']}%\n"
            f"Disk: {data['disk']}%\n"
        )

        await message.answer(text)