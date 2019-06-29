import discord
import asyncio
import random
from os import listdir

file = open("HelpMessage.txt", "r")
client = discord.Client()
resources = "./resources/"

#Outputs the current list of commands
async def sendHelp(channel):
    print("Command received")
    fileContents = file.read()
    await channel.send(fileContents)
    print("Sent successfully")
    return;

#Current maximum number of jpgs and pngs in the resource folders for KC
crimsonimages = listdir(resources + "KingCrimson/")
num_png = len(crimsonimages) - 1

#Sends a random King Crimson image
async def sendKC(channel):
    print("Command received")
    rand = random.randint(0, num_png)
    file_to_send = 'KingCrimson' + str(rand) + '.png'
    print("Sending " + file_to_send)
    await channel.send(file=discord.File(resources + 'KingCrimson/' + file_to_send))
    print("Sent successfully")
    return;

#Number of thinking gifs
thunklist = listdir(resources + "hmm")
num_thunk = len(thunklist) - 1
#Sends a thinking gif
async def sendThunk(channel):
    print("Command received")
    rand = random.randint(0, num_thunk)
    file_to_send = str(rand)+'.gif'
    print("Sending " + file_to_send)
    await channel.send(file=discord.File('./resources/hmm/'+ file_to_send))
    print("Sent successfully")
    return;

async def eraseTime(message):
    print("Erasing \"" + message.content+"\"")
    await message.delete()
    print("Erased successfully")
    return;
