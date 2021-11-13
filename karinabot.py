import discord
from discord.ext import commands
Bot=commands.Bot("k ")
@Bot.event
async def on_ready():
   print("connected")
@Bot.command()
async def start(ctx):
  await ctx.send("""
:full_moon_with_face: Bot işləyir.Bu Bot Karina Kərimova üçün hazırlanıb.Başlamaq üçün bu açar sözünün yaz:k basla
""")
