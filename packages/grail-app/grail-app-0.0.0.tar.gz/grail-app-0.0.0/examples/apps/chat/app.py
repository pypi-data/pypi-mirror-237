from quart import render_template, request
from typing import AsyncGenerator
import asyncio
from quart import websocket
from quart import Quart

class Broker:
    def __init__(self) -> None:
        self.connections = set()

    async def publish(self, message: str) -> None:
        for connection in self.connections:
            await connection.put(message)

    async def subscribe(self) -> AsyncGenerator[str, None]:
        connection = asyncio.Queue()
        self.connections.add(connection)
        try:
            while True:
                yield await connection.get()
        finally:
            self.connections.remove(connection)

app = Quart(__name__)
broker = Broker()

@app.get("/")
async def index():
    return await render_template("index.html")

async def _receive() -> None:
    while True:
        message = await websocket.receive()
        await broker.publish(f" >>> {message}")

@app.websocket("/ws")
async def ws() -> None:
    task = None
    try:
        task = asyncio.ensure_future(_receive())
        async for message in broker.subscribe():
            await websocket.send(message)
    finally:
        if task:
            task.cancel()
            await task

if __name__ == '__main__':
    app.run()