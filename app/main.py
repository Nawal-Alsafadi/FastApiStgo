# 
from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from pathlib import Path
from app.video_processing import process_video

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/video/process/")
async def process_video_and_download_text(file: UploadFile = File(...)):
    video_dir = Path("data/videos")
    video_dir.mkdir(parents=True, exist_ok=True)
    
    file_location = video_dir / file.filename
    
    with file_location.open("wb") as f:
        f.write(await file.read())
    
    text_file_path = process_video(str(file_location))
    
    if not text_file_path:
        raise HTTPException(status_code=500, detail="Video processing failed")
    
    return FileResponse(text_file_path, media_type='application/octet-stream', filename=str(Path(text_file_path).name))
