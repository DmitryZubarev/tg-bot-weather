from aiogram.types import Message
from aiogram.filters import CommandStart
from aiogram import Router

router = Router()

# ---------------------- Command handlers ----------------------

@router.message(CommandStart())
async def process_start_command(message: Message):
  await message.answer(text="Здарова, брат! Введи город, а я выдам базу...")
