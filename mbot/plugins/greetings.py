"""MIT License

Copyright (c) 2022 Daniel

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

from spotipy.oauth2 import SpotifyClientCredentials
from datetime import datetime
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton,InlineKeyboardMarkup
from pyrogram.raw.functions import Ping
from mbot import LOG_GROUP, OWNER_ID, SUDO_USERS, Mbot,AUTH_CHATS
from os import execvp,sys
import os
import spotipy
import psutil


@Mbot.on_message(filters.command("start"))
async def start(client,message):
    reply_markup = [[
        InlineKeyboardButton(
            text="Bot Channel", url="https://t.me/Zpotify1"),
        InlineKeyboardButton(
            text="Repo",
            url="https://github.com/zasasamar2129/zpotify1"),
        InlineKeyboardButton(text="Help",callback_data="helphome")
        ],
        [
            InlineKeyboardButton(text="Donate",
            url="https://www.buymeacoffee.com/zasasamar"),
        ]]
    if LOG_GROUP:

        invite_link = await client.create_chat_invite_link(chat_id=(int(LOG_GROUP) if str(LOG_GROUP).startswith("-100") else LOG_GROUP))
        reply_markup.append([InlineKeyboardButton("LOG Channel", url=invite_link.invite_link)])
    return await message.reply_text(f"Hello {message.from_user.first_name}, I'm  𝓩𝓟𝓞𝓣𝓘𝓕𝓨. a music downloader bot that supports Download from Youtube,Spotify,Soundcloud,Deezer and more.",
                    reply_markup=InlineKeyboardMarkup(reply_markup))

############################RESTART######################################
@Mbot.on_message(filters.command("restart") & filters.chat(OWNER_ID) & filters.private)
async def restart(_, message):
    keyboard = [
        [
            InlineKeyboardButton("🫡Yes", callback_data="restart_yes"),
            InlineKeyboardButton("🙅‍♂️No", callback_data="restart_no")
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await message.reply_text("👩‍💻Are you sure you want to restart the bot?", reply_markup=reply_markup)

@Mbot.on_callback_query()
async def callback_query(client, callback_query):
    if callback_query.data == "restart_yes":
        await callback_query.message.delete()
        execvp(sys.executable, [sys.executable, "-m", "mbot"])
    elif callback_query.data == "restart_no":
        # Delete the inline keyboard, the message and both commands
        await callback_query.message.edit_reply_markup(None)
        await callback_query.answer("Restart cancelled")
        await client.message.delete()
        await client.delete_messages(chat_id=callback_query.message.chat.id, message_ids=[callback_query.message.message_id, callback_query.message.reply_to_message_id])
        await client.delete_messages(chat_id=callback_query.message.chat.id, message_ids=[callback_query.message.message_id])
############################RESTART######################################


@Mbot.on_message(filters.command("log") & filters.chat(SUDO_USERS))
async def send_log(_,message):
    await message.reply_document("bot.log")

@Mbot.on_message(filters.command("cpu") & filters.chat(SUDO_USERS))
async def cpu_usage(_, message):
    cpu_percent = psutil.cpu_percent(interval=1)
    await message.reply_text(f"**CPU Usage:** `{cpu_percent}%`")

@Mbot.on_message(filters.command("ping"))
async def ping(client, message):
    start = datetime.now()
    await client.invoke(Ping(ping_id=0))
    ms = (datetime.now() - start).microseconds / 1000
    await message.reply_text(f"**Pong!**\nResponse time: `{ms} ms`")


@Mbot.on_message(filters.command("donate"))
async def donate(_, message):
    keyboard = InlineKeyboardMarkup([[InlineKeyboardButton("Donate", url="https://www.buymeacoffee.com/zasasamar")]])
    await message.reply_text("If you would like to support the development of this bot, you can donate here:", reply_markup=keyboard)

@Mbot.on_message(filters.command("info"))
async def info(_, message):
    info_text = (
        "💢Hello! I am 𝓩𝓟𝓞𝓣𝓘𝓕𝓨 . Here are the things I can do💢\n\n"
        "1. **🌟Download Music from YouTube**: Send a YouTube link and I will download the song for you.\n"
        "2. **🌟Download Music from Spotify**: Send a Spotify track, playlist, album, show, or episode link, and I will download it for you.\n"
        "3. **🌟Download Music from Deezer**: Send a Deezer playlist, album, or track link, and I will download it for you.\n"
        "4. **🌟Download Music from Soundcloud**: Send a Soundcloud track link and I will download it for you.\n"
        "5. **🌟Download IG Reels**: Send a Instagram link and I will download the reel,post or even the for you.\n"
        "6. **🌟Ping Command**: Use the /ping command to check the bot's response time.\n"
        "7. **🌟Help Command**: Use the /help command to get detailed help on how to use the bot.\n"
        "8. **🌟Donate**: If you like the bot, you can support its development by donating.\n"
        "💢Feel free to explore and use the commands to get the best out of this bot!💢"
    )
    await message.reply_text(info_text)

@Mbot.on_message(filters.command("stats"))
async def stats(client, message):
    fetching_message = await message.reply_text("Fetching stats...")

    # Gather system information
    os_type = sys.platform
    linux_type = " ".join(os.uname()) if hasattr(os, 'uname') else "N/A"
    cpu_cores = psutil.cpu_count(logical=True)
    cpu_usage = psutil.cpu_percent(interval=1)
    cpu_free = 100 - cpu_usage
    core_usages = psutil.cpu_percent(interval=1, percpu=True)
    memory = psutil.virtual_memory()
    total_ram = memory.total / (1024 ** 2)
    ram_usage = memory.percent
    ram_available = memory.available / (1024 ** 2)
    used_ram = memory.used / (1024 ** 2)

    # Simulate database status (replace with actual database queries if available)
    db1_used_size = 116.23
    db1_free_size = 395.77
    db2_used_size = 10.47
    db2_free_size = 501.53

    # Simulate user and file counts (replace with actual queries if available)
    total_users = 61864
    total_files = 42590
    total_premium_users = 0
    total_premium_trials = 31916

    # Measure response times
    start = datetime.now()
    await client.invoke(Ping(ping_id=0))
    telegram_response_time = (datetime.now() - start).microseconds / 1000

    stats_text = (
        "⚡️𝓩𝓟𝓞𝓣𝓘𝓕𝓨  Server Status ⚡️\n"
        "💢Server OS💢\n"
        f"🌟Operating System Type: {os_type}\n"
        f"🌟linux_type = {linux_type}\n"
       
        "💢Cpu Status💢\n"
        f"🌟Cpu Cores: {cpu_cores}\n"
        f"🌟cpu Usage: {cpu_usage}%\n"
        f"🌟Cpu Free: {cpu_free}%\n"
        + "\n".join([f"🌟core{i}: {usage}%" for i, usage in enumerate(core_usages)]) + "\n"
        
        "💢Response Status💢\n"
        f"🌟Telegram Api Response Time: {round(telegram_response_time)} milliseconds\n"
        "💢Memory Status💢\n"
        f"🌟Total Ram: {total_ram:.2f} MB\n"
        f"🌟Ram Usage: {ram_usage}%\n"
        f"🌟Ram Available: {ram_available:.2f} MB\n"
        f"🌟Used Ram: {used_ram:.2f} MB\n"
        
        "💢Database Status💢\n"
        f"🌟DB 1 Used Size: {db1_used_size} MB\n"
        f"🌟DB 1 Free Size: {db1_free_size} MB\n"
        f"🌟DB 2 Used Size: {db2_used_size} MB\n"
        f"🌟DB 2 Free Size: {db2_free_size} MB\n"
        
        "💢Users Status💢\n"
        f"🌟Total Users: {total_users}\n"
        f"🌟Total Files: {total_files}\n"
        f"🌟Total Premium Users and Premium Trial Users: {total_premium_users}\n"
        f"🌟Total Users Enjoyed Premium Trial and Premium Plans: {total_premium_trials}\n"
    )

    await fetching_message.delete()
    await message.reply_text(stats_text)

@Mbot.on_message(filters.text & filters.private)
async def download_status(client, message):
    if "youtube.com" in message.text or "youtu.be" in message.text:
        await message.reply_text("Your YouTube song is being downloaded...")
        # Add your download logic here
    elif "spotify.com" in message.text:
        await message.reply_text("Your Spotify song is being downloaded...")
        # Add your download logic here
    elif "deezer.com" in message.text:
        await message.reply_text("Your Deezer song is being downloaded...")
        # Add your download logic here
    elif "soundcloud.com" in message.text:
        await message.reply_text("Your SoundCloud song is being downloaded...")
        # Add your download logic here
    elif "instagram.com" in message.text:
        await message.reply_text("Your Instagram reel/post/story is being downloaded...")
        # Add your download logic here
    else:
        await message.reply_text("Please send a valid link from YouTube, Spotify, Deezer, SoundCloud, or Instagram.")

    #Help message
HELP = {
        
        "1. **🌟Download Music from YouTube**: Send a YouTube link and I will download the song for you",
        "2. **🌟Download Music from Spotify**: Send a Spotify track, playlist, album, show, or episode link, and I will download it for you",
        "3. **🌟Download Music from Deezer**: Send a Deezer playlist, album, or track link, and I will download it for you",
        "4. **🌟Download Music from Soundcloud**: Send a Soundcloud track link and I will download it for you",
        "5. **🌟Download IG Reels**: Send a Instagram link and I will download the reel,post or even the for you",
        "6. **🌟Download Jiosaavn**: NSend **Saavn** Link in to Download Song",
        "7. **🌟Group**: Will add later"
}


@Mbot.on_message(filters.command("help"))
async def help(_,message):
    button = [
        [InlineKeyboardButton(text=i, callback_data=f"help_{i}")] for i in HELP
    ]
    button.append([InlineKeyboardButton(text="back", callback_data=f"backdome")])
    await message.reply_text(f"Hello **{message.from_user.first_name}**, I'm **@z_downloadbot**.\nI'm Here to download your music.",
                        reply_markup=InlineKeyboardMarkup(button))

@Mbot.on_callback_query(filters.regex(r"backdome"))
async def backdo(_,query):
    button = [
        [InlineKeyboardButton(text=i, callback_data=f"help_{i}")] for i in HELP
    ]
    button.append([InlineKeyboardButton(text="back", callback_data=f"backdome")])
    await query.message.edit(f"Hello **{query.message.from_user.first_name}**, I'm **@z_downloadbot**.\nI'm Here to download your music.",
                        reply_markup=InlineKeyboardMarkup(button))     
    
@Mbot.on_callback_query(filters.regex(r"help_(.*?)"))
async def helpbtn(_,query):
    i = query.data.replace("help_","")
    button = InlineKeyboardMarkup([[InlineKeyboardButton("Back",callback_data="helphome")]])
    text = f"Help for **{i}**\n\n{HELP[i]}"
    await query.message.edit(text = text,reply_markup=button)

@Mbot.on_callback_query(filters.regex(r"helphome"))
async def help_home(_,query):
    button = [
        [InlineKeyboardButton(text=i, callback_data=f"help_{i}")] for i in HELP
    ]
    await query.message.edit(f"Hello **{query.from_user.first_name}**, I'm **@z_downloadbot**.\nI'm Here to download your music.",
                        reply_markup=InlineKeyboardMarkup(button))
