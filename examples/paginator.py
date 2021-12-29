import disnake
from disnake.ext import commands

import disnakeSuperUtils

bot = commands.Bot(command_prefix="-")


@bot.event
async def on_ready():
    print("Page manager is ready.", bot.user)


@bot.command()
async def paginator(ctx):
    messages = [
        disnake.Embed(title="Data (1/2)", description="Hello world"),
        disnake.Embed(title="Data (2/2)", description="Hello world"),
    ]

    await disnakeSuperUtils.ButtonsPageManager(ctx, messages).run()


bot.run("token")
