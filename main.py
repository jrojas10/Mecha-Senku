import os
import discord
import requests
import json

my_secret = os.environ['token']


client = discord.Client()

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] +  " -" + json_data[0]['a']
  return quote

def get_aniquote():
  response = requests.get("https://animechan.vercel.app/api/random")
  json_data = json.loads(response.text)
  quote = json_data['quote'] + " -" + json_data['character'] + " ("+json_data['anime'] +")"
  return quote


@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('$hello'):
    await message.channel.send('Hello!, my name is Mecha Senku')

  if message.content.startswith('$commands'):
    await message.channel.send('View all commands here - https://github.com/jrojas10/Mecha-Senku\n ```$github - links to github\n$hello - replies with hello\n$commands- shows all commands```')

  if message.content.startswith('$github'):
    await message.channel.send('View the source code and commands\nhttps://github.com/jrojas10/Mecha-Senku')

  if message.content.startswith('$inspire'):
    quote = get_quote()
    await message.channel.send(quote)

  if message.content.startswith('$aniquote'):
    quote = get_aniquote()
    await message.channel.send(quote)


  

client.run(my_secret)
