import telebot
from telethon import TelegramClient
from private_constants import API_ID, API_HASH, TOKEN, PHONE_NUMBER
import asyncio


async def get_user_id_by_username(username):
    async def get_id(username):
        client = TelegramClient('session_name', API_ID, API_HASH)
        await client.start(phone=PHONE_NUMBER)
        try:
            user = await client.get_entity(username)
            return user.id
        except Exception as e:
            print(f"Не вдалося отримати ID для користувача {username}: {e}")
            return None
        finally:
            await client.disconnect()

    user_id = await get_id(username)
    return user_id


def send_message_to_username(username, message):
    bot = telebot.TeleBot(TOKEN)
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    user_id = loop.run_until_complete(get_user_id_by_username(username))
    if user_id:
        bot.send_message(user_id, message)
        return user_id
