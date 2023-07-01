""""
Copyright © Krypton 2019-2023 - https://github.com/kkrypt0nn (https://krypton.ninja)
Description:
🐍 A simple template to start to code your own and personalized discord bot in Python programming language.

Version: 5.5.0
"""

import random

import aiohttp
import discord
from discord.ext import commands
from discord.ext.commands import Context

from helpers import checks


class Choice(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.value = None

    @discord.ui.button(label="人頭", style=discord.ButtonStyle.blurple)
    async def confirm(
        self, button: discord.ui.Button, interaction: discord.Interaction
    ):
        self.value = "人頭"
        self.stop()

    @discord.ui.button(label="數字", style=discord.ButtonStyle.blurple)
    async def cancel(self, button: discord.ui.Button, interaction: discord.Interaction):
        self.value = "數字"
        self.stop()


class RockPaperScissors(discord.ui.Select):
    def __init__(self):
        options = [
            discord.SelectOption(
                label="剪刀", description="你選擇剪刀.", emoji="✂"
            ),
            discord.SelectOption(
                label="石頭", description="你選擇石頭.", emoji="🪨"
            ),
            discord.SelectOption(
                label="布", description="你選擇布.", emoji="🧻"
            ),
        ]
        super().__init__(
            placeholder="選擇...",
            min_values=1,
            max_values=1,
            options=options,
        )

    async def callback(self, interaction: discord.Interaction):
        choices = {
            "石頭": 0,
            "布": 1,
            "剪刀": 2,
        }
        user_choice = self.values[0].lower()
        user_choice_index = choices[user_choice]

        bot_choice = random.choice(list(choices.keys()))
        bot_choice_index = choices[bot_choice]

        result_embed = discord.Embed(color=0x9C84EF)
        result_embed.set_author(
            name=interaction.user.name, icon_url=interaction.user.avatar.url
        )
        result_embed.timestamp = interaction.created_at

        if user_choice_index == bot_choice_index:
            result_embed.title = f"**這是平局！**\n你選擇了 {user_choice} 而我選擇了 {bot_choice}."
            result_embed.colour = 0xF59E42
        elif user_choice_index == 0 and bot_choice_index == 2:
            result_embed.title = f"**你贏了!**\n你選擇了 {user_choice} 而我選擇了 {bot_choice}."
            result_embed.colour = 0x9C84EF
        elif user_choice_index == 1 and bot_choice_index == 0:
            result_embed.title = f"**你贏了！**\n你選擇了 {user_choice} 而我選擇了 {bot_choice}."
            result_embed.colour = 0x9C84EF
        elif user_choice_index == 2 and bot_choice_index == 1:
            result_embed.title = f"**你贏了!**\n你選擇了 {user_choice} 而我選擇了 {bot_choice}."
            result_embed.colour = 0x9C84EF
        else:
            result_embed.description = (
                f"**我贏了!**\n你選擇了 {user_choice} 而我選擇了 {bot_choice}."
            )
            result_embed.colour = 0xE02B2B
        await interaction.response.edit_message(
            embed=result_embed, content=None, view=None
        )


class RockPaperScissorsView(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.add_item(RockPaperScissors())


class Fun(commands.Cog, name="fun"):
    def __init__(self, bot):
        self.bot = bot

    @commands.hybrid_command(name="randomfact", description="獲得一個隨機事件。")
    @checks.not_blacklisted()
    async def randomfact(self, context: Context) -> None:
        """
        Get a random fact.

        :param context: The hybrid command context.
        """
        # This will prevent your bot from stopping everything when doing a web request - see: https://discordpy.readthedocs.io/en/stable/faq.html#how-do-i-make-a-web-request
        async with aiohttp.ClientSession() as session:
            async with session.get(
                "https://uselessfacts.jsph.pl/random.json?language=en"
            ) as request:
                if request.status == 200:
                    data = await request.json()
                    #將獲取到的文字轉換成中文
                    if data["language"] == "en":
                        data["language"] = "zh-TW"
                    async with session.get(
                        f"https://translate.googleapis.com/translate_a/single?client=gtx&sl=en&tl={data['language']}&dt=t&q={data['text']}"
                    ) as request:
                        if request.status == 200:
                            data = await request.json()
                            embed = discord.Embed(
                                title=data[0][0][0], color=0xD75BF4
                            )
                            embed.set_footer(text="據可靠消息，上方訊息被google翻譯過",icon_url=self.bot.user.avatar.url)
                            embed.timestamp = context.message.created_at
                        else:
                            embed = discord.Embed(
                                title="Error!",
                                description="API有問題，請稍後重試r",
                                color=0xE02B2B,
                            )
                    await context.send(embed=embed) 

    @commands.hybrid_command(
        name="coinflip", description="拋硬幣，但盡力而為."
    )
    @checks.not_blacklisted()
    async def coinflip(self, context: Context) -> None:
        """
        拋硬幣，但先下注。

        :param context：混合命令上下文。
        """
        buttons = Choice()
        embed = discord.Embed(title="你賭硬幣是人頭還是數字?", color=0x9C84EF)
        embed.set_footer(text="可愛的歸終~",icon_url=self.bot.user.avatar.url)
        embed.timestamp = context.message.created_at
        message = await context.send(embed=embed, view=buttons)
        await buttons.wait()  # We wait for the user to click a button.
        result = random.choice(["人頭", "數字"])
        if buttons.value == result:
            embed = discord.Embed(
                title=f"正確的！你猜 `{buttons.value}` 而我拋出 `{result}`.",
                color=0x9C84EF,
            )
            embed.set_footer(text="可愛的歸終~",icon_url=self.bot.user.avatar.url)
            embed.timestamp = context.message.created_at
        else:
            embed = discord.Embed(
                title=f"哎呀！你猜 `{buttons.value}` 而我拋出 `{result}`, 下次好運!",
                color=0xE02B2B,
            )
            embed.set_footer(text="可愛的歸終~",icon_url=self.bot.user.avatar.url)
            embed.timestamp = context.message.created_at
        await message.edit(embed=embed, view=None, content=None)

    @commands.hybrid_command(
        name="rps", description="與歸終玩石頭剪刀布."
    )
    @checks.not_blacklisted()
    async def rock_paper_scissors(self, context: Context) -> None:
        """
        與機器人玩石頭剪刀布遊戲。

        :param context: 混合命令上下文.
        """
        view = RockPaperScissorsView()
        await context.send("請做出您的選擇", view=view)


async def setup(bot):
    await bot.add_cog(Fun(bot))
