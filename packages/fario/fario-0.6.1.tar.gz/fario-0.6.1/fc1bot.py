#!/usr/bin/env python
import os
import sys
import time
import asyncio
from time import sleep
from dotenv import load_dotenv
from farcaster.HubService import HubService
from farcaster.fcproto.message_pb2 import MessageType
from farcaster.fcproto.message_pb2 import HashScheme, Message, MessageData, CastAddBody, CastId, SignatureScheme, Embed
from farcaster.fcproto.request_response_pb2 import StoreType
from blake3 import blake3
import base64
import argparse
import json
from google.protobuf.json_format import ParseDict
from nacl.signing import SigningKey
from farcaster import FARCASTER_EPOCH

import concurrent.futures

BOT_FID=20396
APP_SIGNER_KEY=""
HUB_ADDRESS=""

def signer_sign(signer_key,m):
    signer=SigningKey(bytes.fromhex(signer_key[2:]))
    signer_pub_key=signer.verify_key.encode()
    if m.hash_scheme == HashScheme.HASH_SCHEME_BLAKE3:
        data_serialized = m.data.SerializeToString()
        msg_hash = blake3(data_serialized).digest(length=20)
        msg_signature = signer.sign(msg_hash).signature
        m.signer=signer_pub_key
        m.signature=msg_signature
        m.hash = msg_hash
        m.data_bytes = data_serialized
    return(m)
def fid_by_name(name):
    ret  = hub.GetUsernameProof(args.username)
    if ret:
        return ret.fid
    else:
        return None
def get_storage_limits_by_fid(fid):
    hub = HubService(HUB_ADDRESS, use_async=False)
    ret  = hub.GetCurrentStorageLimitsByFid(fid)
    limits = { StoreType.Name(l.store_type)[11:].lower(): l.limit for l in ret.limits }
    return (limits)
def get_usage(fid):
    def count(c, fn, args):
        ret = fn(**args)
        if hasattr(ret,'messages'):
            c = c + len(ret.messages)
        if hasattr(ret,'proofs'):
            c = c + len(ret.proofs)
        if getattr(ret,'next_page_token', None):
            args['page_token'] = ret.next_page_token
            return( count(c, fn, args) )
        else:
            return c
    hub = HubService(HUB_ADDRESS, use_async=False)
    embed_url = None
    usage = (
        ('casts', hub.GetCastsByFid, {"fid":fid, "page_size":1000} ),
        ('links', hub.GetLinksByFid, {"fid":fid, "page_size":1000} ),
        ('likes', hub.GetReactionsByFid, {"fid":fid, "reaction_type":1, "page_size":1000} ),
        ('recasts', hub.GetReactionsByFid, {"fid":fid, "reaction_type":2, "page_size":1000} ),
        ('user_data', hub.GetUserDataByFid, {"fid":fid, "page_size":1000} ),
        ('proofs', hub.GetUserNameProofsByFid, {"fid":fid, "page_size":1000} ),
        ('verifications', hub.GetVerificationsByFid, {"fid":fid, "page_size":1000} )
        )
    usage_counts = {}
    for u in usage:
        usage_counts[u[0]] = count(0, u[1], u[2])
    return usage_counts
def respond(cast_fid, cast_hash, cast_text):
    if cast_text.strip() == 'storage':
        print(f"Responding to {cast_fid} cast={cast_hash.hex()}")
        reply_text = "Your storage usage";
        limits = get_storage_limits_by_fid(cast_fid)
        usage  = get_usage(cast_fid)
        reply_text += f"\n{usage['casts']:,} / {limits['casts']:,} casts"
        reply_text += f"\n{usage['links']:,} / {limits['links']:,} follows"
        reply_text += f"\n{(usage['likes']+usage['recasts']):,} / {limits['reactions']:,} reactions"
        reply_text += f"\n{usage['user_data']:,} / {limits['user_data']:,} user_data"
        reply_text += f"\n{usage['proofs']:,} / {limits['username_proofs']:,} proofs"
        reply_text += f"\n{usage['verifications']:,} / {limits['verifications']:,} verifications"
        if (limits['casts'] - usage['casts'] > 3000) and (limits['reactions']-usage['likes']-usage['recasts'] > 2000):
            embed_url="https://cyan-organisational-reindeer-861.mypinata.cloud/ipfs/QmQwhceDnzN6qJ64PtmgHj7ntEQuL1vQG59jupShaa1GFU"
    else:
        reply_text = 'I can only reply to the command "@fc1 storage"'
    print(reply_text)

    reply_pb = Message(
        data = MessageData(
            type=MessageType.MESSAGE_TYPE_CAST_ADD,
            fid=int(BOT_FID),
            timestamp = int( time.time() ) - FARCASTER_EPOCH,
            network=1,
            cast_add_body = CastAddBody(
                parent_cast_id=CastId(
                    fid=cast_fid,
                    hash=cast_hash
                ),
                text=reply_text
            )
        ),
        hash=bytes(000),
        hash_scheme=HashScheme.HASH_SCHEME_BLAKE3,
        signature=bytes(000),
        signature_scheme=SignatureScheme.SIGNATURE_SCHEME_ED25519,
        signer=bytes(000)
    )
    if embed_url:
        reply_bp.data.cast_add_body.embeds = [ Embed(url=embed_url) ]
    
    #print(reply_pb)
    pb = signer_sign(APP_SIGNER_KEY, reply_pb)
    #print(pb)
    hub = HubService(HUB_ADDRESS, use_async=False)
    ret = hub.SubmitMessage(pb)
    print("=== Submited ===")
    #print(ret)

async def main():
    with concurrent.futures.ThreadPoolExecutor() as executor:
        hub = HubService(HUB_ADDRESS, use_async=True)
        feed = hub.Subscribe([1])
        async for m in feed:
            if m.merge_message_body.message.data.type == MessageType.MESSAGE_TYPE_CAST_ADD:
                if BOT_FID in m.merge_message_body.message.data.cast_add_body.mentions:
                    # print(m)
                    executor.submit(
                        respond(
                            m.merge_message_body.message.data.fid, 
                            m.merge_message_body.message.hash, 
                            m.merge_message_body.message.data.cast_add_body.text 
                        )
                    )
                    

if __name__ == "__main__":
    load_dotenv()
    HUB_ADDRESS = os.getenv("FARCASTER_HUB")
    APP_SIGNER_KEY = os.getenv("APP_SIGNER_KEY")
    # ret = respond(3,bytes.fromhex('917a30881a5859b2d2dae6bba3edd7d7c07ed924'), 'hello')
    # print(ret)
    # sys.exit(0)
    if not HUB_ADDRESS:
        print("No hub address. Use --hub of set FARCASTER_HUB in .env.")
        sys.exit(1)

    asyncio.run(main())
