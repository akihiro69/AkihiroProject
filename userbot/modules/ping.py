# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.
#
# Recode @VckyouuBitch
# FROM GeezProjects <https://github.com/vckyou/GeezProjects>
# Copyright © 2021-2022

import random
import asyncio
import time
from datetime import datetime

from speedtest import Speedtest

from userbot import CMD_HANDLER as cmd
from userbot import CMD_HELP, StartTime, bot
from userbot.events import register
from userbot.utils import edit_or_reply, humanbytes, geez_cmd

absen = [
    "**Akihiro Hadir bang** 😁",
    "**Akihiro Hadir kak** 😉",
    "**Akihiro Hadir dong** 😁",
    "**Akihiro Hadir ganteng** 🥵",
    "**Akihiro Hadir bro** 😎",
    "**Akihiro Hadir kak maap telat** 🥺",
]


async def get_readable_time(seconds: int) -> str:
    count = 0
    up_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "Jam", "Hari"]

    while count < 4:
        count += 1
        remainder, result = divmod(seconds, 60) if count < 3 else divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        up_time += time_list.pop() + ", "

    time_list.reverse()
    up_time += ":".join(time_list)

    return up_time


@geez_cmd(pattern="ping$")
async def _(ping):
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    xx = await edit_or_reply(ping, "**Pinging.**")
    await xx.edit("**Pinging..**")
    await xx.edit("**Pinging...**")
    await xx.edit("**Pinging....**")
    await xx.edit("⚡")
    await asyncio.sleep(3)
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    user = await ping.client.get_me()
    await xx.edit(
                  f"**AkihiroProject** 🈴\n"
                  f"**Pong !!** `%sms`\n"
                  f"**Uptime** - `{uptime}`\n" % (duration)
     )


@geez_cmd(pattern=r"twing$")
async def _(ping):
    """For .ping command, ping the userbot from any chat."""
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    twing = await edit_or_reply(ping, "`Pinging....`")
    await twing.edit("**TWICE Ping!!!**")
    await asyncio.sleep(2)
    await twing.edit("**Hana.**")
    await asyncio.sleep(1)
    await twing.edit("**Dul..**")
    await asyncio.sleep(1)
    await twing.edit("**Set...**")
    await asyncio.sleep(1)
    await twing.edit("🥳")
    await asyncio.sleep(3)
    await twing.edit("**One In A Million...**")
    await asyncio.sleep(2)
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    user = await twing.client.get_me()
    await twing.edit(
                     f"**TWICEE IMNIDA** 🍭\n"
                     f"**Twinger !!** `%sms`\n"
                     f"**Uptime** - `{uptime}`\n" % (duration)
    )


@geez_cmd(pattern="pink$")
async def redis(pong):
    """For .ping command, ping the userbot from any chat."""
    await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    ram = await edit_or_reply(pong, "**𓀐.....................................𓂸**")
    await ram.edit("**𓀐..................................𓂸..**")
    await ram.edit("**𓀐................................𓂸....**")
    await ram.edit("**𓀐..............................𓂸......**")
    await ram.edit("**𓀐............................𓂸........**")
    await ram.edit("**𓀐..........................𓂸..........**")
    await ram.edit("**𓀐.......................𓂸.............**")
    await ram.edit("**𓀐.....................𓂸...............**")
    await ram.edit("**𓀐...................𓂸.................**")
    await ram.edit("**𓀐..................𓂸..................**")
    await ram.edit("**𓀐................𓂸....................**")
    await ram.edit("**𓀐..............𓂸......................**")
    await ram.edit("**𓀐............𓂸........................**")
    await ram.edit("**𓀐..........𓂸..........................**")
    await ram.edit("**𓀐........𓂸............................**")
    await ram.edit("**𓀐.......𓂸.............................**")
    await ram.edit("**𓀐....𓂸...............................**")
    await ram.edit("**𓀐..𓂸.................................**")
    await ram.edit("**𓀐.𓂸..................................**")
    await ram.edit("**𓀐𓂸...................................**")
    await ram.edit("**𓀐.𓂸..................................**")
    await ram.edit("**𓀐𓂸...................................**")
    await ram.edit("**𓀐.𓂸..................................**")
    await ram.edit("**𓂺**")
    await asyncio.sleep(2)
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    user= await pong.client.get_me()
    await pong.edit(
        f"**➾ OWNER      :** [{user.first_name}](tg://user?id={user.id}) \n"
        f"**➾ Kecepatan : ** %sms  \n"
        f"**➾ Branch       : ** [AkihiroProject](https://t.me/akihiro69) \n" % (duration)) 


