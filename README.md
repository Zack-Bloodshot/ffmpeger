# Ffmpeg-bot

Ffmpeg command eval bot.

## Main-Usage:
<ul>
<li>
The bot takes ffmpeg commands and tries to eval them
</li>
<li>
The syntax or what commands to send the bot at the moment is <b>ffmpeg (cmds) (output extension)</b>, and reply to the file to use it as the input.'
</li>
</ul>

### Examples:
Examples are taken in mind that the output file extensions will be **mkv**.
#### To trim a video (Replying command to the file to be used as input):
```
ffmpeg -t 3 mk4
```
Here **ffmpeg** is the command handler, **-t 3** is the command and, **mkv** is the output extension.
#### Skip to a part of video + trim it + compress it using crf (Replying command to the file to be used as input):
```
ffmpeg -ss 60 -t 60 -vcodec libx264 -crf 28 mkv
```
Here ffmpeg is the command handler, **-ss 60 -t 60 -vcodec libx264 -crf 28** is the command, and **mkv** is the output extension.

---

## Side-Usage:
The bot also takes a video file and then tries to encode it according to [this guide](https://core.telegram.org/stickers#video-sticker-requirements)

<ul>
<li>
<b>What the bot does:
<img src='https://telegra.ph/file/3bcb1b37493c0375ee840.jpg'>
</li>
<li>
After processing through @Stickers bot:
<img src='https://telegra.ph/file/221a2718e773fe3f72eda.jpg'>
</b>
</li>
</ul>

### Deploy to heroku:

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/Zack-Bloodshot/Tg_Video_sticker_converter)

---

**MADE WITH LOVE, FEEL FREE TO PULL NEW FEATURES!!**