# by:koala @mixiologist
# Lord Userbot

from telethon.events import ChatAction

from userbot import DEVS, bot, owner
from userbot.events import register
from userbot.utils import geez_cmd, get_user_from_event

# Ported For Lord-Userbot by liualvinas/Alvin


@bot.on(ChatAction)
async def handler(tele):
    if not tele.user_joined and not tele.user_added:
        return
    try:
        from userbot.modules.sql_helper.gmute_sql import is_gmuted

        guser = await tele.get_user()
        gmuted = is_gmuted(guser.id)
    except BaseException:
        return
    if gmuted:
        for i in gmuted:
            if i.sender == str(guser.id):
                chat = await tele.get_chat()
                admin = chat.admin_rights
                creator = chat.creator
                if admin or creator:
                    try:
                        await client.edit_permissions(
                            tele.chat_id, guser.id, view_messages=False
                        )
                        await tele.reply(
                            f"**Global Blokir Diaktifkan** \n"
                            f"**Akun :** [{guser.id}](tg://user?id={guser.id})\n"
                            f"**Aksi :** `Blokir`"
                        )
                    except BaseException:
                        return


@geez_cmd(pattern="gband(?: |$)(.*)")
@register(pattern=r"^\.cgband(?: |$)(.*)", sudo=True)
async def gben(userbot):
    dc = userbot
    sender = await dc.get_sender()
    me = await dc.client.get_me()
    if sender.id != me.id:
        dark = await dc.reply("`Memproses...`")
    else:
        dark = await dc.edit("`Memproses Global Blokir..`")
    me = await userbot.client.get_me()
    await dark.edit("`Global Blokir Akan Segera Aktif..`")
    my_mention = "[{}](tg://user?id={})".format(me.first_name, me.id)
    await userbot.get_chat()
    a = b = 0
    if userbot.is_private:
        user = userbot.chat
        reason = userbot.pattern_match.group(1)
    try:
        user, reason = await get_user_from_event(userbot)
    except BaseException:
        pass
    try:
        if not reason:
            reason = "Private"
    except BaseException:
        return await dark.edit("**Gagal Global Blokir :(**")
    if user:
        if user.id in DEVS:
            return await dark.edit("**Gagal Global Blokir, Dia Adalah Pembuat Saya**")
        try:
            from userbot.modules.sql_helper.gmute_sql import gmute
        except BaseException:
            pass
        testuserbot = [
            d.entity.id
            for d in await userbot.client.get_dialogs()
            if (d.is_group or d.is_channel)
        ]
        for i in testuserbot:
            try:
                await userbot.client.edit_permissions(i, user, view_messages=False)
                a += 1
                await dark.edit(
                    r"**Global Blokir Pengguna**"
                    f"\n\n**Akun:** [{user.first_name}](tg://user?id={user.id})\n"
                    f"**ID Pengguna:** `{user.id}`\n"
                    f"**Aksi:** `Global Blokir`"
                )
            except BaseException:
                b += 1
    else:
        await dark.edit("**Mohon Balas Pesan Ini Kepengguna**")
    try:
        if gmute(user.id) is False:
            return await dark.edit(
                "**Sudah TerGlobal Blokir**\n\nPengguna Sudah ada di Daftar Global Blokir.**"
            )

    except BaseException:
        pass
    return await dark.edit(
        r"**Global Blokir Pengguna**"
        f"\n\n**Akun:** [{user.first_name}](tg://user?id={user.id})\n"
        f"**ID Pengguna:** `{user.id}`\n"
        f"**Aksi:** `Global Blokir oleh {owner}`"
    )


@geez_cmd(pattern=r"ungband(?: |$)(.*)")
@register(pattern=r"^\.cungband(?: |$)(.*)", sudo=True)
async def gunben(userbot):
    dc = userbot
    sender = await dc.get_sender()
    me = await dc.client.get_me()
    if sender.id != me.id:
        dark = await dc.reply("`Memproses...`")
    else:
        dark = await dc.edit("`Memproses....`")
    me = await userbot.client.get_me()
    await dark.edit("`Melepaskan Global Blokir`")
    my_mention = "[{}](tg://user?id={})".format(me.first_name, me.id)
    await userbot.get_chat()
    a = b = 0
    if userbot.is_private:
        user = userbot.chat
        reason = userbot.pattern_match.group(1)
    try:
        user, reason = await get_user_from_event(userbot)
    except BaseException:
        pass
    try:
        if not reason:
            reason = "Private"
    except BaseException:
        return await dark.edit("**Gagal Melepaskan Global Blokir :(**")
    if user:
        if user.id in DEVS:
            return await dark.edit(
                "** Maaf Akihiro Tidak Bisa Melakukan Printah Ini Karna Dia Pembuat saya**"
            )
        try:
            from userbot.modules.sql_helper.gmute_sql import ungmute
        except BaseException:
            pass
        testuserbot = [
            d.entity.id
            for d in await userbot.client.get_dialogs()
            if (d.is_group or d.is_channel)
        ]
        for i in testuserbot:
            try:
                await userbot.client.edit_permissions(i, user, send_messages=True)
                a += 1
                await dark.edit("`Melepaskan Global Blokir...`")
            except BaseException:
                b += 1
    else:
        await dark.edit("`Mohon Balas Pesan Ini Kepengguna`")
    try:
        if ungmute(user.id) is False:
            return await dark.edit("**Error! Pengguna Tidak Di Global Blokir.**")
    except BaseException:
        pass
    return await dark.edit(
        r"**Melepaskan Global Blokir Pengguna**"
        f"\n\n**Akun:** [{user.first_name}](tg://user?id={user.id})\n"
        f"**ID Pengguna:** `{user.id}`\n"
        f"**Aksi:** `Lepas Global Blokir oleh {owner}`"
    )
