#
# Copyright (C) 2021-2022 by TeamYukki@Github, < https://github.com/TeamYukki >.
#
# This file is part of < https://github.com/TeamYukki/YukkiMusicBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TeamYukki/YukkiMusicBot/blob/master/LICENSE >
#
# All rights reserved.

import re
import sys
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get it from my.telegram.org
API_ID = int(getenv("29791926", ""))
API_HASH = getenv("550ae225aaa88c599cf71983f40c86ac")

## Get it from @Botfather in Telegram.
BOT_TOKEN = getenv("8077218683:AAEkLo0oU38g_TiwVjMSJ299B3zCklHRNrM")

# Database to save your chats and stats... Get MongoDB:-  https://telegra.ph/How-To-get-Mongodb-URI-04-06
MONGO_DB_URI = getenv("mongodb+srv://HKMUSIC:<db_HKMUSIC@cluster0.vo9ib.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0", None)

# Custom max audio(music) duration for voice chat. set DURATION_LIMIT in variables with your own time(mins), Default to 60 mins.
DURATION_LIMIT_MIN = int(
    getenv("DURATION_LIMIT", "60")
)  # Remember to give value in Minutes

# Duration Limit for downloading Songs in MP3 or MP4 format from bot
SONG_DOWNLOAD_DURATION = int(
    getenv("SONG_DOWNLOAD_DURATION_LIMIT", "180")
)  # Remember to give value in Minutes

# You'll need a Private Group ID for this.
LOG_GROUP_ID = int(getenv("-4705565341", ""))

# A name for your Music bot.
MUSIC_BOT_NAME = getenv("HK MUSIC BOT")

# Your User ID.
OWNER_ID = list(
    map(int, getenv("6720017767", "").split())
)  # Input type must be interger

# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

# You have to Enter the app name which you gave to identify your  Music Bot in Heroku.
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")

# For customized or modified Repository
UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/TeamYukki/YukkiMusicBot",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")

# GIT TOKEN ( if your edited repo is private)
GIT_TOKEN = getenv("GIT_TOKEN", None)

# Only  Links formats are  accepted for this Var value.
SUPPORT_CHANNEL = getenv(
    "SUPPORT_CHANNEL", None
)  # Example:- https://t.me/hkmusic4
SUPPORT_GROUP = getenv(
    "SUPPORT_GROUP", None
)  # Example:- https://t.me/hkmusic4

# Set it in True if you want to leave your assistant after a certain amount of time. [Set time via AUTO_LEAVE_ASSISTANT_TIME]
AUTO_LEAVING_ASSISTANT = getenv("AUTO_LEAVING_ASSISTANT", None)

# Time after which you're assistant account will leave chats automatically.
AUTO_LEAVE_ASSISTANT_TIME = int(
    getenv("ASSISTANT_LEAVE_TIME", "5400")
)  # Remember to give value in Seconds

# Time after which bot will suggest random chats about bot commands.
AUTO_SUGGESTION_TIME = int(
    getenv("AUTO_SUGGESTION_TIME", "5400")
)  # Remember to give value in Seconds

# Set it True if you want to delete downloads after the music playout ends from your downloads folder
AUTO_DOWNLOADS_CLEAR = getenv("AUTO_DOWNLOADS_CLEAR", None)

# Set it True if you want to bot to suggest about bot commands to random chats of your bots.
AUTO_SUGGESTION_MODE = getenv("AUTO_SUGGESTION_MODE", None)

# Set it true if you want your bot to be private only [You'll need to allow CHAT_ID via /authorise command then only your bot will play music in that chat.]
PRIVATE_BOT_MODE = getenv("PRIVATE_BOT_MODE", None)

# Time sleep duration For Youtube Downloader
YOUTUBE_DOWNLOAD_EDIT_SLEEP = int(getenv("YOUTUBE_EDIT_SLEEP", "3"))

# Time sleep duration For Telegram Downloader
TELEGRAM_DOWNLOAD_EDIT_SLEEP = int(getenv("TELEGRAM_EDIT_SLEEP", "5"))

# Your Github Repo.. Will be shown on /start Command
GITHUB_REPO = getenv("GITHUB_REPO", None)

