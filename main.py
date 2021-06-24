import os
from discord.ext import commands
from dotenv import load_dotenv

import cogs.greetings as greetings
import cogs.dice as dice
import cogs.events as events

load_dotenv()
TOKEN = os.environ["TOKEN"]

# prefixが1つのとき
bot = commands.Bot(command_prefix="!")
# prefixが2つ以上のとき
bot = commands.Bot(command_prefix=["!", "/"])

@bot.event
async def on_ready():
    print("------\nLogged in as", bot.user.name, "\n------")
    greetings.setup(bot)
    dice.setup(bot)
    events.setup(bot)

if __name__ == "__main__":
    bot.run(TOKEN)