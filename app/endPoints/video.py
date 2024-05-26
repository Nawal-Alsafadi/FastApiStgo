from fastapi import APIRouter, UploadFile, File, HTTPException
from fastapi.responses import FileResponse
from pathlib import Path
from app.video_processing import process_video

router = APIRouter()

@router.post("/process/")
async def upload_and_process_video(file: UploadFile = File(...)):
    video_dir = Path("data/videos")
    video_dir.mkdir(parents=True, exist_ok=True)
    
    file_location = video_dir / file.filename
    
    with file_location.open("wb") as f:
        f.write(await file.read())
    
    text_file_path = process_video(str(file_location))
    
    if not text_file_path:
        raise HTTPException(status_code=500, detail="Video processing failed")
    
    return FileResponse(text_file_path, media_type='application/octet-stream', filename=Path(text_file_path).name)
