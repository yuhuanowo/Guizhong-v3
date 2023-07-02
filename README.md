![cover](https://www.yuhuanstudio.tech/github.png)

------------------------------------
<p align="center">
  <h2 align="center">歸終</h2>
  <p align="center">
    一個基於discord.py的discord機器人
    <br/>
    <br/>
    <a href="https://docs.yuhuanstudio.tech"><strong>» 查看使用教程 »</strong></a>
    <br/>
  </p>
</p>

<p align="center">

<a href="https://discord.gg/GfUY7ynvXN"><img src="https://img.shields.io/discord/606104244101185558?color=E2CDBC&amp;logo=discord&amp;style=for-the-badge" alt="Discord"></a>
<a href="https://github.com/yuhuanowo/Guizhong-v3/stargazers"><img src="https://img.shields.io/github/stars/yuhuanowo/Guizhong-v3?color=E2CDBC&amp;logo=github&amp;style=for-the-badge" alt="Github stars"></a>
<a href="https://github.com/yuhuanowo/Guizhong-v3/releases" alt="GitHub release"><img src="https://img.shields.io/github/v/release/yuhuanowo/Guizhong-v3?color=E2CDBC&amp;logo=github&amp;style=for-the-badge"></a>
<a href="https://github.com/yuhuanowo/Guizhong-v3"><img src="https://img.shields.io/github/languages/code-size/yuhuanowo/Guizhong-v3?color=E2CDBC&amp;logo=github&amp;style=for-the-badge" alt="GitHub code size in bytes"></a>
<a href="./LICENSE"><img src="https://img.shields.io/github/license/lss233/chatgpt-mirai-qq-bot?&amp;color=E2CDBC&amp;style=for-the-badge" alt="License"></a>
</p>

***

* [Discord ](https://discord.gg/GfUY7ynvXN)
* [官方網站](https://www.yuhuanstudio.tech)

發布最新的項目動態、視頻教程、問題答疑和交流。

如果不能解決，把遇到的問題、**日誌**和配置文件準備好後再提問。

| ![幫助指令](https://img.shields.io/badge/-幫助指令-E2CDBC?style=for-the-badge)                     | ![待開發..](https://img.shields.io/badge/-待開發..-E2CDBC?style=for-the-badge)                   | ![待開發...](https://img.shields.io/badge/-待開發...-E2CDBC?style=for-the-badge)            |
|------------------------------|------------------------------|------------------------------|
| ![image]() | ![image]() | ![image]() |




**⚡ 功能**   
* [x] 幫助指令
* [x] 機器人狀態
* [x] 機器人邀請
* [x] 伺服器邀請
* [x] 伺服器資訊
* [x] 伺服器成員
* [x] 一句沒用的話

**📝 待開發**
* [ ] 音樂功能

## 🐎 命令

**你可以在 [Wiki](https://docs.yuhuanstudio.tech) 了解机器人的内部命令。**  


## 🔧 搭建

此存儲庫現在是一個機器人

您可以執行以下操作：

* 克隆/下載存儲庫y
    * 要克隆它並獲取更新，您絕對可以使用以下命令
      `git clone`
* 創建一個discord機器人 [here](https://discord.com/developers/applications)
* 獲取您的機器人令牌
* 使用以下邀請在服務器上邀請您的機器人:
  https://discord.com/oauth2/authorize?&client_id=YOUR_APPLICATION_ID_HERE&scope=bot+applications.commands&permissions=PERMISSIONS (
  替代 `YOUR_APPLICATION_ID_HERE` 與應用程序 ID 並替換 `PERMISSIONS` 具有所需的權限
你的機器人需要它能夠找到這個的底部
  page https://discord.com/developers/applications/YOUR_APPLICATION_ID_HERE/bot)

## 如何設置

為了設置機器人，我讓它盡可能簡單。我現在創建了一個[config.json](config.json) 您可以在其中放置需要編輯的內容的文件.

這是對一切的解釋：

| 變數                      | 這是什麼                                                              |
| ------------------------- | ----------------------------------------------------------------------|
| YOUR_BOT_PREFIX_HERE      | 您要用於普通命令的前綴                                                |
| YOUR_BOT_TOKEN_HERE       | 您的機器人的令牌                                                      |
| YOUR_BOT_PERMISSIONS_HERE | 您的機器人受到邀請時所需的權限整數                                     | 
| YOUR_APPLICATION_ID_HERE  | 您的機器人的應用程序 ID                                                |
| OWNERS                    | 所有機器人所有者的用戶 ID                                              |


## 如何開始

要啟動機器人，您只需啟動終端（Linux、Mac 和 Windows）或命令提示符（windows）
.

在運行機器人之前，您需要使用以下命令安裝所有要求：

```
python -m pip install -r requirements.txt
```

之後你可以開始它

```
python bot.py
```

> **注意**您可能需要將 `python` 替換為 `py`、`python3`、`python3.11` 等，具體取決於您在計算機上安裝的 Python 版本。

## 🎈 相關項目

如果你自己也有做機器人的想法，可以看看下面這些項目：
- [kkrypt0nn](https://github.com/kkrypt0nn/Python-Discord-Bot-Template) - 一個優秀的機器人模板

本項目基於以上項目開發，所以你可以給他們也點個 star ！

## 🛠 貢獻者名單   

歡迎提出新的點子、 Pull Request。

<a href="https://github.com/yuhuanowo/Guizhong-v3/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=yuhuanowo/Guizhong-v3" />
</a>

## 💪 支持我们

如果我們這個項目對你有所幫助，請給我們一顆 ⭐️3

## 📝 執照

該項目已獲得 Apache License 2.0 許可 -有關詳細信息，請參閱 [LICENSE.md](LICENSE.md) 文件

