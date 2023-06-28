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
from discord import app_commands
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
            title=(f"嗨，{context.author.display_name}!  我是歸終～ "), description="我是歸終，一個可愛的機器人!\n 我們正在努力轉移部分功能的指令到斜線指令\n 可以使用 /help 指令查看斜線的使用方法\n 使用我的服務即表示你已同意我的 隱私權聲明 及 服務條款", color=0x9C84EF)
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
                embed.set_thumbnail(url=self.bot.user.avatar.url)   
                await interaction.response.send_message(embed=embed,ephemeral=True)   

        #button
        button = discord.ui.Button(
        style=discord.ButtonStyle.link,
        label="歸終的官方網站",
            url="https://discord.gg/GfUY7ynvXN",
        )
        
        #embed 圖片
        embed.set_thumbnail(url=self.bot.user.avatar.url)

        #顯示
        view = discord.ui.View()
        view.add_item(dropdown)
        view.add_item(button)

        #發送
        await context.send(embed=embed, view=view)
        dropdown.callback = select_callback
        view = discord.ui.View()
        view.add_item(dropdown)


    """
        for i in self.bot.cogs:
            cog = self.bot.get_cog(i.lower())
            commands = cog.get_commands()
            data = []
            for command in commands:
                description = command.description.partition("\n")[0]
                data.append(f"{prefix}{command.name} - {description}")
            help_text = "\n".join(data)
            embed.add_field(
                name=i.capitalize(), value=f"```{help_text}```", inline=False
            )
        await context.send(embed=embed)
    """

    @commands.hybrid_command(
        name="botinfo",
        description="Get some useful (or not) information about the bot.",
    )
    @checks.not_blacklisted()
    async def botinfo(self, context: Context) -> None:
        """
        Get some useful (or not) information about the bot.

        :param context: The hybrid command context.
        """
        embed = discord.Embed(
            description="Used [Krypton's](https://krypton.ninja) template",
            color=0x9C84EF,
        )
        embed.set_author(name="Bot Information")
        embed.add_field(name="Owner:", value="Krypton#7331", inline=True)
        embed.add_field(
            name="Python Version:", value=f"{platform.python_version()}", inline=True
        )
        embed.add_field(
            name="Prefix:",
            value=f"/ (Slash Commands) or {self.bot.config['prefix']} for normal commands",
            inline=False,
        )
        embed.set_footer(text=f"Requested by {context.author}")
        await context.send(embed=embed)

    @commands.hybrid_command(
        name="serverinfo",
        description="Get some useful (or not) information about the server.",
    )
    @checks.not_blacklisted()
    async def serverinfo(self, context: Context) -> None:
        """
        Get some useful (or not) information about the server.

        :param context: The hybrid command context.
        """
        roles = [role.name for role in context.guild.roles]
        if len(roles) > 50:
            roles = roles[:50]
            roles.append(f">>>> Displaying[50/{len(roles)}] Roles")
        roles = ", ".join(roles)

        embed = discord.Embed(
            title="**Server Name:**", description=f"{context.guild}", color=0x9C84EF
        )
        if context.guild.icon is not None:
            embed.set_thumbnail(url=context.guild.icon.url)
        embed.add_field(name="Server ID", value=context.guild.id)
        embed.add_field(name="Member Count", value=context.guild.member_count)
        embed.add_field(
            name="Text/Voice Channels", value=f"{len(context.guild.channels)}"
        )
        embed.add_field(name=f"Roles ({len(context.guild.roles)})", value=roles)
        embed.set_footer(text=f"Created at: {context.guild.created_at}")
        await context.send(embed=embed)

    @commands.hybrid_command(
        name="ping",
        description="Check if the bot is alive.",
    )
    @checks.not_blacklisted()
    async def ping(self, context: Context) -> None:
        """
        Check if the bot is alive.

        :param context: The hybrid command context.
        """
        embed = discord.Embed(
            title="🏓 Pong!",
            description=f"The bot latency is {round(self.bot.latency * 1000)}ms.",
            color=0x9C84EF,
        )
        await context.send(embed=embed)

    @commands.hybrid_command(
        name="invite",
        description="Get the invite link of the bot to be able to invite it.",
    )
    @checks.not_blacklisted()
    async def invite(self, context: Context) -> None:
        """
        Get the invite link of the bot to be able to invite it.

        :param context: The hybrid command context.
        """
        embed = discord.Embed(
            description=f"Invite me by clicking [here](https://discordapp.com/oauth2/authorize?&client_id={self.bot.config['application_id']}&scope=bot+applications.commands&permissions={self.bot.config['permissions']}).",
            color=0xD75BF4,
        )
        try:
            # To know what permissions to give to your bot, please see here: https://discordapi.com/permissions.html and remember to not give Administrator permissions.
            await context.author.send(embed=embed)
            await context.send("I sent you a private message!")
        except discord.Forbidden:
            await context.send(embed=embed)

    @commands.hybrid_command(
        name="server",
        description="Get the invite link of the discord server of the bot for some support.",
    )
    @checks.not_blacklisted()
    async def server(self, context: Context) -> None:
        """
        Get the invite link of the discord server of the bot for some support.

        :param context: The hybrid command context.
        """
        embed = discord.Embed(
            description=f"Join the support server for the bot by clicking [here](https://discord.gg/mTBrXyWxAF).",
            color=0xD75BF4,
        )
        try:
            await context.author.send(embed=embed)
            await context.send("I sent you a private message!")
        except discord.Forbidden:
            await context.send(embed=embed)

    @commands.hybrid_command(
        name="8ball",
        description="Ask any question to the bot.",
    )
    @checks.not_blacklisted()
    @app_commands.describe(question="The question you want to ask.")
    async def eight_ball(self, context: Context, *, question: str) -> None:
        """
        Ask any question to the bot.

        :param context: The hybrid command context.
        :param question: The question that should be asked by the user.
        """
        answers = [
            "It is certain.",
            "It is decidedly so.",
            "You may rely on it.",
            "Without a doubt.",
            "Yes - definitely.",
            "As I see, yes.",
            "Most likely.",
            "Outlook good.",
            "Yes.",
            "Signs point to yes.",
            "Reply hazy, try again.",
            "Ask again later.",
            "Better not tell you now.",
            "Cannot predict now.",
            "Concentrate and ask again later.",
            "Don't count on it.",
            "My reply is no.",
            "My sources say no.",
            "Outlook not so good.",
            "Very doubtful.",
        ]
        embed = discord.Embed(
            title="**My Answer:**",
            description=f"{random.choice(answers)}",
            color=0x9C84EF,
        )
        embed.set_footer(text=f"The question was: {question}")
        await context.send(embed=embed)

    @commands.hybrid_command(
        name="bitcoin",
        description="Get the current price of bitcoin.",
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
                        title="Bitcoin price",
                        description=f"The current price is {data['bpi']['USD']['rate']} :dollar:",
                        color=0x9C84EF,
                    )
                else:
                    embed = discord.Embed(
                        title="Error!",
                        description="There is something wrong with the API, please try again later",
                        color=0xE02B2B,
                    )
                await context.send(embed=embed)


async def setup(bot):
    await bot.add_cog(General(bot))
