import discord
from discord.ext import commands
import json

from discord_components import DiscordComponents, Button, ButtonStyle

su_color=0x2ecc71
err_color=0xe74c3c
null_color=discord.Color.from_rgb(47,49,56)

class owner(commands.Cog):
    def __init__(self, Bot):
        self.Bot = Bot

    ###TECH###
    @commands.command()
    @commands.is_owner()
    async def status(
        self,
        ctx,
        *,
        sts: str = None
    ):
        with open('databases/server_settings/mass_db.json', 'r') as f:
            server = json.load(f)
        tru = discord.utils.get(self.Bot.emojis, name='ctrue')
        err = discord.utils.get(self.Bot.emojis, name='cfalse')
        if sts == None:
            e = discord.Embed(
                title=f'{err} Вы не указали параметр:',
                description=f'Текст',
                color=err_color
            )
            if str(ctx.guild.id) in server["reply"]:
                await ctx.send(embed=e)
            else:
                await ctx.reply(embed=e, mention_author=False)
        else:
            await self.Bot.change_presence(
                status=discord.Status.idle,
                activity=discord.Activity(
                    type=discord.ActivityType.watching, 
                    name=sts
                )
            )
            e = discord.Embed(
                title=f'{tru} Успешно!',
                description=f'Статус успешно изменен на __{sts}__',
                color=su_color
            )
            if str(ctx.guild.id) in server["reply"]:
                await ctx.send(embed=e)
            else:
                await ctx.reply(embed=e, mention_author=False)

    @commands.command()
    @commands.is_owner()
    async def update(
        self,
        ctx,
        num,
        numname,
        date,
        *,
        txt
    ):
        wt = discord.utils.get(self.Bot.emojis, name='cnone')
        e = discord.Embed(
            title=f'{wt} UPDATE №{num} - {numname} от {date}',
            description=txt,
            color=null_color
        )
        await ctx.message.delete()
        await ctx.send('<@&846307638210723880>', embed=e)

    ###ROOT###
    @commands.command()
    @commands.is_owner()
    async def rootuser(
        self,
        ctx,
        type = None,
        member: discord.Member = None
    ): 
        with open('databases/server_settings/mass_db.json', 'r') as f:
            server = json.load(f)
        with open('databases/users_settings/user_db.json', 'r') as f:
            usr = json.load(f)  
        err = discord.utils.get(self.Bot.emojis, name='cfalse')
        tru = discord.utils.get(self.Bot.emojis, name='ctrue')
        if type == None and member == None:
            e = discord.Embed(
                title=f'{err} Вы не указали параметр:',
                description='''> Действие (-add/-rem) 
> Пользователь''',
                color=err_color
            )
            if str(ctx.guild.id) in server["reply"]:
                await ctx.send(embed=e)
            else:
                await ctx.reply(embed=e, mention_author=False)
        elif not type == None and member == None:
            e = discord.Embed(
                title=f'{err} Вы не указали параметр:',
                description='> Пользователь',
                color=err_color
            )
            if str(ctx.guild.id) in server["reply"]:
                await ctx.send(embed=e)
            else:
                await ctx.reply(embed=e, mention_author=False)
        else:
            if type == '-add':
                if not str(member.id) in usr["root"]:
                    usr["root"][str(member.id)] = True
                    with open('databases/users_settings/user_db.json', 'w') as f:
                        json.dump(usr, f)
                    e = discord.Embed(
                        title=f'{tru} Успешно!',
                        description=f'Пользователь {member.mention} добавлен в список **root-пользователей**.',
                        color=su_color
                    )
                    e.set_footer(text='Будьте осторожены при назначении root-пользователей! Root-пользователь имеет практически полный доступ к закрытым функциям бота.')
                    if str(ctx.guild.id) in server["reply"]:
                        await ctx.send(embed=e)
                    else:
                        await ctx.reply(embed=e, mention_author=False)
                else:
                    e = discord.Embed(
                        title=f'{err} Ошибка!',
                        description=f'Пользователь {member.mention} уже есть в списке **root-пользователей**.',
                        color=err_color
                    )
                    e.set_footer(text='Будьте осторожены при назначении root-пользователей! Root-пользователь имеет практически полный доступ к закрытым функциям бота.')
                    if str(ctx.guild.id) in server["reply"]:
                        await ctx.send(embed=e)
                    else:
                        await ctx.reply(embed=e, mention_author=False)
            elif type == '-rem':
                if str(member.id) in usr["root"]:
                    del usr["root"][str(member.id)]
                    with open('databases/users_settings/user_db.json', 'w') as f:
                        json.dump(usr, f)
                    e = discord.Embed(
                        title=f'{tru} Успешно!',
                        description=f'Пользователь {member.mention} удален из списка **root-пользователей**.',
                        color=su_color
                    )
                    e.set_footer(text='Будьте осторожены при назначении root-пользователей! Root-пользователь имеет практически полный доступ к закрытым функциям бота.')
                    if str(ctx.guild.id) in server["reply"]:
                        await ctx.send(embed=e)
                    else:
                        await ctx.reply(embed=e, mention_author=False)
                else:
                    e = discord.Embed(
                        title=f'{tru} Ошибка!',
                        description=f'Пользователя {member.mention} нету списке **root-пользователей**.',
                        color=err_color
                    )
                    e.set_footer(text='Будьте осторожены при назначении root-пользователей! Root-пользователь имеет практически полный доступ к закрытым функциям бота.')
                    if str(ctx.guild.id) in server["reply"]:
                        await ctx.send(embed=e)
                    else:
                        await ctx.reply(embed=e, mention_author=False)

    ###ITEMS###
    @commands.command()
    @commands.is_owner()
    async def item(
        self,
        ctx,
        act = None,
        it = None,
        member: discord.Member = None
    ):     
        with open('databases/server_settings/mass_db.json', 'r') as f:
            server = json.load(f)
        with open('databases/users_settings/user_db.json', 'r') as f:
            usr = json.load(f)  
        err = discord.utils.get(self.Bot.emojis, name='cfalse')
        tru = discord.utils.get(self.Bot.emojis, name='ctrue')
        if act == None and it == None and member == None:
            e = discord.Embed(
                    title=f'{err} Вы не указали параметр:',
                    description='''> Действие (-add/-rem)
> Предмет 
> Пользователь''',
                    color=err_color
                )
            if str(ctx.guild.id) in server["reply"]:
                await ctx.send(embed=e)
            else:
                await ctx.reply(embed=e, mention_author=False)
        if not act == None and it == None and member == None:
            e = discord.Embed(
                    title=f'{err} Вы не указали параметр:',
                    description='''> Предмет 
> Пользователь''',
                    color=err_color
                )
            if str(ctx.guild.id) in server["reply"]:
                await ctx.send(embed=e)
            else:
                await ctx.reply(embed=e, mention_author=False)
        if not act == None and not it == None and member == None:
            e = discord.Embed(
                title=f'{err} Вы не указали параметр:',
                description='> Пользователь',
                color=err_color
            )
            if str(ctx.guild.id) in server["reply"]:
                await ctx.send(embed=e)
            else:
                await ctx.reply(embed=e, mention_author=False)
        if act == '-add':
            if str(it) in usr["items"]:
                if str(member.id) in usr["items"][str(it)]:
                    e = discord.Embed(
                        title=f'{err} Ошибка!',
                        description=f'Предмет "{it}" уже есть у {member.mention}!',
                        color=err_color
                    )
                    if str(ctx.guild.id) in server["reply"]:
                        await ctx.send(embed=e)
                    else:
                        await ctx.reply(embed=e, mention_author=False)
                else:
                    usr["items"][str(it)][str(member.id)] = True
                    with open('databases/users_settings/user_db.json', 'w') as f:
                        json.dump(usr, f) 
                    e = discord.Embed(
                        title=f'{tru} Успешно!',
                        description=f'Предмет "{it}" добавлен {member.mention}!',
                        color=su_color
                    )
                    if str(ctx.guild.id) in server["reply"]:
                        await ctx.send(embed=e)
                    else:
                        await ctx.reply(embed=e, mention_author=False)
            else:
                e = discord.Embed(
                    title=f'{err} Ошибка!',
                    description=f'Предмета "{it}" нет в списке всех предметов!',
                    color=err_color
                )
                if str(ctx.guild.id) in server["reply"]:
                    await ctx.send(embed=e)
                else:
                    await ctx.reply(embed=e, mention_author=False)
        if act == '-rem':
            if str(it) in usr["items"]:
                if not str(member.id) in usr["items"][str(it)]:
                    e = discord.Embed(
                        title=f'{err} Ошибка!',
                        description=f'У {member.mention} нет предмета "{it}"!',
                        color=err_color
                    )
                    if str(ctx.guild.id) in server["reply"]:
                        await ctx.send(embed=e)
                    else:
                        await ctx.reply(embed=e, mention_author=False)
                else:
                    del usr["items"][str(it)][str(member.id)]
                    with open('databases/users_settings/user_db.json', 'w') as f:
                        json.dump(usr, f) 
                    e = discord.Embed(
                        title=f'{tru} Успешно!',
                        description=f'Предмет "{str(it)}" изъят у {member.mention}!',
                        color=su_color
                    )
                    if str(ctx.guild.id) in server["reply"]:
                        await ctx.send(embed=e)
                    else:
                        await ctx.reply(embed=e, mention_author=False)
            else:
                e = discord.Embed(
                    title=f'{err} Ошибка!',
                    description=f'Предмета "{it}" нет в списке всех предметов!',
                    color=err_color
                )
                if str(ctx.guild.id) in server["reply"]:
                    await ctx.send(embed=e)
                else:
                    await ctx.reply(embed=e, mention_author=False)

    ###ECONOMY###
    @commands.command()
    @commands.is_owner()
    async def course(
        self,
        ctx,
        val: int
    ):
        with open('databases/economy_data/economy_db.json', 'r') as f:
            eco = json.load(f)
        with open('databases/server_settings/mass_db.json', 'r') as f:
            server = json.load(f)
        tru = discord.utils.get(self.Bot.emojis, name='ctrue')
        eco["users"]["crypto"]["cryptovalue"] = val
        with open('databases/economy_data/economy_db.json', 'w') as f:
            json.dump(eco, f)
        e = discord.Embed(
            title=f'{tru} Успешно!',
            description=f'Курс криптовалюты успешно изменен до **{val}₽** за единицу.',
            color=su_color
        )
        if str(ctx.guild.id) in server["reply"]:
            await ctx.send(embed=e)
        else:
            await ctx.reply(embed=e, mention_author=False)

"""
tip for formating seconds in readable type   
hours, seconds = divmod(seconds, 60 ** 2)
minutes, seconds = divmod(seconds, 60)
"Вывод: {round(hours)} ч, {round(minutes)} мин, {round(seconds)} сек"
"""

def setup (Bot):
    Bot.add_cog(owner(Bot))
