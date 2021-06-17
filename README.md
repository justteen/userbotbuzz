# Telegram Voice Chat UserBot

Telegram UserBot untuk Play Lagu di OS.

## Deploy Di Heroku

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/justteen/userbotbuzz)

- Generate Pyrogram session string by
  running [generate-pyrogram-session-string.py](generate-pyrogram-session-string.py)
  by yourself or
  through [Replit](https://replit.com/@dashezup/generate-pyrogram-session-string)
- Enable the worker after deploy the project to Heroku

Ubah value  `PLUGIN` variable kalau kamu mau coba voice chat
plugins lain.


## Introduction

**Features**

- Playlist, queue
- Loop one track when there is only one track in the playlist
- Automatically downloads audio for the first two tracks in the playlist to
  ensure smooth playing
- Automatically pin the current playing track
- Show current playing position of the audio

**Plugin**: vc.`player`

Commands only works in groups, userbot account itself and contacts can use any
commands, all members can use common commands after the userbot join the VC

1. Mulai Userbot ini, ketik `!ping`, `!uptime` atau `!sysinfo`  perintah untuk mengecek kalau bot ini berjalan.
2. kirim `!join` untuk gabung ke OS apabila telah diset semua
   atau manual set admin
   beri akses:
    - Hapus Pesan
    - Atur voice chats (optional)
3. reply ke audio dengan `/play` untuk start play lagu di OS, setiap
   member group bisa gunakan perintah `/play`, `/current`
   dan `!help` 
4. check `!help` untuk perintah lebih lanjut

**Plugin**: vc.`channel`

hampir semua `player` plugin hanya bekerja pada penyimpanan pesan,
`!join` untuk join group atau channel.

**Plugin**: `ping` and `sysinfo`

Perintah ini hanya berlaku untuk userbot itu sendiri dan kontaknya.

## Requirements

- Python 3.6 or higher
- A
  [Telegram API key](https://docs.pyrogram.org/intro/quickstart#enjoy-the-api)
  and a Telegram account
- Choose plugins you need, install dependencies which listed above and run
  `pip install -U -r requirements.txt` to install Python package dependencies
  as well
- [FFmpeg](https://www.ffmpeg.org/)

## Run

Choose one of the two methods and run the userbot with
`python userbot.py`, stop with <kbd>CTRL+c</kbd>. The following example assume
that you were going to use `vc.player` and `ping` plugin, replace
`api_id`, `api_hash` to your own value.

### Method 1: use config.ini

Create a `config.ini` file

```
[pyrogram]
api_id = 1234567
api_hash = 0123456789abcdef0123456789abcdef

[plugins]
root = plugins
include =
    vc.player
    ping
    sysinfo
```

### Method 2: write your own userbot.py

Replace the file content of `userbot.py`

```
from pyrogram import Client, idle

api_id = 1234567
api_hash = "0123456789abcdef0123456789abcdef"

plugins = dict(
    root="plugins",
    include=[
        "vc.player",
        "ping",
        "sysinfo"
    ]
)

app = Client("tgvc", api_id, api_hash, plugins=plugins)
app.start()
print('>>> USERBOT BERMAIN')
idle()
app.stop()
print('\n>>> USERBOT BERHENTI')
```

## Notes

- Read module docstrings of [plugins/](plugins) you are going to use at the
  beginning of the file for extra notes

## Self-hosting

This userbot should run fine on any cloud server. Popular choices of cloud
server providers are DigitalOcean, Vultr and Hetzner. You can use one of the
following referral links to sign up on Vultr to give the project author
credits in case you want to try Vultr.

<a href="https://www.vultr.com/?ref=7321667"><img src="https://www.vultr.com/media/banners/banner_728x90.png" width="728" height="90"></a>

Or [Give100get25 - Vultr](https://www.vultr.com/?ref=8559837-6G)

# License

AGPL-3.0-or-later

```
tgvc-userbot, Telegram Voice Chat Userbot
Copyright (C) 2021  Dash Eclipse

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
```
