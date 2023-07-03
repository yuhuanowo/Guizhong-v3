""""
Copyright © YuhuanStudio 2022-2023 - https://github.com/yuhuanowo (https://www.yuhuanstudio.tech)
描述:
🐍 一個可愛的機器人，用於幫助你的 Discord 伺服器。

Version: 0.0.1(beta)
"""

import discord
from discord import app_commands
from discord.ext import commands
from discord.ext.commands import Context

from helpers import checks, db_manager


class Owner(commands.Cog, name="owner"):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(
        name="sync",
        description="同步斜杠命令.",
    )
    @app_commands.describe(scope="同步範圍. 可以是 `global` or `guild`(全域或伺服器)")
    @checks.is_owner()
    async def sync(self, context: Context, scope: str) -> None:
        """
        同步斜杠命令。

        :param context: 命令上下文。
        :param range: 同步的範圍。可以是“全局”或“行會”。
        """

        if scope == "global":
            await context.bot.tree.sync()
            embed = discord.Embed(
                title="斜杠命令已全局同步.",
                color=0x9C84EF,
            )
            embed.set_footer(text="可愛的歸終~",icon_url=self.bot.user.avatar.url)
            embed.timestamp = context.message.created_at
            await context.send(embed=embed)
            return
        elif scope == "guild":
            context.bot.tree.copy_global_to(guild=context.guild)
            await context.bot.tree.sync(guild=context.guild)
            embed = discord.Embed(
                title="本公會已同步斜線指令.",
                color=0x9C84EF,
            )
            embed.set_footer(text="可愛的歸終~",icon_url=self.bot.user.avatar.url)
            embed.timestamp = context.message.created_at
            await context.send(embed=embed)
            return
        embed = discord.Embed(
            title="範圍必須是`global` or `guild`.", color=0xE02B2B
        )
        embed.set_footer(text="可愛的歸終~",icon_url=self.bot.user.avatar.url)
        embed.timestamp = context.message.created_at
        await context.send(embed=embed)

    @commands.command(
        name="unsync",
        description="不同步斜杠命令.",
    )
    @app_commands.describe(
        scope="同步的範圍。可以是 `global`, `current_guild` or `guild` (全域、當前伺服器或伺服器)"
    )
    @checks.is_owner()
    async def unsync(self, context: Context, scope: str) -> None:
        """
        取消同步斜杠命令。

        :param context: 命令上下文。
        :param range: 同步的範圍。可以是“global”、“current_guild”或“guild”.
        """

        if scope == "global":
            context.bot.tree.clear_commands(guild=None)
            await context.bot.tree.sync()
            embed = discord.Embed(
                title="斜杠命令已設為全域不同步。",
                color=0x9C84EF,
            )
            embed.set_footer(text="可愛的歸終~",icon_url=self.bot.user.avatar.url)
            embed.timestamp = context.message.created_at
            await context.send(embed=embed)
            return
        elif scope == "guild":
            context.bot.tree.clear_commands(guild=context.guild)
            await context.bot.tree.sync(guild=context.guild)
            embed = discord.Embed(
                title="該伺服器中的斜杠命令已不同步.",
                color=0x9C84EF,
            )
            embed.set_footer(text="可愛的歸終~",icon_url=self.bot.user.avatar.url)
            embed.timestamp = context.message.created_at
            await context.send(embed=embed)
            return
        embed = discord.Embed(
            title="範圍必須是 `global` or `guild` (全域或伺服器).", color=0xE02B2B
        )
        embed.set_footer(text="可愛的歸終~",icon_url=self.bot.user.avatar.url)
        embed.timestamp = context.message.created_at
        await context.send(embed=embed)

    @commands.hybrid_command(
        name="load",
        description="Load a cog",
    )
    @app_commands.describe(cog="要加載的cog名稱")
    @checks.is_owner()
    async def load(self, context: Context, cog: str) -> None:
        """
        機器人將加載給定的齒輪。

        :param context：混合命令上下文。
        :param cog: 要加載的 cog 的名稱.
        """
        try:
            await self.bot.load_extension(f"cogs.{cog}")
        except Exception:
            embed = discord.Embed(
                title=f"無法加載 `{cog}` cog.", color=0xE02B2B
            )
            embed.set_footer(text="可愛的歸終~",icon_url=self.bot.user.avatar.url)
            embed.timestamp = context.message.created_at
            await context.send(embed=embed)
            return
        embed = discord.Embed(
            title=f"成功加載 `{cog}` cog.", color=0x9C84EF
        )
        embed.set_footer(text="可愛的歸終~",icon_url=self.bot.user.avatar.url)
        embed.timestamp = context.message.created_at
        await context.send(embed=embed)

    @commands.hybrid_command(
        name="unload",
        description="Unloads a cog.",
    )
    @app_commands.describe(cog="要卸載的cog名稱")
    @checks.is_owner()
    async def unload(self, context: Context, cog: str) -> None:
        """
        機器人將卸載給定的齒輪。

        :param context：混合命令上下文。
        :param cog: 要卸載的 cog 的名稱.
        """
        try:
            await self.bot.unload_extension(f"cogs.{cog}")
        except Exception:
            embed = discord.Embed(
                title=f"無法卸載 `{cog}` cog.", color=0xE02B2B
            )
            embed.set_footer(text="可愛的歸終~",icon_url=self.bot.user.avatar.url)
            embed.timestamp = context.message.created_at
            await context.send(embed=embed)
            return
        embed = discord.Embed(
            title=f"成功卸載了 `{cog}` cog.", color=0x9C84EF
        )
        embed.set_footer(text="可愛的歸終~",icon_url=self.bot.user.avatar.url)
        embed.timestamp = context.message.created_at
        await context.send(embed=embed)

    @commands.hybrid_command(
        name="reload",
        description="Reloads a cog.",
    )
    @app_commands.describe(cog="要重新加載的cog名稱")
    @checks.is_owner()
    async def reload(self, context: Context, cog: str) -> None:
        """
        機器人將重新加載給定的齒輪。

        :param context：混合命令上下文。
        :param cog: 要重新加載的 cog 的名稱。
        """
        try:
            await self.bot.reload_extension(f"cogs.{cog}")
        except Exception:
            embed = discord.Embed(
                title=f"無法重新加載 `{cog}` cog.", color=0xE02B2B
            )
            embed.set_footer(text="可愛的歸終~",icon_url=self.bot.user.avatar.url)
            embed.timestamp = context.message.created_at
            await context.send(embed=embed)
            return
        embed = discord.Embed(
            title=f"重新加載成功 `{cog}` cog.", color=0x9C84EF
        )
        embed.set_footer(text="可愛的歸終~",icon_url=self.bot.user.avatar.url)
        embed.timestamp = context.message.created_at
        await context.send(embed=embed)

    @commands.hybrid_command(
        name="shutdown",
        description="讓歸終關閉.",
    )
    @checks.is_owner()
    async def shutdown(self, context: Context) -> None:
        """
       關閉機器人。

        :param context: 混合命令上下文.
        """
        embed = discord.Embed(description="正在關閉.... 再見! :wave:", color=0x9C84EF)
        embed.set_footer(text="可愛的歸終~",icon_url=self.bot.user.avatar.url)
        embed.timestamp = context.message.created_at
        await context.send(embed=embed)
        await self.bot.close()

    @commands.hybrid_command(
        name="say",
        description="歸終會說你想說的任何話.",
    )
    @app_commands.describe(message="你想歸終重複的消息")
    @checks.is_owner()
    async def say(self, context: Context, *, message: str) -> None:
        """
        機器人會說你想說的任何話。

        :param context：混合命令上下文。
        :param message: 機器人應該重複的消息。
        """
        await context.send(message)

    @commands.hybrid_command(
        name="embed",
        description="歸終會說任何你想說的話，但在嵌入範圍內.",
    )
    @app_commands.describe(message="你想歸終重複的消息")
    @checks.is_owner()
    async def embed(self, context: Context, *, message: str) -> None:
        """
       機器人會說你想說的任何話，但使用嵌入。

        :param context：混合命令上下文。
        :param message: 機器人應該重複的消息。
        """
        embed = discord.Embed(description=message, color=0x9C84EF)
        await context.send(embed=embed)

    @commands.hybrid_group(
        name="blacklist",
        description="獲取所有黑名單用戶列表s.",
    )
    @checks.is_owner()
    async def blacklist(self, context: Context) -> None:
        """
        允許您添加或刪除無法使用機器人的用戶。

        :param context: 混合命令上下文.
        """
        if context.invoked_subcommand is None:
            embed = discord.Embed(
                title="您需要指定一個子命令.\n\n**子命令:**\n`add` - 將用戶添加到黑名單.\n`remove` - 將用戶從黑名單中刪除。",
                color=0xE02B2B,
            )
            embed.set_footer(text="可愛的歸終~",icon_url=self.bot.user.avatar.url)
            embed.timestamp = context.message.created_at
            await context.send(embed=embed)

    @blacklist.command(
        base="blacklist",
        name="show",
        description="顯示所有列入黑名單的用戶列表.",
    )
    @checks.is_owner()
    async def blacklist_show(self, context: Context) -> None:
        """
        顯示所有列入黑名單的用戶的列表。

        :param context: 混合命令上下文.
        """
        blacklisted_users = await db_manager.get_blacklisted_users()
        if len(blacklisted_users) == 0:
            embed = discord.Embed(
                title="目前沒有黑名單用戶.", color=0xE02B2B
            )
            embed.set_footer(text="可愛的歸終~",icon_url=self.bot.user.avatar.url)
            embed.timestamp = context.message.created_at
            await context.send(embed=embed)
            return

        embed = discord.Embed(title="列入黑名單的用戶", color=0x9C84EF)
        users = []
        for bluser in blacklisted_users:
            user = self.bot.get_user(int(bluser[0])) or await self.bot.fetch_user(
                int(bluser[0])
            )
            users.append(f"• {user.mention} ({user}) - 列入黑名單 <t:{bluser[1]}>")
        embed.description = "\n".join(users)
        embed.set_footer(text="可愛的歸終~",icon_url=self.bot.user.avatar.url)
        embed.timestamp = context.message.created_at
        await context.send(embed=embed)

    @blacklist.command(
        base="blacklist",
        name="add",
        description="允許您添加無法使用歸終的用戶.",
    )
    @app_commands.describe(user="想添加到黑名單的用戶")
    @checks.is_owner()
    async def blacklist_add(self, context: Context, user: discord.User) -> None:
        """
        允許您添加無法使用機器人的用戶。

        :param context：混合命令上下文。
        :param user: 需要添加到黑名單的用戶.
        """
        user_id = user.id
        if await db_manager.is_blacklisted(user_id):
            embed = discord.Embed(
                title=f"**{user.name}** 已經在黑名單裡了。",
                color=0xE02B2B,
            )
            embed.set_footer(text="可愛的歸終~",icon_url=self.bot.user.avatar.url)
            embed.timestamp = context.message.created_at
            await context.send(embed=embed)
            return
        total = await db_manager.add_user_to_blacklist(user_id)
        embed = discord.Embed(
            title=f"**{user.name}** 已成功加入黑名單",
            color=0x9C84EF,
        )
        embed.set_footer(text="那裡 {'有' if total == 1 else '有'} {total} {'個用戶' if total == 1 else '個用戶'} 在黑名單中",icon_url=self.bot.user.avatar.url)
        embed.timestamp = context.message.created_at
        await context.send(embed=embed)

    @blacklist.command(
        base="blacklist",
        name="remove",
        description="允許您刪除無法使用歸終的用戶.",
    )
    @app_commands.describe(user="應從黑名單中刪除的用戶.")
    @checks.is_owner()
    async def blacklist_remove(self, context: Context, user: discord.User) -> None:
        """
        允許您刪除無法使用機器人的用戶。

        :param context：混合命令上下文。
        :param user: 需要從黑名單中刪除的用戶.
        """
        user_id = user.id
        if not await db_manager.is_blacklisted(user_id):
            embed = discord.Embed(
                title=f"**{user.name}** 不在黑名單中.", color=0xE02B2B
            )
            embed.set_footer(text="可愛的歸終~",icon_url=self.bot.user.avatar.url)
            embed.timestamp = context.message.created_at
            await context.send(embed=embed)
            return
        total = await db_manager.remove_user_from_blacklist(user_id)
        embed = discord.Embed(
            title=f"**{user.name}** 已成功移出黑名單",
            color=0x9C84EF,
        )
        embed.set_footer(text="那裡 {'有' if total == 1 else '有'} {total} {'個用戶' if total == 1 else '個用戶'} 在黑名單中",icon_url=self.bot.user.avatar.url)
        embed.timestamp = context.message.created_at
        await context.send(embed=embed)


async def setup(bot):
    await bot.add_cog(Owner(bot))
