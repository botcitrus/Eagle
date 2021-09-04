import discord
from discord.ext import commands
from datetime import datetime
import json
import tracemalloc

tracemalloc.start()

base_color=0x3498db
su_color=0x2ecc71
err_color=0xe74c3c
null_color=discord.Color.from_rgb(47,49,56)

class root(commands.Cog):
    def __init__(self, Bot):
        self.Bot = Bot
               
    ###ECONOMY###
    @commands.command()
    async def money(
        self,
        ctx,
        type = None,
        value: int = None,
        member: discord.Member = None
    ):  
        with open('databases/economy_data/economy_db.json', 'r') as f:
            eco = json.load(f)
        with open('databases/server_settings/mass_db.json', 'r') as f:
            server = json.load(f)
        with open('databases/users_settings/user_db.json', 'r') as f:
            usr = json.load(f)
        tru = discord.utils.get(self.Bot.emojis, name='ctrue')
        err = discord.utils.get(self.Bot.emojis, name='cfalse')
        ### CHEKING
        if str(ctx.author.id) in usr["root"]:
            if not member == None:
                if not str(member.id) in eco["users"]["money"]:
                    eco["users"]["money"][str(member.id)] = 25
                if not str(member.id) in eco["users"]["bank"]:
                    eco["users"]["bank"][str(member.id)] = 25
                if not str(member.id) in eco["users"]["crypto"]["userbalance"]:
                    eco["users"]["crypto"]["userbalance"][str(member.id)] = 0
            else:
                pass
            ### CHEKING
            if type == None and value == None and member == None:
                e = discord.Embed(
                    title=f'{err} Вы не указали парметры:',
                    description='''> Действие 
> Сумма
> Пользователь

`!money <type> <value> <member>`''',
                    color=err_color
                )
                if str(ctx.guild.id) in server["reply"]:
                    await ctx.send(embed=e)
                else:
                    await ctx.reply(embed=e, mention_author=False)
            else:
                if type == '-add':
                    eco["users"]["money"][str(member.id)] += value
                    with open('databases/economy_data/economy_db.json', 'w') as f:
                        json.dump(eco, f)
                    e = discord.Embed(
                        title=f'{tru} Успешно!',
                        description=f'К балансу пользователя {member.mention} добавлено **{value}₽**.',
                        color=su_color
                    )
                    if str(ctx.guild.id) in server["reply"]:
                        await ctx.send(embed=e)
                    else:
                        await ctx.reply(embed=e, mention_author=False)
                if type == '-rem':
                    eco["users"]["money"][str(member.id)] -= value
                    with open('databases/economy_data/economy_db.json', 'w') as f:
                        json.dump(eco, f)
                    e = discord.Embed(
                        title=f'{tru} Успешно!',
                        description=f'С баланса пользователя {member.mention} было списано **{value}₽**.',
                        color=su_color
                    )
                    if str(ctx.guild.id) in server["reply"]:
                        await ctx.send(embed=e)
                    else:
                        await ctx.reply(embed=e, mention_author=False)
                if type == '-fix':
                    eco["users"]["money"][str(member.id)] = value
                    with open('databases/economy_data/economy_db.json', 'w') as f:
                        json.dump(eco, f)
                    e = discord.Embed(
                        title=f'{tru} Успешно!',
                        description=f'Баланс пользователя {member.mention} теперь равен **{value}₽**.',
                        color=su_color
                    )
                    if str(ctx.guild.id) in server["reply"]:
                        await ctx.send(embed=e)
                    else:
                        await ctx.reply(embed=e, mention_author=False)
        else:
            e = discord.Embed(
                title=f'{err} Отказано в доступе!',
                description=f'Получите **root** для управления этой командой.',
                color=err_color
            )
            if str(ctx.guild.id) in server["reply"]:
                await ctx.send(embed=e)
            else:
                await ctx.reply(embed=e, mention_author=False)

    ###EVAL
    @commands.command(
        aliases = ['е', 'e', 'евал']
    )
    async def eval(
        self, 
        ctx, 
        *, 
        code = None
    ):
        with open('databases/server_settings/mass_db.json', 'r') as f:
            server = json.load(f)
        with open('databases/users_settings/user_db.json', 'r') as f:
            usr = json.load(f)
        wt = discord.utils.get(self.Bot.emojis, name='cnone')
        err = discord.utils.get(self.Bot.emojis, name='cfalse')
        if str(ctx.author.id) in usr["root"]:
            if code == None:
                e = discord.Embed(
                    title=f'{wt} Вы не ввели параметр:',
                    description = '''> Код
                    
**Примечание:** 
    Словарь:
        Working bot vaiable: {`b`, `self.bot`, `Bot`, `bot`, `self.client`, `self.Client`, `client`, `Client`}.
        "ctx" contains only `ctx`.''',
                    colour=null_color
                    )
                await ctx.reply(embed=e)
            elif code == 'get':
                e = discord.Embed(
                    title=f'{wt} Мини справка по получению сообщений и каналов:',
                    description = '''
**Сообщение:**\n```py\nmessage = await <ctx/channel/message/etc.>.fetch_message(ID)```

**Канал:**\n```py\nchannel = bot.get_channel(ID)```''',
                    colour=null_color
                    )
                await ctx.reply(embed=e)
            else:
                language_specifiers = ["python", "py"]
                loops = 0
                while code.startswith("`"):
                    code = "".join(list(code)[1:])
                    loops += 1
                    if loops == 3:
                        loops = 0
                        break
                for language_specifier in language_specifiers:
                    if code.startswith(language_specifier):
                        code = code.lstrip(language_specifier)
                while code.endswith("`"):
                    code = "".join(list(code)[0:-1])
                    loops += 1
                    if loops == 3:
                        break
                code = "\n".join(f"    {i}" for i in code.splitlines())
                code = f"async def eval_expr():\n{code}"
                env = {
                    "b": self.Bot,
                    "self.bot": self.Bot,
                    "Bot": self.Bot,
                    "bot": self.Bot,
                    "client": self.Bot,
                    "Client": self.Bot,
                    "ctx": ctx
                }
                env.update(globals())
                try:
                    exec(code, env)
                    eval_expr = env["eval_expr"]
                    result = await eval_expr()
                    if result:
                        await ctx.reply(f'```py\n{result}```')
                except Exception as e:
                    class1 = f"{e.__class__}"
                    class2 = class1[1:]
                    class_result = class2[:-1]
                    error = f"{e}"
                    error_result = str.capitalize(error)
                    embed = discord.Embed(
                        title=f"{err} Ошибка -> `{class_result}`", 
                        color=err_color,
                        timestamp=datetime.utcnow()
                        )
                    embed.add_field(
                        name='Ошибка:',
                        value=f' ```py\n{error_result}``` ',
                        inline=False
                    )
                    embed.add_field(
                        name='Код:',
                        value=f' ```py\n{code}``` ',
                        inline=False
                    )
                    if str(ctx.guild.id) in server["reply"]:
                        await ctx.send(embed=embed)
                    else:
                        await ctx.reply(embed=embed, mention_author=False)
        else:
            e = discord.Embed(
                title=f'{err} Отказано в доступе!',
                description=f'Получите **root** для управления этой командой.',
                color=err_color
            )
            if str(ctx.guild.id) in server["reply"]:
                await ctx.send(embed=e)
            else:
                await ctx.reply(embed=e, mention_author=False)

def setup (Bot):
    Bot.add_cog(root(Bot))
