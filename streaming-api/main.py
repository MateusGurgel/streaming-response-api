import asyncio
from time import sleep

from fastapi import FastAPI
from fastapi.responses import StreamingResponse

from .lorem_ipsum import lorem_ipsum

app = FastAPI()
@app.get("/")
async def read_root():

    async def fake_stream():
        for chunk in lorem_ipsum.split(" "):
            yield chunk + " "
            await asyncio.sleep(0.01)

    return StreamingResponse(
        content=fake_stream(),
        media_type="text/plain",
        status_code=200,
    )
