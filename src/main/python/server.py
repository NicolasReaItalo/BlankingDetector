#!/usr/bin/env python

# WS server example

import asyncio
import websockets

from main import *

class Coucou(Window):
    def __init__(self):
        self.project = VideoCheck()

a = Coucou()

async def hello(websocket, path):
    name = await websocket.recv()
    print(name)
    a.mon_vrai_press(name)

start_server = websockets.serve(hello, "localhost", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
