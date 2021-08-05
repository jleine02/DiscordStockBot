import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = "ODcyNTcyNzc3NTMyNjUzNjc5.YQr0uQ.0GcVfDcvVLuJn5Pat9XB4DtUi48"
#TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')


client.run(TOKEN)
