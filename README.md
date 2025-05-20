# ChatGPT Discord Bot

中文 | [English](README.en.md)

[![license](https://img.shields.io/pypi/l/ansicolortags.svg)](LICENSE) [![Release](https://img.shields.io/github/v/release/TheExplainthis/ChatGPT-Discord-Bot)](https://github.com/TheExplainthis/ChatGPT-Discord-Bot/releases/)


ChatGPT 串接到 Discord 上面，使得團隊在協作、溝通、效率上都能夠快速的提升，根據下面的安裝步驟，你也能在自己的 Discord 當中去導入 ChatGPT。

## 更新
- 2023/03/03 模型換成 chat completion: `gpt-3.5-turbo`


## 介紹
在 Discord 裡的每個頻道中導入 ChatGPT Bot，只要在輸入框輸入 `/chat` 就會 有一個 `/chat message` 的關鍵字自動帶入，直接輸入文字即可與 ChatGPT 互動，如下圖所示：
![Demo](https://github.com/TheExplainthis/ChatGPT-Discord-Bot/blob/main/demo/chatgpt-discord-bot.gif)


## 安裝步驟
### Token 取得
1. 取得 OpenAI 給的 API Token：
    1. [OpenAI](https://beta.openai.com/) 平台中註冊/登入帳號
    2. 右上方有一個頭像，點入後選擇 `View API keys`
    3. 點選中間的 `Create new secret key`
    - 注意：每隻 API 有免費額度，也有其限制，詳情請看 [OpenAI Pricing](https://openai.com/api/pricing/)
2. 取得 Discord Token：
    1. 登入 [Discord Developer](https://discord.com/developers/applications)
    2. 創建機器人：
        1. 進入左方 `Applications`
        2. 點擊右上方 `New Application` 並輸入 Bot 的名稱 > 確認後進入新頁面。
        3. 點擊左方 `Bot`
        4. 點擊右方 `Add Bot`
        5. 下方 `MESSAGE CONTENT INTENT` 需打開 
        6. 按下 `Save Change`
        7. Token 在上方選擇 `View Token` 或已申請過則會是 `Reset Token` 的按鈕。
    3. 設定 OAuth2
        1. 點擊左欄 `OAuth2`
        2. 點擊左欄 `URL Generator`
        3. 右欄 `SCOPES` 選擇 `bot`、右欄下方 `BOT PERMISSIONS` 選擇 `Administrator`
        4. 複製最下方網址到瀏覽器中
        5. 選擇欲加入的伺服器
        6. 按下 `繼續` > `授權`

## 运行

`docker run --name -d discord-bot -e SYSTEM_MESSAGE="You are a helpful assistant." -e DISCORD_TOKEN="xxxxxxxx-asQ" -e OPENAI_MODEL_ENGINE="xxxx" -e OPENAI_API="xxxx" -e BASE_URL="https://xxxx/api/v3" jp0id/ai-discord-bot:latest`

## 指令
| 指令 | 說明 |
| --- | ----- |
| `/chat` | 在輸入框直接輸入 `/chat` 會後綴 `message` 直接輸入文字，即可調用 ChatGPT 模型。|
| `/reset` | ChatGPT 會記住前十次的問答紀錄，調用此指令則會清除。|

## 支持我們
如果你喜歡這個專案，願意[支持我們](https://www.buymeacoffee.com/explainthis)，可以請我們喝一杯咖啡，這會成為我們繼續前進的動力！

[<a href="https://www.buymeacoffee.com/explainthis" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" height="45px" width="162px" alt="Buy Me A Coffee"></a>](https://www.buymeacoffee.com/explainthis)


## 相關專案
- [chatGPT-discord-bot](https://github.com/Zero6992/chatGPT-discord-bot)

## 授權
[MIT](LICENSE)
