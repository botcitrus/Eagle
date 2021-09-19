from logging import exception
import discord
from discord.ext import commands, tasks
from discord.ext.commands.core import bot_has_guild_permissions
import random
import json

base_color=0x3498db
su_color=0x2ecc71
err_color=0xe74c3c

sale = ['скидка', 'sale', 'распродажа']
oneuse = ['одноразовая', 'one_use']

class economy(commands.Cog):
    def __init__(self, Bot):
        self.Bot = Bot
        self.sender.start()

    @commands.command(
        aliases = ['награда', 'бонус']
    )
    @commands.cooldown(1, 43200, commands.BucketType.user)
    async def reward(
        self,
        ctx
    ):
        with open('databases/economy_data/economy_db.json', 'r') as f:
            eco = json.load(f)
        with open('databases/server_settings/mass_db.json', 'r') as f:
            server = json.load(f)
        tru = discord.utils.get(self.Bot.emojis, name='ctrue')
        ### CHEKING
        if not str(ctx.author.id) in eco["users"]["money"]:
            eco["users"]["money"][str(ctx.author.id)] = 25
        if not str(ctx.author.id) in eco["users"]["bank"]:
            eco["users"]["bank"][str(ctx.author.id)] = 25
        if not str(ctx.author.id) in eco["users"]["crypto"]["userbalance"]:
            eco["users"]["crypto"]["userbalance"][str(ctx.author.id)] = 0
        ### CHEKING
        eco["users"]["money"][str(ctx.author.id)] += 250
        with open('databases/economy_data/economy_db.json', 'w') as f:
            json.dump(eco, f)
        embed = discord.Embed(
            title=f'{tru} Успешно!',
            description=f'''Вы успешно собрали часовую награду.

Получено **250₽** на карманный баланс.
Ваш баланс: **{eco["users"]["money"][str(ctx.author.id)]}₽**''',
            colour=su_color
            )
        embed.set_footer(text=f'Пользователь: {ctx.author}')
        if str(ctx.guild.id) in server["reply"]:
            await ctx.send(embed=embed)
        else:
            await ctx.reply(embed=embed, mention_author=False)
    
    @commands.command(
        aliases = ['работа', 'работать', 'working', 'work_reward', 'зарплата', 'плата']
    )
    @commands.cooldown(1, 43200, commands.BucketType.user)
    async def work(
        self,
        ctx
    ):
        with open('databases/economy_data/economy_db.json', 'r') as f:
            eco = json.load(f)
        with open('databases/server_settings/mass_db.json', 'r') as f:
            server = json.load(f)
        tru = discord.utils.get(self.Bot.emojis, name='ctrue')
        ### CHEKING
        if not str(ctx.author.id) in eco["users"]["money"]:
            eco["users"]["money"][str(ctx.author.id)] = 25
        if not str(ctx.author.id) in eco["users"]["bank"]:
            eco["users"]["bank"][str(ctx.author.id)] = 25
        if not str(ctx.author.id) in eco["users"]["crypto"]["userbalance"]:
            eco["users"]["crypto"]["userbalance"][str(ctx.author.id)] = 0
        ### CHEKING
        profession = random.choice(['стримером', 'фотографом', 'водителем грузовика', 'курьером', 'ловцом змей'])
        moneyvalue = random.choice([500, 600, 650, 700, 750, 800, 850, 900, 1000])
        eco["users"]["money"][str(ctx.author.id)] += moneyvalue
        with open('databases/economy_data/economy_db.json', 'w') as f:
            json.dump(eco, f)
        embed = discord.Embed(
            title=f'{tru} Успешно!',
            description=f'''Вы поработали __{profession}__ и получили **{moneyvalue}₽** на карманный счет.
            
Ваш баланс: **{eco["users"]["money"][str(ctx.author.id)]}₽**''',
            colour=su_color
            )
        embed.set_footer(text=f'Пользователь: {ctx.author}')
        if str(ctx.guild.id) in server["reply"]:
            await ctx.send(embed=embed)
        else:
            await ctx.reply(embed=embed, mention_author=False)

    @commands.command(
        aliases = ['премиум', 'prem', 'прем']
    )
    @commands.cooldown(1, 86400, commands.BucketType.user)
    async def premium(
        self,
        ctx
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
        if not str(ctx.author.id) in eco["users"]["money"]:
            eco["users"]["money"][str(ctx.author.id)] = 25
        if not str(ctx.author.id) in eco["users"]["bank"]:
            eco["users"]["bank"][str(ctx.author.id)] = 25
        if not str(ctx.author.id) in eco["users"]["crypto"]["userbalance"]:
            eco["users"]["crypto"]["userbalance"][str(ctx.author.id)] = 0
        ### CHEKING
        if str(ctx.author.id) in usr["items"]["premium"]:
            eco["users"]["money"][str(ctx.author.id)] += 2500
            eco["users"]["bank"][str(ctx.author.id)] += 250
            with open('databases/economy_data/economy_db.json', 'w') as f:
                json.dump(eco, f)
            embed = discord.Embed(
                title=f'{tru} Успешно!',
                description=f'''Вы успешно собрали премиум-награду.

Получено **2500₽** на карманный баланс **250₽** на банковский счет.
Ваш баланс: **{eco["users"]["money"][str(ctx.author.id)]}₽**''',
                colour=su_color
                )
            embed.set_footer(text=f'Пользователь: {ctx.author}')
            if str(ctx.guild.id) in server["reply"]:
                await ctx.send(embed=embed)
            else:
                await ctx.reply(embed=embed, mention_author=False)
        else:
            embed = discord.Embed(
                title=f'{err} Ошибка!',
                description=f'''На вашем аккаунте нет премиум статуса.''',
                colour=err_color
                )
            embed.set_footer(text=f'Пользователь: {ctx.author}')
            if str(ctx.guild.id) in server["reply"]:
                await ctx.send(embed=embed)
            else:
                await ctx.reply(embed=embed, mention_author=False)        
            
    @commands.command(
        aliases = ['баланс', 'деньги', 'wallet', 'кошелек', 'кошелёк', 'purse', 'бал', 'bal', 'b', 'б']
    )
    async def balance(
        self,
        ctx,
        member: discord.Member = None
    ):
        if member == None:
            member = ctx.author
        with open('databases/economy_data/economy_db.json', 'r') as f:
            eco = json.load(f)
        with open('databases/server_settings/mass_db.json', 'r') as f:
            server = json.load(f)
        bnk = discord.utils.get(self.Bot.emojis, name='bank')
        ### CHEKING
        if not str(member.id) in eco["users"]["money"]:
            eco["users"]["money"][str(member.id)] = 25
        if not str(member.id) in eco["users"]["bank"]:
            eco["users"]["bank"][str(member.id)] = 25
        if not str(member.id) in eco["users"]["crypto"]["userbalance"]:
            eco["users"]["crypto"]["userbalance"][str(member.id)] = 0
        ### CHEKING
        with open('databases/economy_data/economy_db.json', 'w') as f:
            json.dump(eco, f)
        embed = discord.Embed(
            description=f''':money_with_wings: Карманный баланс: **{round(eco["users"]["money"][str(member.id)], 1)}₽**
{bnk} Банковский баланс: **{round(eco["users"]["bank"][str(member.id)], 1)}₽**
:coin: Крипто-баланс: **{eco["users"]["crypto"]["userbalance"][str(member.id)]}EC**

Для пополнения кошелька используйте 
команды **!работа** и **!премиум** для премиум пользователей.''',
            colour=base_color
            )
        embed.set_author(
            icon_url=member.avatar_url,
            name=f'Баланс и состояние {member}',
            url='https://discord.gg/dVbPMUKFnh'
        )
        embed.set_footer(
            text=f'Вызвал: {ctx.author}',
            icon_url=ctx.author.avatar_url
            )
        if str(ctx.guild.id) in server["reply"]:
            await ctx.send(embed=embed)
        else:
            await ctx.reply(embed=embed, mention_author=False) 
    
    @commands.command(
        aliases = ['перевод', 'перевести', 'заплатить', 'pay']
    )
    async def transfer(
        self,
        ctx,
        summ: int = None,
        member: discord.Member = None
    ):
        with open('databases/economy_data/economy_db.json', 'r') as f:
            eco = json.load(f)
        with open('databases/server_settings/mass_db.json', 'r') as f:
            server = json.load(f)
        err = discord.utils.get(self.Bot.emojis, name='cfalse')
        tru = discord.utils.get(self.Bot.emojis, name='ctrue')
        ### CHEKING1
        if not str(ctx.author.id) in eco["users"]["money"]:
            eco["users"]["money"][str(ctx.author.id)] = 25
        if not str(ctx.author.id) in eco["users"]["bank"]:
            eco["users"]["bank"][str(ctx.author.id)] = 25
        if not str(ctx.author.id) in eco["users"]["crypto"]["userbalance"]:
            eco["users"]["crypto"]["userbalance"][str(ctx.author.id)] = 0
        ### CHEKING1
        ### CHEKING2
        if not str(member.id) in eco["users"]["money"]:
            eco["users"]["money"][str(member.id)] = 25
        if not str(member.id) in eco["users"]["bank"]:
            eco["users"]["bank"][str(member.id)] = 25
        if not str(member.id) in eco["users"]["crypto"]["userbalance"]:
            eco["users"]["crypto"]["userbalance"][str(member.id)] = 0
        ### CHEKING2
        if summ == None and member == None:
            embed = discord.Embed(
                title=f'{err} Вы не указали параметр:',
                description = """> Сумма 
> Получатель""",
                colour=err_color
                )
            embed.set_footer(text = f'Пользователь: {ctx.author}')
            if str(ctx.guild.id) in server["reply"]:
                await ctx.send(embed=embed)
            else:
                await ctx.reply(embed=embed, mention_author=False)
        if not summ == None and member == None:
            embed = discord.Embed(
                title=f'{err} Вы не указали параметр:',
                description = "> Получатель",
                colour=err_color
                )
            embed.set_footer(text = f'Пользователь: {ctx.author}')
            if str(ctx.guild.id) in server["reply"]:
                await ctx.send(embed=embed)
            else:
                await ctx.reply(embed=embed, mention_author=False)
        elif member == ctx.author:
            embed = discord.Embed(
                title=f'{err} Ошибка!',
                description = "Вы не можете совершить перевод самому себе.",
                colour=err_color
                )
            embed.set_footer(text = f'Пользователь: {ctx.author}')
            if str(ctx.guild.id) in server["reply"]:
                await ctx.send(embed=embed)
            else:
                await ctx.reply(embed=embed, mention_author=False)
        elif summ > eco["users"]["money"][str(ctx.author.id)]:
            embed = discord.Embed(
                title=f'{err} Ошибка!',
                description = "На Вашем краманном балансе недостаточно средств для совершения перевода в банк.",
                colour=err_color
                )
            embed.set_footer(text = f'Пользователь: {ctx.author}')
            if str(ctx.guild.id) in server["reply"]:
                await ctx.send(embed=embed)
            else:
                await ctx.reply(embed=embed, mention_author=False)
        elif summ < 1 or summ > 1000000000:
            embed = discord.Embed(
                title=f'{err} Ошибка!',
                description = "Вы не можете перевести сумму меньше 1₽ и больше 1.000.000.000₽",
                colour=err_color
                )
            embed.set_footer(text = f'Пользователь: {ctx.author}')
            if str(ctx.guild.id) in server["reply"]:
                await ctx.send(embed=embed)
            else:
                await ctx.reply(embed=embed, mention_author=False)
        else:
            eco["users"]["money"][str(ctx.author.id)] -= summ
            eco["users"]["money"][str(member.id)] += round(summ*0.99, 1)
            with open('databases/economy_data/economy_db.json', 'w') as f:
                json.dump(eco, f)
            embed = discord.Embed(
                title=f'{tru} Успешно!',
                description = f"Совершен перевод {member.mention} на сумму **{round(summ*0.99, 1)}₽**.",
                colour=su_color
                )
            embed.set_footer(text = f'Пользователь: {ctx.author}')
            if str(ctx.guild.id) in server["reply"]:
                await ctx.send(embed=embed)
            else:
                await ctx.reply(embed=embed, mention_author=False)
    
    @commands.command(
        aliases = ['депозит', 'в_банк', 'вбанк']
    )
    async def deposit(
        self,
        ctx,
        summ: int = None
    ):
        with open('databases/economy_data/economy_db.json', 'r') as f:
            eco = json.load(f)
        with open('databases/server_settings/mass_db.json', 'r') as f:
            server = json.load(f)
        tru = discord.utils.get(self.Bot.emojis, name='ctrue')
        err = discord.utils.get(self.Bot.emojis, name='cfalse')
        ### CHEKING1
        if not str(ctx.author.id) in eco["users"]["money"]:
            eco["users"]["money"][str(ctx.author.id)] = 25
        if not str(ctx.author.id) in eco["users"]["bank"]:
            eco["users"]["bank"][str(ctx.author.id)] = 25
        if not str(ctx.author.id) in eco["users"]["crypto"]["userbalance"]:
            eco["users"]["crypto"]["userbalance"][str(ctx.author.id)] = 0
        ### CHEKING1
        if summ == None:
            embed = discord.Embed(
                title=f'{err} Вы не указали параметр:',
                description = "> Сумма",
                colour=err_color
                )
            embed.set_footer(text = f'Пользователь: {ctx.author}')
            if str(ctx.guild.id) in server["reply"]:
                await ctx.send(embed=embed)
            else:
                await ctx.reply(embed=embed, mention_author=False)
        elif summ < 1 or summ > 1000000000:
            embed = discord.Embed(
                title=f'{err} Ошибка!',
                description = "Вы не можете перевести сумму меньше 1₽ и больше 1.000.000.000₽",
                colour=err_color
                )
            embed.set_footer(text = f'Пользователь: {ctx.author}')
            if str(ctx.guild.id) in server["reply"]:
                await ctx.send(embed=embed)
            else:
                await ctx.reply(embed=embed, mention_author=False)
        elif summ > eco["users"]["money"][str(ctx.author.id)]:
            embed = discord.Embed(
                title=f'{err} Ошибка!',
                description = "На Вашем краманном балансе недостаточно средств для совершения перевода в банк.",
                colour=err_color
                )
            embed.set_footer(text = f'Пользователь: {ctx.author}')
            if str(ctx.guild.id) in server["reply"]:
                await ctx.send(embed=embed)
            else:
                await ctx.reply(embed=embed, mention_author=False)
        else:
            eco["users"]["money"][str(ctx.author.id)] -= summ
            eco["users"]["bank"][str(ctx.author.id)] += summ
            with open('databases/economy_data/economy_db.json', 'w') as f:
                json.dump(eco, f)
            embed = discord.Embed(
                title=f'{tru} Успешно!',
                description = f"Переведено **{(summ)}₽** на Ваш банковский счёт.",
                colour=su_color
                )
            embed.set_footer(text = f'Пользователь: {ctx.author}')
            if str(ctx.guild.id) in server["reply"]:
                await ctx.send(embed=embed)
            else:
                await ctx.reply(embed=embed, mention_author=False)

    @commands.command(
        aliases = ['снять', 'обналичить']
    )
    async def withdraw(
        self,
        ctx,
        summ: int = None
    ):
        with open('databases/economy_data/economy_db.json', 'r') as f:
            eco = json.load(f)
        with open('databases/server_settings/mass_db.json', 'r') as f:
            server = json.load(f)
        err = discord.utils.get(self.Bot.emojis, name='cfalse')
        tru = discord.utils.get(self.Bot.emojis, name='ctrue')
        ### CHEKING1
        if not str(ctx.author.id) in eco["users"]["money"]:
            eco["users"]["money"][str(ctx.author.id)] = 25
        if not str(ctx.author.id) in eco["users"]["bank"]:
            eco["users"]["bank"][str(ctx.author.id)] = 25
        if not str(ctx.author.id) in eco["users"]["crypto"]["userbalance"]:
            eco["users"]["crypto"]["userbalance"][str(ctx.author.id)] = 0
        ### CHEKING1
        if summ == None:
            embed = discord.Embed(
                title=f'{err} Вы не указали параметр:',
                description = "> Сумма",
                colour=err_color
                )
            embed.set_footer(text = f'Пользователь: {ctx.author}')
            if str(ctx.guild.id) in server["reply"]:
                await ctx.send(embed=embed)
            else:
                await ctx.reply(embed=embed, mention_author=False)
        elif summ < 1 or summ > 1000000000:
            embed = discord.Embed(
                title=f'{err} Ошибка!',
                description = "Вы не можете перевести сумму меньше 1₽ и больше 1.000.000.000₽",
                colour=err_color
                )
            embed.set_footer(text = f'Пользователь: {ctx.author}')
            if str(ctx.guild.id) in server["reply"]:
                await ctx.send(embed=embed)
            else:
                await ctx.reply(embed=embed, mention_author=False)
        elif summ > eco["users"]["bank"][str(ctx.author.id)]:
            embed = discord.Embed(
                title=f'{err} Ошибка!',
                description = "На Вашем банковском счёте недостаточно средств для совершения обналичивания.",
                colour=err_color
                )
            embed.set_footer(text = f'Пользователь: {ctx.author}')
            if str(ctx.guild.id) in server["reply"]:
                await ctx.send(embed=embed)
            else:
                await ctx.reply(embed=embed, mention_author=False)
        else:
            eco["users"]["money"][str(ctx.author.id)] += summ
            eco["users"]["bank"][str(ctx.author.id)] -= summ
            with open('databases/economy_data/economy_db.json', 'w') as f:
                json.dump(eco, f)
            embed = discord.Embed(
                title=f'{tru} Успешно!',
                description = f"**{summ}₽** снято на Ваш карманный кошелек.",
                colour=su_color
                )
            embed.set_footer(text = f'Пользователь: {ctx.author}')
            if str(ctx.guild.id) in server["reply"]:
                await ctx.send(embed=embed)
            else:
                await ctx.reply(embed=embed, mention_author=False)

    @commands.command(
        aliases = ['кено', 'fifteen', 'пятнадцать']
    )
    async def keno(
        self,
        ctx,
        type: int = None,
        summ: int = None
    ):
        with open('databases/economy_data/economy_db.json', 'r') as f:
            eco = json.load(f)
        with open('databases/server_settings/mass_db.json', 'r') as f:
            server = json.load(f)
        err = discord.utils.get(self.Bot.emojis, name='cfalse')
        tru = discord.utils.get(self.Bot.emojis, name='ctrue')
        ### CHEKING1
        if not str(ctx.author.id) in eco["users"]["money"]:
            eco["users"]["money"][str(ctx.author.id)] = 25
        if not str(ctx.author.id) in eco["users"]["bank"]:
            eco["users"]["bank"][str(ctx.author.id)] = 25
        if not str(ctx.author.id) in eco["users"]["crypto"]["userbalance"]:
            eco["users"]["crypto"]["userbalance"][str(ctx.author.id)] = 0
        ### CHEKING1
        if type == None and summ == None:
            embed = discord.Embed(
                title=f'{err} Вы не указали параметр:',
                description = """> Число
> Сумма""",
                colour=err_color
                )
            embed.set_footer(text = f'Пользователь: {ctx.author}')
            if str(ctx.guild.id) in server["reply"]:
                await ctx.send(embed=embed)
            else:
                await ctx.reply(embed=embed, mention_author=False)
        elif not type == None and summ == None:
            embed = discord.Embed(
                title=f'{err} Вы не указали параметр:',
                description = "> Сумма",
                colour=err_color
                )
            embed.set_footer(text = f'Пользователь: {ctx.author}')
            if str(ctx.guild.id) in server["reply"]:
                await ctx.send(embed=embed)
            else:
                await ctx.reply(embed=embed, mention_author=False)
        elif summ < 1 or summ > 1000000000:
            embed = discord.Embed(
                title=f'{err} Ошибка!',
                description = "Вы не можете поставить сумму меньше 1₽ и больше 1.000.000.000₽",
                colour=err_color
                )
            embed.set_footer(text = f'Пользователь: {ctx.author}')
            if str(ctx.guild.id) in server["reply"]:
                await ctx.send(embed=embed)
            else:
                await ctx.reply(embed=embed, mention_author=False)
        elif summ > eco["users"]["money"][str(ctx.author.id)]:
            embed = discord.Embed(
                title=f'{err} Ошибка!',
                description = "На Вашем краманном балансе недостаточно средств для совершения перевода в банк.",
                colour=err_color
                )
            embed.set_footer(text = f'Пользователь: {ctx.author}')
            if str(ctx.guild.id) in server["reply"]:
                await ctx.send(embed=embed)
            else:
                await ctx.reply(embed=embed, mention_author=False)
        elif type < 1 or type > 10:
            embed = discord.Embed(
                title=f'{err} Ошибка!',
                description = "Неправильно введено значение угадываемого числа. Вы можете ввсети число не меньше 0 и не больше 10.",
                colour=err_color
                )
            embed.set_footer(text = f'Пользователь: {ctx.author}')
            if str(ctx.guild.id) in server["reply"]:
                await ctx.send(embed=embed)
            else:
                await ctx.reply(embed=embed, mention_author=False)
        else:
            hitnum = random.randint(1, 10)
            if type == hitnum:
                eco["users"]["money"][str(ctx.author.id)] += round(summ*2)
                with open('databases/economy_data/economy_db.json', 'w') as f:
                    json.dump(eco, f)
                embed = discord.Embed(
                    title=f'{tru} Вы точно угадали число!',
                    description = f"""Ваш выигрыш составляет: **+{round(summ*2)}₽** (Коофициент Х2)
На барабане число: **{hitnum}**.

:money_with_wings: Карманный баланс: **{eco["users"]["money"][str(ctx.author.id)]}₽**""",
                    colour=su_color
                    )
                embed.set_footer(text = f'Пользователь: {ctx.author}')
                if str(ctx.guild.id) in server["reply"]:
                    await ctx.send(embed=embed)
                else:
                    await ctx.reply(embed=embed, mention_author=False)
            elif type + 1 == hitnum or type - 1 == hitnum or type + 2 == hitnum or type - 2 == hitnum:
                eco["users"]["money"][str(ctx.author.id)] += round(summ*1.25)
                with open('databases/economy_data/economy_db.json', 'w') as f:
                    json.dump(eco, f)
                embed = discord.Embed(
                    title=f'{tru} Вы почти угадали число!',
                    description = f"""Ваш выигрыш составляет: **+{round(summ*1.25)}₽** (Коофициент Х1.25)
На барабане число: **{hitnum}**.

:money_with_wings: Карманный баланс: **{eco["users"]["money"][str(ctx.author.id)]}₽**""",
                    colour=su_color
                    )
                embed.set_footer(text = f'Пользователь: {ctx.author}')
                if str(ctx.guild.id) in server["reply"]:
                    await ctx.send(embed=embed)
                else:
                    await ctx.reply(embed=embed, mention_author=False)
            else:
                eco["users"]["money"][str(ctx.author.id)] -= summ
                with open('databases/economy_data/economy_db.json', 'w') as f:
                    json.dump(eco, f)
                embed = discord.Embed(
                    title=f'{err} Вы не угадали число.',
                    description = f"""Итого: **-{summ}₽**
На барабане число: **{hitnum}**.

:money_with_wings: Карманный баланс: **{eco["users"]["money"][str(ctx.author.id)]}₽**""",
                    colour=err_color
                    )
                embed.set_footer(text = f'Пользователь: {ctx.author}')
                if str(ctx.guild.id) in server["reply"]:
                    await ctx.send(embed=embed)
                else:
                    await ctx.reply(embed=embed, mention_author=False)
    
    @commands.command(
        aliases = ['крипто', 'криптовалюта', 'крипта', 'есоин', 'ecoin']
    )
    async def crypto(
        self,
        ctx
    ):
        with open('databases/economy_data/economy_db.json', 'r') as f:
            eco = json.load(f)
        with open('databases/server_settings/mass_db.json', 'r') as f:
            server = json.load(f)
        err = discord.utils.get(self.Bot.emojis, name='cfalse')
        ### CHEKING1
        if not str(ctx.author.id) in eco["users"]["money"]:
            eco["users"]["money"][str(ctx.author.id)] = 25
        if not str(ctx.author.id) in eco["users"]["bank"]:
            eco["users"]["bank"][str(ctx.author.id)] = 25
        if not str(ctx.author.id) in eco["users"]["crypto"]["userbalance"]:
            eco["users"]["crypto"]["userbalance"][str(ctx.author.id)] = 0
        ### CHEKING1
        if eco["users"]["crypto"]["cryptovalue"] > 1000000:
            mark = discord.utils.get(self.Bot.emojis, name='idle')
            text = "Тяжелодоступные"
        elif eco["users"]["crypto"]["cryptovalue"] < 1000000:
            mark = discord.utils.get(self.Bot.emojis, name='online1')
            text = "Легкодоступные"
        embed = discord.Embed(
            title=f'Курс, цена и состояние криптовалюты Eternal EagleCoin.',
            description = f"""Цена за 1 единицу актива: **{eco["users"]["crypto"]["cryptovalue"]}₽**
Состояние активов: {mark} **{text}**.
Ваш крипто-баланс: **{eco["users"]["crypto"]["userbalance"][str(ctx.author.id)]}EC**

Для операции активами использвуйте команды **!крипто купить**, **!крипто продать**, указывая сумму для покупки активов или кол-во активов для их продажи.""",
            colour=base_color
            )
        embed.set_footer(text = f'Пользователь: {ctx.author}')
        if str(ctx.guild.id) in server["reply"]:
            await ctx.send(embed=embed)
        else:
            await ctx.reply(embed=embed, mention_author=False)

    @commands.command(
        aliases = ['крипто_купить', 'к_купить', 'крипто_к']
    )
    async def crypto_buy(
        self,
        ctx,
        var: int = None
    ):
        with open('databases/economy_data/economy_db.json', 'r') as f:
            eco = json.load(f)
        with open('databases/server_settings/mass_db.json', 'r') as f:
            server = json.load(f)
        err = discord.utils.get(self.Bot.emojis, name='cfalse')
        tru = discord.utils.get(self.Bot.emojis, name='ctrue')
        ### CHEKING1
        if not str(ctx.author.id) in eco["users"]["money"]:
            eco["users"]["money"][str(ctx.author.id)] = 25
        if not str(ctx.author.id) in eco["users"]["bank"]:
            eco["users"]["bank"][str(ctx.author.id)] = 25
        if not str(ctx.author.id) in eco["users"]["crypto"]["userbalance"]:
            eco["users"]["crypto"]["userbalance"][str(ctx.author.id)] = 0
        ### CHEKING1
        if var == None:
            embed = discord.Embed(
                title=f'{err} Вы не указали параметр:',
                description = "> Сумма",
                colour=err_color
                )
            embed.set_footer(text = f'Пользователь: {ctx.author}')
            if str(ctx.guild.id) in server["reply"]:
                await ctx.send(embed=embed)
            else:
                await ctx.reply(embed=embed, mention_author=False)
        elif var < 1 or var > 1000000000:
            embed = discord.Embed(
                title=f'{err} Ошибка!',
                description = "Вы не можете вложить сумму меньше 1₽ и больше 1.000.000.000₽",
                colour=err_color
                )
            embed.set_footer(text = f'Пользователь: {ctx.author}')
            if str(ctx.guild.id) in server["reply"]:
                await ctx.send(embed=embed)
            else:
                await ctx.reply(embed=embed, mention_author=False)
        
        elif var > eco["users"]["money"][str(ctx.author.id)]:
            embed = discord.Embed(
                title=f'{err} Ошибка!',
                description = "На Вашем краманном балансе недостаточно средств для совершения совершения операции.",
                colour=err_color
                )
            embed.set_footer(text = f'Пользователь: {ctx.author}')
            if str(ctx.guild.id) in server["reply"]:
                await ctx.send(embed=embed)
            else:
                await ctx.reply(embed=embed, mention_author=False)
        else:
            eco["users"]["money"][str(ctx.author.id)] -= var
            eco["users"]["crypto"]["userbalance"][str(ctx.author.id)] += var/eco["users"]["crypto"]["cryptovalue"]
            with open('databases/economy_data/economy_db.json', 'w') as f:
                json.dump(eco, f)
            embed = discord.Embed(
                title=f'{tru} Успешно!',
                description = f'Вы успешно приобрели **{eco["users"]["crypto"]["userbalance"][str(ctx.author.id)]}** активов EC на сумму {var}₽',
                colour=su_color
                )
            embed.set_footer(text = f'Пользователь: {ctx.author}')
            if str(ctx.guild.id) in server["reply"]:
                await ctx.send(embed=embed)
            else:
                await ctx.reply(embed=embed, mention_author=False)
    
    @commands.command(
        aliases = ['крипто_продать', 'крипто_п', 'к_продать']
    )
    async def crypto_sell(
        self,
        ctx,
        var: float = None
    ):
        with open('databases/economy_data/economy_db.json', 'r') as f:
            eco = json.load(f)
        with open('databases/server_settings/mass_db.json', 'r') as f:
            server = json.load(f)
        err = discord.utils.get(self.Bot.emojis, name='cfalse')
        tru = discord.utils.get(self.Bot.emojis, name='ctrue')
        ### CHEKING1
        if not str(ctx.author.id) in eco["users"]["money"]:
            eco["users"]["money"][str(ctx.author.id)] = 25
        if not str(ctx.author.id) in eco["users"]["bank"]:
            eco["users"]["bank"][str(ctx.author.id)] = 25
        if not str(ctx.author.id) in eco["users"]["crypto"]["userbalance"]:
            eco["users"]["crypto"]["userbalance"][str(ctx.author.id)] = 0
        ### CHEKING1
        if var == None:
            embed = discord.Embed(
                title=f'{err} Вы не указали параметр:',
                description = "> Кол-во активов",
                colour=err_color
                )
            embed.set_footer(text = f'Пользователь: {ctx.author}')
            if str(ctx.guild.id) in server["reply"]:
                await ctx.send(embed=embed)
            else:
                await ctx.reply(embed=embed, mention_author=False)
        elif var < 0 or var > 10000:
            embed = discord.Embed(
                title=f'{err} Ошибка!',
                description = "Вы не можете продать число активов меньше 0 и больше 10000.",
                colour=err_color
                )
            embed.set_footer(text = f'Пользователь: {ctx.author}')
            if str(ctx.guild.id) in server["reply"]:
                await ctx.send(embed=embed)
            else:
                await ctx.reply(embed=embed, mention_author=False)
        elif var > eco["users"]["crypto"]["userbalance"][str(ctx.author.id)]:
            embed = discord.Embed(
                title=f'{err} Ошибка!',
                description = "На Вашем краманном крипто-балансе недостаточно активов для совершения совершения операции.",
                colour=err_color
                )
            embed.set_footer(text = f'Пользователь: {ctx.author}')
            if str(ctx.guild.id) in server["reply"]:
                await ctx.send(embed=embed)
            else:
                await ctx.reply(embed=embed, mention_author=False)
        else:
            eco["users"]["crypto"]["userbalance"][str(ctx.author.id)] -= var
            eco["users"]["money"][str(ctx.author.id)] += round(var*eco["users"]["crypto"]["cryptovalue"], 1)
            with open('databases/economy_data/economy_db.json', 'w') as f:
                json.dump(eco, f)
            embed = discord.Embed(
                title=f'{tru} Успешно!',
                description = f'Вы успешно продали {var} активов EC на сумму **{round(var*eco["users"]["crypto"]["cryptovalue"], 1)}₽**',
                colour=su_color
                )
            embed.set_footer(text = f'Пользователь: {ctx.author}')
            if str(ctx.guild.id) in server["reply"]:
                await ctx.send(embed=embed)
            else:
                await ctx.reply(embed=embed, mention_author=False)

    @commands.command(
        aliases = ['роль+', 'лот+', 'role+', 'lot+']
    )
    @commands.has_guild_permissions(administrator=True)
    async def shop_addrole(
        self, 
        ctx, 
        role: discord.Role = None,
        cost: int = None,
        tp = None,
        salevar: int = None
        ):
        with open('databases/economy_data/economy_db.json', 'r') as f:
            eco = json.load(f)
        with open('databases/server_settings/mass_db.json', 'r') as f:
            server = json.load(f)
        ### CHEKING1
        if not str(ctx.guild.id) in eco["tech"]["shop"]["base"]:
            eco["tech"]["shop"]["base"][str(ctx.guild.id)] = {}
        if not str(ctx.guild.id) in eco["tech"]["shop"]["sale"]["roleid"]:
            eco["tech"]["shop"]["sale"]["roleid"][str(ctx.guild.id)] = {}
        if not str(ctx.guild.id) in eco["tech"]["shop"]["sale"]["salevalue"]:
            eco["tech"]["shop"]["sale"]["salevalue"][str(ctx.guild.id)] = {}
        if not str(ctx.guild.id) in eco["tech"]["shop"]["oneuse"]:
            eco["tech"]["shop"]["oneuse"][str(ctx.guild.id)] = {}
        ### CHEKING1
        err = discord.utils.get(self.Bot.emojis, name='cfalse')
        tru = discord.utils.get(self.Bot.emojis, name='ctrue')
        if role == None and cost == None and tp == None:
            embed = discord.Embed(
                title=f'{err} Вы не указали параметр:',
                description = """> Роль
> Сумма
> Тип лота [Опционально]
> Скидка [Опционально]""",
                colour=err_color
                )
            embed.set_footer(text = f'Пользователь: {ctx.author}')
            if str(ctx.guild.id) in server["reply"]:
                await ctx.send(embed=embed)
            else:
                await ctx.reply(embed=embed, mention_author=False)
        elif not role == None and cost == None and tp == None:
            embed = discord.Embed(
                title=f'{err} Вы не указали параметр:',
                description = """> Сумма
> Тип лота [Опционально]
> Скидка [Опционально]""",
                colour=err_color
                )
            embed.set_footer(text = f'Пользователь: {ctx.author}')
            if str(ctx.guild.id) in server["reply"]:
                await ctx.send(embed=embed)
            else:
                await ctx.reply(embed=embed, mention_author=False)
        else:
            if cost < 0 or cost > 100000000:
                embed = discord.Embed(
                    title=f'{err} Ошибка!',
                    description = "Вы не можете ввести стоимость роли меньше 0₽ и больше 100.000.000₽.",
                    colour=err_color
                    )
                embed.set_footer(text = f'Пользователь: {ctx.author}')
                if str(ctx.guild.id) in server["reply"]:
                    await ctx.send(embed=embed)
                else:
                    await ctx.reply(embed=embed, mention_author=False)
            else:
                if bot_has_guild_permissions(manage_roles=True):
                    if tp == None:
                        if not str(role.id) in eco["tech"]["shop"]["sale"]["roleid"][str(ctx.guild.id)] and not str(role.id) in eco["tech"]["shop"]["base"][str(ctx.guild.id)] and not str(role.id) in eco["tech"]["shop"]["oneuse"][str(ctx.guild.id)]:
                            eco["tech"]["shop"]["base"][str(ctx.guild.id)][str(role.id)] = cost
                            with open('databases/economy_data/economy_db.json', 'w') as f:
                                json.dump(eco, f)
                            embed = discord.Embed(
                                title=f'{tru} Успешно!',
                                description = f'Роль {role.mention} стоимостью **{cost}** добавлена в __обыкновенный__ лот.',
                                colour=su_color
                                )
                            embed.set_footer(text = f'Добавлено: {ctx.author}')
                            if str(ctx.guild.id) in server["reply"]:
                                await ctx.send(embed=embed)
                            else:
                                await ctx.reply(embed=embed, mention_author=False)
                        else:
                            embed = discord.Embed(
                                title=f'{err} Ошибка!',
                                description = f"Данная роль ({role.mention}) уже присутствует в магазине.",
                                colour=err_color
                                )
                            if str(ctx.guild.id) in server["reply"]:
                                await ctx.send(embed=embed)
                            else:
                                await ctx.reply(embed=embed, mention_author=False)
                    elif tp in sale:
                        if salevar < 0 or salevar > 100:
                            embed = discord.Embed(
                                title=f'{err} Ошибка!',
                                description = "Размер скидки не может быть меньше 0 и больше 100.",
                                colour=err_color
                                )
                            if str(ctx.guild.id) in server["reply"]:
                                await ctx.send(embed=embed)
                            else:
                                await ctx.reply(embed=embed, mention_author=False)
                        else:
                            if not str(role.id) in eco["tech"]["shop"]["sale"]["roleid"][str(ctx.guild.id)] and not str(role.id) in eco["tech"]["shop"]["base"][str(ctx.guild.id)] and not str(role.id) in eco["tech"]["shop"]["oneuse"][str(ctx.guild.id)]:
                                eco["tech"]["shop"]["sale"]["roleid"][str(ctx.guild.id)][str(role.id)] = cost
                                eco["tech"]["shop"]["sale"]["salevalue"][str(ctx.guild.id)][str(role.id)] = salevar
                                with open('databases/economy_data/economy_db.json', 'w') as f:
                                    json.dump(eco, f)
                                embed = discord.Embed(
                                    title=f'{tru} Успешно!',
                                    description = f'Роль {role.mention} стоимостью **{cost}** добавлена в __скидочный__ лот.',
                                    colour=su_color
                                    )
                                embed.set_footer(text = f'Добавлено: {ctx.author}')
                                if str(ctx.guild.id) in server["reply"]:
                                    await ctx.send(embed=embed)
                                else:
                                    await ctx.reply(embed=embed, mention_author=False)
                            else:
                                embed = discord.Embed(
                                    title=f'{err} Ошибка!',
                                    description = f"Данная роль ({role.mention}) уже присутствует в магазине.",
                                    colour=err_color
                                    )
                                if str(ctx.guild.id) in server["reply"]:
                                    await ctx.send(embed=embed)
                                else:
                                    await ctx.reply(embed=embed, mention_author=False)
                    elif tp in oneuse:
                        if not str(role.id) in eco["tech"]["shop"]["sale"]["roleid"][str(ctx.guild.id)] and not str(role.id) in eco["tech"]["shop"]["base"][str(ctx.guild.id)] and not str(role.id) in eco["tech"]["shop"]["oneuse"][str(ctx.guild.id)]:
                            eco["tech"]["shop"]["oneuse"][str(ctx.guild.id)][str(role.id)] = cost
                            with open('databases/economy_data/economy_db.json', 'w') as f:
                                json.dump(eco, f)
                            embed = discord.Embed(
                                title=f'{tru} Успешно!',
                                description = f'Роль {role.mention} стоимостью **{cost}** добавлена в __одноразовый__ лот.',
                                colour=su_color
                                )
                            embed.set_footer(text = f'Добавлено: {ctx.author}')
                            if str(ctx.guild.id) in server["reply"]:
                                await ctx.send(embed=embed)
                            else:
                                await ctx.reply(embed=embed, mention_author=False)
                        else:
                            embed = discord.Embed(
                                title=f'{err} Ошибка!',
                                description = f"Данная роль ({role.mention}) уже присутствует в магазине.",
                                colour=err_color
                                )
                            if str(ctx.guild.id) in server["reply"]:
                                await ctx.send(embed=embed)
                            else:
                                await ctx.reply(embed=embed, mention_author=False)
                else:
                    e = discord.Embed(
                        title=f'{err} Невозможно совершить операцию',
                        description=f'У меня нет права "Управлять ролями" на этом сервере. Без него я не смогу выдавать роли при покупке. Для разрешения проблемы выдайте мне данное право или обратитесь к создателю сервера.',
                        color=err_color
                    )
                    if str(ctx.guild.id) in server["reply"]:
                        await ctx.send(embed=e)
                    else:
                        await ctx.reply(embed=e, mention_author=False)
                                                
    @commands.command(
        aliases = ['роль-', 'лот-', 'role-', 'lot-']
    )
    @commands.has_guild_permissions(administrator=True)
    async def shop_remrole(
        self, 
        ctx, 
        role: discord.Role = None
        ):
        with open('databases/economy_data/economy_db.json', 'r') as f:
            eco = json.load(f)
        with open('databases/server_settings/mass_db.json', 'r') as f:
            server = json.load(f)
        ### CHEKING1
        if not str(ctx.guild.id) in eco["tech"]["shop"]["base"]:
            eco["tech"]["shop"]["base"][str(ctx.guild.id)] = {}
        if not str(ctx.guild.id) in eco["tech"]["shop"]["sale"]["roleid"]:
            eco["tech"]["shop"]["sale"]["roleid"][str(ctx.guild.id)] = {}
        if not str(ctx.guild.id) in eco["tech"]["shop"]["sale"]["salevalue"]:
            eco["tech"]["shop"]["sale"]["salevalue"][str(ctx.guild.id)] = {}
        if not str(ctx.guild.id) in eco["tech"]["shop"]["oneuse"]:
            eco["tech"]["shop"]["oneuse"][str(ctx.guild.id)] = {}
        ### CHEKING1
        err = discord.utils.get(self.Bot.emojis, name='cfalse')
        tru = discord.utils.get(self.Bot.emojis, name='ctrue')
        if role == None:
            embed = discord.Embed(
                title=f'{err} Вы не указали параметр:',
                description = "> Роль",
                colour=err_color
                )
            embed.set_footer(text = f'Пользователь: {ctx.author}')
            if str(ctx.guild.id) in server["reply"]:
                await ctx.send(embed=embed)
            else:
                await ctx.reply(embed=embed, mention_author=False)
        else:
            if bot_has_guild_permissions(manage_roles=True):
                ###BASE###
                if str(role.id) in eco["tech"]["shop"]["base"][str(ctx.guild.id)] or str(role.id) in eco["tech"]["shop"]["sale"]["roleid"][str(ctx.guild.id)] or str(role.id) in eco["tech"]["shop"]["oneuse"][str(ctx.guild.id)]:
                    if str(role.id) in eco["tech"]["shop"]["base"][str(ctx.guild.id)]:
                        del eco["tech"]["shop"]["base"][str(ctx.guild.id)][str(role.id)] 
                        with open('databases/economy_data/economy_db.json', 'w') as f:
                            json.dump(eco, f)
                        embed = discord.Embed(
                            title=f'{tru} Успешно!',
                            description = f'Роль {role.mention} удалена из __обыкновенного__ лота.',
                            colour=su_color
                            )
                        embed.set_footer(text = f'Удалено: {ctx.author}')
                        if str(ctx.guild.id) in server["reply"]:
                            await ctx.send(embed=embed)
                        else:
                            await ctx.reply(embed=embed, mention_author=False)
                    else:
                        pass
                    ###SALE###
                    if str(role.id) in eco["tech"]["shop"]["sale"]["roleid"][str(ctx.guild.id)]:              
                        del eco["tech"]["shop"]["sale"]["roleid"][str(ctx.guild.id)][str(role.id)]
                        del eco["tech"]["shop"]["sale"]["salevalue"][str(ctx.guild.id)][str(role.id)]
                        with open('databases/economy_data/economy_db.json', 'w') as f:
                            json.dump(eco, f)
                        embed = discord.Embed(
                            title=f'{tru} Успешно!',
                            description = f'Роль {role.mention} убрана из __скидочного__ лотa.',
                            colour=su_color
                            )
                        embed.set_footer(text = f'Добавлено: {ctx.author}')
                        if str(ctx.guild.id) in server["reply"]:
                            await ctx.send(embed=embed)
                        else:
                            await ctx.reply(embed=embed, mention_author=False)
                    else:
                        pass
                    ###ONEUSE###
                    if str(role.id) in eco["tech"]["shop"]["oneuse"][str(ctx.guild.id)]:
                        del eco["tech"]["shop"]["oneuse"][str(ctx.guild.id)][str(role.id)]
                        with open('databases/economy_data/economy_db.json', 'w') as f:
                            json.dump(eco, f)
                        embed = discord.Embed(
                            title=f'{tru} Успешно!',
                            description = f'Роль {role.mention} ',
                            colour=su_color
                            )
                        embed.set_footer(text = f'Добавлено: {ctx.author}')
                        if str(ctx.guild.id) in server["reply"]:
                            await ctx.send(embed=embed)
                        else:
                            await ctx.reply(embed=embed, mention_author=False)
                    else:
                        pass
                else:
                    embed = discord.Embed(
                        title=f'{err} Ошибка!',
                        description = f"Данной роли ({role.mention}) нет в магазине.",
                        colour=err_color
                        )
                    if str(ctx.guild.id) in server["reply"]:
                        await ctx.send(embed=embed)
                    else:
                        await ctx.reply(embed=embed, mention_author=False)
            else:
                e = discord.Embed(
                    title=f'{err} Невозможно совершить операцию',
                    description=f'У меня нет права "Управлять ролями" на этом сервере. Без него я не смогу выдавать роли при покупке. Для разрешения проблемы выдайте мне данное право или обратитесь к создателю сервера.',
                    color=err_color
                )
                if str(ctx.guild.id) in server["reply"]:
                    await ctx.send(embed=e)
                else:
                    await ctx.reply(embed=e, mention_author=False)

    @commands.command(
        aliases = ['магазин', 'магазин_ролей', 'role_shop']
    )
    async def shop(
        self,
        ctx
    ):
        with open('databases/economy_data/economy_db.json', 'r') as f:
            eco = json.load(f)
        with open('databases/server_settings/mass_db.json', 'r') as f:
            server = json.load(f)
        ### CHEKING1
        if not str(ctx.guild.id) in eco["tech"]["shop"]["base"]:
            eco["tech"]["shop"]["base"][str(ctx.guild.id)] = {}
        if not str(ctx.guild.id) in eco["tech"]["shop"]["sale"]["roleid"]:
            eco["tech"]["shop"]["sale"]["roleid"][str(ctx.guild.id)] = {}
        if not str(ctx.guild.id) in eco["tech"]["shop"]["sale"]["salevalue"]:
            eco["tech"]["shop"]["sale"]["salevalue"][str(ctx.guild.id)] = {}
        if not str(ctx.guild.id) in eco["tech"]["shop"]["oneuse"]:
            eco["tech"]["shop"]["oneuse"][str(ctx.guild.id)] = {}
        ### CHEKING1
        wt = discord.utils.get(self.Bot.emojis, name='cnone')
        embed = discord.Embed(
            title=f'{wt} Магазин ролей сервера {ctx.guild.name}:',
            colour=base_color
            )
        if eco["tech"]["shop"]["base"][str(ctx.guild.id)] == {} and eco["tech"]["shop"]["sale"]["roleid"][str(ctx.guild.id)] == {} and eco["tech"]["shop"]["oneuse"][str(ctx.guild.id)] == {}:
            embed.set_footer(text = 'В магазине нет ни одной роли.')
        else:
            embed.set_footer(text = 'Покупка роли -> !купить [@роль]')
        for role in eco["tech"]["shop"]["base"][str(ctx.guild.id)]:
            embed.add_field(
                name="Базовая роль",
                value=f""" `Роль:` <@&{role}> 
`Стоимость:` **{eco["tech"]["shop"]["base"][str(ctx.guild.id)][role]}₽**""",
                inline=True
            )
        for role in eco["tech"]["shop"]["sale"]["roleid"][str(ctx.guild.id)]:
            embed.add_field(
                name=":tada: Роль с скидкой {}%".format(eco["tech"]["shop"]["sale"]["salevalue"][str(ctx.guild.id)][role]),
                value=f""" `Роль:` <@&{role}> 
`Стоимость:` **{eco["tech"]["shop"]["sale"]["roleid"][str(ctx.guild.id)][role]}₽**""",
                inline=True
            )
        for role in eco["tech"]["shop"]["oneuse"][str(ctx.guild.id)]:
            embed.add_field( 
                name="Одноразовая роль",
                value=f""" Роль: <@&{role}> 
`Стоимость:` **{eco["tech"]["shop"]["oneuse"][str(ctx.guild.id)][role]}₽**""",
                inline=True
            )
        if str(ctx.guild.id) in server["reply"]:
            await ctx.send(embed=embed)
        else:
            await ctx.reply(embed=embed, mention_author=False)

    @commands.command(
        aliases = ['купить', 'приобрести', 'купить_роль', 'приобрести_роль', 'buy_role', 'role_buy']
    )
    async def buy(
        self,
        ctx,
        role: discord.Role = None
    ):
        with open('databases/economy_data/economy_db.json', 'r') as f:
            eco = json.load(f)
        with open('databases/server_settings/mass_db.json', 'r') as f:
            server = json.load(f)
        ### CHEKING
        if not str(ctx.guild.id) in eco["tech"]["shop"]["base"]:
            eco["tech"]["shop"]["base"][str(ctx.guild.id)] = {}
        if not str(ctx.guild.id) in eco["tech"]["shop"]["sale"]["roleid"]:
            eco["tech"]["shop"]["sale"]["roleid"][str(ctx.guild.id)] = {}
        if not str(ctx.guild.id) in eco["tech"]["shop"]["sale"]["salevalue"]:
            eco["tech"]["shop"]["sale"]["salevalue"][str(ctx.guild.id)] = {}
        if not str(ctx.guild.id) in eco["tech"]["shop"]["oneuse"]:
            eco["tech"]["shop"]["oneuse"][str(ctx.guild.id)] = {}
        ### CHEKING
        if not str(ctx.author.id) in eco["users"]["money"]:
            eco["users"]["money"][str(ctx.author.id)] = 25
        if not str(ctx.author.id) in eco["users"]["bank"]:
            eco["users"]["bank"][str(ctx.author.id)] = 25
        if not str(ctx.author.id) in eco["users"]["crypto"]["userbalance"]:
            eco["users"]["crypto"]["userbalance"][str(ctx.author.id)] = 0
        ### CHEKING
        err = discord.utils.get(self.Bot.emojis, name='cfalse')
        tru = discord.utils.get(self.Bot.emojis, name='ctrue')
        if role == None:
            embed = discord.Embed(
                title=f'{err} Вы не указали параметр:',
                description = "> Роль",
                colour=err_color
                )
            embed.set_footer(text = f'Пользователь: {ctx.author}')
            if str(ctx.guild.id) in server["reply"]:
                await ctx.send(embed=embed)
            else:
                await ctx.reply(embed=embed, mention_author=False)
        else:
            if bot_has_guild_permissions(manage_roles=True):
                if not str(role.id) in eco["tech"]["shop"]["base"][str(ctx.guild.id)] and not str(role.id) in eco["tech"]["shop"]["sale"]["roleid"][str(ctx.guild.id)] and not str(role.id) in eco["tech"]["shop"]["oneuse"][str(ctx.guild.id)]:
                    embed = discord.Embed(
                        title=f'{err} Ошибка!',
                        description = f"Данной роли ({role.mention}) нет в магазине.",
                        colour=err_color
                        )
                    if str(ctx.guild.id) in server["reply"]:
                        await ctx.send(embed=embed)
                    else:
                        await ctx.reply(embed=embed, mention_author=False)
                else:
                    if str(role.id) in eco["tech"]["shop"]["base"][str(ctx.guild.id)]:
                        cst = eco["tech"]["shop"]["base"][str(ctx.guild.id)][str(role.id)]
                        shopath = eco["tech"]["shop"]["base"][str(ctx.guild.id)]
                        mark = "PASS"
                    elif str(role.id) in eco["tech"]["shop"]["sale"]["roleid"][str(ctx.guild.id)]:
                        cst = eco["tech"]["shop"]["sale"]["roleid"][str(ctx.guild.id)][str(role.id)]
                        shopath = eco["tech"]["shop"]["sale"]["roleid"][str(ctx.guild.id)]
                        mark = "PASS"
                    elif str(role.id) in eco["tech"]["shop"]["oneuse"][str(ctx.guild.id)]:
                        cst = eco["tech"]["shop"]["oneuse"][str(ctx.guild.id)][str(role.id)]
                        shopath = eco["tech"]["shop"]["oneuse"][str(ctx.guild.id)]
                        mark = "DELETE!"                 
                    if eco["users"]["money"][str(ctx.author.id)] >= cst:
                        if not role in ctx.author.roles:
                            for i in shopath:
                                if i == str(role.id):
                                    ###USER###
                                    try:
                                        buy_role = discord.utils.get(ctx.guild.roles, id=int(i))
                                        await ctx.author.add_roles(buy_role)
                                        eco["users"]["money"][str(ctx.author.id)] -= cst
                                        ###ROLE CHECKER###
                                        if mark == 'DELETE!':
                                            del eco["tech"]["shop"]["oneuse"][str(ctx.guild.id)][str(role.id)]
                                        with open('databases/economy_data/economy_db.json', 'w') as f:
                                            json.dump(eco, f)
                                        embed = discord.Embed(
                                            title=f'{tru} Успешно!',
                                            description = f'Вы успешно приобрели роль {role.mention}. Списано **{cst}₽**',
                                            colour=su_color
                                            )
                                        embed.set_footer(text = f'Добавлено: {ctx.author}')
                                        if str(ctx.guild.id) in server["reply"]:
                                            await ctx.send(embed=embed)
                                        else:
                                            await ctx.reply(embed=embed, mention_author=False)
                                    except Exception:
                                        pass
                                else:
                                    pass
                        else:
                            embed = discord.Embed(
                                title=f'{err} Ошибка!',
                                description = f"{ctx.author.mention}, у Вас уже есть данная роль.",
                                colour=err_color
                                )
                            embed.set_footer(text = f'Пользователь: {ctx.author}')
                            if str(ctx.guild.id) in server["reply"]:
                                await ctx.send(embed=embed)
                            else:
                                await ctx.reply(embed=embed, mention_author=False)
                    else:
                        embed = discord.Embed(
                            title=f'{err} Ошибка!',
                            description = "На Вашем краманном балансе недостаточно средств для совершения совершения операции.",
                            colour=err_color
                            )
                        embed.set_footer(text = f'Пользователь: {ctx.author}')
                        if str(ctx.guild.id) in server["reply"]:
                            await ctx.send(embed=embed)
                        else:
                            await ctx.reply(embed=embed, mention_author=False)
            else:
                e = discord.Embed(
                    title=f'{err} Невозможно совершить операцию',
                    description=f'У меня нет права "Управлять ролями" на этом сервере. Без него я не смогу выдавать роли при покупке. Для разрешения проблемы выдайте мне данное право или обратитесь к создателю сервера.',
                    color=err_color
                )
                if str(ctx.guild.id) in server["reply"]:
                    await ctx.send(embed=e)
                else:
                    await ctx.reply(embed=e, mention_author=False)

    ###CD ERRORS###    
    @work.error
    async def cd_work_error(
        self, 
        ctx, 
        error
    ):
        with open('databases/server_settings/mass_db.json', 'r') as f:
            server = json.load(f)
        err = discord.utils.get(self.Bot.emojis, name='cfalse')
        if isinstance(error, commands.CommandOnCooldown):
            hours, error.retry_after = divmod(error.retry_after, 60 ** 2)
            minutes, error.retry_after = divmod(error.retry_after, 60)
            e = discord.Embed(
                title=f"{err} Ошибка!", 
                description=f"""Недавно вы уже работали. Вы не можете работать менее, чем раз в 12 часов. 
Попробуйте снова через `{round(hours)} ч, {round(minutes)} мин, {round(error.retry_after)} сек`""", color=err_color)
            if str(ctx.guild.id) in server["reply"]:
                await ctx.send(embed=e)
            else:
                await ctx.reply(embed=e, mention_author=False)

    @premium.error
    async def cd_premium_error(
        self, 
        ctx, 
        error
    ):
        with open('databases/server_settings/mass_db.json', 'r') as f:
            server = json.load(f)
        err = discord.utils.get(self.Bot.emojis, name='cfalse')
        if isinstance(error, commands.CommandOnCooldown):
            hours, error.retry_after = divmod(error.retry_after, 60 ** 2)
            minutes, error.retry_after = divmod(error.retry_after, 60)
            e = discord.Embed(
                title=f"{err} Ошибка!", 
                description=f"""Недавно вы уже забирали премиум-награду. Вы не можете собирать её менее, чем раз в 24 часа. 
Попробуйте снова через `{round(hours)} ч, {round(minutes)} мин, {round(error.retry_after)} сек`""", color=err_color)
            if str(ctx.guild.id) in server["reply"]:
                await ctx.send(embed=e)
            else:
                await ctx.reply(embed=e, mention_author=False)

    @shop_addrole.error
    async def perm_addrole_error(
        self, 
        ctx, 
        error
    ):
        with open('databases/server_settings/mass_db.json', 'r') as f:
            server = json.load(f)
        if isinstance(error, commands.MissingPermissions):
            err = discord.utils.get(self.Bot.emojis, name='cfalse')
            e = discord.Embed(
                title=f"{err} Ошибка!", 
                description=f'Недостаточно прав для выполнения команды. Для просмотра и управленния магазином сервера Вам нужно право "Администратор".', color=err_color)
            if str(ctx.guild.id) in server["reply"]:
                await ctx.send(embed=e)
            else:
                await ctx.reply(embed=e, mention_author=False)
    
    @shop_remrole.error
    async def perm_remrole_error(
        self, 
        ctx, 
        error
    ):
        with open('databases/server_settings/mass_db.json', 'r') as f:
            server = json.load(f)
        if isinstance(error, commands.MissingPermissions):
            err = discord.utils.get(self.Bot.emojis, name='cfalse')
            e = discord.Embed(
                title=f"{err} Ошибка!", 
                description=f'Недостаточно прав для выполнения команды. Для просмотра и управленния магазином сервера Вам нужно право "Администратор".', color=err_color)
            if str(ctx.guild.id) in server["reply"]:
                await ctx.send(embed=e)
            else:
                await ctx.reply(embed=e, mention_author=False)
    
    ###TASKS LOOP###
    @tasks.loop(
        hours=12, 
        reconnect=True
    )
    async def sender(self):
        with open('databases/economy_data/economy_db.json', 'r') as f:
            eco = json.load(f)
        channel = self.Bot.get_channel(866662493048799242)
        value = random.randint(10, 30000)
        action = random.choice(['plus', 'minus'])
        if action == 'plus':
            eco["users"]["crypto"]["cryptovalue"] += value
            with open('databases/economy_data/economy_db.json', 'w') as f:
                json.dump(eco, f)
            crs = eco["users"]["crypto"]["cryptovalue"]
            embed = discord.Embed(
                title=f'Курс криптовалюты успешно изменен!',
                description = f"Произошёл скачок в цене на **{value}₽**. Текущий курс валюты: {crs}.",
                colour=base_color
                )
            await channel.send(embed=embed)
        else:
            eco["users"]["crypto"]["cryptovalue"] -= value 
            with open('databases/economy_data/economy_db.json', 'w') as f:
                json.dump(eco, f)
            crs = eco["users"]["crypto"]["cryptovalue"]
            embed = discord.Embed(
                title=f'Курс криптовалюты успешно изменен!',
                description = f"Произошло падение в цене на **{value}₽**. Текущий курс валюты: {crs}.",
                colour=base_color
                )
            await channel.send(embed=embed)    
    
    @sender.before_loop
    async def before_sender(self):
        await self.Bot.wait_until_ready()

def setup(Bot):
    Bot.add_cog(economy(Bot))