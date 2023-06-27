""""
Copyright © Krypton 2019-2023 - https://github.com/kkrypt0nn (https://krypton.ninja)
Description:
🐍 A simple template to start to code your own and personalized discord bot in Python programming language.

Version: 5.5.0
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
