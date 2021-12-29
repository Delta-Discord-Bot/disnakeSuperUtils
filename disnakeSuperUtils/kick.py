from __future__ import annotations

from typing import TYPE_CHECKING

import disnake

from .base import EventManager
from .punishments import Punisher

if TYPE_CHECKING:
    from disnake.ext import commands
    from .punishments import Punishment


__all__ = ("KickManager",)


class KickManager(EventManager, Punisher):
    """
    A KickManager that manages kicks for guilds.
    """

    __slots__ = ("bot",)

    def __init__(self, bot: commands.Bot):
        super().__init__()
        self.bot = bot

    async def punish(
        self, ctx: commands.Context, member: disnake.Member, punishment: Punishment
    ) -> None:
        try:
            await member.kick(reason=punishment.punishment_reason)
        except disnake.errors.Forbidden as e:
            raise e
        else:
            await self.call_event("on_punishment", ctx, member, punishment)
