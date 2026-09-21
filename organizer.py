from pathlib import Path

downloads_dir = Path.home() / "downloads"

categories = {
    # images
    ".jpg": "Images",
    ".jpeg": "Images",
    ".png": "Images",
    ".gif": "Images",
    
    # Documents
    ".pdf": "Documents",
    ".docx": "Documents",
    ".txt": "Documents",
    
    # Programs & Archives
    ".exe": "Programs",
    ".msi": "Programs",
    ".zip": "Archives",
    ".rar": "Archives"
}

print(f"Targeting directory: {downloads_dir}")
print(f"Does this directory exist? {downloads_dir.exists()}")

for file_path in downloads_dir.iterdir():

    if file_path.is_file():
        file_extension = file_path.suffix.lower()
        if file_extension in categories:
            folder_name = categories[file_extension]
            target_folder = downloads_dir / folder_name
            target_folder.mkdir(exist_ok=True)
            destination_path = target_folder / file_path.name

            file_path.rename(destination_path)
            print(f"Moved: {file_path.name} -> {folder_name}/")