# Spotify Client.. Get it from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("ff16281232b0423b853fcd77e56c431a", None)
SPOTIFY_CLIENT_SECRET = getenv("4b7f4f59a0ae4072a108ce9c65d416ee", None)

# Maximum number of video calls allowed on bot. You can later set it via /set_video_limit on telegram
VIDEO_STREAM_LIMIT = int(getenv("VIDEO_STREAM_LIMIT", "3"))

# Maximum Limit Allowed for users to save playlists on bot's server
SERVER_PLAYLIST_LIMIT = int(getenv("SERVER_PLAYLIST_LIMIT", "30"))

# MaximuM limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", "25"))

# Cleanmode time after which bot will delete its old messages from chats
CLEANMODE_DELETE_MINS = int(
    getenv("CLEANMODE_MINS", "5")
)  # Remember to give value in Seconds


# Telegram audio  and video file size limit

TG_AUDIO_FILESIZE_LIMIT = int(
    getenv("TG_AUDIO_FILESIZE_LIMIT", "104857600")
)  # Remember to give value in bytes

TG_VIDEO_FILESIZE_LIMIT = int(
    getenv("TG_VIDEO_FILESIZE_LIMIT", "1073741824")
)  # Remember to give value in bytes

# Chceckout https://www.gbmb.org/mb-to-bytes  for converting mb to bytes

# If you want your bot to setup the commands automatically in the bot's menu set it to true.
# Refer to https://i.postimg.cc/Bbg3LQTG/image.png
SET_CMDS = getenv("SET_CMDS", False)

# You'll need a Pyrogram String Session for these vars. Generate String from our session generator bot @YukkiStringBot
STRING1 = getenv("BQHGlrYAuZYGy94y-unYeJ-pExVSxQ-bztKgY7XHmrKU1jQb6M_5Zqqm2VR6COl-v3hYDo8an85h6K7RxxY6Xzcj-1zhLOYhEM6BWXiiBmr7GPA24SsTmMglKnEGX0GJg_4YBaxCOfaHCvzLl806OCGFUxgw3NrWK_tkpwxjMMI4tRLL2qYwUgwcUKd-Qc3IbgOj61_mOB4mbJMXkT6aapw0m3XcCCElhZIiQIclnsMqmh8JZLeNPu-Zrt8yI78MememPj-F3dbY-PEhomr2wg3MJTcczAzJuO_3YRz1NTXb97FaKNuZal7GVoRuYjiav5gEytVxg4ZqKLzi3v-HGhYcsPdD9gAAAAGQi1VnAA", None)
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


#  __     ___    _ _  ___  _______   __  __ _    _  _____ _____ _____   ____   ____ _______
#  \ \   / / |  | | |/ / |/ /_   _| |  \/  | |  | |/ ____|_   _/ ____| |  _ \ / __ \__   __|
#   \ \_/ /| |  | | ' /| ' /  | |   | \  / | |  | | (___   | || |      | |_) | |  | | | |
#    \   / | |  | |  < |  <   | |   | |\/| | |  | |\___ \  | || |      |  _ <| |  | | | |
#     | |  | |__| | . \| . \ _| |_  | |  | | |__| |____) |_| || |____  | |_) | |__| | | |
#     |_|   \____/|_|\_\_|\_\_____| |_|  |_|\____/|_____/|_____\_____| |____/ \____/  |_|


### DONT TOUCH or EDIT codes after this line
BANNED_USERS = filters.user()
YTDOWNLOADER = 1
LOG = 2
LOG_FILE_NAME = "Yukkilogs.txt"
adminlist = {}
lyrical = {}
chatstats = {}
userstats = {}
clean = {}

autoclean = []


