# FastAPI.
from fastapi.responses import FileResponse

# Custom.
from configure import *
from event import setting_event
from database import db
import os
import uvicorn

# Setting base app.
app: FastAPI = ready()
setting_event(app)


@app.get("/")
async def entry():
    return {"success": True, "content": "How about seek other APIs?"}


@app.get("/get_photos", responses={
    200: {
        "success": True,
        "content": {
            "application/json": {
                "example": "No example available. Just imagine urls!"
            }
        }
    }
})
async def get_photos():
    urls = db.get_photos()
    file_names = []

    for url in urls:
        file_names.append(url.split("/")[-1])

    if not urls:
        return {"success": False, "content": "File not found! Literally, Nothing!!!"}
    else:
        return {"success": True, "content": file_names, "len": len(file_names)}


@app.get("/get_photo/{photo_file_name}", responses={
    200: {
        "success": True,
        "content": {
            "image/jpg": {
                "example": "No example available. Just imagine a picture!"
            }
        }
    },
    422: {
        "success": False,
        "content": "id is not available!"
    }
})
async def get_photo(photo_file_name=""):
    path = '{}'.format(os.getcwd() + "/database/images/" + photo_file_name)
    print("path: ", path)

    print("photo_file_name: ", photo_file_name)
    if not photo_file_name:
        return {"success": False, "content": "Please give me any file name!", "param": photo_file_name}
    elif os.path.exists(path):
        return FileResponse(path, media_type="image/jpg")
    else:
        return {"success": False, "content": "id is not available!", "requested_id": photo_file_name}


@app.get("/update_photos", responses={
    200: {
        "success": True,
        "message": "Success to update photos.",
        "file_name": ["example_file_name_1", "example_file_name_2"]
    }
})
async def update_photos():
    urls = db.update_photos()
    file_name = []

    for url in urls:
        file_name.append(url.split("/")[-1])

    return {
        "success": True,
        "message": "Success to update photos.",
        "file_name": file_name
    }


if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0", port=10120, reload=True, log_level="info")
