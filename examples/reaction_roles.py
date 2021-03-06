import disnake
from disnake.ext import commands

import disnakeSuperUtils

bot = commands.Bot(command_prefix="-", intents=disnake.Intents.all())
ReactionManager = disnakeSuperUtils.ReactionManager(bot)


@ReactionManager.event()
async def on_reaction_event(guild, channel, message, member, emoji):
    """This event will be run if there isn't a role to add to the member."""

    if ...:
        print("Created ticket.")


@bot.event
async def on_ready():
    database = disnakeSuperUtils.DatabaseManager.connect(...)
    await ReactionManager.connect_to_database(database, ["reaction_roles"])

    print("Reaction manager is ready.", bot.user)


@bot.command()
async def reaction(
    ctx, message, emoji: str, remove_on_reaction, role: disnake.Role = None
):
    message = await ctx.channel.fetch_message(message)

    await ReactionManager.create_reaction(
        ctx.guild, message, role, emoji, remove_on_reaction
    )


bot.run("token")
