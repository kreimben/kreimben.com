from configure import *
from event import setting_event
import frontend
import uvicorn

# Setting base app.
app: FastAPI = ready()
setting_event(app)

app.include_router(frontend.router)

if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0", port=10120, reload=True, log_level="info")
