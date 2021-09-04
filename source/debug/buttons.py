"""
This test-debug file. Here you can test some new features.
"""

from discord_components import DiscordComponents, ComponentsBot, Button

bot = ComponentsBot(command_prefix = "=")


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}!")


@bot.command()
async def b(ctx):
    await ctx.send(
        "Hello, World!",
        components = [
            Button(label = "WOW button!", custom_id = "button1")
        ]
    )

    interaction = await bot.wait_for("button_click", check = lambda i: i.custom_id == "button1")
    await interaction.send(content = "Button clicked!")


bot.run('toke')
