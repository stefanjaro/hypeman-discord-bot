# bot.py
import os
import random
import math
import discord
from discord.ext import commands
from dotenv import load_dotenv

# load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

# set prefix
bot = commands.Bot(command_prefix='hypeman')

@bot.event
async def on_ready():
    guild = discord.utils.get(bot.guilds, name=GUILD)

    print(
        f'{bot.user} has connected to Discord!\n'
        f'Guild Details: {guild.name} (id: {guild.id})'
    )

@bot.command(name="test", help='See if the bot\'s been connected and is working')
async def movie_details_with_name(ctx, *args): 
    test_response = 'Yes I\'ve been connected and I\'m working!'
    await ctx.send(test_response)

bot.run(TOKEN)