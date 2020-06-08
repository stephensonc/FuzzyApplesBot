import os
import sys
import discord
import asyncio
import json
import spotipy
import webbrowser
import spotipy.util as util
from json.decoder import JSONDecodeError
SPOTIFYUSERNAME = os.environ['SPOTIFYUSERNAME']
SPOTIFYCLIENTID = os.environ['CLIENTID']
SPOTIFYTOKEN = os.environ['SPOTIFYTOKEN']
SPOTIFYREDIRECTURI = os.environ['REDIRECTURI']
scope = 'user-read-private user-read-playback-state user-modify-playback-state'
# util.prompt_for_user_token(SPOTIFYUSERNAME,
#                            scope,
#                            client_id=SPOTIFYCLIENTID,
#                            client_secret=SPOTIFYTOKEN,
#                            redirect_uri=SPOTIFYREDIRECTURI)

spotifyObject = spotipy.Spotify(auth=SPOTIFYTOKEN)
devices = spotifyObject.devices()
print(json.dumps(devices, sort_keys=True, indent=4))
deviceID = devices['devices'][0]['id']

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

async def disconnect_from_voice(voice_client):
    await voice_client.disconnect()
