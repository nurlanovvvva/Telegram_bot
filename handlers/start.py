from aiogram import Router, types
from aiogram.filters import Command

from config import bot
router = Router()

@router.message(Command('start'))
async def start_menu(message: types.Message, db=AsyncDatabes()):
    print(message)
    await db.execute_query(
        query=sql_queries.INSERT_USER_QUERY, params=(
            None, message.from_user.id, message.from_user.username, message.from_user.first_name,
            message.from_user.last_name
        ),
        fetch=' none'
    )
    await bot.send_message(
        chat_id=message.chat.id,
        text=f"Hello {message.from_user.first_name}!",
    )

