import os
from pathlib import Path

def process_video(file_path: str) -> str:
    print("Hola 1!!!")
    print(file_path)
    # Dummy processing - for example, just create a dummy text file
    text_file_name = os.path.basename(file_path).replace(".mp4", ".txt")
    text_file_path = Path(f"data/texts/{text_file_name}")
    
    text_file_path.parent.mkdir(parents=True, exist_ok=True)
    
    with open(text_file_path, "w") as f:
        f.write("Dana Is The Best!!!.")
        
    print("Hola !!!")
    print(text_file_path)
        
    return str(text_file_path)
