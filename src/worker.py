import discord
import asyncio
import random
import commands
import os

client = discord.Client()

command_dict = commands.command_dict
command_trigger = "."


@client.event
async def on_ready():
    print("Logged in as")
    print(client.user.name)
    game = discord.Game("with time")
    await client.change_presence(status=discord.Status.online, activity=game)
    print("------")


@client.event
async def on_message(message):
    content = message.content.lower()
    channel = message.channel

    if message.author == client.user:
        return

    # King Crimson's power
    # await commands.eraseTime(message)

    # if the text should be parsed for a command
    if content.startswith(command_trigger):
        print("Command received")
        command_found = False
        for key in command_dict.keys():
            if key in content:
                await commands.command_dict[key][0](channel)
                command_found = True
        # Invalid message
        if command_found is False:
            await channel.send(
                f'Invalid command. Type "{command_trigger}help" for a list of commands'
            )
    return


def printMonitored():
    for chnl in commands.monitoredChannels:
        print(chnl.name + ", ")
    return


TOKEN = os.environ["TOKEN"]
client.run(TOKEN)
