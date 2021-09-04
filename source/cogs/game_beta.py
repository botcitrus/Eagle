import discord
from discord.ext import commands
from datetime import datetime
import json

base_color=0x3498db
su_color=0x2ecc71
err_color=0xe74c3c

class game(commands.Cog):
    def __init__(self, Bot):
        self.Bot = Bot

    @commands.command(
        #aliases = []
    )
    @commands.is_owner()
    async def roleplay(
        self,
        ctx
    ):
        pass
        #you can add something ftom yourself here because this section in beta.

def setup (Bot):
    Bot.add_cog(game(Bot))
