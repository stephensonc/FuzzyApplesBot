import discord
import asyncio
import random
import KingCrimsonBot
import os

client = discord.Client()
command_trigger = '!'
bot = KingCrimsonBot(client=client, resources_folder='./resources/', command_trigger=command_trigger, help_file=open("HelpMessage.txt", "r"))
command_dict = bot.get_commands()
if not discord.opus.is_loaded():
    discord.opus.load_opus('opus')

@client.event
async def on_ready():
    print("Logged in as")
    print(client.user.name)
    game = discord.Game("with time")
    await client.change_presence(status=discord.Status.online, activity=game)
    print("------")


@client.event
async def on_message(message):
    content = message.content.lower()
    channel = message.channel

    if message.author == client.user:
        return

    # King Crimson's power
    # await commands.erase_time(message)

    # if the text should be parsed for a command
    if content.startswith(command_trigger):
        command_found = False
        for key in command_dict.keys():
            if key in content:
                print(key + ' command received.')
                await bot.command_dict[key][0](message)
                command_found = True
        # Invalid message
        # if command_found is False:
        #     await channel.send(
        #         f'Invalid command. Type "{command_trigger}help" for a list of commands'
        #     )
    return


def print_monitored():
    for chnl in bot.monitored_channels:
        print(chnl.name + ", ")
    return


TOKEN = os.environ["TOKEN"]
client.run(TOKEN)
