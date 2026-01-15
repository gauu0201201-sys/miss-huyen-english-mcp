from fastapi import FastAPI
from fastapi.responses import StreamingResponse
import json
import asyncio

app = FastAPI()

@app.get("/")
def root():
    return {"status": "Miss Huyền English MCP Server is running"}

@app.get("/sse")
async def sse():
    async def event_generator():
        while True:
            data = {
                "message": "Miss Huyền English MCP – học tiếng Anh từ mất gốc đến IELTS"
            }
            yield f"data: {json.dumps(data)}\n\n"
            await asyncio.sleep(5)

    return StreamingResponse(event_generator(), media_type="text/event-stream")
