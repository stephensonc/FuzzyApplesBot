import discord
import asyncio
import random
import commands

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

num_jpg = 4
num_png = 5

@client.event
async def on_message(message):
    channel = message.channel
    if message.author == client.user:
        return;

    if message.content.startswith("!"):#if the text should be parsed for a command

        #Help Command
        if message.content.lower() == "!help":
            commands.sendHelp(channel)
            await channel.send('Command list: \n------------------\n'
             + '!AngeryKC - Responds with an angery King Crimson')

            #King Crimson command
        elif message.content.lower() == "!angerykc":
            rand = random.randint(0,1)
            if rand == 0:
                rand = random.randint(0, num_jpg)
                file_to_send = 'KingCrimson' + str(rand) + '.jpg'
                await channel.send(file=discord.File('./resources/KingCrimson/' + file_to_send))
            elif rand == 1:
                rand = random.randint(0, num_png)
                file_to_send = 'KingCrimson' + str(rand) + '.png'
                await channel.send(file=discord.File('./resources/KingCrimsonPNG/' + file_to_send))
                #End of King Crimson Command

        else:
            await channel.send('Invalid command. Type "!help" for a list of commands')



client.run('NTkyODk4NDM0MzQwNzQ5MzEz.XRGYDg.77FbXwZPipf-Q2k_TEcUVz8IPx8')
