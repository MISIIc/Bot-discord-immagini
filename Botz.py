import discord
import os
import random
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Hai fatto l\'accesso come {bot.user}')

@bot.command()
async def ciao(ctx):
    await ctx.send(f'Ciao! Sono un bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def nuovaPassword(ctx, lunghezza_password = 10):
    await ctx.send(gen_pass(lunghezza_password))

def gen_pass(lunghezza_password):
    elements = "+-/*!&$#?=@<>abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    password = ""

    for i in range(lunghezza_password):
        password += random.choice(elements)

    return password

@bot.command()
async def mem(ctx):
    with open('adoug.png', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

@bot.command()
async def animal(ctx):   
    img_name = random.choice(os.listdir('.'))
    with open(f'{img_name}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)


bot.run('token')