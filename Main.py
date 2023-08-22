import requests as request
import discord

client = discord.client


@client.event
async def on_ready():
  print("I'm online!".format(client))

client.run(Token)
