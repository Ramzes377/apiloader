from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive


class AuthSession:
    def __init__(self):
        _auth = GoogleAuth()
        _auth.LocalWebserverAuth()
        self._drive = GoogleDrive(_auth)

    def __call__(self):
        return self._drive


auth = AuthSession()

