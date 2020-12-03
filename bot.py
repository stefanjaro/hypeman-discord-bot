# bot.py
import os
from datetime import datetime, timedelta, timezone
import discord
from discord.ext import commands
from dotenv import load_dotenv

# load environment params
# load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

# set prefix
bot = commands.Bot(command_prefix='hype')

def time_until(target_date):
    """
    Calculates the number of days, hours and seconds to a particular date and time
    """
    # get current utc date and time
    current_utc_datetime = datetime.utcnow()

    # adjust to sri lankan time
    current_sl_datetime = current_utc_datetime + timedelta(hours=5, minutes=30)

    # get difference between target date and current sl datetime
    time_remaining = target_date - current_sl_datetime

    # get time components
    time_remaining_days = time_remaining.days
    time_remaining_total_seconds = time_remaining.seconds
    time_remaining_hours = time_remaining_total_seconds // 3600
    time_remaining_minutes = (time_remaining_total_seconds // 60) % 60

    return f"We've got {time_remaining_days} days {time_remaining_hours} hours and {time_remaining_minutes} minutes until the epic showdown between Wasim and Lahiru!"

def help_user():
    """
    Help response for when the user types in an invalid command.
    """
    help_response = "There are only 4 primary commands (for now): \n`hypeman who`\n`hypeman watch`\n`hypeman when`\n`hypeman time`"
    return help_response

@bot.event
async def on_ready():
    guild = discord.utils.get(bot.guilds, name=GUILD)

    print(
        f'{bot.user} has connected to Discord!\n'
        f'Guild Details: {guild.name} (id: {guild.id})'
    )

@bot.command(name='man')
async def hypeman_main(ctx, *args):
    # stich together user input
    user_input = " ".join(args).lower()

    # specify time of the event in sl time
    time_of_event = datetime(year=2020, month=12, day=6, hour=21, minute=30)

    # response repository
    response_repo = {
        "who": "It's Wasim vs Lahiru on Age of Empires II Definitive Edition!",
        "watch": "You can watch it live on discord! Just tune into Althaf's stream!",
        "when": "This Sunday Night! The 6th of December 2020.",
        "time": time_until(time_of_event),
        "why": "It's an Age of Empires kinda thing, you wouldn't get it.",
        "charitha": "**CHARITHA THE MATCH ANNOUNCER SAYS**:\nFighting from the red corner ... hailing for the land of the maple leaves ... the only man to reject onella's advances ... **Wasim**!!!!\nand fighting from the blue corner .... hailing from Brussels , the country not the vegetable , the only man to peddle a bike downhill , ***** a pillow during a trip ... the former deputy head boy of some made up school ... **Lahiru**!!!"
    }

    # get response and handle for wrong commands
    response = response_repo.get(user_input)

    if response == None:
        response = f"I don't recognize that command. {help_user()}"

    await ctx.send(response)

@bot.command(name='test')
async def test_bot(ctx):
    response = "Yes I've been connected and I'm working!"
    await ctx.send(response)

bot.run(TOKEN)