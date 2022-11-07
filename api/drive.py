import os

from api.auth import auth


def upload_data(filepath: str, filename: str | None = None) -> None:
    gfilename = filename if filename is not None else os.path.split(filepath)[1]

    drive = auth()
    gfile = drive.CreateFile({'title': gfilename})
    gfile.SetContentFile(filepath)
    gfile.Upload()
