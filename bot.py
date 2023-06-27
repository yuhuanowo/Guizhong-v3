"""
Copyright © Krypton 2019-2023 - https://github.com/kkrypt0nn (https://krypton.ninja)
Description:
🐍 A simple template to start to code your own and personalized discord bot in Python programming language.

Version: 5.5.0
"""

import asyncio
import json
import logging
import os
import platform
import random
import sys

import aiosqlite
import discord
from discord.ext import commands, tasks
from discord.ext.commands import Bot, Context

import exceptions

#系統找不到config.json
if not os.path.isfile(f"{os.path.realpath(os.path.dirname(__file__))}/config.json"):
    sys.exit("'config.json' not found! Please add it and try again.")
else:
    with open(f"{os.path.realpath(os.path.dirname(__file__))}/config.json") as file:
        config = json.load(file)

#設置bot的intents
intents = discord.Intents.default()

# 創建bot
bot = Bot(
    command_prefix=commands.when_mentioned_or(config["prefix"]),
    intents=intents,
    help_command=None,
)

#設置紀錄器

# 定義自訂的日誌格式化類別 LoggingFormatter
class LoggingFormatter(logging.Formatter):
    # 顏色
    black = "\x1b[30m"
    red = "\x1b[31m"
    green = "\x1b[32m"
    yellow = "\x1b[33m"
    blue = "\x1b[34m"
    gray = "\x1b[38m"
    # Styles
    reset = "\x1b[0m" # 重置樣式
    bold = "\x1b[1m"  # 加粗樣式

    # 定義不同日誌級別與對應顏色的映射關係
    COLORS = {
        logging.DEBUG: gray + bold, # DEBUG 級別的日誌使用灰色加粗樣式
        logging.INFO: blue + bold, # INFO 級別的日誌使用藍色加粗樣式
        logging.WARNING: yellow + bold, # WARNING 級別的日誌使用黃色加粗樣式
        logging.ERROR: red,  # ERROR 級別的日誌使用紅色樣式
        logging.CRITICAL: red + bold, # CRITICAL 級別的日誌使用紅色加粗樣式
    }

    # 覆寫 format 方法，用於格式化日誌紀錄
    def format(self, record):
        log_color = self.COLORS[record.levelno] # 根據紀錄的日誌級別獲取對應的顏色
        format = "(black){asctime}(reset) (levelcolor){levelname:<8}(reset) (green){name}(reset) {message}"
        format = format.replace("(black)", self.black + self.bold) # 將 (black) 替換為黑色加粗樣式
        format = format.replace("(reset)", self.reset) # 將 (reset) 替換為重置樣式
        format = format.replace("(levelcolor)", log_color)  # 將 (levelcolor) 替換為紀錄的顏色
        format = format.replace("(green)", self.green + self.bold) # 將 (green) 替換為綠色加粗樣式
        formatter = logging.Formatter(format, "%Y-%m-%d %H:%M:%S", style="{")  # 創建日誌格式化物件
        return formatter.format(record)  # 格式化日誌紀錄

# 創建名為 "discord_bot" 的 logger 物件
logger = logging.getLogger("discord_bot")
logger.setLevel(logging.INFO) # 設定日誌

# Console handler 控制台處理器
console_handler = logging.StreamHandler() # 創建控制台處理器
console_handler.setFormatter(LoggingFormatter()) # 設定日誌格式化器為自訂的 LoggingFormatter
# File handler 檔案處理器
file_handler = logging.FileHandler(filename="discord.log", encoding="utf-8", mode="w") # 創建檔案處理器，將日誌寫入名為 "discord.log" 的檔案中
file_handler_formatter = logging.Formatter(
    "[{asctime}] [{levelname:<8}] {name}: {message}", "%Y-%m-%d %H:%M:%S", style="{"
) # 創建檔案處理器的日誌格式化器
file_handler.setFormatter(file_handler_formatter) # 設定檔案處理器的日誌格式化器

# Add the handlers 加入處理器到 logger
logger.addHandler(console_handler) # 將控制台處理器加入到 logger
logger.addHandler(file_handler) # 將檔案處理器加入到 logger
bot.logger = logger # 將 logger 分配給 bot 物件的 logger 屬性


# 創建資料庫
async def init_db():
    async with aiosqlite.connect(
        f"{os.path.realpath(os.path.dirname(__file__))}/database/database.db"
    ) as db:
        with open(
            f"{os.path.realpath(os.path.dirname(__file__))}/database/schema.sql"
        ) as file:
            await db.executescript(file.read()) # 執行 SQL 腳本
        await db.commit() # 提交事務


"""
創建一個 bot 變量來訪問 cogs 中的配置文件，這樣您就不需要每次都導入它。
該配置可使用以下代碼獲得：
- bot.config # In this file
- self.bot.config # In cogs
"""
bot.config = config


# 設置bot的事件 (on_ready, on_message, on_command_error, on_command_completion) 和 tasks (status_task) 事件 
# on_ready: 當bot準備好時執行
@bot.event
async def on_ready() -> None:
    """
    當機器人準備好時執行此事件中的代碼.
    """
    bot.logger.info(f"Logged in as {bot.user.name}")
    bot.logger.info(f"discord.py API version: {discord.__version__}")
    bot.logger.info(f"Python version: {platform.python_version()}")
    bot.logger.info(f"Running on: {platform.system()} {platform.release()} ({os.name})")
    bot.logger.info("-------------------")
    status_task.start()
    if config["sync_commands_globally"]:
        bot.logger.info("Syncing commands globally...")
        await bot.tree.sync()