# Images
START_IMG_URL = getenv("https://imagekit.io/tools/asset-public-link?detail=%7B%22name%22%3A%22b143f84feb666349700b99168db9aee3.jpg%22%2C%22type%22%3A%22image%2Fjpeg%22%2C%22signedurl_expire%22%3A%222028-03-24T06%3A24%3A32.150Z%22%2C%22signedUrl%22%3A%22https%3A%2F%2Fmedia-hosting.imagekit.io%2F%2F14556c5680ca4f51%2Fb143f84feb666349700b99168db9aee3.jpg%3FExpires%3D1837491872%26Key-Pair-Id%3DK2ZIVPTIP2VGHC%26Signature%3Dt1mXeA4JvjLTeDBOQmTWB1ta17MnYxtfSDKJ-3lFRPhL0Y-4iXCXKOmNljamgUXVEbUmG2hkEIQTRr-oVyAi4EB3kAbzjZ2aS~fR6N17jFU-sMPVTCWPt~j8NMVuu6KcMlqxQoEVi9BU4fvsML~ekt5WoMGrxos~e6BUvvTWd78nLD5LrUnJHYcc~FB8pK1C44Mp4PEqa-iJsvzYTPOshGdKHdSRYxg71v0BJH6QTOc-ui5TVWVrAbGuP9Pqc8mOAx0w87iXteIcdjneXXgj-mYW40w~cpuhof75vrtLUmBwRQvo8XRSAdE6trOoXBa7622HXtfPp1R29vxLbrleNQ__%22%7D", None)

PING_IMG_URL = getenv(
    "https://imagekit.io/tools/asset-public-link?detail=%7B%22name%22%3A%2299a178bee3952e9fe7e3313f4af5b550.jpg%22%2C%22type%22%3A%22image%2Fjpeg%22%2C%22signedurl_expire%22%3A%222028-03-24T06%3A27%3A26.129Z%22%2C%22signedUrl%22%3A%22https%3A%2F%2Fmedia-hosting.imagekit.io%2F%2F900bd7bd0d064698%2F99a178bee3952e9fe7e3313f4af5b550.jpg%3FExpires%3D1837492046%26Key-Pair-Id%3DK2ZIVPTIP2VGHC%26Signature%3DzS89l8F84mSfn7ElF4~j~gytIfyaRPQNN3WYs9lr7hfWGf8fNEJFoLwkzNvXTJoMQgfRnLey0kZoTky1-wbl0YpI1Ob~bGN93J0Ed86BDZhaCONJB4rpViHQR5P5MPrJ3btA6Sj2E8fCqfuYXArj5Lu7k-1dey6MZevNZ6ftBmWKPLLyqCi91JYrzb~xWDRihzyuTwPcwXPkaOrlEKbbnUblsBCJ99CZoVyYgt46BPHSib1KL1E930yDFxXCKAkLP~rM~1qNHnLblYSKtoqPeI9~La5Z4pk9hZj6C1jzhywWZXMuCbRu8MEjJWHHQ0tC3XIU4H9~FXKx4gbcLU74zg__%22%7D",
    "assets/Ping.jpeg",
)

PLAYLIST_IMG_URL = getenv(
    "https://imagekit.io/tools/asset-public-link?detail=%7B%22name%22%3A%2262e54b54e32a50dc07bc207f4ceee9d9.jpg%22%2C%22type%22%3A%22image%2Fjpeg%22%2C%22signedurl_expire%22%3A%222028-03-24T06%3A28%3A13.209Z%22%2C%22signedUrl%22%3A%22https%3A%2F%2Fmedia-hosting.imagekit.io%2F%2F514cb6868c454f37%2F62e54b54e32a50dc07bc207f4ceee9d9.jpg%3FExpires%3D1837492093%26Key-Pair-Id%3DK2ZIVPTIP2VGHC%26Signature%3DXyN-P2qs1bCwb4y70~VTpYNK8ODjCkIB8mqWb2NLHvmEHOCaRD5w8heL-Mp16yx4Wxp7xOcUygyrbju9c3GxSP39gmybs3A1XpPNAhTtP8HpBqf~faiGQHLj4wJQw8WvPCnP0bwMRPmhr5oFYpiyZ~VzAE9X0F2hwkDEqPK5K6Pfk9ORhel-vxjZ2hLfPY6pdLL~LLyRcbqWSAvZA7h9o8rIBGyVHLFxw5fBGcAWzqDLG5M8f5StBsX4kbWzl8-B5WUVCa9QTtx-MNmvL-R7-uU80JFomzR4Z5T2~dpx4qlYSaE7~SlWyh9NsfYxtKPwy~osyiKehUr9iRhHdpkbVg__%22%7D",
    "assets/Playlist.jpeg",
)

