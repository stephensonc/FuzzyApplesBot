import discord
import asyncio
import random
import commands

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
        return;

    if message.content.startswith("!"):#if the text should be parsed for a command
        #Help Command
        if message.content.lower() == "!help":
            await commands.sendHelp(channel)

        #King Crimson command
        elif message.content.lower() == "!angerykc":
            await commands.sendKC(channel)

        elif message.content.lower().find("hmm") > -1:
            await commands.sendThunk(channel)

        else:
            await channel.send('Invalid command. Type "!help" for a list of commands')

client.run('NTkyODk4NDM0MzQwNzQ5MzEz.XRGYDg.77FbXwZPipf-Q2k_TEcUVz8IPx8')
