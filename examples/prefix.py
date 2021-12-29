from disnake.ext import commands

import disnakeSuperUtils

bot = commands.Bot(command_prefix="-")
PrefixManager = disnakeSuperUtils.PrefixManager(
    bot, default_prefixes=("-",), mentioned=True
)


@bot.command()
async def prefix(ctx, new_prefix):
    new_prefix = new_prefix[
        :3
    ]  # I recommend capping the prefix length to save storage.
    await PrefixManager.set_prefix(ctx.guild, new_prefix)
    await ctx.send(f"Successfully changed the prefix to '{new_prefix}'")


@bot.event
async def on_ready():
    database = disnakeSuperUtils.DatabaseManager.connect(...)
    await PrefixManager.connect_to_database(database, ["prefixes"])
    print("Prefix manager is ready.", bot.user)


@bot.command()
async def ping(ctx):
    await ctx.send(f"Pong! ping is {bot.latency * 1000}ms")


bot.run("token")
