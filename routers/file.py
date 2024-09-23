from fastapi import APIRouter, File, UploadFile
from fastapi.responses import FileResponse
import shutil
import os


router = APIRouter(
    prefix="/file",
    tags=["file"]
)

@router.get("/{name}", response_class=FileResponse)
def download_file(name: str):
    path = f"files/{name}"
    return path

@router.post("/")
def upload_file(file: bytes = File(...)):
    content = file.decode("utf-8")
    lines = content.split("\n")
    return {
        "lines": lines
    }

@router.post("/uploadfile")
def upload_large_file(file: UploadFile = File(...)):
    os.makedirs("files", exist_ok=True)

    path = f"files/{file.filename}"
    with open(path, "w+b") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {
        'filename': file.filename,
        'type': file.content_type
    }