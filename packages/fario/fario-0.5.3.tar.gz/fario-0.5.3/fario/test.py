#!/usr/bin/env python
import os
from dotenv import load_dotenv
from farcaster.HubService import HubService
from farcaster.fcproto.message_pb2 import SignatureScheme, HashScheme, Embed
from farcaster.fcproto.onchain_event_pb2 import OnChainEventType, OnChainEvent
from farcaster import Message

import argparse
"""
GetOnChainEvents(self, fid, event_type, page_size=50, page_token=None, reverse=True) -> OnChainEventResponse:
        return self._stub.GetOnChainEvents(OnChainEventRequest(
            fid=fid,
            event_type=event_type,
            page_size=page_size,
            page_token=page_token,
            reverse=reverse
        ))
"""
def main():

	load_dotenv()
	# Make sure you check .env.sample to create .env
	hub_address	= os.getenv("FARCASTER_HUB")

	hub = HubService(hub_address, use_async=False)
	ret  = hub.GetIdRegistryOnChainEvent(3887)
	print(ret)
	for i in (0,1,2,3,4,5,6):
		ret  = hub.GetOnChainEvents(3887,i)
		print(ret)
	#print(ret.id_register_event_body.to.hex())


if __name__ == '__main__':
	main()