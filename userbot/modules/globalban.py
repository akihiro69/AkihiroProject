import asyncio
from datetime import datetime
from io import BytesIO

from telethon import events
from telethon.errors import BadRequestError
from telethon.tl.functions.channels import EditBannedRequest
from telethon.tl.types import Channel

import userbot.modules.sql_helper.gban_sql as gban_sql
from userbot import BOTLOG_CHATID
from userbot import CMD_HANDLER as cmd
from userbot import CMD_HELP, DEVS, bot
from userbot.events import register
from userbot.utils import edit_or_reply, geez_cmd, get_user_from_event

from .admin import BANNED_RIGHTS, UNBAN_RIGHTS


async def admin_groups(grp):
    admgroups = []
    async for dialog in grp.client.iter_dialogs():
        entity = dialog.entity
        if (
            isinstance(entity, Channel)
            and entity.megagroup
            and (entity.creator or entity.admin_rights)
        ):
            admgroups.append(entity.id)
    return admgroups


def mentionuser(name, userid):
    return f"[{name}](tg://user?id={userid})"


@geez_cmd(pattern="gban(?: |$)(.*)")
@register(pattern=r"^\.cgban(?: |$)(.*)", sudo=True)
async def gban(event):
    if event.fwd_from:
        return
    gbun = await edit_or_reply(event, "`Memproses Global Blokir...`")
    start = datetime.now()
    user, reason = await get_user_from_event(event, gbun)
    if not user:
        return
    if user.id == (await event.client.get_me()).id:
        await gbun.edit("**Terjadi Kesalahan, Harap Balas Kepesan Untuk melakukan Global Blokir**")
        return
    if user.id in DEVS:
        await gbun.edit("**Gagal Melakukan Global Blokir, Karna Dia Adalah Pembuat Saya**")
        return
    if gban_sql.is_gbanned(user.id):
        await gbun.edit(
            f"[{user.first_name}](tg://user?id={user.id}) **Sudah Berada Di Daftar Gban List**"
        )
    else:
        gban_sql.freakgban(user.id, reason)
    san = []
    san = await admin_groups(event)
    count = 0
    fiz = len(san)
    if fiz == 0:
        await gbun.edit("**Maaf Anda Tidak Mempunyai Hak Admin Di Group Ini**")
        return
    await gbun.edit(
        f"**Memulai Global Blokir dari** [{user.first_name}](tg://user?id={user.id}) **dalam** `{len(san)}` **Grup**"
    )
    for i in range(fiz):
        try:
            await event.client(EditBannedRequest(san[i], user.id, BANNED_RIGHTS))
            await asyncio.sleep(0.5)
            count += 1
        except BadRequestError:
            await event.client.send_message(
                BOTLOG_CHATID,
                f"**Anda tidak memiliki izin Blokir di :**\n**Grup :** `{event.chat_id}`",
            )
    end = datetime.now()
    timetaken = (end - start).seconds
    if reason:
        await gbun.edit(
            f"**Global Blokir** [{user.first_name}](tg://user?id={user.id}) **di** `{count}` **Grup, dalam waktu** `{timetaken}` **detik**!!\n**Alasan :** `{reason}`"
        )
    else:
        await gbun.edit(
            f"**Global Blokir** [{user.first_name}](tg://user?id={user.id}) **di** `{count}` **Grup, dalam waktu** `{timetaken}` **detik**!!\n**Ditambahkan ke Daftar Global Blokir.**"
        )


