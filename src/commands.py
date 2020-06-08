import discord
import asyncio
import random
from os import listdir
import spotify_commands

file = open("HelpMessage.txt", "r")
client = discord.Client()
resources = "./resources/"
command_trigger = "!"
monitoredChannels = []


# Outputs the current list of commands
async def sendHelp(message):
    print("Sending help message")
    help_message = ""
    for key in command_dict.keys():
        help_message += command_trigger + key + " " + command_dict[key][1] + "\n"
    await message.channel.send(help_message)
    print("Sent successfully")
    return


# Current maximum number of jpgs and pngs in the resource folders for KC
crimsonimages = listdir(resources + "KingCrimson/")
num_png = len(crimsonimages) - 1


# Sends a random King Crimson image
async def sendKC(message):
    print("Sending angery King Crimson")
    rand = random.randint(0, num_png)
    file_to_send = "KingCrimson" + str(rand) + ".png"
    print("Sending " + file_to_send)
    await message.channel.send(
        file=discord.File(resources + "KingCrimson/" + file_to_send)
    )
    print("Sent successfully")
    return


# Number of thinking gifs
thunklist = listdir(resources + "hmm")
num_thunk = len(thunklist) - 1


# Sends a thinking gif
async def sendThunk(message):
    print("Sending thonking image")
    rand = random.randint(0, num_thunk)
    file_to_send = str(rand) + ".gif"
    print("Sending " + file_to_send)
    await message.channel.send(file=discord.File("./resources/hmm/" + file_to_send))
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
    "help": (sendHelp, "- Outputs a list of commands"),
    "angerykc": (sendKC, "- Responds with an angery King Crimson"),
    "thonking": (sendThunk, "- Responds with a random thinking image"),
    "kcplay": (spotify_commands.playSong, "- Joins voice channel and plays specified song"),
    "testspotify": (spotify_commands.testSpotifyIntegration, "- Attempts to connect to spotify")
    # "erase": (commands.primeAbility, "- Activates King Crimson's ability")
}
