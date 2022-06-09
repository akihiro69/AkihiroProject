# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.c (the "License");
# you may not use this file except in compliance with the License.
#
# Copyright (C) 2021 TeamUltroid for autobot
""" Userbot start point """

import sys
import requests
from importlib import import_module

from pytgcalls import idle

from userbot import BOT_TOKEN, BOT_VER, blacklistgeez
from userbot import DEVS, LOGS, LOOP, bot, call_py, BOTLOG_CHATID
from userbot.clients import geez_userbot_on, multigeez
from userbot.modules import ALL_MODULES
from userbot.utils import autobot, autocreategroup, checking

try:
    client = multigeez()
    total = 5 - client
    bot.start()
    call_py.start()
    user = bot.get_me()
    blacklistgeez = requests.get(
        "https://raw.githubusercontent.com/akihiro69/Reforestation/master/blacklistgeez.json"
    ).json()
    if user.id in blacklistgeez:
        LOGS.warning(
            "NAMPAKNYA USERBOT TIDAK DAPAT BEKERJA, MUNGKIN ANDA TELAH DI BLACKLIST OLEH PEMILIK USERBOT.\nCredits: @VckyouuBitch"        )
        sys.exit(1)
    if 874946835 not in DEVS:
        LOGS.warning(
            f"EOL\nGeezProjects v{BOT_VER}, Copyright © 2021-2022 VICKY <https://github.com/vckyou>"
        )
        sys.exit(1)
    if 655953567 not in DEVS:
        LOGS.warning(
            f"EOL\nAkihiroProject v{BOT_VER}, Copyright © 2021-2022 AKIHIRO69 <https://github.com/akihiro69>"
        )
        sys.exit(1)
except Exception as e:
    LOGS.info(str(e), exc_info=True)
    sys.exit(1)

for module_name in ALL_MODULES:
    imported_module = import_module("userbot.modules." + module_name)

LOGS.info(
    f"Join Grup https://t.me/AkihiroSupport"
)

LOGS.info(f"🍭 Akihiro - UserBot Berhasil Diaktifkan 🍭",
            )

LOOP.run_until_complete(geez_userbot_on())
LOOP.run_until_complete(checking())
if not BOTLOG_CHATID:
    LOOP.run_until_complete(autocreategroup())
if not BOT_TOKEN:
    LOOP.run_until_complete(autobot())
idle()
if len(sys.argv) not in (1, 3, 4):
    bot.disconnect()
else:
    try:
        bot.run_until_disconnected()
    except ConnectionError:
        pass
