import asyncio
import websockets

async def send_messages(websocket, username):
    loop = asyncio.get_event_loop()
    while True:
        msg = await loop.run_in_executor(None, input, f"{username}: ")
        # Only send to server, don’t print locally
        await websocket.send(f"[{username}] {msg}")

async def receive_messages(websocket):
    while True:
        try:
            response = await websocket.recv()
            print(response)
        except websockets.ConnectionClosed:
            print("Connection closed by server.")
            break

async def chat():
    username = input("Enter your username: ")
    async with websockets.connect("ws://localhost:8765") as websocket:
        print("Connected to chat server!")
        await asyncio.gather(
            send_messages(websocket, username),
            receive_messages(websocket)
        )

asyncio.run(chat())