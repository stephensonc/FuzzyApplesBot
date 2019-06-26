import discord
import asyncio
import random

file = open("HelpMessage.txt", "r")

#Outputs the current list of commands
async def sendHelp(channel):
    fileContents = file.read()
    await channel.send(fileContents)
    return;

#Current maximum number of jpgs and pngs in the resource folders for KC
num_jpg = 4
num_png = 5

#Sends a random King Crimson image
async def sendKC(channel):
    rand = random.randint(0,1)
    if rand == 0:
        rand = random.randint(0, num_jpg)
        file_to_send = 'KingCrimson' + str(rand) + '.jpg'
        await channel.send(file=discord.File('./resources/KingCrimson/' + file_to_send))
    elif rand == 1:
        rand = random.randint(0, num_png)
        file_to_send = 'KingCrimson' + str(rand) + '.png'
        await channel.send(file=discord.File('./resources/KingCrimsonPNG/' + file_to_send))
    return;

#Number of thinking gifs
num_thunk = 8
#Sends a thinking gif
async def sendThunk(channel):
    rand = random.randint(0, num_thunk)
    await channel.send(file=discord.File('./resources/hmm/'+str(rand)+'.gif' ))
    return;
