import discord
import asyncio
import random
from os import listdir
import spotify_commands

file = open("HelpMessage.txt", "r")
client = discord.Client()
resources = "./resources/"
command_trigger = "!"
monitored_channels = []


# Outputs the current list of commands
async def send_help(message):
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
async def send_KC(message):
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
async def send_thunk(message):
    print("Sending thonking image")
    rand = random.randint(0, num_thunk)
    file_to_send = str(rand) + ".gif"
    print("Sending " + file_to_send)
    await message.channel.send(file=discord.File("./resources/hmm/" + file_to_send))
    print("Sent successfully")
    return


async def erase_time(message):
    global monitored_channels
    channel = message.channel
    monitored = True if channel in monitored_channels else False

    if "disarm" in message.content.lower() and monitored is True:
        monitored_channels.remove(channel)
        print("Disarmed " + channel.name + " successfully")
    elif monitored is True:
        await delete_message(message)
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
        monitored_channels.remove(channel)
        print("Ability successfully used")
    return


async def delete_message(message):
    print('Erasing "' + message.content + '"')
    await message.delete()
    print("Erased successfully")
    return


def prime_ability(message):
    monitor_channel(message.channel)
    delete_message(message)
    return


def monitor_channel(channel):
    monitored_channels.append(channel)
    print("Monitoring " + channel.name)
    return

# Dictionary of all commands
command_dict = {
    "help": (send_help, "- Outputs a list of commands"),
    "angerykc": (send_KC, "- Responds with an angery King Crimson"),
    "thonking": (send_thunk, "- Responds with a random thinking image"),
    "kcplay": (spotify_commands.play_song, "- Joins voice channel and plays specified song"),
    "kcplaylist": (spotify_commands.play_list, "- Joins voice channel and plays a list of songs"),
    "testspotify": (spotify_commands.print_user_playlist_names, "- Attempts to connect to spotify"),
    "summon": (spotify_commands.summon, "- Attempts to join the user's voice channel"),
    "banish": (spotify_commands.banish, "- Leaves a voice channel, if it is in one")
    # "erase": (commands.prime_ability, "- Activates King Crimson's ability")
}
