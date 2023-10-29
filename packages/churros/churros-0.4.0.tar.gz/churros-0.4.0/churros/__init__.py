from pathlib import Path
import shutil
from tempfile import mktemp
import requests
from churros.api import Client as AriadneClient
from churros.api.group import GroupGroup
from churros.api.user import UserUser


class InvalidCredentials(Exception):
    pass


class UnknownError(Exception):
    pass


class Unauthorized(Exception):
    pass


class DownloadablePictureFile:
    def download_picture_file(self, to: Path | str|None = None) -> Path|None:
        picture_filename = getattr(self, "picture_file")
        if not picture_filename:
            return None

        to = to or mktemp(suffix=".png")

        response = requests.get(
            f"https://churros.inpt.fr/storage/{picture_filename}",
            stream=True,
        )

        if isinstance(to, str):
            to = Path(to)

        if response.status_code < 400:
            with to.open("wb") as file:
                response.raw.decode_content = True
                shutil.copyfileobj(response.raw, file)
        
        return to


class Group(GroupGroup, DownloadablePictureFile):
    pass


class User(UserUser, DownloadablePictureFile):
    pass


class Churros:
    _client: AriadneClient

    def __init__(
        self,
        url: str = "https://churros.inpt.fr/graphql",
        token: str | None = None,
    ) -> None:
        self._client = AriadneClient(url)
        self._client.headers = {
            "User-Agent": "Churros Python Library (https://pypi.org/project/churros)"
        }
        if token:
            self._client.headers["Authorization"] = f"Bearer {token}"

    @property
    def token(self) -> str | None:
        if headers := self._client.headers:
            return headers.get("Authorization", "").replace("Bearer ", "") or None

    @token.setter
    def token(self, value):
        self._client.http_client.headers["Authorization"] = f"Bearer {value}"
        print(self.token)

    @token.deleter
    def token(self):
        if not self._client.headers:
            return

        del self._client.headers["Authorization"]

    async def login(self, username: str, password: str) -> str:
        result = (await self._client.login(username, password)).login

        if result.typename__ == "Error":
            raise InvalidCredentials(result.message)

        self.token = result.data.token
        return result.data.token

    async def logout(self):
        result = (await self._client.logout()).logout

        if not result:
            raise UnknownError("Could not log out")

        del self.token

    @staticmethod
    def _rethrow_error(error: Exception):
        if str(error) == "Tu n'es pas autorisé à effectuer cette action.":
            raise Unauthorized(str(error))
        raise UnknownError(str(error))

    async def me(self) -> User:
        try:
            me = (await self._client.me()).me
            return User(**me.model_dump())
        except Exception as error:
            Churros._rethrow_error(error)

    async def user(self, uid: str) -> User:
        try:
            user = (await self._client.user(uid)).user
            return User(**user.model_dump())
        except Exception as error:
            Churros._rethrow_error(error)

    async def group(self, uid: str) -> Group:
        try:
            group = (await self._client.group(uid)).group
            return Group(**group.model_dump())
        except Exception as error:
            Churros._rethrow_error(error)
