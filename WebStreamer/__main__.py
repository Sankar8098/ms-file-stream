# This file is a part of ms-file-stream
# Coding : Mr Malik [@mrmalik_offl]

import sys
import asyncio
import logging
from .vars import Var
from aiohttp import web
from pyrogram import idle
from WebStreamer import utils
from WebStreamer import StreamBot
from WebStreamer.server import web_server
from WebStreamer.bot.clients import initialize_clients


logging.basicConfig(
    level=logging.DEBUG if Var.DEBUG else logging.INFO,
    datefmt="%d/%m/%Y %H:%M:%S",
    format="[%(asctime)s][%(name)s][%(levelname)s] ==> %(message)s",
    handlers=[logging.StreamHandler(stream=sys.stdout),
              logging.FileHandler("streambot.log", mode="a", encoding="utf-8")],)

logging.getLogger("aiohttp").setLevel(logging.DEBUG if Var.DEBUG else logging.ERROR)
logging.getLogger("pyrogram").setLevel(logging.INFO if Var.DEBUG else logging.ERROR)
logging.getLogger("aiohttp.web").setLevel(logging.DEBUG if Var.DEBUG else logging.ERROR)

server = web.AppRunner(web_server())

# if sys.version_info[1] > 9:
#     loop = asyncio.new_event_loop()
#     asyncio.set_event_loop(loop)
# else:
loop = asyncio.get_event_loop()



async def start_services():
    logging.info("Initializing Telegram Bot")
    await StreamBot.start()
    bot_info = await StreamBot.get_me()
    logging.debug(bot_info)
    StreamBot.username = bot_info.username
    logging.info("Initialized Telegram Bot")
    await initialize_clients()
    if Var.KEEP_ALIVE:
        asyncio.create_task(utils.ping_server())
    await server.setup()
    await web.TCPSite(server, Var.BIND_ADDRESS, Var.PORT).start()
    logging.info("Service Started")
    logging.info("bot =>> {}".format(bot_info.first_name))
    if bot_info.dc_id:
        logging.info("DC ID =>> {}".format(str(bot_info.dc_id)))
    logging.info("URL =>> {}".format(Var.URL))
    await idle()

async def cleanup():
    await server.cleanup()
    await StreamBot.stop()

if __name__ == "__main__":
    try:
        loop.run_until_complete(start_services())

async def get_shortlink(link):
    https = link.split(":")[0]
    if "http" == https:
        https = "https"
        link = link.replace("http", https)

    url = f'https://dulink.in/api'
    params = {'api': URL_SHORTNER_WEBSITE_API,
              'url': link,        
              }

    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url, params=params, raise_for_status=True, ssl=False) as response:
                data = await response.json()
                if data["status"] == "success":
                    return data['shortenedUrl']
                else:
                    logger.error(f"Error: {data['message']}")
                    return f'https://{URL_SHORTENR_WEBSITE}/api?api={URL_SHORTNER_WEBSITE_API}&link={link}'

    except Exception as e:
        logger.error(e)
        return f'{URL_SHORTENR_WEBSITE}/api?api={URL_SHORTNER_WEBSITE_API}&link={link}'
