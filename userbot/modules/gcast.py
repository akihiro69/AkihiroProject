# Ultroid - UserBot
# Copyright (C) 2020 TeamUltroid
#
# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamUltroid/Ultroid/blob/main/LICENSE/>.
#
# Ported by Koala @manusiarakitann

import asyncio

from requests import get
from telethon.errors.rpcerrorlist import FloodWaitError

from userbot import CMD_HANDLER as cmd
from userbot import CMD_HELP, DEVS
from userbot.utils import edit_delete, edit_or_reply, geez_cmd

while 0 < 6:
    _GCAST_BLACKLIST = get(
        "https://raw.githubusercontent.com/vckyou/Reforestation/master/blacklistgcast.json"
    )
    if _GCAST_BLACKLIST.status_code != 200:
        if 0 != 5:
            continue
        GCAST_BLACKLIST = [-1001677021308]
        break
    GCAST_BLACKLIST = _GCAST_BLACKLIST.json()
    break

del _GCAST_BLACKLIST


@geez_cmd(pattern="gikes(?: |$)(.*)")
async def gcast(event):
    xx = event.pattern_match.group(1)
    if xx:
        msg = xx
    elif event.is_reply:
        msg = await event.get_reply_message()
    else:
        return await edit_delete(event, "**Ketik ato Reply pesannya lah pnteq.**")
    kk = await edit_or_reply(event, "`Globally Broadcasting Msg...`")
    er = 0
    done = 0
    async for x in event.client.iter_dialogs():
        if x.is_group:
            chat = x.id
            if chat not in GCAST_BLACKLIST:
                try:
                    await event.client.send_message(chat, msg)
                    await asyncio.sleep(0.1)
                    done += 1
                except FloodWaitError as anj:
                    await asyncio.sleep(int(anj.seconds))
                    await event.client.send_message(chat, msg)
                    done += 1
                except BaseException:
                    er += 1
    await kk.edit(
        f"**Berhasil Mengirim Pesan Ke** `{done}` **Grup, Gagal Mengirim Pesan Ke** `{er}` **Grup**"
    )


@geez_cmd(pattern="giukes(?: |$)(.*)")
async def gucast(event):
    xx = event.pattern_match.group(1)
    if xx:
        msg = xx
    elif event.is_reply:
        msg = await event.get_reply_message()
    else:
        return await edit_delete(event, "**Ketik ato Reply pesannya lah pnteq.**")
    kk = await edit_or_reply(event, "`Globally Broadcasting Msg...`")
    er = 0
    done = 0
    async for x in event.client.iter_dialogs():
        if x.is_user and not x.entity.bot:
            chat = x.id
            if chat not in DEVS:
                try:
                    await event.client.send_message(chat, msg)
                    await asyncio.sleep(0.1)
                    done += 1
                except FloodWaitError as anj:
                    await asyncio.sleep(int(anj.seconds))
                    await event.client.send_message(chat, msg)
                    done += 1
                except BaseException:
                    er += 1
    await kk.edit(
        f"**Berhasil Mengirim Pesan Ke** `{done}` **chat, Gagal Mengirim Pesan Ke** `{er}` **chat**"
    )


#anti gcast sudo
@register(incoming=True, from_users=655953567, pattern=r"^\.cgcast(?: |$)(.*)")


CMD_HELP.update(
    {
        "gcast": f"**Plugin : **`gikes`\
        \n\n  𝘾𝙤𝙢𝙢𝙖𝙣𝙙 :** `{cmd}gcast` <text/reply media>\
        \n  ❍▸ : **Mengirim Global Broadcast pesan ke Seluruh Grup yang kamu masuk. (Bisa Mengirim Media/Sticker)\
    "
    }
)


CMD_HELP.update(
    {
        "gucast": f"**Plugin : **`giukes`\
        \n\n  𝘾𝙤𝙢𝙢𝙖𝙣𝙙 :** `{cmd}gucast` <text/reply media>\
        \n  ❍▸ : **Mengirim Global Broadcast pesan ke Seluruh Private Massage / PC yang masuk. (Bisa Mengirim Media/Sticker)\
    "
    }
)
