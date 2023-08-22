import requests as request
import discord
import os

client = discord.client

#hide
Token = os.environ['TOKEN']

@client.event
async def on_ready():
  print("I'm online!".format(client))

client.run(Token)
