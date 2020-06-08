import discord
import asyncio

client = discord.Client()
if not discord.opus.is_loaded():
    discord.opus.load_opus('opus')

async def playSong(message):
    user=message.author
    voice_channel=user.voice.channel
    if voice_channel!= None:
        # create StreamPlayer
        voice_client = await voice_channel.connect()
        # player = vc.create_ffmpeg_player('./resources/mp3s/HeheBoi.mp3', after=lambda: print('done'))
        try:
            audio_source = discord.FFmpegPCMAudio('./resources/mp3s/HeheBoi.mp3')
            voice_client.play(audio_source, after=await voice_client.disconnect())
        except:
                await voice_client.disconnect()
                await message.channel.send('Error playing audio file')
                raise
    else:
        await message.channel.send('User is not in a voice channel.')
