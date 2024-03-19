import asyncio
from telethon.sync import TelegramClient

# Replace the values of the variables with your data
api_id = YOURS_API_ID
api_hash = 'YOURS_API_HASH'
phone_number = 'YOURS_PHONE_NUMBER'

# Create Telegram client object
client = TelegramClient('session_name', api_id, api_hash)

# Replace 'source_chat_id' with the ID of the chat room you want to redirect messages from
# Replace 'destination_chat_id' with the ID of the chat room you want to redirect messages to
source_chat_id = 'FROM_CHAT_ID'
destination_chat_id = 'TO_CHAT_ID'

last_message_id = None

async def forward_messages():
    global last_message_id
    async with TelegramClient('session_name', api_id, api_hash) as client:
        # Authorize in Telegram
        await client.start(phone=phone_number)

        async for message in client.iter_messages(int(source_chat_id), reverse=True):
            if last_message_id is None or message.id > last_message_id:
                await client.send_message(int(destination_chat_id), message)
                last_message_id = message.id

async def main():
    while True:
        await forward_messages()
        await asyncio.sleep(1)  # Pause, so as not to overload the server

# Run the asynchronous main() function
asyncio.run(main())