import discord
import os
import json
import logging
import asyncio
import random
import aiofiles
from discord.ext import commands


@client.event
async def on_ready():
  print("bot is ready")



#this is my token
TOKEN = ("token here")


# saying that client = an bot
client = commands.Bot(command_prefix='prefix here')

# sayinig that the bot is online
@client.event
async def on_ready():
	print('BOT Is ready to work!')





#keep this at end of code
client.run(TOKEN)