GLOBAL_IMG_URL = getenv(
    "https://imagekit.io/tools/asset-public-link?detail=%7B%22name%22%3A%22d245a484765feb05098cbb825b41e0a8.jpg%22%2C%22type%22%3A%22image%2Fjpeg%22%2C%22signedurl_expire%22%3A%222028-03-24T06%3A28%3A53.922Z%22%2C%22signedUrl%22%3A%22https%3A%2F%2Fmedia-hosting.imagekit.io%2F%2Fbd7a4054124f4c15%2Fd245a484765feb05098cbb825b41e0a8.jpg%3FExpires%3D1837492134%26Key-Pair-Id%3DK2ZIVPTIP2VGHC%26Signature%3DUrS49qJR0FpPutrkaZX6v2RyMNFsVCGWcpYkD6MrcbvM3ay~kGQiKwvWH5UGyYngllebV8BDCDkNcwRU~GEh09smEQgvCLNbTFUfD0nNJ3pmDu8LwOneTp2Jm6ro~AzkFtMp6RZOgRqk~GAVF0RpsDeNz-hxNEJuynBhkEqWwvbk6jiPIPTwDXKwRI5XE3MlUNJePl~pRRdkvAjqPOLedIV-N-FZUP0~2znRFNHeqTXdT756ztX5zgm7Wj6FJyeKuh8IvId3pwU0vOgzshiY~IMO~Fat9FQq4M1O4F9jPDn2UWOBvQXjA2UWxonpNnbXk9HxlTdtvdvrUjwZYwQ1WQ__%22%7D",
    "assets/Global.jpeg",
)

STATS_IMG_URL = getenv(
    "https://imagekit.io/tools/asset-public-link?detail=%7B%22name%22%3A%22d56d6feb2b36091e2c12f9bd8b541972.jpg%22%2C%22type%22%3A%22image%2Fjpeg%22%2C%22signedurl_expire%22%3A%222028-03-24T06%3A29%3A26.154Z%22%2C%22signedUrl%22%3A%22https%3A%2F%2Fmedia-hosting.imagekit.io%2F%2F95a82013db3b4712%2Fd56d6feb2b36091e2c12f9bd8b541972.jpg%3FExpires%3D1837492166%26Key-Pair-Id%3DK2ZIVPTIP2VGHC%26Signature%3DSA0Olin4Bezi5XbNAzqFZfie~CRS~u2SucCGgr1qQi4zViqUS0l7hKdEYepv5WSVYjYY1fEZezfE9kMkF0ajTKtMrYZVc~SqFS8CMQ16CgEB0hpTI71~ptwXgppHOWhzAcSWt96sHfw7S335zMBbbROM8jeCDmg1G3Myru6Xo8Nmv~mRttJiX-ReoXB7bXzpQV5Z9YBbtD3SBmGFLmT~jssIqW0hNX4qX2P~4VKsGl1yYifLQYBnYVFwJUU6uE3oordYOxlXy9wF0OFUF1cVL~pkGOAN5RwUebSMwQfCLix-3g3PhCo7yIfydw0XO99uu1lecD8ZiAP6qA7d-9-ZUw__%22%7D",
    "assets/Stats.jpeg",
)

TELEGRAM_AUDIO_URL = getenv(
    "AgADwhkAApkGEFc",
    "assets/Audio.jpeg",
)

TELEGRAM_VIDEO_URL = getenv(
    "AAMCBQADGQEB5Eo3Z-JQE4oeimOnlZRUOJdvbAzS8yQAAsMZAAKZBhBXvbhdnqhJZgIBAAdtAAM2BA",
    "assets/Video.jpeg",
)

