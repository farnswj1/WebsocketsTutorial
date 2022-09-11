import asyncio
from websockets import connect


async def hello(uri):
    print('Ready to go!')
    async with connect(uri) as websocket:
        await websocket.send('This is my message!')
        res = await websocket.recv()
        print(res)


if __name__ == '__main__':
    asyncio.run(hello('ws://localhost:8765'))
