import asyncio
import random
import os
from os import listdir
import sys
import spotipy
import discord
from spotipy.oauth2 import SpotifyClientCredentials

class KingCrimsonBot:
    def __init__(self, client, resources_folder='./resources/', command_trigger='!', help_file=open("HelpMessage.txt", "r")):
        self.client = client
        self.help_file = help_file
        self.resources_folder = resources_folder
        self.command_trigger = command_trigger
        self.monitored_channels = []
        self.voice_client = None
        self.SPOTIFYUSERNAME = os.environ['SPOTIFYUSERNAME']
        self.spotipy_obj = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
        self.command_dict = { #Dictionary of all commands
            "help": (self.send_help, "- Outputs a list of commands"),
            "angerykc": (self.send_KC, "- Responds with an angery King Crimson"),
            "thonking": (self.send_thunk, "- Responds with a random thinking image"),
            "kcplay": (self.play_song, "- Joins voice channel and plays specified song"),
            "kcplaylist": (self.play_list, "- Joins voice channel and plays a list of songs"),
            "testspotify": (self.print_user_playlist_names, "- Attempts to connect to spotify"),
            "summonkc": (self.summon, "- Attempts to join the user's voice channel"),
            "banishkc": (self.banish, "- Leaves a voice channel, if it is in one")
            # "erase": (commands.prime_ability, "- Activates King Crimson's ability")
        }

    # Outputs the current list of commands
    async def send_help(self, message):
        print("Sending help message")
        help_message = ""
        for key in self.command_dict.keys():
            help_message += self.command_trigger + key + " " + self.command_dict[key][1] + "\n"
        await message.channel.send(help_message)
        print("Sent successfully")
        return

    # Current maximum number of jpgs and pngs in a resource folder
    def num_images_in_folder(self, foldername):
        return len(listdir(self.resources_folder + foldername)) - 1

    # Sends a random King Crimson image
    async def send_KC(self, message):
        print("Sending angery King Crimson")
        rand = random.randint(0, self.num_images_in_folder('KingCrimson/'))
        file_to_send = "KingCrimson" + str(rand) + ".png"
        print("Sending " + file_to_send)
        await message.channel.send(
            file=discord.File(self.resources_folder + "KingCrimson/" + file_to_send)
        )
        print("Sent successfully")
        return

    # Sends a thinking gif
    async def send_thunk(self, message):
        print("Sending thonking image")
        rand = random.randint(0, self.num_images_in_folder('hmm/'))
        file_to_send = str(rand) + ".gif"
        print("Sending " + file_to_send)
        await message.channel.send(file=discord.File(self.resources_folder + "hmm/" + file_to_send))
        print("Sent successfully")
        return

    async def erase_time(self, message):
        channel = message.channel
        monitored = True if channel in self.monitored_channels else False
        if "disarm" in message.content.lower() and monitored is True:
            self.monitored_channels.remove(channel)
            print("Disarmed " + channel.name + " successfully")
        elif monitored is True:
            await self.delete_message(message)
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
            self.monitored_channels.remove(channel)
            print("Ability successfully used")
        return

    async def delete_message(self, message):
        print('Erasing "' + message.content + '"')
        await message.delete()
        print("Erased successfully")
        return

    def prime_ability(self, message):
        self.monitor_channel(message.channel)
        self.delete_message(message)
        return

    def monitor_channel(self, channel):
        self.monitored_channels.append(channel)
        print("Monitoring " + channel.name)
        return

    async def summon(self, message):
        voice_channel = message.author.voice.channel
        if voice_channel is not None:
            self.voice_client = await voice_channel.connect()
        else:
            await message.channel.send('User is not in a voice channel.')
            return False

    async def banish(self, message):
        if self.voice_client is not None:
            await self.voice_client.disconnect()
            self.voice_client = None
            return True
        else:
            await message.channel.send('User is not in a voice channel.')
            return False

    async def play_song(self, message):
        if await self.summon(message): # Connected to voice channel properly
            try:
                audio_source = discord.FFmpegPCMAudio(source='./resources/mp3s/HeheBoi.mp3', pipe=True)
                self.voice_client.play(audio_source, after=lambda x: print('Played audio.'))
                playing_for = 0
                while(self.voice_client.is_playing()):
                    playing_for += 1
                    # wait until end of audio
                await self.banish(message)
            except:
                    print('Error playing audio file')
                    await self.banish(message)
                    await message.channel.send('Error playing audio file')
                    raise

    async def play_list(self, message):
        playlist = self.get_songs_from_playlist(message.content[12:])
        for song in playlist:
            await self.play_song(message, song)

    async def print_user_playlist_names(self, message):
        playlists = self.spotipy_obj.user_playlists(self.SPOTIFYUSERNAME)
        playlistnames = ''
        for list in playlists['items']:
            playlistnames += list['name'] + '\n'
        await message.channel.send(playlistnames)

    def get_songs_from_playlist(self, to_search):
        """Return a list of songs and their artists from a Spotify Playlist."""
        print(tosearch)
        playlists = self.spotipy_obj.user_playlists(self.SPOTIFYUSERNAME)
        song_list = []
        for list in playlists['items']:
            if tosearch in list['name'].lower():
                if tosearch in list['name'].lower():
                    tracks = self.spotipy_obj.playlist_tracks(playlist_id=list['id'], fields='items.track.name,items.track.artists')
                    for track in tracks['items']:
                        track = track['track']
                        song_list.append(str(track['name']) + ' - ' + str(track['artists'][0]['name']))
        if song_list:
            print(song_list)
            return song_list
        else:
            return None

    def get_commands(self):
        return self.command_dict
