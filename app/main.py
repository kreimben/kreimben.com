# FastAPI.
from fastapi.responses import FileResponse

# Custom.
from configure import *
from event import setting_event
import os
import uvicorn

# Setting base app.
app: FastAPI = ready()
setting_event(app)


@app.get("/")
async def entry():
    return {"success": True, "content": "How about seek other APIs?"}


if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0", port=10120, reload=True, log_level="info")
