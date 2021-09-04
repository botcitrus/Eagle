import discord
from discord.ext import commands
from typing import Optional as t
import random
import aiohttp
import json

base_color=0x3498db
su_color=0x2ecc71
err_color=0xe74c3c
null_color=discord.Color.from_rgb(47,49,56)

class fun(commands.Cog):
    def __init__(self, Bot):
        self.Bot = Bot

    @commands.command(
        aliases = ['аватар', 'ава', 'аватарка', 'фотография', 'иконка']
    )
    async def avatar(
        self,
        ctx,
        member: discord.Member = None
    ):
        with open('databases/server_settings/mass_db.json', 'r') as f:
            server = json.load(f)
        if member == None:
            member = ctx.author
        embed = discord.Embed(
            title=f"Аватар {member}", 
            color=base_color
            )
        embed.set_image(url=member.avatar_url)
        if str(ctx.guild.id) in server["reply"]:
            await ctx.send(embed=embed)
        else:
            await ctx.reply(embed=embed, mention_author=False)

    @commands.command(
        aliases = ['coinflip', 'монетка', 'подбросить', 'подбросить_монетку', 'орел_решка', 'орелрешка', 'орёл_решка', 'орёлрешка']
    )
    async def coin(
        self,
        ctx
    ):
        with open('databases/server_settings/mass_db.json', 'r') as f:
            server = json.load(f)
        coin = random.choice(['Орёл', 'Решка'])
        embed = discord.Embed(
            title=f"Подбрасываем монетку!", 
            description=f'На монетке выпало: **{coin}**.',
            color=base_color
            )
        if str(ctx.guild.id) in server["reply"]:
            await ctx.send(embed=embed)
        else:
            await ctx.reply(embed=embed, mention_author=False)

    @commands.command(
        aliases = ['собака', 'пёсик', 'песик', 'пёсель', 'песель', 'собакен', 'собачка']
    )
    async def dog(
        self,
        ctx
    ):
        with open('databases/server_settings/mass_db.json', 'r') as f:
            server = json.load(f)
        async with aiohttp.ClientSession() as session:
           request = await session.get('https://some-random-api.ml/img/dog')
           dogjson = await request.json()
        embed = discord.Embed(
           title="Wuf-wuf!", 
           color=base_color
           )
        embed.set_image(url=dogjson['link'])
        if str(ctx.guild.id) in server["reply"]:
            await ctx.send(embed=embed)
        else:
            await ctx.reply(embed=embed, mention_author=False)

    @commands.command(
        aliases = ['кошка', 'кот', 'котик', 'котэ', 'котэвич', 'коте', 'котевич']
    )
    async def cat(
        self,
        ctx
    ):
        with open('databases/server_settings/mass_db.json', 'r') as f:
            server = json.load(f)
        async with aiohttp.ClientSession() as session:
           request = await session.get('https://some-random-api.ml/img/cat')
           dogjson = await request.json()
        embed = discord.Embed(
           title="Meow!", 
           color=base_color
           )
        embed.set_image(url=dogjson['link'])
        if str(ctx.guild.id) in server["reply"]:
            await ctx.send(embed=embed)
        else:
            await ctx.reply(embed=embed, mention_author=False)

def setup(Bot):
    Bot.add_cog(fun(Bot))
