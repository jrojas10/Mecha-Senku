import os
import discord

my_secret = os.environ['token']


client = discord.Client()

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('$hello'):
    await message.channel.send('Hello!')

  if message.content.startswith('$commands'):
    await message.channel.send('View all commands here - https://github.com/jrojas10/Mecha-Senku\n ```$github - links to github\n$hello - replies with hello\n$commands- shows all commands```')

  if message.content.startswith('$github'):
    await message.channel.send('View the source code and commands\nhttps://github.com/jrojas10/Mecha-Senku')


client.run(my_secret)
