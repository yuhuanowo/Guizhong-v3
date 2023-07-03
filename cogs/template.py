""""
Copyright © YuhuanStudio 2022-2023 - https://github.com/yuhuanowo (https://www.yuhuanstudio.tech)
描述:
🐍 一個可愛的機器人，用於幫助你的 Discord 伺服器。

Version: 0.0.1(beta)
"""

from discord.ext import commands
from discord.ext.commands import Context

from helpers import checks


# 在這裡，我們命名cog並為其創建一個新類 cog.
class Template(commands.Cog, name="template"):
    def __init__(self, bot):
        self.bot = bot

    #在這裡您可以添加自己的命令，您始終需要提供"self"作為第一個參數。

    @commands.hybrid_command(
        name="testcommand",
        description="這是一個不執行任何操作的測試命令.",
    )
    # 這將只允許非黑名單成員執行該命令
    @checks.not_blacklisted()
    # 這將只允許機器人的所有者執行命令 -> config.json
    @checks.is_owner()
    async def testcommand(self, context: Context):
        """
        這是一個不執行任何操作的測試命令.

        :param context: 應用程序命令上下文.
        """
        # 在這裡做你的事情

        # 不要忘記刪除"pass"，我添加這個只是因為方法中沒有內容.
        pass


# 然後我們最後將 cog 添加到機器人中，以便它可以加載、卸載、重新加載和使用其內容.
async def setup(bot):
    await bot.add_cog(Template(bot))
