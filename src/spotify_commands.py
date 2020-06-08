import discord
import asyncio

client = discord.Client()

async def playSong(message):
    user=message.author
    voice_channel=user.voice.channel
    if voice_channel!= None:
        # create StreamPlayer
        vc= await voice_channel.connect()
        player = vc.create_ffmpeg_player('./resources/mp3s/HeheBoi.mp3', after=lambda: print('done'))
        player.start()
        while not player.is_done():
            await asyncio.sleep(1)
        # disconnect after the player has finished
        player.stop()
        await vc.disconnect()
    else:
        await message.channel.send('User is not in a voice channel.')