@geez_cmd(pattern="ungban(?: |$)(.*)")
@register(pattern=r"^\.cungban(?: |$)(.*)", sudo=True)
async def ungban(event):
    if event.fwd_from:
        return
    ungbun = await edit_or_reply(event, "`Melepas Global Blokir...`")
    start = datetime.now()
    user, reason = await get_user_from_event(event, ungbun)
    if not user:
        return
    if gban_sql.is_gbanned(user.id):
        gban_sql.freakungban(user.id)
    else:
        await ungbun.edit(
            f"[{user.first_name}](tg://user?id={user.id}) **Tidak Berada Di Daftar Global Blokir!!!**"
        )
        return
    san = []
    san = await admin_groups(event)
    count = 0
    fiz = len(san)
    if fiz == 0:
        await ungbun.edit("**Terjadi Kesalahan Karna Anda Bukan lah admin.**")
        return
    await ungbun.edit(
        f"**Memulai Lepas Blokir dari** [{user.first_name}](tg://user?id={user.id}) **dalam** `{len(san)}` **Grup**"
    )
    for i in range(fiz):
        try:
            await event.client(EditBannedRequest(san[i], user.id, UNBAN_RIGHTS))
            await asyncio.sleep(0.5)
            count += 1
        except BadRequestError:
            await event.client.send_message(
                BOTLOG_CHATID,
                f"**Anda tidak memiliki izin Blokir di :**\n**Grup :** `{event.chat_id}`",
            )
    end = datetime.now()
    timetaken = (end - start).seconds
    if reason:
        await ungbun.edit(
            f"**Melepas Global Blokir** [{user.first_name}](tg://user?id={user.id}) **di** `{count}` **Grup dalam waktu** `{timetaken}` **detik**!!\n**Alasan :** `{reason}`"
        )
    else:
        await ungbun.edit(
            f"**Melepas Global Blokir** [{user.first_name}](tg://user?id={user.id}) **di** `{count}` **Grup dalam waktu** `{timetaken}` **detik**!!\n**Dihapus dari Daftar Global Blokir**"
        )


@geez_cmd(pattern="listgban$")
async def gablist(event):
    if event.fwd_from:
        return
    gbanned_users = gban_sql.get_all_gbanned()
    GBANNED_LIST = "**Daftar Global Blokir Anda Saat Ini**\n"
    if len(gbanned_users) > 0:
        for a_user in gbanned_users:
            if a_user.reason:
                GBANNED_LIST += f"👉 [{a_user.chat_id}](tg://user?id={a_user.chat_id}) **Alasan** `{a_user.reason}`\n"
            else:
                GBANNED_LIST += (
                    f"👉 [{a_user.chat_id}](tg://user?id={a_user.chat_id}) `Tanpa Alasan`\n"
                )
    if len(gbanned_users) >= 4096:
        with BytesIO(str.encode(GBANNED_LIST)) as fileuser:
            fileuser.name = "list-gban.txt"
            await event.client.send_file(
                event.chat_id,
                fileuser,
                force_document=True,
                thumb="userbot/resources/logo.jpg",
                caption="**Daftar Global Blokir**",
                allow_cache=False,
            )
    else:
        GBANNED_LIST = "`Belum ada Pengguna yang Di-GlobalBlokir`"
    await edit_or_reply(event, GBANNED_LIST)


@bot.on(events.ChatAction)
async def _(event):
    if event.user_joined or event.added_by:
        user = await event.get_user()
        chat = await event.get_chat()
        if gban_sql.is_gbanned(user.id) and chat.admin_rights:
            try:
                await event.client.edit_permissions(
                    chat.id,
                    user.id,
                    view_messages=False,
                )
                await event.reply(
                    f"**Global Blokir Pengguna** Bergabung.\n\n** • Akun:** [{user.first_name}](tg://user?id={user.id})\n • **Aksi:** `Blokir`"
                )
            except BaseException:
                pass


CMD_HELP.update(
    {
        "gban": f"**Plugin : **`gban`\
        \n\n  𝘾𝙤𝙢𝙢𝙖𝙣𝙙 :** `{cmd}gban` <username/id>\
        \n  ❍▸ : **Melakukan Banned Secara Global Ke Semua Grup Dimana anda Sebagai Admin.\
        \n\n  𝘾𝙤𝙢𝙢𝙖𝙣𝙙 :** `{cmd}ungban` <username/id>\
        \n  ❍▸ : **Membatalkan Global Banned\
        \n\n  𝘾𝙤𝙢𝙢𝙖𝙣𝙙 :** `{cmd}listgban`\
        \n  ❍▸ : **Menampilkan List Global Banned\
    "
    }
)
