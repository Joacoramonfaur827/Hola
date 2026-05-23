import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'✅ {bot.user} está en línea!')

@bot.command()
async def hola(ctx):
    await ctx.send(f'¡Hola {ctx.author.mention}!')

@bot.command()
async def ping(ctx):
    await ctx.send(f'🏓 Pong! {round(bot.latency * 1000)}ms')

bot.run(os.getenv('TOKEN'))
