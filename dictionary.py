import discord
from discord.ext import commands

intents = discord.Intents(messages=True)
Bot = commands.Bot(command_prefix="!",a=intents)


@Bot.event
async def on_ready():
    print("The Bronx")


@Bot.event
async def on_message(msg):
    with open("Botun lügət sözləri.txt", "r",encoding="utf-8") as a:
        for i in a:
            if msg.content.lower() in i.lower():
                await msg.author.send(i)
                break


Bot.run('OTE5MzM0MzQ2NTEzNTg0MTc5.YbUS1A.1P1VwBt7AXU9mscXkXFxaefFxvg')
