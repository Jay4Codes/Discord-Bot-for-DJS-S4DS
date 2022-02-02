import discord
import math
import random
import string
import statistics
import os
import pyjokes
import wikipedia
import datetime
from replit import db
from active import keep_active

client = discord.Client()

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('~hello'):
      await message.channel.send('Hello')

  if message.content.startswith('~tell me a joke') or message.content.startswith('~joke'):
      await message.channel.send(pyjokes.get_joke())
  
  if message.content.startswith('~wiki'):
    try:
      search = message.content.replace('~wiki', '')
      await message.channel.send(wikipedia.summary(search, 4))
    except:
      await message.channel.send('No Wikipedia Page Found')

  if message.content.startswith('~time'):
        time = datetime.datetime.now().strftime('%I:%M %p')
        await message.channel.send('Its ' + time)


keep_active()
client.run(os.getenv('djs4ds'))