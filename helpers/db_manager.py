""""
Copyright © YuhuanStudio 2022-2023 - https://github.com/yuhuanowo (https://www.yuhuanstudio.tech)
描述:
🐍 一個可愛的機器人，用於幫助你的 Discord 伺服器。

Version: 0.0.1(beta)
"""

import os

import aiosqlite

# 數據庫路徑   # Path: helpers\db_manager.py
DATABASE_PATH = f"{os.path.realpath(os.path.dirname(__file__))}/../database/database.db"

#獲取所有黑名單用戶 (Get all blacklisted users) 
async def get_blacklisted_users() -> list:
    """
    該函數將返回所有列入黑名單的用戶的列表。

    :param user_id: 需要檢查的用戶ID。
    :return: 如果用戶被列入黑名單則為 True，否則為 False。
    """
    async with aiosqlite.connect(DATABASE_PATH) as db: # 連接數據庫
        async with db.execute( 
            "SELECT user_id, strftime('%s', created_at) FROM blacklist" # strftime('%s', created_at) 代表創建時間 (created_at) 的時間戳     
        ) as cursor:
            result = await cursor.fetchall() # 獲取所有結果 
            return result

#檢查用戶是否被列入黑名單 (Check if user is blacklisted)
async def is_blacklisted(user_id: int) -> bool:
    """
    該功能將檢查用戶是否被列入黑名單。

    :param user_id: 需要檢查的用戶ID。
    :return: 如果用戶被列入黑名單則為 True，否則為 False。
    """
    async with aiosqlite.connect(DATABASE_PATH) as db: # 連接數據庫
        async with db.execute(
            "SELECT * FROM blacklist WHERE user_id=?", (user_id,) # 檢查用戶是否被列入黑名單
        ) as cursor:
            result = await cursor.fetchone() # 獲取所有結果
            return result is not None 

#將用戶添加到黑名單 (Add user to blacklist)
async def add_user_to_blacklist(user_id: int) -> int:
    """
    T他的功能將根據黑名單中的 ID 添加用戶。

    :param user_id: 需要加入黑名單的用戶ID。
    """
    async with aiosqlite.connect(DATABASE_PATH) as db: # 連接數據庫
        await db.execute("INSERT INTO blacklist(user_id) VALUES (?)", (user_id,)) # 將用戶添加到黑名單
        await db.commit() # 提交更改
        rows = await db.execute("SELECT COUNT(*) FROM blacklist") # 獲取所有結果
        async with rows as cursor: 
            result = await cursor.fetchone() # 獲取所有結果
            return result[0] if result is not None else 0

#將用戶從黑名單中刪除 (Remove user from blacklist)
async def remove_user_from_blacklist(user_id: int) -> int:
    """
    此功能將根據用戶 ID 將用戶從黑名單中刪除。

    :param user_id: 需要從黑名單中刪除的用戶的ID。
    """
    async with aiosqlite.connect(DATABASE_PATH) as db:
        await db.execute("DELETE FROM blacklist WHERE user_id=?", (user_id,))
        await db.commit()
        rows = await db.execute("SELECT COUNT(*) FROM blacklist")
        async with rows as cursor:
            result = await cursor.fetchone()
            return result[0] if result is not None else 0

#增加警告 (Add warn)
async def add_warn(user_id: int, server_id: int, moderator_id: int, reason: str) -> int:
    """
    T他的功能將向數據庫添加警告。

    :param user_id: 需要警告的用戶ID。
    :param Reason: 應該警告用戶的原因。
    """
    async with aiosqlite.connect(DATABASE_PATH) as db:
        rows = await db.execute(
            "SELECT id FROM warns WHERE user_id=? AND server_id=? ORDER BY id DESC LIMIT 1",
            (
                user_id,
                server_id,
            ),
        )
        async with rows as cursor:
            result = await cursor.fetchone()
            warn_id = result[0] + 1 if result is not None else 1
            await db.execute(
                "INSERT INTO warns(id, user_id, server_id, moderator_id, reason) VALUES (?, ?, ?, ?, ?)",
                (
                    warn_id,
                    user_id,
                    server_id,
                    moderator_id,
                    reason,
                ),
            ) # 將用戶添加到黑名單
            await db.commit() # 提交更改
            return warn_id

#刪除警告 (Remove warn)
async def remove_warn(warn_id: int, user_id: int, server_id: int) -> int:
    """
    此函數將從數據庫中刪除警告。

    :param warn_id: 警告的 ID。
    :param user_id: 被警告的用戶的ID。
    :param server_id: 已警告用戶的服務器ID
    """
    async with aiosqlite.connect(DATABASE_PATH) as db:
        await db.execute(
            "DELETE FROM warns WHERE id=? AND user_id=? AND server_id=?",
            (
                warn_id,
                user_id,
                server_id,
            ),
        )
        await db.commit()
        rows = await db.execute(
            "SELECT COUNT(*) FROM warns WHERE user_id=? AND server_id=?",
            (
                user_id,
                server_id,
            ),
        )
        async with rows as cursor:
            result = await cursor.fetchone()
            return result[0] if result is not None else 0  # Path: helpers\db_manager.py 

#獲取所有警告 (Get all warns)
async def get_warnings(user_id: int, server_id: int) -> list:
    """
    該函數將獲取用戶的所有警告。

    :param user_id: 需要檢查的用戶ID。
    :param server_id: 需要檢查的服務器的ID。
    :return: 用戶所有警告的列表。
    """
    async with aiosqlite.connect(DATABASE_PATH) as db:
        rows = await db.execute(
            "SELECT user_id, server_id, moderator_id, reason, strftime('%s', created_at), id FROM warns WHERE user_id=? AND server_id=?",
            (
                user_id,
                server_id,
            ),
        )
        async with rows as cursor:
            result = await cursor.fetchall()
            result_list = []
            for row in result:
                result_list.append(row)
            return result_list
