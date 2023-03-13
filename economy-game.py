import os
import asyncio
import discord
from discord.ext import commands

intents = discord.Intents(guilds=True, messages=True)
bot = commands.Bot(command_prefix='econ.', intents=intents)

# a confirmation for the console that the bot has successfully signed in
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

# a simple hello command to test if the bot is working correctly.
@bot.command
async def hello():
    print(f'Hello')
    await ctx.send('Hello!')

# Code for the game begins here.



# starts the bot
bot.run('bot_token')