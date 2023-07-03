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


class Moderation(commands.Cog, name="moderation"):
    def __init__(self, bot):
        self.bot = bot

    @commands.hybrid_command(
        name="kick",
        description="將成員踢出服務器.",
    )
    @commands.has_permissions(kick_members=True)
    @commands.bot_has_permissions(kick_members=True)
    @checks.not_blacklisted()
    @app_commands.describe(
        user="想踢出的成員.",
        reason="成員被踢出的原因.",
    )
    async def kick(
        self, context: Context, user: discord.User, *, reason: str = "未指定"
    ) -> None:
        """
        將用戶踢出服務器。

        :param context：混合命令上下文。
        :param user: 應從服務器踢出的用戶。
        :param Reason: 踢球的原因。默認為“未指定".
        """
        member = context.guild.get_member(user.id) or await context.guild.fetch_member(
            user.id
        )
        if member.guild_permissions.administrator:
            embed = discord.Embed(
                description="成員具有管理員權限.", color=0xE02B2B
            )
            embed.set_footer(text="可愛的歸終~",icon_url=self.bot.user.avatar.url)
            embed.timestamp = context.message.created_at
            await context.send(embed=embed)
        else:
            try:
                embed = discord.Embed(
                    description=f"**{member}** 被 **{context.author}**踢出!",
                    color=0x9C84EF,
                )
                embed.set_footer(text="可愛的歸終~",icon_url=self.bot.user.avatar.url)
                embed.timestamp = context.message.created_at
                embed.add_field(name="原因:", value=reason)
                await context.send(embed=embed)
                try:
                    await member.send(
                        f"你被 **{context.author}** 踢出 **{context.guild.name}**了!\n原因n: {reason}"
                    )
                except:
                    # 無法在用戶的私人消息中發送消息
                    pass
                await member.kick(reason=reason)
            except:
                embed = discord.Embed(
                    description="嘗試踢成員時發生錯誤。確保我的身分組高於您要踢出的成員的身分組。",
                    color=0xE02B2B,
                )
                embed.set_footer(text="可愛的歸終~",icon_url=self.bot.user.avatar.url)
                embed.timestamp = context.message.created_at
                await context.send(embed=embed)

    @commands.hybrid_command(
        name="nick",
        description="更改伺服器上成員的暱稱.",
    )
    @commands.has_permissions(manage_nicknames=True)
    @commands.bot_has_permissions(manage_nicknames=True)
    @checks.not_blacklisted()
    @app_commands.describe(
        user="應該有新暱稱的成員。",
        nickname="應設置的新暱稱.",
    )
    async def nick(
        self, context: Context, user: discord.User, *, nickname: str = None
    ) -> None:
        """
        更改服務器上用戶的暱稱。

        :param context：混合命令上下文。
        :param user: 應該更改暱稱的用戶。
        :param暱稱：用戶的新暱稱。默認為 None，這將重置暱稱.
        """
        member = context.guild.get_member(user.id) or await context.guild.fetch_member(
            user.id
        )
        try:
            await member.edit(nick=nickname)
            embed = discord.Embed(
                description=f"**{member}** 的新暱稱是 **{nickname}**!",
                color=0x9C84EF,
            )
            embed.set_footer(text="可愛的歸終~",icon_url=self.bot.user.avatar.url)
            embed.timestamp = context.message.created_at
            await context.send(embed=embed)
        except:
            embed = discord.Embed(
                description="嘗試更改成員的暱稱時發生錯誤。確保我的身分組高於您要更改暱稱的成員的身分組。",
                color=0xE02B2B,
            )
            embed.set_footer(text="可愛的歸終~",icon_url=self.bot.user.avatar.url)
            embed.timestamp = context.message.created_at
            await context.send(embed=embed)

    @commands.hybrid_command(
        name="ban",
        description="Ban掉成員.",
    )
    @commands.has_permissions(ban_members=True)
    @commands.bot_has_permissions(ban_members=True)
    @checks.not_blacklisted()
    @app_commands.describe(
        user="要Ban的成員.",
        reason="他被Ban的原因.",
    )
    async def ban(
        self, context: Context, user: discord.User, *, reason: str = "未指定"
    ) -> None:
        """
        禁止用戶訪問服務器。

        :param context：混合命令上下文。
        :param user: 應該被禁止訪問服務器的用戶。
        :param Reason: 禁止的原因。默認為“未指定".
        """
        member = context.guild.get_member(user.id) or await context.guild.fetch_member(
            user.id
        )
        try:
            if member.guild_permissions.administrator:
                embed = discord.Embed(
                    description="成員具有管理員權限", color=0xE02B2B
                )
                embed.set_footer(text="可愛的歸終~",icon_url=self.bot.user.avatar.url)
                embed.timestamp = context.message.created_at
                await context.send(embed=embed)
            else:
                embed = discord.Embed(
                    description=f"**{member}** 被 **{context.author}**Ban了!",
                    color=0x9C84EF,
                )
                embed.set_footer(text="可愛的歸終~",icon_url=self.bot.user.avatar.url)
                embed.timestamp = context.message.created_at
                embed.add_field(name="原因:", value=reason)
                await context.send(embed=embed)
                try:
                    await member.send(
                        f"你被 **{context.author}** 在 **{context.guild.name}**Ban了!\n原因: {reason}"
                    )
                except:
                    # 無法在用戶的私人消息中發送消息
                    pass
                await member.ban(reason=reason)
        except:
            embed = discord.Embed(
                title="Error!",
                description="嘗試更改成員的暱稱時發生錯誤。確保我的身分組高於您要更改暱稱的成員的身分組.",
                color=0xE02B2B,
            )
            embed.set_footer(text="可愛的歸終~",icon_url=self.bot.user.avatar.url)
            embed.timestamp = context.message.created_at
            await context.send(embed=embed)

    @commands.hybrid_group(
        name="warning",
        description="管理伺服器上成員的警告.",
    )
    @commands.has_permissions(manage_messages=True)
    @checks.not_blacklisted()
    async def warning(self, context: Context) -> None:
        """
        管理服務器上用戶的警告。

        :param context: 混合命令上下文.
        """
        if context.invoked_subcommand is None:
            embed = discord.Embed(
                description="請指定子命令.\n\n**子命令s:**\n`add` - 向用戶添加警告.\n`remove` - 刪除用戶的警告.\n`list` - 列出用戶的所有警告.",
                color=0xE02B2B,
            )
            embed.set_footer(text="可愛的歸終~",icon_url=self.bot.user.avatar.url)
            embed.timestamp = context.message.created_at
            await context.send(embed=embed)

    @warning.command(
        name="add",
        description="向伺服器中的成員添加警告.",
    )
    @checks.not_blacklisted()
    @commands.has_permissions(manage_messages=True)
    @app_commands.describe(
        user="應該被警告的用戶.",
        reason="警告的原因.",
    )
    async def warning_add(
        self, context: Context, user: discord.User, *, reason: str = "未指定"
    ) -> None:
        """
        在用戶的私人消息中警告用戶。

        :param context：混合命令上下文。
        :param user: 應該被警告的用戶。
        :param Reason: 警告的原因。默認為“未指定”.
        """
        member = context.guild.get_member(user.id) or await context.guild.fetch_member(
            user.id
        )
        total = await db_manager.add_warn(
            user.id, context.guild.id, context.author.id, reason
        )
        embed = discord.Embed(
            description=f"**{member}** 被 **{context.author}**警告!\n該用戶的警告總數： {total}",
            color=0x9C84EF,
        )
        embed.set_footer(text="可愛的歸終~",icon_url=self.bot.user.avatar.url)
        embed.timestamp = context.message.created_at
        embed.add_field(name="原因:", value=reason)
        await context.send(embed=embed)
        try:
            await member.send(
                f"您被 **{context.author}** 在 **{context.guild.name}**中警告!\n原因： {reason}"
            )
        except:
            # 無法在用戶的私人消息中發送消息
            await context.send(
                f"{member.mention}, 你被 **{context.author}**警告!\n原因: {reason}"
            )

    @warning.command(
        name="remove",
        description="刪除伺服器中成員的警告.",
    )
    @checks.not_blacklisted()
    @commands.has_permissions(manage_messages=True)
    @app_commands.describe(
        user="應該刪除警告的用戶.",
        warn_id="應刪除的警告 ID.",
    )
    async def warning_remove(
        self, context: Context, user: discord.User, warn_id: int
    ) -> None:
        """
       在用戶的私人消息中警告用戶。

        :param context：混合命令上下文。
        :param user：應該刪除警告的用戶。
        :param warn_id: 應刪除的警告的 ID。
        """
        member = context.guild.get_member(user.id) or await context.guild.fetch_member(
            user.id
        )
        total = await db_manager.remove_warn(warn_id, user.id, context.guild.id)
        embed = discord.Embed(
            description=f"我已經刪除了警告 **#{warn_id}** 從 **{member}**!\n該用戶的警告總數: {total}",
            color=0x9C84EF,
        )
        embed.set_footer(text="可愛的歸終~",icon_url=self.bot.user.avatar.url)
        embed.timestamp = context.message.created_at
        await context.send(embed=embed)

    @warning.command(
        name="list",
        description="顯示伺服器中成員的警告.",
    )
    @commands.has_guild_permissions(manage_messages=True)
    @checks.not_blacklisted()
    @app_commands.describe(user="您想要收到警告的成員.")
    async def warning_list(self, context: Context, user: discord.User):
        """
        顯示服務器中用戶的警告。

        :param context：混合命令上下文。
        :param user: The user you want to get the warnings of.
        """
        warnings_list = await db_manager.get_warnings(user.id, context.guild.id)
        embed = discord.Embed(title=f"{user}的警告", color=0x9C84EF)
        description = ""
        if len(warnings_list) == 0:
            description = "該成員沒有任何警告."
        else:
            for warning in warnings_list:
                description += f"• 警告者 <@{warning[2]}>: **{warning[3]}** (<t:{warning[4]}>) - 警告ID #{warning[5]}\n"
        embed.description = description
        embed.set_footer(text="可愛的歸終~",icon_url=self.bot.user.avatar.url)
        embed.timestamp = context.message.created_at
        await context.send(embed=embed)

    @commands.hybrid_command(
        name="purge",
        description="刪除消息.",
    )
    @commands.has_guild_permissions(manage_messages=True)
    @commands.bot_has_permissions(manage_messages=True)
    @checks.not_blacklisted()
    @app_commands.describe(amount="想刪除的訊息數量.")
    async def purge(self, context: Context, amount: int) -> None:
        """
        刪除多條消息。

        :param context：混合命令上下文。
        :param amount: 應刪除的消息數。
        """
        await context.send(
            "正在刪除消息..."
        )  #確保機器人響應交互並且不會得到“未知交互”響應的有點古怪的方法
        purged_messages = await context.channel.purge(limit=amount + 1)
        embed = discord.Embed(
            description=f"**{context.author}** 已清除 **{len(purged_messages)-1}** 條訊息!",
            color=0x9C84EF,
        )
        embed.set_footer(text="可愛的歸終~",icon_url=self.bot.user.avatar.url)
        embed.timestamp = context.message.created_at
        await context.channel.send(embed=embed)

    @commands.hybrid_command(
        name="hackban",
        description="禁止用戶而無需該用戶位於服務器中.",
    )
    @commands.has_permissions(ban_members=True)
    @commands.bot_has_permissions(ban_members=True)
    @checks.not_blacklisted()
    @app_commands.describe(
        user_id="應該被Ban的用戶的 ID.",
        reason="他被Ban的原因.",
    )
    async def hackban(
        self, context: Context, user_id: str, *, reason: str = "未指定"
    ) -> None:
        """
        禁止用戶，而無需該用戶位於服務器中。

        :param context：混合命令上下文。
        :param user_id: 應該被禁止的用戶的ID。
        :param Reason: 禁止的原因。默認為“未指定”.
        """
        try:
            await self.bot.http.ban(user_id, context.guild.id, reason=reason)
            user = self.bot.get_user(int(user_id)) or await self.bot.fetch_user(
                int(user_id)
            )
            embed = discord.Embed(
                description=f"**{user}** (ID: {user_id}) 被 **{context.author}**Ban!",
                color=0x9C84EF,
            )
            embed.set_footer(text="可愛的歸終~",icon_url=self.bot.user.avatar.url)
            embed.timestamp = context.message.created_at
            embed.add_field(name="原因:", value=reason)
            await context.send(embed=embed)
        except Exception as e:
            embed = discord.Embed(
                description="嘗試禁止成員時發生錯誤。確保 ID 是屬於成員的現有 ID.",
                color=0xE02B2B,
            )
            embed.set_footer(text="可愛的歸終~",icon_url=self.bot.user.avatar.url)
            embed.timestamp = context.message.created_at
            await context.send(embed=embed)


async def setup(bot):
    await bot.add_cog(Moderation(bot))
