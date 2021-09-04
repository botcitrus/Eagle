import discord
from discord.ext import commands
import json

base_color=0x3498db
su_color=0x2ecc71
err_color=0xe74c3c

on = ['вкл', 'включить', 'on']
off = ['выкл', 'выключить', 'off']   

class utils(commands.Cog):
    def __init__(self, Bot):
        self.Bot = Bot
       
    @commands.command(
        aliases = ['центр', 'центральная', 'центр_сервера', 'server_center', 'панель', 'панель_сервера', 'серверная_панель']
    )
    @commands.has_guild_permissions(administrator=True)
    async def center(
        self,
        ctx
    ):
        
        with open('databases/server_settings/mass_db.json', 'r') as f:
            server = json.load(f)
        wt = discord.utils.get(self.Bot.emojis, name='cnone')
        tru = discord.utils.get(self.Bot.emojis, name='ctrue')
        err = discord.utils.get(self.Bot.emojis, name='cfalse')
        embed = discord.Embed(
            title=f'{wt} Центр управления сервером {ctx.guild.name}.',
            colour=base_color
            )
        if not str(ctx.guild.id) in server["reply"]:
            embed.add_field(
                name='Продвинутые ответы бота:',
                value=f'''Серверное состояние: **{tru} Включены**.
Описание: Во включенном состоянии бот отвечает на ваши сообщения с указанием автора и вызывающего сообщения.
Команды изменения: `!ответы <вкл/выкл>`.''',
                inline=False
                )
        else:
            embed.add_field(
                name='Продвинутые ответы бота:',
                value=f'''Серверное состояние: **{err} Выключены**.
Описание: Во включенном состоянии бот отвечает на ваши сообщения с указанием автора и вызывающего сообщения.
Команды изменения: `!ответы <вкл/выкл>`.''',
                inline=False
                )
        if not str(ctx.guild.id) in server["errors"]:
            embed.add_field(
                name='Оповещения об ошибках:',
                value=f'''Серверное состояние: **{tru} Включены**.
Описание: Во включенном состоянии бот оповещает Вас об отсутствии неправльно введенной команды.
Команды изменения: `!ошибки <вкл/выкл>`.''',
                inline=False
                )
        else:
            embed.add_field(
                name='Оповещения об ошибках:',
                value=f'''Серверное состояние: **{err} Выключены**.
Описание: Во включенном состоянии бот оповещает Вас об отсутствии неправльно введенной команды.
Команды изменения: `!ошибки <вкл/выкл>`.''',
                inline=False
                )
        if not str(ctx.guild.id) in server["mentions"]:
            embed.add_field(
                name='Упоминания бота:',
                value=f'''Серверное состояние: **{err} Вsключены**.
Описание: Во включенном состоянии бот выведет краткое описание при @пинге.
Команды изменения: `!ошибки <вкл/выкл>`.''',
                inline=False
                )
        else:
            embed.add_field(
                name='Упоминания бота:',
                value=f'''Серверное состояние: **{tru} Включены**.
Описание: Во включенном состоянии бот выведет краткое описание при @пинге.
Команды изменения: `!ошибки <вкл/выкл>`.''',
                inline=False
                )
        embed.set_thumbnail(url=ctx.guild.icon_url)
        embed.set_footer(
            text = f'Администратор: {ctx.author}',
            icon_url=ctx.author.avatar_url
            )
        if str(ctx.guild.id) in server["reply"]:
            await ctx.send(embed=embed)
        else:
            await ctx.reply(embed=embed, mention_author=False)
        
    @commands.command(
        aliases = ['ответы', 'ответы_бота', 'ответ', 'bot_answer', 'answer']
    )
    @commands.has_guild_permissions(administrator=True)
    async def answers(
        self,
        ctx,
        tp = None
    ):
        with open('databases/server_settings/mass_db.json', 'r') as f:
            server = json.load(f)
        tru = discord.utils.get(self.Bot.emojis, name='ctrue')
        err = discord.utils.get(self.Bot.emojis, name='cfalse')
        if tp == None:
            embed = discord.Embed(
                title=f'{err} Вы не указали параметр:',
                description = """> Тип переключателя (вкл/выкл)""",
                colour=err_color
                )
            embed.set_footer(text = f'Пользователь: {ctx.author}')
            if str(ctx.guild.id) in server["reply"]:
                await ctx.send(embed=embed)
            else:
                await ctx.reply(embed=embed, mention_author=False)
        else:
            if tp in off:
                if not str(ctx.guild.id) in server["reply"]:
                    server["reply"][str(ctx.guild.id)] = True
                    with open('databases/server_settings/mass_db.json', 'w') as f:
                        json.dump(server, f)
                    embed = discord.Embed(
                        title=f'{tru} Успешно!',
                        description = "Параметр \"ответы бота\" успешно выключены для этого сервера.",
                        colour=su_color
                        )
                    embed.set_footer(
                        text = f'Администратор: {ctx.author}',
                        icon_url=ctx.author.avatar_url
                        )
                    if str(ctx.guild.id) in server["reply"]:
                        await ctx.send(embed=embed)
                    else:
                        await ctx.reply(embed=embed, mention_author=False)
                else:
                    embed = discord.Embed(
                        title=f'{err} Ошибка!',
                        description = "На сервере уже выключен параметр ответов бота.",
                        colour=err_color
                        )
                    embed.set_footer(
                        text = f'Администратор: {ctx.author}',
                        icon_url=ctx.author.avatar_url
                        )
                    if str(ctx.guild.id) in server["reply"]:
                        await ctx.send(embed=embed)
                    else:
                        await ctx.reply(embed=embed, mention_author=False)
            if tp in on:
                if str(ctx.guild.id) in server["reply"]:
                    del server["reply"][str(ctx.guild.id)]
                    with open('databases/server_settings/mass_db.json', 'w') as f:
                        json.dump(server, f)
                    embed = discord.Embed(
                        title=f'{tru} Успешно!',
                        description = "Параметр \"ответы бота\" успешно включены для этого сервера.",
                        colour=su_color
                        )
                    embed.set_footer(
                        text = f'Администратор: {ctx.author}',
                        icon_url=ctx.author.avatar_url
                        )
                    if str(ctx.guild.id) in server["reply"]:
                        await ctx.send(embed=embed)
                    else:
                        await ctx.reply(embed=embed, mention_author=False)
                else:
                    embed = discord.Embed(
                        title=f'{err} Ошибка!',
                        description = "На сервере уже включен параметр ответов бота.",
                        colour=err_color
                        ) 
                    embed.set_footer(
                        text = f'Администратор: {ctx.author}',
                        icon_url=ctx.author.avatar_url
                        )
                    if str(ctx.guild.id) in server["reply"]:
                        await ctx.send(embed=embed)
                    else:
                        await ctx.reply(embed=embed, mention_author=False)

    @commands.command(
        aliases = ['ошибки', 'уведомления_ошибок']
    )
    @commands.has_guild_permissions(administrator=True)
    async def errors(
        self,
        ctx,
        tp = None
    ):
        with open('databases/server_settings/mass_db.json', 'r') as f:
            server = json.load(f)
        tru = discord.utils.get(self.Bot.emojis, name='ctrue')
        err = discord.utils.get(self.Bot.emojis, name='cfalse')
        if tp == None:
            embed = discord.Embed(
                title=f'{err} Вы не указали параметр:',
                description = """> Тип переключателя (вкл/выкл)""",
                colour=err_color
                )
            embed.set_footer(text = f'Пользователь: {ctx.author}')
            if str(ctx.guild.id) in server["reply"]:
                await ctx.send(embed=embed)
            else:
                await ctx.reply(embed=embed, mention_author=False)
        else:
            if tp in off:
                if not str(ctx.guild.id) in server["errors"]:
                    server["errors"][str(ctx.guild.id)] = True
                    with open('databases/server_settings/mass_db.json', 'w') as f:
                        json.dump(server, f)
                    embed = discord.Embed(
                        title=f'{tru} Успешно!',
                        description = "Параметр \"уведомления об ошибках\" успешно выключены для этого сервера.",
                        colour=su_color
                        )
                    embed.set_footer(
                        text = f'Администратор: {ctx.author}',
                        icon_url=ctx.author.avatar_url
                        )
                    if str(ctx.guild.id) in server["reply"]:
                        await ctx.send(embed=embed)
                    else:
                        await ctx.reply(embed=embed, mention_author=False)
                else:
                    embed = discord.Embed(
                        title=f'{err} Ошибка!',
                        description = "На сервере уже выключен параметр уведомлений об ошибках.",
                        colour=err_color
                        )
                    embed.set_footer(
                        text = f'Администратор: {ctx.author}',
                        icon_url=ctx.author.avatar_url
                        )
                    if str(ctx.guild.id) in server["reply"]:
                        await ctx.send(embed=embed)
                    else:
                        await ctx.reply(embed=embed, mention_author=False)
            if tp in on:
                if str(ctx.guild.id) in server["errors"]:
                    del server["errors"][str(ctx.guild.id)]
                    with open('databases/server_settings/mass_db.json', 'w') as f:
                        json.dump(server, f)
                    embed = discord.Embed(
                        title=f'{tru} Успешно!',
                        description = "Параметр \"уведомления об ошибках\" успешно включены для этого сервера.",
                        colour=su_color
                        )
                    embed.set_footer(
                        text = f'Администратор: {ctx.author}',
                        icon_url=ctx.author.avatar_url
                        )
                    if str(ctx.guild.id) in server["reply"]:
                        await ctx.send(embed=embed)
                    else:
                        await ctx.reply(embed=embed, mention_author=False)
                else:
                    embed = discord.Embed(
                        title=f'{err} Ошибка!',
                        description = "На сервере уже включен параметр уведомлений об ошибках.",
                        colour=err_color
                        ) 
                    embed.set_footer(
                        text = f'Администратор: {ctx.author}',
                        icon_url=ctx.author.avatar_url
                        )
                    if str(ctx.guild.id) in server["reply"]:
                        await ctx.send(embed=embed)
                    else:
                        await ctx.reply(embed=embed, mention_author=False)

    @commands.command(
        #aliases = ['пинг', 'уведомления_пинг']
    )
    @commands.has_guild_permissions(administrator=True)
    async def mention(
        self,
        ctx,
        tp = None
    ):
        with open('databases/server_settings/mass_db.json', 'r') as f:
            server = json.load(f)
        tru = discord.utils.get(self.Bot.emojis, name='ctrue')
        err = discord.utils.get(self.Bot.emojis, name='cfalse')
        if tp == None:
            embed = discord.Embed(
                title=f'{err} Вы не указали параметр:',
                description = """> Тип переключателя (вкл/выкл)""",
                colour=err_color
                )
            embed.set_footer(text = f'Пользователь: {ctx.author}')
            if str(ctx.guild.id) in server["reply"]:
                await ctx.send(embed=embed)
            else:
                await ctx.reply(embed=embed, mention_author=False)
        else:
            if tp in off:
                if not str(ctx.guild.id) in server["пинг бота"]:
                    server["пинг бота"][str(ctx.guild.id)] = True
                    with open('databases/server_settings/mass_db.json', 'w') as f:
                        json.dump(server, f)
                    embed = discord.Embed(
                        title=f'{tru} Успешно!',
                        description = "Параметр \"пинг бота\" успешно выключены для этого сервера.",
                        colour=su_color
                        )
                    embed.set_footer(
                        text = f'Администратор: {ctx.author}',
                        icon_url=ctx.author.avatar_url
                        )
                    if str(ctx.guild.id) in server["reply"]:
                        await ctx.send(embed=embed)
                    else:
                        await ctx.reply(embed=embed, mention_author=False)
                else:
                    embed = discord.Embed(
                        title=f'{err} Ошибка!',
                        description = "На сервере уже выключен параметр пинг бота.",
                        colour=err_color
                        )
                    embed.set_footer(
                        text = f'Администратор: {ctx.author}',
                        icon_url=ctx.author.avatar_url
                        )
                    if str(ctx.guild.id) in server["reply"]:
                        await ctx.send(embed=embed)
                    else:
                        await ctx.reply(embed=embed, mention_author=False)
            if tp in on:
                if str(ctx.guild.id) in server["пинг бота"]:
                    del server["пинг бота"][str(ctx.guild.id)]
                    with open('databases/server_settings/mass_db.json', 'w') as f:
                        json.dump(server, f)
                    embed = discord.Embed(
                        title=f'{tru} Успешно!',
                        description = "Параметр \"пинг бота\" успешно включены для этого сервера.",
                        colour=su_color
                        )
                    embed.set_footer(
                        text = f'Администратор: {ctx.author}',
                        icon_url=ctx.author.avatar_url
                        )
                    if str(ctx.guild.id) in server["reply"]:
                        await ctx.send(embed=embed)
                    else:
                        await ctx.reply(embed=embed, mention_author=False)
                else:
                    embed = discord.Embed(
                        title=f'{err} Ошибка!',
                        description = "На сервере уже включен параметр пинг бота.",
                        colour=err_color
                        ) 
                    embed.set_footer(
                        text = f'Администратор: {ctx.author}',
                        icon_url=ctx.author.avatar_url
                        )
                    if str(ctx.guild.id) in server["reply"]:
                        await ctx.send(embed=embed)
                    else:
                        await ctx.reply(embed=embed, mention_author=False)
    
    @center.error
    async def perm_center_error(self, ctx, error):
        with open('databases/server_settings/mass_db.json', 'r') as f:
            server = json.load(f)
        if isinstance(error, commands.MissingPermissions):
            err = discord.utils.get(self.Bot.emojis, name='cfalse')
            e = discord.Embed(
                title=f"{err} Ошибка!", 
                description=f'Недостаточно прав для выполнения команды. Для просмотра и управленния центром сервера вам нужно право "Администратор".', color=err_color)
            if str(ctx.guild.id) in server["reply"]:
                await ctx.send(embed=e)
            else:
                await ctx.reply(embed=e, mention_author=False)

    @answers.error
    async def perm_answers_error(self, ctx, error):
        with open('databases/server_settings/mass_db.json', 'r') as f:
            server = json.load(f)
        if isinstance(error, commands.MissingPermissions):
            err = discord.utils.get(self.Bot.emojis, name='cfalse')
            e = discord.Embed(
                title=f"{err} Ошибка!", 
                description=f'Недостаточно прав для выполнения команды. Для просмотра и управленния параметрами центра сервера вам нужно право "Администратор".', color=err_color)
            if str(ctx.guild.id) in server["reply"]:
                await ctx.send(embed=e)
            else:
                await ctx.reply(embed=e, mention_author=False)

    @errors.error
    async def perm_errors_error(self, ctx, error):
        with open('databases/server_settings/mass_db.json', 'r') as f:
            server = json.load(f)
        if isinstance(error, commands.MissingPermissions):
            err = discord.utils.get(self.Bot.emojis, name='cfalse')
            e = discord.Embed(
                title=f"{err} Ошибка!", 
                description=f'Недостаточно прав для выполнения команды. Для просмотра и управленния параметрами центра сервера вам нужно право "Администратор".', color=err_color)
            if str(ctx.guild.id) in server["reply"]:
                await ctx.send(embed=e)
            else:
                await ctx.reply(embed=e, mention_author=False)

def setup (Bot):
    Bot.add_cog(utils(Bot))
