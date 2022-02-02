import discord
import pyjokes
import wikipedia


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

  if message.content.startswith('~tell me a joke'):
      await message.channel.send(pyjokes.get_joke())
  
  if message.content.startswith('~wiki'):
    try:
      search = message.content.replace('~wiki', '')
      await message.channel.send(wikipedia.summary(search, 4))
    except:
      await message.channel.send('No Wikipedia Page Found')

client.run('ODk2MTQwOTQxNjk2NTczNDYx.YWCySQ.vPUMmtde4-eVFDmIo9890zjTC7Y')