# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.
#
""" Userbot help command for multi client """

from time import sleep

from AyiinXd import CMD_HANDLER as cmd
from AyiinXd import CMD_HELP, ICON_HELP, ch
from AyiinXd.ayiin import ayiin_cmd, eod, eor
from Stringyins import get_string


@ayiin_cmd(pattern="chelp(?: |$)(.*)")
async def help(event):
    args = event.pattern_match.group(1).lower()
    if args:
        if args in CMD_HELP:
            await eor(event, get_string("help_5").format(CMD_HELP[args], ch))
        else:
            await eod(event, get_string("help_10").format(args, cmd))
    else:
        user = await event.client.get_me()
        string = ""
        for i in CMD_HELP:
            string += "`" + str(i)
            string += f"`\t\t\t{ICON_HELP}\t\t\t"
        xnxx = await eor(event, "🗿")
        sleep(3)
        await xnxx.edit(
            f"**[⍟ ᴋᴀᴢᴜ ᴜsᴇʀʙᴏᴛ ⍟](https://github.com/zokazu/Kazu-Userbot)**\n"
            f"**➱ ᴊᴜᴍʟᴀʜ** `{len(CMD_HELP)}` **Modules**\n"
            f"**✰ ᴏᴡɴ ✰:** [{user.first_name}](tg://user?id={user.id})\n\n"
            f"{ICON_HELP}   {string}"
            f"\n\n☞  **𝚂𝚄𝙿𝙿𝙾𝚁𝚃** : @privategrupnya\n☞  **𝙽𝙾𝚃𝙴𝚂** :  `{cmd}help yinsubot` **Untuk Melihat Modules Lainnya**"
        )
