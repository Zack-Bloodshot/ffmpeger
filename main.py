from telethon import events
from os import getenv
from dotenv import load_dotenv
from telethon.sync import TelegramClient
import os
import asyncio
import ffmpeg
from FastTelethonhelper import fast_download, fast_upload
import logging

API_ID= int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
BOT_TOKEN = getenv("BOT_TOKEN")

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN)

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level = logging.INFO)

logger = logging.getLogger("__name__")


def vidsticker(in_filename):
  out_filename =f'{in_filename[:-3]}_processed.webm'
  try:
    (
      ffmpeg.
      input(in_filename)
      .output(out_filename, vcodec='libvpx-vp9', crf=40, pix_fmt='yuva420p', vf='scale=512:-1')
      .global_args('-report')
      .run()
    )
  except ffmpeg.Error as e:
     print(e.stderr.decode())
  return out_filename
  
@bot.on(events.NewMessage(pattern=r'/vs'))
async def stickervid(event):
  video = await event.get_reply_message()
  if video.file.duration > 3:
    return await event.reply('Should be smaller than 3 secs as per Telegram video-sticker guideline.')
  m = await event.reply('Downloading...')
  dl = await fast_download(bot, video)
  await m.edit('Encoding....')
  hek = vidsticker(dl)
  await m.edit('Uploading...')
  fu = await fast_upload(bot, hek)
  await bot.send_message(event.chat_id, file = fu, force_document=True)
  await m.delete()
  os.remove(dl)
  os.remove(hek)  


print('Starting...')
bot.start() 
print('Bot started!')
bot.run_until_disconnected()  