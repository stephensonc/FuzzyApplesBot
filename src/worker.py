import discord
import asyncio
import random
import commands
import os
client = discord.Client()

command_dict = {
            "help": (commands.sendHelp, "- Outputs a list of bot commands"),
            "angerykc": (commands.sendKC, "- Responds with an angery King Crimson"),
            "hmm": (commands.sendThunk, "- Responds with a random thinking gif"),
            #"erase": (commands.primeAbility, "- Activates King Crimson's ability")
}

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    game = discord.Game("with time")
    await client.change_presence(status = discord.Status.online, activity = game)
    print('------')

@client.event
async def on_message(message):
    content = message.content.lower()
    channel = message.channel

    if message.author == client.user:
        return;

    #Effectively King Crimson's power
    #await commands.eraseTime(message)

    #if the text should be parsed for a command
    if content.startswith("!"):
        print("Command received")
        command_found = False
        for key in command_dict.keys():
            if key in content:
                await command_dict[key](0)(channel)
                command_found = True
        #Invalid message
        if command_found is False:
            await channel.send('Invalid command. Type "!help" for a list of commands')
    return;

def printMonitored():
    for chnl in monitoredChannels:
        print(chnl.name + ", ")
    return;

TOKEN= os.environ["TOKEN"]
client.run(TOKEN)