@geez_cmd(pattern="rping$")
async def _(pong):
    """For .ping command, ping the userbot from any chat."""
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    ram = await edit_or_reply(pong, "**Mengecek Sinyal...**")
    await ram.edit("**0% ▒▒▒▒▒▒▒▒▒▒**")
    await ram.edit("**20% ██▒▒▒▒▒▒▒▒**")
    await ram.edit("**40% ████▒▒▒▒▒▒**")
    await ram.edit("**60% ██████▒▒▒▒**")
    await ram.edit("**80% ████████▒▒**")
    await ram.edit("**100% ██████████**")
    await ram.edit("✨")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    user = await pong.client.get_me()
    await ram.edit(
        f"**💥𝗞𝗢𝗡𝗧𝗢𝗟-𝗠𝗘𝗟𝗘𝗗𝗔𝗞💥**\n"
        f"** ➠  Sɪɢɴᴀʟ   :** "
        f"`%sms` \n"
        f"** ➠  Uᴘᴛɪᴍᴇ  :** "
        f"`{uptime}` \n"
        f"** ➠  Oᴡɴᴇʀ   :** [{user.first_name}](tg://user?id={user.id})" % (duration)
    )


@geez_cmd(pattern="tping$")
async def _(pong):
    """ For .ping command, ping the userbot from any chat.  """
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    await pong.edit("**Kontol**")
    await pong.edit("__**Kontol⚡**__")
    await pong.edit("__**konto⚡l**__")
    await pong.edit("__**kon⚡tol**__")
    await pong.edit("__**k⚡ontol**__")
    await pong.edit("__**⚡kontol⚡**__")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await pong.edit(
        f"**⚡Kontol ᴘɪɴɢ⚡**\n"
        f"⚡ **ᴘɪɴɢ:** "
        f"`%sms` \n"
        f"⚡ **ᴏɴʟɪɴᴇ:** "
        f"`{uptime}` \n" % (duration))


@geez_cmd(pattern="fping$")
async def _(pong):
    """ For .ping command, ping the userbot from any chat.  """
    start = datetime.now()
    await pong.edit("`Pong.....🚑`")
    await pong.edit("`Pong....🚒.`")
    await pong.edit("`Pong...🚑..`")
    await pong.edit("`Pong..🚒...`")
    await pong.edit("`Pong.🚑....`")
    await pong.edit("`Pong🚒.....`")
    end = datetime.now()
    duration = (end - start).microseconds / 9000
    await pong.edit("✘ **Ping!**\n`%sms`" % (duration))



@geez_cmd(pattern=r"keping$")
async def _(pong):
    await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    kopong = await edit_or_reply(pong, "**『⍟𝐊𝐎𝐍𝐓𝐎𝐋』**")
    await kopong.edit("**◆◈𝐊𝐀𝐌𝐏𝐀𝐍𝐆◈◆**")
    await kopong.edit("**𝐏𝐄𝐂𝐀𝐇𝐊𝐀𝐍 𝐁𝐈𝐉𝐈 𝐊𝐀𝐔 𝐀𝐒𝐔**")
    await kopong.edit("**☬𝐒𝐈𝐀𝐏 𝐊𝐀𝐌𝐏𝐀𝐍𝐆 𝐌𝐄𝐍𝐔𝐌𝐁𝐔𝐊 𝐀𝐒𝐔☬**")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    user = await bot.get_me()
    await kopong.edit(
        f"**✲ 𝙺𝙾𝙽𝚃𝙾𝙻 𝙼𝙴𝙻𝙴𝙳𝚄𝙶** "
        f"\n ⫸ ᴷᵒⁿᵗᵒˡ `%sms` \n"
        f"**✲ 𝙱𝙸𝙹𝙸 𝙿𝙴𝙻𝙴𝚁** "
        f"\n ⫸ ᴷᵃᵐᵖᵃⁿᵍ『[{user.first_name}](tg://user?id={user.id})』 \n" % (duration)
    )


