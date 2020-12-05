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

    # get difference between target date and current sl datetime and handle
    # for datetimes after the target date
    if target_date > current_sl_datetime:
        before_target_date = True
        time_remaining = target_date - current_sl_datetime
    else:
        before_target_date = False
        time_remaining = current_sl_datetime - target_date

    # get time components
    time_remaining_days = time_remaining.days
    time_remaining_total_seconds = time_remaining.seconds
    time_remaining_hours = time_remaining_total_seconds // 3600
    time_remaining_minutes = (time_remaining_total_seconds // 60) % 60

    if before_target_date == True:
        return f"We've got {time_remaining_days} day(s) {time_remaining_hours} hour(s) and {time_remaining_minutes} minute(s) until the epic showdown between Wasim and Lahiru!"
    else:
        return f"{time_remaining_days} day(s) {time_remaining_hours} hour(s) and {time_remaining_minutes} minute(s) have passed since the epic showdown between Wasim and Lahiru began. What a match!"

def help_user():
    """
    Help response for when the user types in an invalid command.
    """
    help_response = "There are only a few primary commands: \n`hypeman who`\n`hypeman watch`\n`hypeman when`\n`hypeman time`\n`hypeman why`\n`hypeman charitha`\n`hypeman odds`\n`hypeman odds for lahiru`\n`hypeman odds for wasim`\n`hypeman lol`\n`hypeman idea of wasim`\n`hypeman lahirus bike`"
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
        "charitha": "**CHARITHA THE MATCH ANNOUNCER SAYS**:\nFighting from the red corner ... hailing for the land of the maple leaves ... the only man to reject onella's advances ... **Wasim**!!!!\nand fighting from the blue corner .... hailing from Brussels , the country not the vegetable , the only man to peddle a bike downhill , ***** a pillow during a trip ... the former deputy head boy of some made up school ... **Lahiru**!!!",
        "odds": "According to Paul the Octopus (2008-2010) there is a 90 percent chance that either Lahiru or Wasim will win. There is a 10 percent chance that the boars will win.",
        "odds for lahiru": "According to Nostradamus (1503-1566), Lahiru's stars are aligned and his victory star in particular shines bright.",
        "odds for wasim": "According to the Oracle from the Matrix (2136-Unknown), there is no Wasim, there is only your idea of Wasim and my idea of Wasim and our idea of whether he'll win this match.",
        "lol": "This is no time for jokes. I'm a serious bot.",
        "idea of wasim": f"https://i.imgur.com/PzqiXuB.jpg",
        "lahirus bike": "Oh god, please don't break your hand before the game Lahiru.",
        "winner": "What an incredible match! INSERT_NAME_HERE played brilliantly and INSERT_NAME_HERE did a fantastic job as well. In the end INSERT_NAME_HERE was the better player! Fantastic stuff! Congratulations to INSERT_NAME_HERE and I bet INSERT_NAME_HERE wants a rematch!"
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