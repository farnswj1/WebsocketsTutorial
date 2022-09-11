import asyncio
from websockets import serve


async def echo(websocket):
    async for message in websocket:
        msg = f'Message received: {message}'
        print(msg)
        await websocket.send(msg)


async def main():
    print('Ready to serve!')
    async with serve(echo, 'localhost', 8765):
        await asyncio.Future()  # run forever


if __name__ == '__main__':
    asyncio.run(main())