STREAM_IMG_URL = getenv(
    "https://imagekit.io/tools/asset-public-link?detail=%7B%22name%22%3A%22d245a484765feb05098cbb825b41e0a8.jpg%22%2C%22type%22%3A%22image%2Fjpeg%22%2C%22signedurl_expire%22%3A%222028-03-24T06%3A28%3A53.922Z%22%2C%22signedUrl%22%3A%22https%3A%2F%2Fmedia-hosting.imagekit.io%2F%2Fbd7a4054124f4c15%2Fd245a484765feb05098cbb825b41e0a8.jpg%3FExpires%3D1837492134%26Key-Pair-Id%3DK2ZIVPTIP2VGHC%26Signature%3DUrS49qJR0FpPutrkaZX6v2RyMNFsVCGWcpYkD6MrcbvM3ay~kGQiKwvWH5UGyYngllebV8BDCDkNcwRU~GEh09smEQgvCLNbTFUfD0nNJ3pmDu8LwOneTp2Jm6ro~AzkFtMp6RZOgRqk~GAVF0RpsDeNz-hxNEJuynBhkEqWwvbk6jiPIPTwDXKwRI5XE3MlUNJePl~pRRdkvAjqPOLedIV-N-FZUP0~2znRFNHeqTXdT756ztX5zgm7Wj6FJyeKuh8IvId3pwU0vOgzshiY~IMO~Fat9FQq4M1O4F9jPDn2UWOBvQXjA2UWxonpNnbXk9HxlTdtvdvrUjwZYwQ1WQ__%22%7D",
    "assets/Stream.jpeg",
)

SOUNCLOUD_IMG_URL = getenv(
    "https://imagekit.io/tools/asset-public-link?detail=%7B%22name%22%3A%22d56d6feb2b36091e2c12f9bd8b541972.jpg%22%2C%22type%22%3A%22image%2Fjpeg%22%2C%22signedurl_expire%22%3A%222028-03-24T06%3A29%3A26.154Z%22%2C%22signedUrl%22%3A%22https%3A%2F%2Fmedia-hosting.imagekit.io%2F%2F95a82013db3b4712%2Fd56d6feb2b36091e2c12f9bd8b541972.jpg%3FExpires%3D1837492166%26Key-Pair-Id%3DK2ZIVPTIP2VGHC%26Signature%3DSA0Olin4Bezi5XbNAzqFZfie~CRS~u2SucCGgr1qQi4zViqUS0l7hKdEYepv5WSVYjYY1fEZezfE9kMkF0ajTKtMrYZVc~SqFS8CMQ16CgEB0hpTI71~ptwXgppHOWhzAcSWt96sHfw7S335zMBbbROM8jeCDmg1G3Myru6Xo8Nmv~mRttJiX-ReoXB7bXzpQV5Z9YBbtD3SBmGFLmT~jssIqW0hNX4qX2P~4VKsGl1yYifLQYBnYVFwJUU6uE3oordYOxlXy9wF0OFUF1cVL~pkGOAN5RwUebSMwQfCLix-3g3PhCo7yIfydw0XO99uu1lecD8ZiAP6qA7d-9-ZUw__%22%7D",
    "assets/Soundcloud.jpeg",
)

YOUTUBE_IMG_URL = getenv(
    "https://imagekit.io/tools/asset-public-link?detail=%7B%22name%22%3A%223dc70fe88c2cb49d62b91a8cf4b4fae6.jpg%22%2C%22type%22%3A%22image%2Fjpeg%22%2C%22signedurl_expire%22%3A%222028-03-24T06%3A30%3A45.848Z%22%2C%22signedUrl%22%3A%22https%3A%2F%2Fmedia-hosting.imagekit.io%2F%2F6eb612451b664e75%2F3dc70fe88c2cb49d62b91a8cf4b4fae6.jpg%3FExpires%3D1837492246%26Key-Pair-Id%3DK2ZIVPTIP2VGHC%26Signature%3Djvtd~cbgiChpMRlaTrEvvFXJKnWDK7E2AAfVtzZnHfCCg8xI4BLEnOBuvAn791lkplgD9MrsMh2YAP07TLuJdrQql-2EgSLawDPJbqLbQCOAIHam8oCjDF4km-pdC9jzcuhVx3i7fA3thg3yC2GWpreAG3alNfpeGfubM14Ih94mQY4jTm9jhzUl3SnHy8uMvR-PrXlCFp4EiOV4FlTFCK-JTeYPRdwzDG8~TUsmDpfH4GXBaLBoIoLE2xBrXbcWcucPCJLE0r8s2kO1DakFuAUWIf0kH-7tNv4c~HYZnJHrxqePf4ShFLQJOqIcr61-IuQ7vi4htRN28Z~WpIag~A__%22%7D",
    "assets/Youtube.jpeg",
)

