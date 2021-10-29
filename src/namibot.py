import sys
import asyncio
import logging
import discord
from time import sleep

# sys.path.append("/mnt/c/Users/rafae/Documents/discord_bot")

MUSIC_DIR = "/mnt/datawindows/Users/rafae/Documents/discord_bot/songs/"

sys.path.append("/mnt/datawindows/Users/rafae/Documents/discord_bot/")

from diceroller.dicethrower import DiceThrower
from playlist.musicmanager import MusicManager
from discord.ext import commands#, task

class Namibot(commands.Cog):
    def __init__(self,bot):
        self.bot=bot
        self.mm = MusicManager()
        self.instream = False
        self.roller = DiceThrower()
        # super().__init__()
    @commands.command()
    async def r(self,ctx,message):
        self.roller.treat_string(message)
        self.roller.roll()
        await ctx.send(self.roller.result())

    @commands.command()
    async def join(self, ctx, description="Join in the channel that was called") -> None:
        channel = ctx.author.voice.channel
        await channel.connect()

    @commands.command()
    async def leave(self,ctx) -> None:
        await ctx.voice_client.disconnect()

    @commands.command()
    async def play(self,ctx, url) -> None:
        if not self.instream:
            self.mm.add_music(url)
            title = self.mm.now
            sleep(3)
            source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio(MUSIC_DIR+title))
            ctx.voice_client.play(source)
            self.instream = True
            await ctx.send(f"Now playing {self.mm.music.title}")    
        else:
            ctx.send("Not possible to play, when another music playing")

    @commands.command()
    async def add(self, ctx, url):
        self.mm.add_music(url)
        title = self.mm.now
        await ctx.send(f"Add in queue {self.mm[-1].title}")

    @commands.command()
    async def next(self,ctx):
        ctx.voice_client.stop()
        self.mm.next()
        title = self.mm.now
        source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio(MUSIC_DIR+title))
        ctx.voice_client.play(source)
        await ctx.send(f"Now Playing {self.mm.music.title}")

    @commands.command()
    async def prev(self,ctx):
        ctx.voice_client.stop()
        self.mm.prev()
        title = self.mm.now
        source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio(MUSIC_DIR+title))
        ctx.voice_client.play(source)
        await ctx.send(f"Now Playing {self.mm.music.title}")

    @commands.command()
    async def q(self,ctx):
        await ctx.send(self.mm)



bot = commands.Bot(command_prefix=commands.when_mentioned_or("!"),description="RPG and Music bot")
@bot.event
async def on_ready():
    print("Hello World!")
    print('Logged in as {0} ({0.id})'.format(bot.user))
    print('------')

def main():

    bot.run("YOUR TOKEN")
if __name__=="__main__":
    main()
