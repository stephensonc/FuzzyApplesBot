import os
import sys
import discord
import asyncio
import json
import spotipy
import webbrowser
import spotipy.util as util
from spotipy.oauth2 import SpotifyClientCredentials

SPOTIFYUSERNAME = os.environ['SPOTIFYUSERNAME']
client = discord.Client()

if not discord.opus.is_loaded():
    discord.opus.load_opus('opus')

async def summon(message):
    voice_channel = message.author.voice.channel
    if voice_channel is not None:
        voice_client = await voice_channel.connect()
    else:
        await message.channel.send('User is not in a voice channel.')
        return False

async def banish(message):
    voice_channel = message.author.voice.channel
    if voice_channel is not None:
        voice_client = await voice_channel.connect()
    else:
        await message.channel.send('User is not in a voice channel.')
        return False

async def play_song(message):
    if await summon(message): # Connected to voice channel properly
        try:
            audio_source = discord.FFmpegPCMAudio('https://www.youtube.com/watch?v=W4YW1bk04-U')
            voice_client.play(audio_source, after=lambda x: print('Played audio.'))
            playing_for = 0
            while(voice_client.is_playing()):
                playing_for += 1
                # wait until end of audio
            await voice_client.disconnect()
        except:
                print('Error playing audio file')
                await voice_client.disconnect()
                await message.channel.send('Error playing audio file')
                raise

async def print_user_playlist_names(message):
    client_credentials_manager = SpotifyClientCredentials()
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
    playlists = sp.user_playlists(SPOTIFYUSERNAME)
    playlistnames = ''
    for list in playlists['items']:
        playlistnames += list['name'] + '\n'
    await message.channel.send(playlistnames)

async def get_songs_from_playlist(to_search):
    """Return a list of songs and their artists from a Spotify Playlist."""
    print(tosearch)
    client_credentials_manager = SpotifyClientCredentials()
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
    playlists = sp.user_playlists(SPOTIFYUSERNAME)
    song_list = []
    for list in playlists['items']:
        if tosearch in list['name'].lower():
            if tosearch in list['name'].lower():
                tracks = sp.playlist_tracks(playlist_id=list['id'], fields='items.track.name,items.track.artists')
                for track in tracks['items']:
                    track = track['track']
                    song_list.append(str(track['name']) + ' - ' + str(track['artists'][0]['name']))
    if song_list:
        print(song_list)
        return song_list
    else:
        return None
