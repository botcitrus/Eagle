import discord
from discord.ext import commands
from discord.ext.commands.core import bot_has_guild_permissions
from datetime import datetime
import typing as t
import json

base_color=0x3498db
su_color=0x2ecc71
err_color=0xe74c3c

class mod(commands.Cog):
    def __init__(self, Bot):
        self.Bot = Bot

    @commands.command(
        aliases = ['кик', 'кикнуть', 'выгнать']
    )
    @commands.has_guild_permissions(kick_members=True)
    async def kick(
        self,
        ctx,
        members: commands.Greedy[discord.Member] = None,
        *,
        res: t.Optional[str] = 'Не указана.'
    ):
        with open('databases/server_settings/mass_db.json', 'r') as f:
            server = json.load(f)
        tru = discord.utils.get(self.Bot.emojis, name='ctrue')
        err = discord.utils.get(self.Bot.emojis, name='cfalse')
        if members == None:
            e = discord.Embed(
                title=f'{err} Вы не указали параметр:',
                description='> Пользователь/ли',
                color=err_color
            )
            if str(ctx.guild.id) in server["reply"]:
                await ctx.send(embed=e)
            else:
                await ctx.reply(embed=e, mention_author=False)
        elif bot_has_guild_permissions(kick_members=True):
            for member in members:
                await member.kick(reason = res)
                e = discord.Embed(
                    title=f'{tru} Пользователь выгнан с сервера.',
                    description=f'''`Пользователь`: {member.mention}
`Причина`: {res}
`Модератор`: {ctx.author.mention}''',
                    color=su_color,
                    timestamp=datetime.utcnow()
                )
                if str(ctx.guild.id) in server["reply"]:
                    await ctx.send(embed=e)
                else:
                    await ctx.reply(embed=e, mention_author=False)
                try:
                    e2 = discord.Embed(
                        title=f'{member}, Вас выгнали с сервера {ctx.guild.name}',
                        description=f'''`Причина`: {res}
`Модератор`: {ctx.author.mention}''',
                        color=base_color,
                        timestamp=datetime.utcnow()
                    )
                    await member.send(embed=e2)
                except Exception:
                    pass
        else:
            e = discord.Embed(
                title=f'{err} Невозможно совершить операцию',
                description=f'У меня нет права "Выгонять пользователей" на этом сервере. Без него я не смогу выгонять пользователей. Для разрешения проблемы выдайте мне данное право или обратитесь к создателю сервера.',
                color=err_color
            )
            if str(ctx.guild.id) in server["reply"]:
                await ctx.send(embed=e)
            else:
                await ctx.reply(embed=e, mention_author=False)

    @commands.command(
        aliases = ['бан', 'забанить', 'заблокировать']
    )
    @commands.has_guild_permissions(ban_members=True)
    async def ban(
        self,
        ctx,
        members: commands.Greedy[discord.Member] = None,
        *,
        res: str = 'Не указана.'
    ):
        with open('databases/server_settings/mass_db.json', 'r') as f:
            server = json.load(f)
        tru = discord.utils.get(self.Bot.emojis, name='ctrue')
        err = discord.utils.get(self.Bot.emojis, name='cfalse')
        if members == None:
            e = discord.Embed(
                title=f'{err} Вы не указали параметр:',
                description='> Пользователь/ли',
                color=err_color
            )
            if str(ctx.guild.id) in server["reply"]:
                await ctx.send(embed=e)
            else:
                await ctx.reply(embed=e, mention_author=False)
        elif bot_has_guild_permissions(ban_members=True):
            for member in members:
                await member.ban(reason = res)
                e = discord.Embed(
                    title=f'{tru} Пользователь забанен.',
                    description=f'''`Пользователь`: {member.mention}
`Причина`: {res}
`Модератор`: {ctx.author.mention}''',
                    color=su_color,
                    timestamp=datetime.utcnow()
                )
                if str(ctx.guild.id) in server["reply"]:
                    await ctx.send(embed=e)
                else:
                    await ctx.reply(embed=e, mention_author=False)
                try:
                    e2 = discord.Embed(
                        title=f'{member}, Вас забанили на сервере {ctx.guild.name}',
                        description=f'''`Причина`: {res}
`Модератор`: {ctx.author.mention}''',
                        color=base_color,
                        timestamp=datetime.utcnow()
                    )
                    await member.send(embed=e2)
                except Exception:
                    pass
        else:
            e = discord.Embed(
                title=f'{err} Невозможно совершить операцию',
                description=f'У меня нет права "Банить пользователей" на этом сервере. Без него я не смогу Банить пользователей. Для разрешения проблемы выдайте мне данное право или обратитесь к создателю сервера.',
                color=err_color
            )
            if str(ctx.guild.id) in server["reply"]:
                await ctx.send(embed=e)
            else:
                await ctx.reply(embed=e, mention_author=False)

    @commands.command(
        aliases = ['clear', 'purge', 'очистить', 'удалить', 'чистка']
    )
    @commands.has_guild_permissions(manage_messages=True)
    async def clean(
        self,
        ctx,
        amount: int = 0
    ):
        with open('databases/server_settings/mass_db.json', 'r') as f:
            server = json.load(f)
        tru = discord.utils.get(self.Bot.emojis, name='ctrue')
        err = discord.utils.get(self.Bot.emojis, name='cfalse')
        if bot_has_guild_permissions(manage_messages=True):
            if amount > 3500:
                e = discord.Embed(
                    title=f'{err} Невозможно совершить операцию',
                    description=f'Указан слишком большой параметр сообщений. Вы можете указать число сообщений не меньше 0 и не больше 3500.',
                    color=err_color
                )
                await ctx.send(embed=e)
            else:
                await ctx.channel.purge(limit=amount+1)
                e = discord.Embed(
                    title=f'{tru} Успешно!',
                    description=f'''`Пользователем`: {ctx.author.mention}
`Удалено сообщений`: {amount}''',
                    color=su_color,
                    timestamp=datetime.utcnow()
                )
                await ctx.send(embed=e)
        else:
            e = discord.Embed(
                title=f'{err} Невозможно совершить операцию',
                description=f'У меня нет права "Управлять сообщениями" на этом сервере. Без него я не смогу выгонять пользователей. Для разрешения проблемы выдайте мне данное право или обратитесь к создателю сервера.',
                color=err_color
            )
            await ctx.send(embed=e)

    @commands.command(
        aliases = ['addrole', 'arole', 'role', 'роль', 'добавить_роль']
    )
    @commands.has_guild_permissions(manage_roles=True)
    async def add_role(
        self,
        ctx,
        member: discord.Member = None,
        *,
        role: discord.Role = None
    ):
        with open('databases/server_settings/mass_db.json', 'r') as f:
            server = json.load(f)
        tru = discord.utils.get(self.Bot.emojis, name='ctrue')
        err = discord.utils.get(self.Bot.emojis, name='cfalse')
        if member == None and role == None:
            e = discord.Embed(
                title=f'{err} Вы не указали параметр:',
                description='''> Пользователь
> Роль''',
                color=err_color
            )
            if str(ctx.guild.id) in server["reply"]:
                await ctx.send(embed=e)
            else:
                await ctx.reply(embed=e, mention_author=False)
        elif not member == None and role == None:
            e = discord.Embed(
                title=f'{err} Вы не указали параметр:',
                description='> Роль',
                color=err_color
            )
            if str(ctx.guild.id) in server["reply"]:
                await ctx.send(embed=e)
            else:
                await ctx.reply(embed=e, mention_author=False)
        else:
            if bot_has_guild_permissions(manage_roles=True):
                add_role = discord.utils.get(ctx.guild.roles, id=role.id)
                await member.add_roles(add_role)
                e = discord.Embed(
                    title=f'{tru} Добавлена роль.',
                    description=f'''`Роль`: {role.mention}
`Выдана`: {member.mention}
`Модератор`: {ctx.author.mention}''',
                    color=su_color,
                    timestamp=datetime.utcnow()
                )
                if str(ctx.guild.id) in server["reply"]:
                    await ctx.send(embed=e)
                else:
                    await ctx.reply(embed=e, mention_author=False)
            else:
                e = discord.Embed(
                    title=f'{err} Невозможно совершить операцию',
                    description=f'У меня нет права "Выгонять пользователей" на этом сервере. Без него я не смогу выгонять пользователей. Для разрешения проблемы выдайте мне данное право или обратитесь к создателю сервера.',
                    color=err_color
                )
                if str(ctx.guild.id) in server["reply"]:
                    await ctx.send(embed=e)
                else:
                    await ctx.reply(embed=e, mention_author=False)

    @commands.command(
        aliases = ['r_role', 'rrole', 'rem_role', 'рроль', 'убрать_роль']
    )
    @commands.has_guild_permissions(manage_roles=True)
    async def remove_role(
        self,
        ctx,
        member: discord.Member = None,
        *,
        role: discord.Role = None
    ):
        with open('databases/server_settings/mass_db.json', 'r') as f:
            server = json.load(f)
        tru = discord.utils.get(self.Bot.emojis, name='ctrue')
        err = discord.utils.get(self.Bot.emojis, name='cfalse')
        if member == None and role == None:
            e = discord.Embed(
                title=f'{err} Вы не указали параметр:',
                description='''> Пользователь
> Роль''',
                color=err_color
            )
            if str(ctx.guild.id) in server["reply"]:
                await ctx.send(embed=e)
            else:
                await ctx.reply(embed=e, mention_author=False)
        elif not member == None and role == None:
            e = discord.Embed(
                title=f'{err} Вы не указали параметр:',
                description='> Роль',
                color=err_color
            )
            if str(ctx.guild.id) in server["reply"]:
                await ctx.send(embed=e)
            else:
                await ctx.reply(embed=e, mention_author=False)
        else:
            if bot_has_guild_permissions(manage_roles=True):
                remove_role = discord.utils.get(ctx.guild.roles, id=role.id)
                await member.remove_roles(remove_role)
                e = discord.Embed(
                    title=f'{tru} Снята роль.',
                    description=f'''`Роль`: {role.mention}
`Снята у`: {member.mention}
`Модератор`: {ctx.author.mention}''',
                    color=su_color,
                    timestamp=datetime.utcnow()
                )
                if str(ctx.guild.id) in server["reply"]:
                    await ctx.send(embed=e)
                else:
                    await ctx.reply(embed=e, mention_author=False)
            else:
                e = discord.Embed(
                    title=f'{err} Невозможно совершить операцию',
                    description=f'У меня нет права "Выгонять пользователей" на этом сервере. Без него я не смогу выгонять пользователей. Для разрешения проблемы выдайте мне данное право или обратитесь к создателю сервера.',
                    color=err_color
                )
                if str(ctx.guild.id) in server["reply"]:
                    await ctx.send(embed=e)
                else:
                    await ctx.reply(embed=e, mention_author=False)          

    ###PERMISSION ERRORS###
    @kick.error
    async def perm_kick_error(self, ctx, error):
        with open('databases/server_settings/mass_db.json', 'r') as f:
            server = json.load(f)
        err = discord.utils.get(self.Bot.emojis, name='cfalse')
        if isinstance(error, commands.MissingPermissions):
            embed = discord.Embed(
                title=f'{err} Ошибка!',
                description = "У Вас недостаточно прав (`Выгонять участников`) для выполения данной команды.",
                colour=err_color,
                )
            if str(ctx.guild.id) in server["reply"]:
                await ctx.send(embed=embed)
            else:
                await ctx.reply(embed=embed, mention_author=False)
            
    @ban.error
    async def perm_ban_error(self, ctx, error):
        with open('databases/server_settings/mass_db.json', 'r') as f:
            server = json.load(f)
        err = discord.utils.get(self.Bot.emojis, name='cfalse')
        if isinstance(error, commands.MissingPermissions):
            embed = discord.Embed(
                title=f'{err} Ошибка!',
                description = "У Вас недостаточно прав (`Банить участников`) для выполения данной команды.",
                colour=err_color,
                )
            if str(ctx.guild.id) in server["reply"]:
                await ctx.send(embed=embed)
            else:
                await ctx.reply(embed=embed, mention_author=False)
    
    @clean.error
    async def perm_clean_error(self):
        pass

    @add_role.error
    async def perm_add_role_error(self):
        pass

    @remove_role.error
    async def perm_remove_role_error(self):
        pass

def setup (Bot):
    Bot.add_cog(mod(Bot))
