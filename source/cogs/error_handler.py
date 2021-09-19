import discord
from discord.ext import commands
from datetime import datetime
import json
import traceback

base_color=0x3498db
err_color=0xe74c3c

class error_handler(commands.Cog):
    def __init__(self, Bot):
        self.Bot = Bot

    @commands.Cog.listener()
    async def on_command_error(
        self, 
        ctx, 
        exception   
    ):
        with open('databases/server_settings/mass_db.json', 'r') as f:
            server = json.load(f)
        err = discord.utils.get(self.Bot.emojis, name='cfalse')
        channel = self.Bot.get_channel(866662493048799242)
        e = exception
        if isinstance(e, commands.CommandNotFound): #commands.errors.CommandOnCooldown
            if not str(ctx.guild.id) in server["errors"]:
                embed = discord.Embed(
                    title=f'{err} Ошибка!',
                    description = f"Такой команды нет в моем списке.", 
                    colour=err_color,
                    )
                if str(ctx.guild.id) in server["reply"]:
                    await ctx.send(embed=embed)
                else:
                    await ctx.reply(embed=embed, mention_author=False)
            else:
                pass
        elif isinstance(e, commands.CommandOnCooldown):
            pass
        elif isinstance(e, commands.MissingPermissions):
            pass
        elif isinstance(e, commands.NotOwner):
        	pass
        elif isinstance(e, commands.CommandInvokeError):
            if ctx.command == "buy":
                pass
        else:
            ###ANNOUNCEMET###
            await ctx.message.add_reaction(err)
            ###LOG###
            class1 = f"{e.__class__}"
            class2 = class1[1:]
            class_result = class2[:-1]
            error = f"{e}"
            error_result = str.capitalize(error)
            embed = discord.Embed(
                title=f'{err} Ошибка команды (commands.command)',
                description = f"""**Класс:**\n```py\n{class_result}```
**Ошибка:**\n```py\n{error_result}```
**Команда:** `{ctx.command}`""", 
                colour=err_color,
                timestamp = datetime.utcnow()
                )
            embed.add_field(
                name='Подробнее',
                value=f"""Сервер: **{ctx.guild.name}**
Канал: <#{ctx.channel.id}>
Автор: {ctx.author.mention}""",
                inline=False
            )
            await channel.send(embed=embed)

    @commands.Cog.listener() #EVENTS
    async def on_error(
        self, 
        event, 
        *args, 
        **kwargs
    ):
        with open('databases/server_settings/mass_db.json', 'r') as f:
            server = json.load(f)
        err = discord.utils.get(self.Bot.emojis, name='cfalse')
        channel = self.Bot.get_channel(866662493048799242)
        embed = discord.Embed(
            title=f'{err} Ошибка События (@commands.Cog.listener)', 
            description = f"```py\n{traceback.format_exc()}```",
            color=err_color,
            timestamp = datetime.utcnow()
            )
        embed.add_field(
            name='Событие', 
            value="`{}`".format(event)
            )
        await channel.send(embed=embed)

def setup (Bot):
    Bot.add_cog(error_handler(Bot))
