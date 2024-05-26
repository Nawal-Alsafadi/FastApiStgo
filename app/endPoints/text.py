# from fastapi import APIRouter, UploadFile, File, HTTPException
# from pathlib import Path
# from app.video_processing import process_video

# router = APIRouter()

# @router.post("/upload/")
# async def upload_video(file: UploadFile = File(...)):
#     video_dir = Path("data/videos")
#     video_dir.mkdir(parents=True, exist_ok=True)
    
#     file_location = video_dir / file.filename
    
#     with file_location.open("wb") as f:
#         f.write(await file.read())
    
#     text_file_path = process_video(str(file_location))
    
#     if not text_file_path:
#         raise HTTPException(status_code=500, detail="Video processing failed")
    
#     return {"message": "Video uploaded and processed successfully", "text_file": text_file_path}
