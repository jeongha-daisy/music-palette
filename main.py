from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import os
import uuid

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.post("/upload")
async def upload_image(file: UploadFile = File(...)):
    filename = f"{uuid.uuid4()}.png"
    file_path = os.path.join(UPLOAD_FOLDER, filename)

    with open(file_path, "wb") as buffer:
        buffer.write(await file.read())

    return {"filename": filename}

# ✅ 이미지 리스트 반환 API
@app.get("/images")
async def list_images():
    files = os.listdir(UPLOAD_FOLDER)
    files = [f for f in files if f.endswith(".png")]
    return {"files": files}


# 정적 파일 서빙 추가
app.mount("/uploads", StaticFiles(directory=UPLOAD_FOLDER), name="uploads")
