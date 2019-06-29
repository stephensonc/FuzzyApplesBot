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

    channel = message.channel

    if message.author == client.user:
        return;

    #Effectively King Crimson's power
    await crimsonCheck(message)

    #if the text should be parsed for a command
    if message.content.startswith("!"):
        #Help Command
        if message.content.lower().find("help") > -1:
            await commands.sendHelp(channel)
        #Angery face command
        elif message.content.lower().find("angerykc") > -1:
            await commands.sendKC(channel)
        #Hmm command
        elif message.content.lower().find("hmm") > -1:
            await commands.sendThunk(channel)
        #Erase time command
        elif message.content.lower().find("erase") > -1:
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
    if message.content.lower().find('disarm') >-1 and monitored == True:
        monitoredChannels.remove(channel)
        print("Disarmed "+ channel.name +" successfully")
    elif monitored == True:
        print("Starting crimson check")
        await commands.eraseTime(message)
        await channel.send('I erased the time in which '+ message.author.mention +' sent their message and leapt past it.')
        #await channel.send('I erased the time in which '+ message.author.mention +' sent their message and leapt past it.',file=discord.File('./resources/ErasingTime.png'))
        await channel.send('...but if you must know, ' + message.author.name + ' said \"' + message.content + '\"' )
        monitoredChannels.remove(channel)
        printMonitored()
        print("Ability successfuly used")
    return;

def isMonitored(channel):
    monitored = False
    for chnl in monitoredChannels:
        if(chnl == channel):
            monitored = True
    return monitored;

def printMonitored():
    for chnl in monitoredChannels:
        print(chnl.name)
    return;

client.run('NTkyODk4NDM0MzQwNzQ5MzEz.XRGYDg.77FbXwZPipf-Q2k_TEcUVz8IPx8')
