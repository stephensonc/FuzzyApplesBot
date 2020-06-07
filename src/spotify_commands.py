import discord
import asyncio


async def playSong(message):
    user=message.author
    voice_channel=user.voice.channel
    channel=None
    if voice_channel!= None:
        await client.say('User is in channel: '+ voice_channel)
        # create StreamPlayer
        vc= await client.join_voice_channel(voice_channel)
        player = vc.create_ffmpeg_player('./resources/mp3s/HeheBoi.mp3', after=lambda: print('done'))
        player.start()
        while not player.is_done():
            await asyncio.sleep(1)
        # disconnect after the player has finished
        player.stop()
        await vc.disconnect()
    else:
        await client.say('User is not in a voice channel.')
