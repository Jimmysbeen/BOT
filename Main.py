import requests as request
import discord

client = discord.client

env:
  Token: ${{ secrets.Token }}

@client.event
async def on_ready():
  print("I'm online!".format(client))

