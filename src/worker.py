import discord
import asyncio
import random
import commands
client = discord.Client()


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
        #Help Command
        if 'help' in content:
            await commands.sendHelp(channel)
        #Angery face command
        elif 'angerykc' in content:
            await commands.sendKC(channel)
        #Hmm command
        elif 'hmm' in content:
            await commands.sendThunk(channel)
        #Erase time command
        # elif 'erase' in content:
        #     commands.monitorChannel(channel)
        #     await commands.deleteMessage(message)
        #Invalid message
        else:
            await channel.send('Invalid command. Type "!help" for a list of commands')
    return;

def printMonitored():
    for chnl in monitoredChannels:
        print(chnl.name + ", ")
    return;

print("Sending client.run() command")
client.run("NTkyODk4NDM0MzQwNzQ5MzEz.Xg1J3Q.p_bGhi38xy7Ad7cXA2qw1ON3e6w")
