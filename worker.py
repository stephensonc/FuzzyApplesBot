import discord
import asyncio
import random


client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    channel = message.channel
    if message.author == client.user:
        return

    if message.content.startswith("!"):
        if message.content.lower() == "!angerykc":
            rand = random.randint(0, 1)
            file_to_send = 'KingCrimson' + str(rand) + '.jpg'
            await channel.send(file=discord.File('./resources/KingCrimson/' + file_to_send))

client.run('NTkyODk4NDM0MzQwNzQ5MzEz.XRGYDg.77FbXwZPipf-Q2k_TEcUVz8IPx8')
