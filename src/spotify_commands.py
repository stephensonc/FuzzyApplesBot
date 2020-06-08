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
            client.voice.play(discord.FFmpegPCMAudio('./resources/mp3s/HeheBoi.mp3'))
        except discord.errors.ClientException as e:
            if str(e) == "Not connected to voice.":
                raise UserError("Error playing clip.")
                await vc.disconnect()
            else:
                raise
                await vc.disconnect()
        # disconnect after the player has finished
        await vc.disconnect()
    else:
        await message.channel.send('User is not in a voice channel.')
