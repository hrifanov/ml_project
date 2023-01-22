from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive
import os
import io

def google_drive_get_photos(drive, save_path):
    file_list = drive.ListFile({'q': "'1hOAGM4vongZKqMc3QtvNEV7UEHlX528f' in parents and trashed=false"}).GetList()
    for file in file_list:
        photo = drive.CreateFile({"id": file["id"]})
        photo.GetContentFile(os.path.join(save_path, file["title"] + ".jpg"))

if __name__ == "__main__":
    gauth = GoogleAuth()
    gauth.LocalWebserverAuth()
    drive = GoogleDrive(gauth)
    
    google_drive_get_photos(drive, save_path = "processed_images\\")