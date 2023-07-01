""""
Copyright © Krypton 2019-2023 - https://github.com/kkrypt0nn (https://krypton.ninja)
Description:
🐍 A simple template to start to code your own and personalized discord bot in Python programming language.

Version: 5.5.0
"""

import platform
import random

import aiohttp
import discord
from discord import Guild, app_commands
from discord.ext import commands
from discord.ext.commands import Context

from helpers import checks


class General(commands.Cog, name="general"):
    def __init__(self, bot):
        self.bot = bot

    @commands.hybrid_command(
        name="help", description="你想來認識歸終嗎.?"
    )
    @checks.not_blacklisted()
    async def help(self, context: Context) -> None:
        prefix = self.bot.config["prefix"]      
        #對使用指令的使用者說嗨
        embed = discord.Embed(
            title=(f"嗨，{context.author.display_name}!  我是歸終～ "),color=0x9C84EF)
        embed.add_field(name="我們正在努力轉移部分功能的指令到斜線指令\n可以使用 /help 指令查看斜線的使用方法", value="\u200b", inline=False)
        embed.add_field(name="使用我的服務即表示你已同意我的 隱私權聲明 及 服務條款", value="\u200b", inline=False)
        embed.set_footer(text="可愛的歸終~",icon_url=self.bot.user.avatar.url)
        embed.timestamp = context.message.created_at
        #下拉選單 
        dropdown = discord.ui.Select(
            placeholder="請選擇",
            min_values=1,
            max_values=None,
            options=[
                discord.SelectOption(label="常用指令", description="常用指令", emoji="📜"),
                discord.SelectOption(label="娛樂指令", description="娛樂指令", emoji="🎮"),
                discord.SelectOption(label="管理指令", description="管理指令", emoji="🔨"),
                discord.SelectOption(label="其他指令", description="其他指令", emoji="📦"),
            ],
        )
        #下拉回复
        async def select_callback(interaction: discord.Interaction):
            selected_option = interaction.data["values"][0]            
            if selected_option == "常用指令":
                embed = discord.Embed(
                    title="常用指令",
                    description="/help - 想了解更多有關歸終嗎？\n"
                                "/botinfo - 獲取有關機器人的一些有用（或無用）信息\n"
                                "/serverinfo - 獲取有關伺服器的一些有用（或無用）信息\n"
                                "/ping - 檢查機器人是否在線\n"
                                "/invite - 獲取機器人的邀請連結以便邀請它\n"
                                "/server - 獲取機器人所在的 DC 伺服器的邀請連結以獲得支援\n"
                                "/8ball - 向機器人提問\n"
                                "/bitcoin - 獲取比特幣的當前價格",
                    color=0x9C84EF,
                  
                )
                embed.set_footer(text="可愛的歸終~",icon_url=self.bot.user.avatar.url)
                embed.timestamp = context.message.created_at
                embed.set_thumbnail(url=self.bot.user.avatar.url)
                await interaction.response.send_message(embed=embed,ephemeral=True)
            if selected_option == "娛樂指令":
                embed = discord.Embed(
                    title="娛樂指令",
                    description="/randomfact - 獲取一個隨機事實\n"
                                "/coinflip - 擲硬幣，但請在之前給出你的猜測\n"
                                "/rps - 與機器人玩剪刀石頭布遊戲",
                    color=0x9C84EF,
                  
                )
                embed.set_footer(text="可愛的歸終~",icon_url=self.bot.user.avatar.url)
                embed.timestamp = context.message.created_at
                embed.set_thumbnail(url=self.bot.user.avatar.url)      
                await interaction.response.send_message(embed=embed,ephemeral=True)      
            if selected_option == "管理指令":
                embed = discord.Embed(
                    title="管理指令",
                    description="/kick - 將使用者從伺服器踢出\n"
                                "/nick - 更改伺服器上使用者的暱稱\n"
                                "/ban - 將使用者從伺服器封鎖\n"
                                "/warning - 管理伺服器上使用者的警告\n"
                                "/purge - 刪除一定數量的訊息\n"
                                "/hackban - 封鎖伺服器中未加入的使用者",
                    color=0x9C84EF,
                  
                )
                embed.set_footer(text="可愛的歸終~",icon_url=self.bot.user.avatar.url)
                embed.timestamp = context.message.created_at
                embed.set_thumbnail(url=self.bot.user.avatar.url)   
                await interaction.response.send_message(embed=embed,ephemeral=True)         
            if selected_option == "其他指令":
                embed = discord.Embed(
                    title="其他指令",
                    description="/sync - 同步斜線指令\n"
                                "/unsync - 取消同步斜線指令\n"
                                "/load - 載入一個模組\n"
                                "/unload - 卸載一個模組\n"
                                "/reload - 重新載入一個模組\n"
                                "/shutdown - 關閉機器人\n"
                                "/say - 機器人會說出你想要的內容\n"
                                "/embed - 機器人會以Embed形式說出你想要的內容\n"
                                "/blacklist - 獲取所有被列入黑名單的使用者列表",
                    color=0x9C84EF,
                  
                )
                embed.set_footer(text="可愛的歸終~",icon_url=self.bot.user.avatar.url)
                embed.timestamp = context.message.created_at
                embed.set_thumbnail(url=self.bot.user.avatar.url)   
                await interaction.response.send_message(embed=embed,ephemeral=True)   

        #button
        button = discord.ui.Button(
        style=discord.ButtonStyle.link,
        label="歸終的官方Discord伺服器",
            url="https://discord.gg/GfUY7ynvXN",
        )
        #button2
        button2 = discord.ui.Button(
        style=discord.ButtonStyle.link,
        label="歸終的官方網站",
            url="https://www.yuhuanstudio.tech",
        )
        #button3
        button3 = discord.ui.Button(
        style=discord.ButtonStyle.link,
        label="邀請我",
            url="https://discord.com/api/oauth2/authorize?client_id=1082152889209860247&permissions=8&scope=bot",
        )
        
        #embed 圖片
        embed.set_thumbnail(url=self.bot.user.avatar.url)

        #顯示
        view = discord.ui.View()
        view.add_item(dropdown)
        view.add_item(button)
        view.add_item(button2)
        view.add_item(button3)
        
        #發送
        await context.send(embed=embed, view=view)
        dropdown.callback = select_callback
        view = discord.ui.View()
        view.add_item(dropdown)

    @commands.hybrid_command(
        name="botinfo",
        description="查看一些關於歸終的訊息.",
    )
    @checks.not_blacklisted()
    async def botinfo(self, context: Context) -> None:
        """
        獲取有關機器人的一些有用（或無用）信息。

        :param context：混合命令上下文。
        [text](url)
        """
        embed = discord.Embed(
            description="由[YuhuanStudio](https://www.yuhuanstudio.tech)提供支援",
            color=0x9C84EF,
        )
        embed.set_author(name="☆歸終～”的身分證")
        embed.add_field(name="Owner:", value="yuhuan1125", inline=True)
        embed.add_field(
            name="Python Version:", value=f"{platform.python_version()}", inline=True
        )
        embed.add_field(name="discord.py:", value=f"{discord.__version__}", inline=True)
        embed.add_field(
            name="前綴:",
            value=f"/ (Slash Commands) or {self.bot.config['prefix']} for normal commands",
            inline=False,
        )
        embed.set_footer(text="可愛的歸終~",icon_url=self.bot.user.avatar.url)
        embed.timestamp = context.message.created_at
        embed.set_thumbnail(url=self.bot.user.avatar.url)
        await context.send(embed=embed)

    @commands.hybrid_command(
        name="serverinfo",
        description="獲取此伺服器的一些信息.",
    )
    @checks.not_blacklisted()
    async def serverinfo(self, context: Context) -> None:
        """
       獲取有關服務器的一些有用（或無用）信息。

        :param context：混合命令上下文。
        """
        roles = [role.name for role in context.guild.roles]
        if len(roles) > 50:
            roles = roles[:50]
            roles.append(f">>>> Displaying[50/{len(roles)}] Roles")
        roles = ", ".join(roles)

        embed = discord.Embed(
            title="**伺服器名稱:**", description=f"{context.guild}", color=0x9C84EF
        )
        if context.guild.icon is not None:
            embed.set_thumbnail(url=context.guild.icon.url)
        embed.add_field(name="伺服器 ID", value=context.guild.id)
        embed.add_field(name="成員數量", value=context.guild.member_count)
        embed.add_field(
            name="文字/語音通道總數", value=f"{len(context.guild.channels)}"
        )
        embed.add_field(name=f"身分組 ({len(context.guild.roles)})", value=roles)
        embed.set_footer(text="可愛的歸終~",icon_url=self.bot.user.avatar.url)
        embed.timestamp = context.message.created_at
        await context.send(embed=embed)

    @commands.hybrid_command(
        name="ping",
        description="檢查歸終是否還活著.",
    )
    @checks.not_blacklisted()
    async def ping(self, context: Context) -> None:
        """
        檢查機器人是否還活著。

        :param context：混合命令上下文。
        """
        embed = discord.Embed(
            title="🏓 Pong!",color=0x9C84EF,
        )
        #legacy 
        embed.add_field(name="延遲", value=f"{round(self.bot.latency * 1000)}ms")
        embed.set_footer(text="可愛的歸終~",icon_url=self.bot.user.avatar.url)
        embed.timestamp = context.message.created_at
        await context.send(embed=embed)

    @commands.hybrid_command(
        name="invite",
        description="獲取歸終的邀請鏈接.",
    )
    @checks.not_blacklisted()
    async def invite(self, context: Context) -> None:
        """
        Get the invite link of the bot to be able to invite it.

        :param context: The hybrid command context.
        """
        embed = discord.Embed(
            description=f"[點擊我邀請](https://discordapp.com/oauth2/authorize?&client_id={self.bot.config['application_id']}&scope=bot+applications.commands&permissions={self.bot.config['permissions']}).",
            color=0xD75BF4,
        )
        embed.set_footer(text="可愛的歸終~",icon_url=self.bot.user.avatar.url)
        embed.timestamp = context.message.created_at
        #button
        button = discord.ui.Button(
        style=discord.ButtonStyle.link,
        label="邀請我",
            url=f"https://discord.com/api/oauth2/authorize?client_id={self.bot.config['application_id']}&permissions={self.bot.config['permissions']}&scope=bot%20applications.commands",
        )
        #顯示
        
        try:
            # To know what permissions to give to your bot, please see here: https://discordapi.com/permissions.html and remember to not give Administrator permissions.
            view = discord.ui.View()
            view.add_item(button)
            await context.author.send(embed=embed)
            await context.send("我給你發了私訊!",ephemeral=True)
        except discord.Forbidden:
            view = discord.ui.View()
            view.add_item(button)
            await context.send(embed=embed)


    @commands.hybrid_command(
        name="server",
        description="獲取歸終的discord服務器邀請鏈接以獲得一些支持.",
    )
    @checks.not_blacklisted()
    async def server(self, context: Context) -> None:
        """
        Get the invite link of the discord server of the bot for some support.

        :param context: The hybrid command context.
        """
        embed = discord.Embed(
            description=f"[單擊加入歸終支持服務器](https://discord.com/invite/GfUY7ynvXN).",
            color=0xD75BF4,
        )
        embed.set_footer(text="可愛的歸終~",icon_url=self.bot.user.avatar.url)
        embed.timestamp = context.message.created_at
        try:
            await context.author.send(embed=embed)
            await context.send("I sent you a private message!",ephemeral=True)
        except discord.Forbidden:
            await context.send(embed=embed)

    @commands.hybrid_command(
        name="8ball",
        description="向歸終詢問任何問題。",
    )
    @checks.not_blacklisted()
    @app_commands.describe(question="你想問的問題.")
    async def eight_ball(self, context: Context, *, question: str) -> None:
        """
        Ask any question to the bot.

        :param context: The hybrid command context.
        :param question: The question that should be asked by the user.
        """
        answers = [
            "可以肯定的是。",
            "確實如此。",
            "您可以信賴它。",
            "毫無疑問.",
            "當然是.",
            "據我所知，是的.",
            "最有可能的。",
            "前景良好。",
            "Yes.",
            "跡象表明是的.",
            "回复模糊，再試一次.",
            "稍後再詢問.",
            "現在最好不告訴你.",
            "現在無法預測.",
            "集中注意力，稍後再問。",
            "不要指望它.",
            "我的回答是否定的。",
            "我的消息來源說不.",
            "前景不太好.",
            "很可疑.",
        ]
        embed = discord.Embed(
            title="**我的答案:**",
            description=f"{random.choice(answers)}",
            color=0x9C84EF,
        )
        embed.timestamp = context.message.created_at
        embed.set_footer(text=f"問題: {question}",icon_url=self.bot.user.avatar.url)

        await context.send(embed=embed)

    @commands.hybrid_command(
        name="bitcoin",
        description="獲取比特幣的當前價格.",
    )
    @checks.not_blacklisted()
    async def bitcoin(self, context: Context) -> None:
        """
        Get the current price of bitcoin.

        :param context: The hybrid command context.
        """
        # This will prevent your bot from stopping everything when doing a web request - see: https://discordpy.readthedocs.io/en/stable/faq.html#how-do-i-make-a-web-request
        async with aiohttp.ClientSession() as session:
            async with session.get(
                "https://api.coindesk.com/v1/bpi/currentprice/BTC.json"
            ) as request:
                if request.status == 200:
                    data = await request.json(
                        content_type="application/javascript"
                    )  # For some reason the returned content is of type JavaScript
                    embed = discord.Embed(
                        title="比特幣價格",
                        description=f"目前的價格是 {data['bpi']['USD']['rate']} :dollar:",
                        color=0x9C84EF,
                    )
                    embed.set_footer(text="可愛的歸終~",icon_url=self.bot.user.avatar.url)
                    embed.timestamp = context.message.created_at
                else:
                    embed = discord.Embed(
                        title="Error!",
                        description="API有問題，請稍後重試",
                        color=0xE02B2B,
                    )
                    embed.set_footer(text="可愛的歸終~",icon_url=self.bot.user.avatar.url)
                    embed.timestamp = context.message.created_at
                await context.send(embed=embed)


async def setup(bot):
    await bot.add_cog(General(bot))
