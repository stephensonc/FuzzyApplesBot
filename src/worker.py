import discord
import asyncio
import random
import commands

client = discord.Client()


monitoredChannels = []


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    #print(client.user.id)
    game = discord.Game("with time")

    await client.change_presence(status = discord.Status.online, activity = game)
    print('------')


@client.event
async def on_message(message):
    global monitoredChannels
    content = message.content.lower()
    channel = message.channel

    if message.author == client.user:
        return;

    #Effectively King Crimson's power
    await crimsonCheck(message)

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
        elif 'erase' in content:
            monitoredChannels.append(channel)
            print("Monitoring " + channel.name)
            await commands.eraseTime(message)
        #Invalid message
        else:
            await channel.send('Invalid command. Type "!help" for a list of commands')
    return;

async def crimsonCheck(message):

    global monitoredChannels

    channel = message.channel

    monitored = isMonitored(channel)
    if 'disarm' in message.content.lower() and monitored == True:
        monitoredChannels.remove(channel)
        print("Disarmed "+ channel.name +" successfully")
    elif monitored == True:
        #print("Starting crimson check")
        await commands.eraseTime(message)
        await channel.send('I erased the time in which '+ message.author.mention +' sent their message and leapt past it.')
        #await channel.send('I erased the time in which '+ message.author.mention +' sent their message and leapt past it.',file=discord.File('./resources/ErasingTime.png'))
        await channel.send('...but if you must know, ' + message.author.name + ' said: \"' + message.content + '\"' )
        monitoredChannels.remove(channel)
        #printMonitored() #Debug, ensures it actually removed it.
        print("Ability successfuly used")
    return;

def isMonitored(channel):
    monitored = True if channel in monitoredChannels else False
    return monitored;

def printMonitored():
    for chnl in monitoredChannels:
        print(chnl.name + ", ")
    return;

client.run('NTkyODk4NDM0MzQwNzQ5MzEz.XRGYDg.77FbXwZPipf-Q2k_TEcUVz8IPx8')
