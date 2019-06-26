import discord
import asyncio
import random

async def sendHelp(channel):
    await channel.send('Command list: \n------------------\n'
     + '!AngeryKC - Responds with an angery King Crimson')
    return;

num_jpg = 4
num_png = 5

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
