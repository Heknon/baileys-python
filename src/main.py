import asyncio
import base64
import json
import os
import time

import websockets.legacy.client
from websockets.typing import Origin
from websockets.uri import WebSocketURI

WHATSAPP_URI = WebSocketURI(True, 'web.whatsapp.com', 443, '/ws/chat', '')


async def main():
    client: websockets.legacy.client.WebSocketClientProtocol = await websockets.legacy.client.connect(
        'wss://web.whatsapp.com/ws/chat',
        origin=Origin('https://web.whatsapp.com')
    )

    await client.send(
        f'{time.time()},{json.dumps(["admin", "init", [0, 3, 2390], ["Long browser description", "ShortBrowserDesc"], base64.b64encode(os.urandom(16)).decode(), True])}'.encode())

    response = await client.recv()
    print(response)


if __name__ == '__main__':
    asyncio.run(main())