# .keping & kping Coded by Koala


@geez_cmd(pattern=r"kping$")
async def _(pong):
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    kping = await edit_or_reply(pong, "8✊===D")
    await kping.edit("8=✊==D")
    await kping.edit("8==✊=D")
    await kping.edit("8===✊D")
    await kping.edit("8==✊=D")
    await kping.edit("8=✊==D")
    await kping.edit("8✊===D")
    await kping.edit("8=✊==D")
    await kping.edit("8==✊=D")
    await kping.edit("8===✊D")
    await kping.edit("8==✊=D")
    await kping.edit("8=✊==D")
    await kping.edit("8✊===D")
    await kping.edit("8=✊==D")
    await kping.edit("8==✊=D")
    await kping.edit("8===✊D")
    await kping.edit("8===✊D💦")
    await kping.edit("8====D💦💦")
    await kping.edit("**CROOTTTT PINGGGG!**")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await kping.edit(
        f"**NGENTOT!! 🐨**\n**KAMPANG** : %sms\n**Bot Uptime** : {uptime}🕛" % (duration)
    )


@geez_cmd(pattern="speedtest$")
async def _(speed):
    """For .speedtest command, use SpeedTest to check server speeds."""
    xxnx = await edit_or_reply(speed, "`Running speed test...`")
    test = Speedtest()
    test.get_best_server()
    test.download()
    test.upload()
    test.results.share()
    result = test.results.dict()
    msg = (
        f"**Started at {result['timestamp']}**\n\n"
        "**Client**\n"
        f"**ISP :** `{result['client']['isp']}`\n"
        f"**Country :** `{result['client']['country']}`\n\n"
        "**Server**\n"
        f"**Name :** `{result['server']['name']}`\n"
        f"**Country :** `{result['server']['country']}`\n"
        f"**Sponsor :** `{result['server']['sponsor']}`\n\n"
        f"**Ping :** `{result['ping']}`\n"
        f"**Upload :** `{humanbytes(result['upload'])}/s`\n"
        f"**Download :** `{humanbytes(result['download'])}/s`"
    )
    await xxnx.delete()
    await speed.client.send_file(
        speed.chat_id,
        result["share"],
        caption=msg,
        force_document=False,
    )


@geez_cmd(pattern="pong$")
async def _(pong):
    """For .ping command, ping the userbot from any chat."""
    start = datetime.now()
    xx = await edit_or_reply(pong, "`PONG!.....🏓`")
    end = datetime.now()
    duration = (end - start).microseconds / 9000
    await xx.edit("🏓 **Ping!**\n`%sms`" % (duration))


# KALO NGEFORK absen ini GA USAH DI HAPUS YA GOBLOK 😡
@register(pattern=r"^\.absen$", sudo=True)
async def geez(ganteng):
    await ganteng.reply(random.choice(absen))


# JANGAN DI HAPUS GOBLOK 😡 LU COPY AJA TINGGAL TAMBAHIN
# DI HAPUS GUA GBAN YA 🥴 GUA TANDAIN LU AKUN TELENYA 😡


CMD_HELP.update(
    {
        "ping": f"**Plugin : **`ping`\
        \n\n  𝘾𝙤𝙢𝙢𝙖𝙣𝙙 :** `{cmd}ping` ; `{cmd}twing` ; `{cmd}kping`\
        \n  ❍▸ : **Untuk menunjukkan ping userbot.\
        \n\n  𝘾𝙤𝙢𝙢𝙖𝙣𝙙 :** `{cmd}pong`\
        \n  ❍▸ : **Sama seperti perintah ping\
        \n\n  𝘾𝙤𝙢𝙢𝙖𝙣𝙙 :** `{cmd}rping` ; `{cmd}tping` ; `{cmd}fping` ; `{cmd}pink` ; `{cmd}keping` \
        \n  ❍▸ : **Sama Seperti perintah ping (Lihat sendiri)\
    "
    }
)


CMD_HELP.update(
    {
        "speedtest": f"**Plugin : **`speedtest`\
        \n\n  𝘾𝙤𝙢𝙢𝙖𝙣𝙙 :** `{cmd}speedtest`\
        \n  ❍▸ : **Untuk Mengetes kecepatan server userbot.\
    "
    }
)
