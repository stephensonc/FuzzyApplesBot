import discord
import asyncio
import random

file = open("HelpMessage.txt", "r")
client = discord.Client()

#Outputs the current list of commands
async def sendHelp(channel):
    print("Command received")
    fileContents = file.read()
    await channel.send(fileContents)
    print("Sent successfully")
    return;

#Current maximum number of jpgs and pngs in the resource folders for KC
num_jpg = 4
num_png = 5

#Sends a random King Crimson image
async def sendKC(channel):
    print("Command received")
    rand = random.randint(0,1)
    if rand == 0:
        rand = random.randint(0, num_jpg)
        file_to_send = 'KingCrimson' + str(rand) + '.jpg'
        print("Sending " + file_to_send)
        await channel.send(file=discord.File('./resources/KingCrimson/' + file_to_send))
        print("Sent successfully")
    elif rand == 1:
        rand = random.randint(0, num_png)
        file_to_send = 'KingCrimson' + str(rand) + '.png'
        print("Sending " + file_to_send)
        await channel.send(file=discord.File('./resources/KingCrimsonPNG/' + file_to_send))
        print("Sent successfully")
    return;

#Number of thinking gifs
num_thunk = 8
#Sends a thinking gif
async def sendThunk(channel):
    print("Command received")
    rand = random.randint(0, num_thunk)
    file_to_send = str(rand)+'.gif'
    print("Sending " + file_to_send)
    await channel.send(file=discord.File('./resources/hmm/'+ file_to_send))
    print("Sent successfully")
    return;


async def eraseTime(command, channel):
    print("Erasing command comment")
    await command.delete()
    print("Erased successfully")
    @client.event
    async def on_message(message1):
        print("Erasing next message")
        if message1.author == client.user:
            return;
        await message1.delete()
        await channel.send(file=discord.File('./resources/EraseTime.png'))
    return;
