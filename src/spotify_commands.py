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
        player = discord.FFmpegPCMAudio('./resources/mp3s/HeheBoi.mp3')
        player.start()
        while not player.is_done():
            await asyncio.sleep(1)
        # disconnect after the player has finished
        player.stop()
        await vc.disconnect()
    else:
        await message.channel.send('User is not in a voice channel.')