# status_task: 設置bot的狀態
@tasks.loop(minutes=1.0)
async def status_task() -> None:
    """
    設置bot的遊戲狀態任務.
    """
    statuses = ["with you!", "with Krypton!", "with humans!"]
    await bot.change_presence(activity=discord.Game(random.choice(statuses)))

# on_message: 當有訊息時執行
@bot.event
async def on_message(message: discord.Message) -> None:
    """
    每次有人發送消息時都會執行此事件中的代碼，無論是否帶有前綴

    :param message: 已發送的消息.
    """
    if message.author == bot.user or message.author.bot:
        return
    await bot.process_commands(message)

# on_command_completion: 當有指令完成時執行
@bot.event
async def on_command_completion(context: Context) -> None:
    """
    每次“成功”執行正常命令時都會執行此事件中的代碼。

    :param context: 已執行命令的上下文.
    """
    full_command_name = context.command.qualified_name
    split = full_command_name.split(" ")
    executed_command = str(split[0])
    if context.guild is not None:
        bot.logger.info(
            f"Executed {executed_command} command in {context.guild.name} (ID: {context.guild.id}) by {context.author} (ID: {context.author.id})"
        )
    else:
        bot.logger.info(
            f"Executed {executed_command} command by {context.author} (ID: {context.author.id}) in DMs"
        )

# on_command_error: 當有指令錯誤時執行
@bot.event
async def on_command_error(context: Context, error) -> None:
    """
    每次正常的有效命令捕獲錯誤時都會執行此事件中的代碼.

    :param context: 執行失敗的正常命令的上下文.
    :param error: 所遇到的錯誤。
    """
    if isinstance(error, commands.CommandOnCooldown):
        minutes, seconds = divmod(error.retry_after, 60)
        hours, minutes = divmod(minutes, 60)
        hours = hours % 24
        embed = discord.Embed(
            description=f"**Please slow down** - You can use this command again in {f'{round(hours)} hours' if round(hours) > 0 else ''} {f'{round(minutes)} minutes' if round(minutes) > 0 else ''} {f'{round(seconds)} seconds' if round(seconds) > 0 else ''}.",
            color=0xE02B2B,
        )
        await context.send(embed=embed)
    elif isinstance(error, exceptions.UserBlacklisted):
        """
        僅當錯誤是“UserBlacklisted”的實例時才會執行此處的代碼,這可能在使用時發生
        @checks.not_blacklisted() 檢查你的命令，或者你可以自己提出錯誤.
        """
        embed = discord.Embed(
            description="You are blacklisted from using the bot!", color=0xE02B2B
        )
        await context.send(embed=embed)
        if context.guild:
            bot.logger.warning(
                f"{context.author} (ID: {context.author.id}) tried to execute a command in the guild {context.guild.name} (ID: {context.guild.id}), but the user is blacklisted from using the bot."
            )
        else:
            bot.logger.warning(
                f"{context.author} (ID: {context.author.id}) tried to execute a command in the bot's DMs, but the user is blacklisted from using the bot."
            )
    elif isinstance(error, exceptions.UserNotOwner):
        """
        與上面相同，僅用於 @checks.is_owner() 檢查.
        """
        embed = discord.Embed(
            description="You are not the owner of the bot!", color=0xE02B2B
        )
        await context.send(embed=embed)
        if context.guild:
            bot.logger.warning(
                f"{context.author} (ID: {context.author.id}) tried to execute an owner only command in the guild {context.guild.name} (ID: {context.guild.id}), but the user is not an owner of the bot."
            )
        else:
            bot.logger.warning(
                f"{context.author} (ID: {context.author.id}) tried to execute an owner only command in the bot's DMs, but the user is not an owner of the bot."
            )
    elif isinstance(error, commands.MissingPermissions):
        embed = discord.Embed(
            description="You are missing the permission(s) `"
            + ", ".join(error.missing_permissions)
            + "` to execute this command!",
            color=0xE02B2B,
        )
        await context.send(embed=embed)
    elif isinstance(error, commands.BotMissingPermissions):
        embed = discord.Embed(
            description="I am missing the permission(s) `"
            + ", ".join(error.missing_permissions)
            + "` to fully perform this command!",
            color=0xE02B2B,
        )
        await context.send(embed=embed)
    elif isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(
            title="Error!",
            # 我們需要大寫，因為命令參數在代碼中沒有大寫字母。
            description=str(error).capitalize(),
            color=0xE02B2B,
        )
        await context.send(embed=embed)
    else:
        raise error

# 載入cogs
async def load_cogs() -> None:
    """
    每當機器人啟動時都會執行此函數中的代碼.
    """
    for file in os.listdir(f"{os.path.realpath(os.path.dirname(__file__))}/cogs"):
        if file.endswith(".py"):
            extension = file[:-3]
            try:
                await bot.load_extension(f"cogs.{extension}")
                bot.logger.info(f"Loaded extension '{extension}'")
            except Exception as e:
                exception = f"{type(e).__name__}: {e}"
                bot.logger.error(f"Failed to load extension {extension}\n{exception}")

# 執行bot
asyncio.run(init_db())
asyncio.run(load_cogs())
bot.run(config["token"])
