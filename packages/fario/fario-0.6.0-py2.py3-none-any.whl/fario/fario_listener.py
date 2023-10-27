#!/usr/bin/env python
import os
import sys
import asyncio
from time import sleep
from dotenv import load_dotenv
from farcaster.HubService import HubService
from farcaster.fcproto.message_pb2 import MessageType, Message

import base64
import argparse

#def Subscribe(self, event_types, from_id=None)  -> HubEvent:

async def main():
	load_dotenv()
	hub_address = os.getenv("FARCASTER_HUB")

	if not hub_address:
		print("No hub address. Use --hub of set FARCASTER_HUB in .env.")
		sys.exit(1)

	hub = HubService(hub_address, use_async=True)
	feed = hub.Subscribe([1])
	async for m in feed:
		print(m)

if __name__ == "__main__":
    asyncio.run(main())
