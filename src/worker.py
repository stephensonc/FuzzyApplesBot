import discord
import asyncio
import random
import commands

client = discord.Client()

standAbilityActivated = False
channelToParse = 'Not defined'


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
    global standAbilityActivated
    global channelToParse
    channel = message.channel

    if message.author == client.user:
        return;

    #Effectively King Crimson's power
    if message.content.lower().find('disarm') >-1:
        print("Disarming stand")
        standAbilityActivated = False

    if standAbilityActivated and channelToParse == channel:
        await commands.eraseTime(message)
        standAbilityActivated = False
        await channel.send('I erased the time in which '+ message.author.mention +' sent their message and leapt past it.')
        #await channel.send('I erased the time in which '+ message.author.mention +' sent their message and leapt past it.',file=discord.File('./resources/ErasingTime.png'))
        await channel.send('...but if you must know, ' + message.author.name + 'said \"' + message.content + '\"' )
        print("Ability successfuly used")
    elif message.content.lower().find('disarm') >-1 and channelToParse == channel:
        print("Disarmed successfully")
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
            channelToParse = channel
            print("Monitoring " + channel.name)
            await commands.eraseTime(message)
            standAbilityActivated = True

        #Invalid message
        else:
            await channel.send('Invalid command. Type "!help" for a list of commands')
    return;



client.run('NTkyODk4NDM0MzQwNzQ5MzEz.XRGYDg.77FbXwZPipf-Q2k_TEcUVz8IPx8')
