import discord
import asyncio
import random
from os import listdir

file = open("HelpMessage.txt", "r")
client = discord.Client()
resources = "./resources/"
monitoredChannels = []


# Outputs the current list of commands
async def sendHelp(channel):
    print("Sending help message")
    help_message = ""
    for key in command_dict.keys():
        help_message += "!" + key + " " + command_dict[key][1] + "\n"
    await channel.send(help_message)
    print("Sent successfully")
    return


# Current maximum number of jpgs and pngs in the resource folders for KC
crimsonimages = listdir(resources + "KingCrimson/")
num_png = len(crimsonimages) - 1


# Sends a random King Crimson image
async def sendKC(channel):
    print("Sending angery King Crimson")
    rand = random.randint(0, num_png)
    file_to_send = "KingCrimson" + str(rand) + ".png"
    print("Sending " + file_to_send)
    await channel.send(
        file=discord.File(resources + "KingCrimson/" + file_to_send)
    )
    print("Sent successfully")
    return


# Number of thinking gifs
thunklist = listdir(resources + "hmm")
num_thunk = len(thunklist) - 1


# Sends a thinking gif
async def sendThunk(channel):
    print("Sending thonking image")
    rand = random.randint(0, num_thunk)
    file_to_send = str(rand) + ".gif"
    print("Sending " + file_to_send)
    await channel.send(file=discord.File("./resources/hmm/" + file_to_send))
    print("Sent successfully")
    return


async def eraseTime(message):
    global monitoredChannels
    channel = message.channel
    monitored = True if channel in monitoredChannels else False

    if "disarm" in message.content.lower() and monitored is True:
        monitoredChannels.remove(channel)
        print("Disarmed " + channel.name + " successfully")
    elif monitored is True:
        await deleteMessage(message)
        await channel.send(
            "I erased the time in which "
            + message.author.mention
            + " sent their message and leapt past it."
        )
        # await channel.send(
        #     "...but if you must know, "
        #     + message.author.name
        #     + ' said: "'
        #     + message.content
        #     + '"'
        # )
        monitoredChannels.remove(channel)
        print("Ability successfuly used")
    return


async def deleteMessage(message):
    print('Erasing "' + message.content + '"')
    await message.delete()
    print("Erased successfully")
    return


def primeAbility(message):
    monitorChannel(message.channel)
    deleteMessage(message)
    return


def monitorChannel(channel):
    monitoredChannels.append(channel)
    print("Monitoring " + channel.name)
    return


# Dictionary of all commands
command_dict = {
    "helpvibes": (sendHelp, "- Outputs a list of vibe commands"),
    "checkvibe": (sendKC, "- Responds with an angery vibe check"),
    "thonkvibes": (sendThunk, "- Responds with a random thinking vibe"),
    # "erase": (commands.primeAbility, "- Activates King Crimson's ability")
}
