import discord
import sqlite3
from discord.ext import commands
import json

base_color=0x3498db
su_color=0x2ecc71
err_color=0xe74c3c

class ivents(commands.Cog):
    def __init__(self, Bot):
        self.Bot = Bot       

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'''
Powered by________                     ______      _            ________
         |  ______|       /\          /  ___ \    | |          |  ______|
         | |             /  \        /  /   \_\   | |          | |
         | |____        /  _ \       |  |         | |          | |____
         |  ____|      /  /_\ \      |  |   __    | |          |  ____|
         | |          /  ____  \     |  |  |_ |   | |          | |
         | |______   /  /    \  \    \  \___/ /   | |_______   | |______
         |________| /__/      \__\    \______/    |_________|  |________|''')
        await self.Bot.change_presence(
            status=discord.Status.idle,
            activity=discord.Activity(
                type=discord.ActivityType.watching, 
                name='!хелп, @Eagle | U. 3.1.2'
            )
        )

    @commands.Cog.listener()
    async def on_message(
        self,
        message
    ):
        with open('databases/server_settings/mass_db.json', 'r') as f:
            server = json.load(f)
        if not str(message.guild.id) in server["mentions"]:
            pass
        else:
            if self.Bot.user in message.mentions:
                e = discord.Embed(
                    title=f'Основная информация про меня:',
                    description=f'''**!хелп** - список команд и важные ссылки.
**!команды** - детальное описание команд.
**!инвайт** - ссылка для приглашения.''',
                    color=base_color
                )
                owner = self.Bot.get_user(599490357754855435)
		emb.set_footer(
		    text=f"By {owner}", 
		    icon_url=owner.avatar_url
		    )
                await message.channel.send(embed=e)
            else:
                pass
                
    @commands.command(
        aliases = ['юникоин']
    )
    async def unicoin(
        self,
        ctx
    ):
        with open('databases/users_settings/user_db.json', 'r') as f:
            usr = json.load(f)
        tru = discord.utils.get(self.Bot.emojis, name='ctrue')
        if not str(ctx.author.id) in usr["items"]["haknow"]:
            usr["items"]["haknow"][str(ctx.author.id)] = True
            with open('databases/users_settings/user_db.json', 'w') as f:
                json.dump(usr, f)
            embed = discord.Embed(
                title=f'{tru} Успешно!',
                description = f'Секретный персональный значок "Просвещённый" активирован.',
                colour=su_color
                )
            await ctx.author.send(embed=embed)
        else:
            pass

def setup (Bot):
    Bot.add_cog(ivents(Bot))