SPOTIFY_ARTIST_IMG_URL = getenv(
    "https://imagekit.io/tools/asset-public-link?detail=%7B%22name%22%3A%2208929cd487b958e3f6975a7c23f143f4.jpg%22%2C%22type%22%3A%22image%2Fjpeg%22%2C%22signedurl_expire%22%3A%222028-03-24T06%3A31%3A35.445Z%22%2C%22signedUrl%22%3A%22https%3A%2F%2Fmedia-hosting.imagekit.io%2F%2F9da280c5ffbd4e4e%2F08929cd487b958e3f6975a7c23f143f4.jpg%3FExpires%3D1837492295%26Key-Pair-Id%3DK2ZIVPTIP2VGHC%26Signature%3DbSSQNL3TI0zbDddiDqhgIHooSyVilBbz4~Pu94Tv77Y639ye3dj~WXlry4M4Cg~7LW2HJriYmiIl6BLulcU~rNlAoHv~vGEapbF0nJr0CkHkxBInrgYYdGg4-rZ6bE2jWwXDuef~0cPTyANiwxbEj5jbQSYi~qoZbi~d8vaQttO~UloSt7-yAA7OlQQUrOq58tfHU03GbZdAh6D0ZXqXQrzpDDql1Y0oXK1lNPwyRIhuh5bm7qLpLVb5bjc6Fa8jcHeG9ALftro~CGAxcF2bpexJFV1HFsbcSg7u2GfNPq6fbzGw-LbptaaVevu9guo0Y5zOv5QtRLIN0URfmGPWiA__%22%7D",
    "assets/SpotifyArtist.jpeg",
)

SPOTIFY_ALBUM_IMG_URL = getenv(
    "https://imagekit.io/tools/asset-public-link?detail=%7B%22name%22%3A%223a136589b6087156cf280a65cc88089b.jpg%22%2C%22type%22%3A%22image%2Fjpeg%22%2C%22signedurl_expire%22%3A%222028-03-24T06%3A31%3A35.443Z%22%2C%22signedUrl%22%3A%22https%3A%2F%2Fmedia-hosting.imagekit.io%2F%2F156801a022a4442e%2F3a136589b6087156cf280a65cc88089b.jpg%3FExpires%3D1837492295%26Key-Pair-Id%3DK2ZIVPTIP2VGHC%26Signature%3DW-LYP9op1~U0S~qUultGqSuezPKhKP5A~GJ9JiocIVDh0Xok20wBwUhWKZAhrZQrq~HdwQDxG7cHgqmOyi2F7dVmONgJVfIWlot9v-eKT8Rk~i16VFBjsg1oOBTSICAHkpmZCrrz51hI-jLnYNFhpih01nULLU8M7OQCp37~7U2R8BBCgJzJ1g8h29fK3gWLsq10HvfxlIzV74u4UyVG7ckEN4HB24nkBjB7jTVK8BJc0TGryUN3rtzEtOA1VVYdjReoYPPvn7ylHomuYc~iuuIxem2pI5hZUoKjaJ1JUaL9KGo-jB02u99V72K~~D-j1Q3z0ZbCwt3SlE2MejUMsA__%22%7D",
    "assets/SpotifyAlbum.jpeg",
)

SPOTIFY_PLAYLIST_IMG_URL = getenv(
    "https://imagekit.io/tools/asset-public-link?detail=%7B%22name%22%3A%229f05abb4dde3d1d692ec69a8487e8fcb.jpg%22%2C%22type%22%3A%22image%2Fjpeg%22%2C%22signedurl_expire%22%3A%222028-03-24T06%3A31%3A35.438Z%22%2C%22signedUrl%22%3A%22https%3A%2F%2Fmedia-hosting.imagekit.io%2F%2Fd05e9ef333344246%2F9f05abb4dde3d1d692ec69a8487e8fcb.jpg%3FExpires%3D1837492295%26Key-Pair-Id%3DK2ZIVPTIP2VGHC%26Signature%3DAv-RD-wDPQ80pODe49VgVUgvHyBFd9-k-qce9M2zVSdgxcEqTHKETz6yJQ84US6yfoqPIwWzAaq855~rh6keCkYpWcNMFlw0YAQnCjA1L1vh674wgYYLaZbh-2HUgoBON2suaZ2eITDQIGFKpjJTXiFbMKTu4byCkMTinAv0NMqaT3U8JX4m8uRZ2IEdKC-k4i6iMeTV61WgPbKD9TeeuMSe9bX9XCWw8EjUnbsQ4MqHFjEv~QJ6jZ6rXlrjQbPwVmm10fVLA6iZ3OFpvSFw1ci2JxWs-TCYKWdhVFa-oaUNnWfPzmNd-ugvK99y0WgqDM2pKhW-3BM4ptqnW3HV0Q__%22%7D",
    "assets/SpotifyPlaylist.jpeg",
)


