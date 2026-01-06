import asyncio
import websockets
from datetime import datetime

connected_clients = set()

async def handler(websocket):
    connected_clients.add(websocket)
    print(f"Client connected. Total: {len(connected_clients)}")
    try:
        async for message in websocket:
            timestamp = datetime.now().strftime("%H:%M:%S")
            broadcast = f"[{timestamp}] {message}"
            print(f"Broadcasting: {broadcast} to {len(connected_clients)} clients")
            for client in connected_clients.copy():
                try:
                    await client.send(broadcast)
                except websockets.ConnectionClosed:
                    connected_clients.remove(client)
    finally:
        connected_clients.remove(websocket)
        print(f"Client disconnected. Total: {len(connected_clients)}")

async def main():
    async with websockets.serve(handler, "localhost", 8765):
        print("Chat server running on ws://localhost:8765")
        await asyncio.Future()  # run forever

asyncio.run(main())