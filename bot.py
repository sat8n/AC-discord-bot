import os

import discord
from dotenv import load_dotenv

from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.command(name='test')
async def test(ctx):
    await ctx.send("Test successful.")

from getAnimal import getSpecies, getType

@bot.command(name='animal', help='Taking an animal\'s name as input, the bot will return the animal\'s characteristics')
async def get_type(ctx, animal_name):
    animal_name = animal_name.lower()

    animal_species = getSpecies(animal_name)
    animal_type = getType(animal_name)

    url = "https://nookipedia.com/wiki/" + animal_name
    sentence = animal_name.title() + "'s species is " + animal_species + ", with a " + animal_type + " personality. " + url
    await ctx.send(sentence)

bot.run(TOKEN)