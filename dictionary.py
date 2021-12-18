import discord
from discord.ext import commands

intents = discord.Intents(messages=True)
Bot = commands.Bot(command_prefix="!",a=intents)


@Bot.event
async def on_ready():
    print("The Bronx")


@Bot.event
async def on_message(msg):
 with open("123.txt","r",encoding="utf-8") as a:
   for i in a:
            if msg.content.lower() in i.lower():
                await msg.author.send(i)
                break
                
Bot.run('OTIxNzY3MjQ2MTk4NjE2MTI0.Yb3spQ.HQGToTS-KPJrK8qubT64O0KhKAw')
