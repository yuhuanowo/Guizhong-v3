""""
Copyright © YuhuanStudio 2022-2023 - https://github.com/yuhuanowo (https://www.yuhuanstudio.tech)
描述:
🐍 一個可愛的機器人，用於幫助你的 Discord 伺服器。

Version: 0.0.1(beta)
"""

import json
import os
from typing import Callable, TypeVar

from discord.ext import commands

from exceptions import *
from helpers import db_manager

T = TypeVar("T")

# 客製化檢查 (Custom Checks) 用於檢查是否為擁有者的裝飾器函式
def is_owner() -> Callable[[T], T]: # Callable[[T], T] 代表函式的參數和回傳值都是 T 型別
    """
    這是一項自定義檢查，用於查看執行命令的用戶是否是機器人的所有者。
    """
    # 定義一個檢查函式，用於檢查是否為擁有者   
    async def predicate(context: commands.Context) -> bool: # commands.Context 代表命令上下文
        with open( # 開啟 config.json
            f"{os.path.realpath(os.path.dirname(__file__))}/../config.json"
        ) as file: # 讀取 config.json 
            data = json.load(file)
        if context.author.id not in data["owners"]: # 如果執行命令的用戶不是機器人的所有者
            raise UserNotOwner 
        return True 

    return commands.check(predicate) # 回傳檢查函式

# 客製化檢查 (Custom Checks) 用於檢查是否為黑名單的裝飾器函式
def not_blacklisted() -> Callable[[T], T]:
    """
    這是一項自定義檢查，用於查看執行命令的用戶是否已被列入黑名單。
    """
    # 定義一個檢查函式，用於檢查是否為黑名單
    async def predicate(context: commands.Context) -> bool: # commands.Context 代表命令上下文
        if await db_manager.is_blacklisted(context.author.id): # 如果執行命令的用戶已被列入黑名單
            raise UserBlacklisted
        return True

    return commands.check(predicate) # 回傳檢查函式
