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
        vc = await voice_channel.connect()
        # player = vc.create_ffmpeg_player('./resources/mp3s/HeheBoi.mp3', after=lambda: print('done'))
        try:
            audio_source = discord.FFmpegPCMAudio('./resources/mp3s/HeheBoi.mp3')
            vc.play(audio_source)
        except:
                await vc.disconnect()
                await message.channel.send('Error playing audio file')
                raise
        finally:
            await vc.disconnect()
    else:
        await message.channel.send('User is not in a voice channel.')
