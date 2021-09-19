import discord
from discord import mentions
from discord.ext import commands
from Cybernator import Paginator
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
        emb1 = discord.Embed(
            title=f'{wt} Центр управления сервером {ctx.guild.name}.',
            color=base_color
        )
        ###REPLIES###
        if not str(ctx.guild.id) in server["reply"]:
            emb1.add_field(
                name='Продвинутые ответы бота:',
                value=f'''Серверное состояние: **{tru} Включены**.''',
                inline=False
            )
        else:
            emb1.add_field(
                name='Продвинутые ответы бота:',
                value=f'''Серверное состояние: **{err} Выключены**.''',
                inline=False
                )
        ###ERRORS###
        if not str(ctx.guild.id) in server["errors"]:
            emb1.add_field(
                name='Оповещения об ошибках:',
                value=f'''Серверное состояние: **{tru} Включены**.''',
                inline=False
                )
        else:
            emb1.add_field(
                name='Оповещения об ошибках:',
                value=f'''Серверное состояние: **{err} Выключены**.''',
                inline=False
                )
        ###MENTIONS###
        if not str(ctx.guild.id) in server["mentions"]:
            emb1.add_field(
                name='Ответы на упоминания:',
                value=f'''Серверное состояние: **{err} Выключены**.''',
                inline=False
                )
        else:
            emb1.add_field(
                name='Ответы на упоминания:',
                value=f'''Серверное состояние: **{err} Выключены**.''',
                inline=False
                )
        emb1.set_thumbnail(url=ctx.guild.icon_url)
        emb1.set_footer(
            text = f'Администратор: {ctx.author} | Страница 1 из 4',
            icon_url=ctx.author.avatar_url
            )
        emb2 = discord.Embed(
            title=f'{wt} Центр управления сервером {ctx.guild.name}.',
            color=base_color
        )
        if not str(ctx.guild.id) in server["reply"]:
            emb2.add_field(
                name='Продвинутые ответы бота:',
                value=f'''Серверное состояние: **{tru} Включены**.
Описание: Во включенном состоянии бот отвечает на ваши сообщения с указанием автора и вызывающего сообщения.
Команды изменения: `!ответы <вкл/выкл>`.''',
                inline=False
                )
        else:
            emb2.add_field(
                name='Продвинутые ответы бота:',
                value=f'''Серверное состояние: **{err} Выключены**.
Описание: Во включенном состоянии бот отвечает на ваши сообщения с указанием автора и вызывающего сообщения.
Команды изменения: `!ответы <вкл/выкл>`.''',
                inline=False
                )
        emb2.set_thumbnail(url=ctx.guild.icon_url)
        emb2.set_footer(
            text = f'Администратор: {ctx.author} | Страница 2 из 4',
            icon_url=ctx.author.avatar_url
            )
        emb3 = discord.Embed(
            title=f'{wt} Центр управления сервером {ctx.guild.name}.',
            color=base_color
        )
        if not str(ctx.guild.id) in server["errors"]:
            emb3.add_field(
                name='Оповещения об ошибках:',
                value=f'''Серверное состояние: **{tru} Включены**.
Описание: Во включенном состоянии бот оповещает Вас об отсутствии неправльно введенной команды.
Команды изменения: `!ошибки <вкл/выкл>`.''',
                inline=False
                )
        else:
            emb3.add_field(
                name='Оповещения об ошибках:',
                value=f'''Серверное состояние: **{err} Выключены**.
Описание: Во включенном состоянии бот оповещает Вас об отсутствии неправльно введенной команды.
Команды изменения: `!ошибки <вкл/выкл>`.''',
                inline=False
                )
        emb3.set_thumbnail(url=ctx.guild.icon_url)
        emb3.set_footer(
            text = f'Администратор: {ctx.author} | Страница 3 из 4',
            icon_url=ctx.author.avatar_url
            )
        emb4 = discord.Embed(
            title=f'{wt} Центр управления сервером {ctx.guild.name}.',
            color=base_color
        )
        if not str(ctx.guild.id) in server["mentions"]:
            emb4.add_field(
                name='Ответы на упоминания:',
                value=f'''Серверное состояние: **{err} Выключены**.
Описание: Во включенном состоянии бот будет реагировать сообщением с навигацией на @упоминание.
Команды изменения: `!упоминание <вкл/выкл>`''',
                inline=False
                )
        else:
            emb4.add_field(
                name='Ответы на упоминания:',
                value=f'''Серверное состояние: **{tru} Включены**.
Описание: Во включенном состоянии бот будет реагировать сообщением с навигацией на @упоминание.
Команды изменения: `!упоминание <вкл/выкл>`''',
                inline=False
                )
        emb4.set_thumbnail(url=ctx.guild.icon_url)
        emb4.set_footer(
            text = f'Администратор: {ctx.author} | Страница 4 из 4',
            icon_url=ctx.author.avatar_url
            )
        embeds = [emb1, emb2, emb3, emb4]
        if str(ctx.guild.id) in server["reply"]:
            message = await ctx.send(embed=emb1)
        else:
            message = await ctx.reply(embed=emb1, mention_author=False)
        page = Paginator(self.Bot, message, only=ctx.author, use_more=False, use_exit=True, footer=False, embeds=embeds) 
        await page.start()
        
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
        aliases = ['упоминание', 'пинг', 'пинги', 'тег', 'теги']
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
                if str(ctx.guild.id) in server["mentions"]:
                    del server["mentions"][str(ctx.guild.id)]
                    with open('databases/server_settings/mass_db.json', 'w') as f:
                        json.dump(server, f)
                    embed = discord.Embed(
                        title=f'{tru} Успешно!',
                        description = "Параметр \"упоминание бота\" успешно выключен для этого сервера.",
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
                        description = "На сервере уже выключен параметр упоминание бота.",
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
                if not str(ctx.guild.id) in server["mentions"]:
                    server["mentions"][str(ctx.guild.id)] = True
                    with open('databases/server_settings/mass_db.json', 'w') as f:
                        json.dump(server, f)
                    embed = discord.Embed(
                        title=f'{tru} Успешно!',
                        description = "Параметр \"упоминание бота\" успешно включен для этого сервера.",
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
                        description = "На сервере уже включен параметр упоминание бота.",
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
    
    ###ERRORS###
    @center.error
    async def perm_center_error(self, ctx, error):
        with open('databases/server_settings/mass_db.json', 'r') as f:
            server = json.load(f)
        if isinstance(error, commands.MissingPermissions):
            err = discord.utils.get(self.Bot.emojis, name='cfalse')
            e = discord.Embed(
                title=f"{err} Ошибка!", 
                description=f'Недостаточно прав для выполнения команды. Для просмотра и управленния центром сервера Вам нужно право "Администратор".', color=err_color)
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
                description=f'Недостаточно прав для выполнения команды. Для просмотра и управленния параметрами центра сервера Вам нужно право "Администратор".', color=err_color)
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
                description=f'Недостаточно прав для выполнения команды. Для просмотра и управленния параметрами центра сервера Вам нужно право "Администратор".', color=err_color)
            if str(ctx.guild.id) in server["reply"]:
                await ctx.send(embed=e)
            else:
                await ctx.reply(embed=e, mention_author=False)

    @mention.error
    async def perm_mentions_error(self, ctx, error):
        with open('databases/server_settings/mass_db.json', 'r') as f:
            server = json.load(f)
        if isinstance(error, commands.MissingPermissions):
            err = discord.utils.get(self.Bot.emojis, name='cfalse')
            e = discord.Embed(
                title=f"{err} Ошибка!", 
                description=f'Недостаточно прав для выполнения команды. Для просмотра и управленния параметрами центра сервера Вам нужно право "Администратор".', color=err_color)
            if str(ctx.guild.id) in server["reply"]:
                await ctx.send(embed=e)
            else:
                await ctx.reply(embed=e, mention_author=False)

def setup (Bot):
    Bot.add_cog(utils(Bot))
