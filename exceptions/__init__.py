""""
Copyright © YuhuanStudio 2022-2023 - https://github.com/yuhuanowo (https://www.yuhuanstudio.tech)
描述:
🐍 一個可愛的機器人，用於幫助你的 Discord 伺服器。

Version: 0.0.1(beta)
"""

from discord.ext import commands

#客製化檢查 (Custom Checks) 用於檢查是否為擁有者的裝飾器函式
class UserBlacklisted(commands.CheckFailure):
    """
    當用戶嘗試某些操作但被列入黑名單時拋出.
    """

    def __init__(self, message="您已被列入黑名單！"):
        self.message = message
        super().__init__(self.message)


class UserNotOwner(commands.CheckFailure):
    """
    當用戶嘗試某些操作但不是機器人的所有者時拋出.
    """

    def __init__(self, message="您不是歸終的所有者!"):
        self.message = message
        super().__init__(self.message)
