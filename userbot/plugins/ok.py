"""Emoji

Available Commands:

.ok"""

from telethon import events

import asyncio

from userbot.utils import admin_cmd

@borg.on(admin_cmd("(.*)"))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.00001
    animation_ttl = range(0, 90)
    input_str = event.pattern_match.group(1)
    if input_str == "ok":
        await event.edit(input_str)
        animation_chars = [
            "O",
            "K",
            "B",
            "R",
            "O",
            "T",
            "H",
            "E",
            "R",
            "E",
            "I",
            "A",
            "M",
            "T",
            "O",
            "O",
            "HAPPY",
            "OK BROTHER NO PROBLEM 😇"
        ]

        for i in animation_ttl:
        	
            await asyncio.sleep(animation_interval)
            await event.edit(animation_chars[i % 18])
