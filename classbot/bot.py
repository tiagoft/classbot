import router
import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
import random

# Load environment variables from .env file


def get_discord_token():
    load_dotenv()
    discord_token = os.getenv('DISCORD_TOKEN')
    return discord_token

def get_discord_bot(discord_token):
    description = "I am a chatbot!"
    intents = discord.Intents.default()
    intents.members = True
    intents.message_content = True

    bot = commands.Bot(command_prefix='?', description=description, intents=intents)
    return bot

def register_on_ready(bot):
    @bot.event
    async def on_ready():
        print(f'Logged in as {bot.user} (ID: {bot.user.id})')
        print('------')
        channel = bot.get_channel(1266426977976324219)
        await channel.send(f'Testing. My random number is: {random.random()}')
        print("Online!")
    return on_ready

def main():
    discord_token = get_discord_token()
    bot = get_discord_bot(discord_token)
    register_on_ready(bot)
    print("Getting ready to run the bot...")
    bot.run(discord_token)
    
if __name__ == "__main__":
    main()
    