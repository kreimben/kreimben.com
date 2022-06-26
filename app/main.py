import uvicorn

import frontend
import routers.api as api
from configure import ready, FastAPI
from event import setting_event

# Setting base app.
app: FastAPI = ready()
setting_event(app)

app.include_router(frontend.router)
app.include_router(api.router)

if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0", port=10120, reload=True, log_level="info")
