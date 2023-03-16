import asyncio
import websockets
import json

async def main():
    async with websockets.connect("wss://ws.blockchain.info/inv") as client:
        print("[main] Connected to wss://ws.blockchain.info/inv")
        cmd = '{"op":"unconfirmed_sub"}'
        print('[main] Send:', cmd)
        await client.send(cmd)
        reav = client.recv()
        print('[main] Recv:', await reav)
        return reav
if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())

fileobj = open("list.json","w")
json.dump(main(),index=6)
fileobj.close()