import os
import sys
import discord
import asyncio
import json
import spotipy
import webbrowser
import spotipy.util as util
from spotipy.oauth2 import SpotifyClientCredentials
from json.decoder import JSONDecodeError

SPOTIFYUSERNAME = os.environ['SPOTIFYUSERNAME']
SPOTIFYCLIENTID = os.environ['SPOTIPY_CLIENT_ID']
SPOTIFYTOKEN = os.environ['SPOTIPY_CLIENT_SECRET']
SPOTIFYREDIRECTURI = os.environ['REDIRECTURI']
scope = 'user-read-private user-read-playback-state user-modify-playback-state'

client = discord.Client()

if not discord.opus.is_loaded():
    discord.opus.load_opus('opus')

async def playSong(message):
    user=message.author
    voice_channel=user.voice.channel
    if voice_channel!= None:
        # create StreamPlayer
        voice_client = await voice_channel.connect()
        try:
            audio_source = discord.FFmpegPCMAudio('./resources/mp3s/HeheBoi.mp3')
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
    else:
        await message.channel.send('User is not in a voice channel.')

async def testSpotifyIntegration(message):

    client_credentials_manager = SpotifyClientCredentials()
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
    playlists = sp.user_playlists(SPOTIFYUSERNAME)
    playlistnames = ''
    for list in playlists['items']:
        playlistnames += list['name'] + '\n'
    await message.channel.send(playlistnames)

async def getSongsFromPlaylist(message):
    tosearch = message.content.lower()[15:]
    print(tosearch)
    client_credentials_manager = SpotifyClientCredentials()
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
    playlists = sp.user_playlists(SPOTIFYUSERNAME)
    song_list = ''
    for list in playlists['items']:
        if tosearch in list['name'].lower():
            if tosearch in list['name'].lower():
                tracks = sp.playlist_tracks(playlist_id=list['id'], fields='items.track.name,items.track.artists')
                for track in tracks['items']:
                    track = track['track']
                    print(type(track['artists']))
                    song_list += str(track['name']) +' - ' + str(track['artists'][0]['name']) + '\n'
    if song_list is not '':
        await message.channel.send(song_list)
        return song_list
    else:
        await message.channel.send("Playlist not found")