def time_to_seconds(time):
    stringt = str(time)
    return sum(
        int(x) * 60**i
        for i, x in enumerate(reversed(stringt.split(":")))
    )


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))
SONG_DOWNLOAD_DURATION_LIMIT = int(
    time_to_seconds(f"{SONG_DOWNLOAD_DURATION}:00")
)

if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        print(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )
        sys.exit()

if SUPPORT_GROUP:
    if not re.match("(?:http|https)://", SUPPORT_GROUP):
        print(
            "[ERROR] - Your SUPPORT_GROUP url is wrong. Please ensure that it starts with https://"
        )
        sys.exit()

if UPSTREAM_REPO:
    if not re.match("(?:http|https)://", UPSTREAM_REPO):
        print(
            "[ERROR] - Your UPSTREAM_REPO url is wrong. Please ensure that it starts with https://"
        )
        sys.exit()

if GITHUB_REPO:
    if not re.match("(?:http|https)://", GITHUB_REPO):
        print(
            "[ERROR] - Your GITHUB_REPO url is wrong. Please ensure that it starts with https://"
        )
        sys.exit()


if PING_IMG_URL:
    if PING_IMG_URL != "assets/Ping.jpeg":
        if not re.match("(?:http|https)://", PING_IMG_URL):
            print(
                "[ERROR] - Your PING_IMG_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()

if PLAYLIST_IMG_URL:
    if PLAYLIST_IMG_URL != "assets/Playlist.jpeg":
        if not re.match("(?:http|https)://", PLAYLIST_IMG_URL):
            print(
                "[ERROR] - Your PLAYLIST_IMG_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()

if GLOBAL_IMG_URL:
    if GLOBAL_IMG_URL != "assets/Global.jpeg":
        if not re.match("(?:http|https)://", GLOBAL_IMG_URL):
            print(
                "[ERROR] - Your GLOBAL_IMG_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()


if STATS_IMG_URL:
    if STATS_IMG_URL != "assets/Stats.jpeg":
        if not re.match("(?:http|https)://", STATS_IMG_URL):
            print(
                "[ERROR] - Your STATS_IMG_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()


if TELEGRAM_AUDIO_URL:
    if TELEGRAM_AUDIO_URL != "assets/Audio.jpeg":
        if not re.match("(?:http|https)://", TELEGRAM_AUDIO_URL):
            print(
                "[ERROR] - Your TELEGRAM_AUDIO_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()


if STREAM_IMG_URL:
    if STREAM_IMG_URL != "assets/Stream.jpeg":
        if not re.match("(?:http|https)://", STREAM_IMG_URL):
            print(
                "[ERROR] - Your STREAM_IMG_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()


if SOUNCLOUD_IMG_URL:
    if SOUNCLOUD_IMG_URL != "assets/Soundcloud.jpeg":
        if not re.match("(?:http|https)://", SOUNCLOUD_IMG_URL):
            print(
                "[ERROR] - Your SOUNCLOUD_IMG_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()

if YOUTUBE_IMG_URL:
    if YOUTUBE_IMG_URL != "assets/Youtube.jpeg":
        if not re.match("(?:http|https)://", YOUTUBE_IMG_URL):
            print(
                "[ERROR] - Your YOUTUBE_IMG_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()


if TELEGRAM_VIDEO_URL:
    if TELEGRAM_VIDEO_URL != "assets/Video.jpeg":
        if not re.match("(?:http|https)://", TELEGRAM_VIDEO_URL):
            print(
                "[ERROR] - Your TELEGRAM_VIDEO_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()


if not MUSIC_BOT_NAME.isascii():
    print(
        "[ERROR] - You've defined MUSIC_BOT_NAME wrong. Please don't use any special characters or Special font for this... Keep it simple and small."
    )
    sys.exit()
