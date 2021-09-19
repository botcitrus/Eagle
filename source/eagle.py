import discord
from discord.ext import commands
from discord.ext.commands import AutoShardedBot
import json
import time
import os

with open("data/bot_data.json", "r") as f:
    data = json.load(f)

base_color=0x3498db
err_color=0xe74c3c
null_color=discord.Color.from_rgb(47,49,56)

eagle = AutoShardedBot(
    command_prefix=data["tech"]["prefix"],
    intents=discord.Intents.all(), 
    fetch_offline_members=True,
    shard_count=2
    )
eagle.remove_command('help')

start = time.perf_counter()

@eagle.command()
@commands.is_owner()
async def files(ctx):
    e = discord.Embed(
        title='Список файлов обнаруженных в директории `./cogs`:', 
        color=null_color
        )
    for filename in os.listdir('./cogs'):
        if filename[:-3] in eagle.cogs:
            fl = discord.utils.get(eagle.emojis, name='ctrue')
        else:
            fl = discord.utils.get(eagle.emojis, name='cfalse')
        if filename.endswith('.py'):
            e.add_field(name=filename, value=f'╰〔:page_with_curl:〕- `Размер`: {os.path.getsize(f"./cogs/{filename}") // 1024} Кбайт | `Загружен как ког:` {fl}', inline=True)
    await ctx.reply(embed=e, mention_author=False)

@eagle.command()
@commands.is_owner()
async def cog(
    ctx, 
    acti, 
    extension = None
    ):
    if extension == None:
        if acti == 'list':
            list = "\n".join([cog for cog in eagle.cogs])
            e = discord.Embed(title='Список загруженных когов:', description=f'**{list}**', color=null_color)
            await ctx.reply(embed=e, mention_author=False)
        else:   
            await ctx.message.add_reaction('⚠️')
    else:
        if acti == 'load':
            eagle.load_extension(f'cogs.{extension}')
            await ctx.message.add_reaction('✅')
        elif acti == 'reload':
            eagle.reload_extension(f'cogs.{extension}')
            await ctx.message.add_reaction('✅')
        elif acti == 'unload':
            eagle.unload_extension(f'cogs.{extension}')
            await ctx.message.add_reaction('✅')
        else:
            await ctx.message.add_reaction('⚠️')

@eagle.command()
@commands.is_owner()
async def clusters(ctx):
    end = time.perf_counter()
    if end - start <= 15:
        cluster_marker = "Получение данных..."
    else:
        time_result_end = (end - start) - 14
        hours, time_result_end = divmod(time_result_end, 60 ** 2)
        minutes, time_result_end = divmod(time_result_end, 60)
        cluster_marker = f"{round(hours)} ч, {round(minutes)} мин, {round(time_result_end)} сек"
    shard_id = ctx.guild.shard_id
    shard = eagle.get_shard(shard_id)
    shard_ping = round(shard.latency * 1000) 
    embed = discord.Embed(
        title=f"Информация о `{len(eagle.shards)}` кластерах:",
        description=f"**Текущий кластер [`{shard_id}`]**\n`Работает уже:` {cluster_marker}\n`Пинг:` {shard_ping}",
        colour=base_color
    )
    sh=0
    for shard in eagle.latencies:
        guilds  = 0
        members = 0
        for guild in eagle.guilds:
            if guild.shard_id == sh:
                guilds += 1
                for member in guild.members:
                    members += 1
        sh += 1
        embed.add_field(
            name=f'Кластер `#{sh}`', 
            value=f"Пинг кластера: `{eagle.latencies[sh - 1][1] * 1000:.0f}ms`\nСерверов на кластере: `{guilds}`\nПользоватлей на кластере: `{members}`",
            inline=False    
        )
    await ctx.reply(embed=embed, mention_author=False)


for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
       eagle.load_extension(f'cogs.{filename[:-3]}')

eagle.run(data["unique"]["token"])
