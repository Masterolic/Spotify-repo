![Spotify Logo](https://upload.wikimedia.org/wikipedia/commons/1/19/Spotify_logo_without_text.svg)

# Spotify Downloader Bot

[DEMO VERSION @z_downloadbot](https://t.me/z_downloadbot)


### Is this source code used for [@z_downloadbot](https://t.me/z_downloadbot)?
> No, this [bot](https://github.com/rozari0/NeedMusicRobot) was the inspiration to build our bot. You can see our bot is entirely different, and some features will be implemented in this repository.

## Deployment

### Easy way to deploy on Local/VPS
1. First, add variables in [config.env](https://github.com/zasasamar2129/zpotify1/blob/Latest/config.env):
   ```sh
   sudo apt update && apt upgrade -y 
   sudo apt install git ffmpeg python3 python3-pip -y
   git clone https://github.com/zasasamar2129/zpotify1.git 
   cd zpotify1
   pip3 install -r requirements.txt 
   python3 -m mbot 
   ```

### Docker
1. Build and run the Docker image:
   ```sh
   docker build . -t musicbot
   docker run musicbot  
   ```



## Config Example
Add these variables in [config.env](https://github.com/zasasamar2129/zpotify1/blob/Latest/config.env):

### Required Environment Variables

### Get `api_id` and `api_hash` from [my.telegram.org](https://my.telegram.org) (required)
```sh
API_ID = ""
API_HASH = ""
```

### Your Telegram bot token (required)
```sh
BOT_TOKEN = ""
```

### ID of the owner of the bot (not username) (required)
```sh
OWNER_ID = ""
```
### Spotify Client Secret (get it from developers.spotify.com) (required)
```sh
SPOTIPY_CLIENT_SECRET = ""
```

### Spotify Client ID (get it from developers.spotify.com) (required)
```sh
SPOTIPY_CLIENT_ID = ""
```

### Optional Environment Variables

### Users with God permission (separate them with spaces) (optional)
```sh
SUDO_USERS = ""
```

### Chats that can use the bot (separate them with spaces) (optional)
```sh
AUTH_CHATS = ""
```

### Group ID for the log channel or leave it empty if not required (optional)
```sh
LOG_GROUP = ""
```


### Add your group ID for getting error log messages or leave it empty if not required (optional)
```sh
BUG = ""
```

### Get it from https://genius.com/developers (optional)
```sh
GENIUS_API = ""
```

### Temporary file storage path (optional)
```sh
XDG_CACHE_HOME = "~/.tmp"
```

### Paste your proxy URL here or leave it empty if not required (optional)
```sh
FIXIE_SOCKS_HOST = ""
```

### Pass `True` to make F_Sub enabled (default to `False`) (optional)
```sh
F_SUB = False
```

### Pass channel ID username or ID that starts with `-100` (optional)
```sh
F_SUB_CHANNEL_ID = ""
```

### Pass the invite link to the channel (e.g., `https://t.me/username` or `https://t.me/+jwjjwjw`) (optional)
```sh
F_SUB_CHANNEL_INVITE_LINK = ""
```

## Donation
> Please support me by buying me a pizza using the link below:
[Buy Me A Pizza](https://www.buymeacoffee.com/zasasamar)

## Feedback
> Rate our bot [FEEDBACK](https://t.me/dailychannelsbot?start=z_downloadbot)

## About
> A Simple Open Source Spotify Downloader Bot for Telegram.

## Contact
> If you need any help or want to provide feedback, don't hesitate to contact me:

- [Instagram](https://instagram.com/zaco.game)
- [Telegram](https://t.me/Itachi2129)
