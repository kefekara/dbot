import discord
from discord.ext import commands
import random
import os

# Erstelle den Bot-Client mit den erforderlichen Intents
intents = discord.Intents.default()
intents.messages = True  # Ermögliche den Zugriff auf Nachrichten-Events

bot = commands.Bot(command_prefix='!', intents=intents)
memes = [
    "images\8enx7z.jpg",
    "images\Screenshot 2024-02-09 191921.png",
    "images\8enxhi.jpg"
    "images\Screenshot 2024-02-09 192408.png"
    "images\Screenshot 2024-02-09 192930.png"
]

@bot.command()
async def memrandom(ctx):
    img_name = random.choice(os.listdir('images'))
    print (img_name)
    with open(f'images/{img_name}', 'rb') as f:
        picture = discord.File(f)
    
    await ctx.send(file=picture)
    
# Event, das beim Start des Bots aufgerufen wird
@bot.event
async def on_ready():
    print('Bot ist bereit!')

# Token des Bots
TOKEN = 'MTE5NTQyMDQxMzUwMTY0ODk2OA.G8zYeb.8CVb6WZST8gzmXba4BNxh5L8iN53cU9LVrDDS0'

# Den Bot starten
bot.run("MTE5NTQyMDQxMzUwMTY0ODk2OA.G8zYeb.8CVb6WZST8gzmXba4BNxh5L8iN53cU9LVrDDS0")