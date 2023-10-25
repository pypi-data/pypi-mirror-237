#!/usr/bin/env python
import os
import sys
from time import sleep
from dotenv import load_dotenv
from farcaster.HubService import HubService
from farcaster.fcproto.message_pb2 import MessageType, Message

import base64
import argparse

#def Subscribe(self, event_types, from_id=None)  -> HubEvent:
