from .exceptions import InvalidCredentialsError, LoginRequiredError, InternalException
from .links import POINTS_URL, LOGOUT_URL, LOGIN_URL
from requests import JSONDecodeError, Session
from re import search as re_search
from typing import Any


class APISession:
    def __init__(
        self, user: str | int | None = None, password: str | None = None
    ) -> None:
        """login: Either the salary number or the phone number.
        password: Password for the account."""
        self.__user = None
        if user != None:
            self.__user = str(user)
        self.__password = password

        self.__is_logged_in = False
        if self.__user != None and self.__password != None:
            self.login(self.__user, self.__password)

        self.__worker_type = None
        self.__session = Session()

    def get_earned_points(self) -> int:
        self.__ensure_logged_in()

        response = self.__session.get(POINTS_URL)
        response_text = response.text

        if not response.ok:
            raise InternalException(
                f"unhandled response code {response.status_code} from server"
            )

        match_results = re_search(r"<span>[0-9]{1,10}<\/span>", response_text)
        if match_results == None:
            raise InternalException("invalid response from api")

        return int(match_results.group().replace("<span>", "").replace("</span>", ""))

    def logout(self) -> None:
        self.__ensure_logged_in()

        self.__session.get(LOGOUT_URL)
        self.__is_logged_in = False

    def login(self, user: str | int, password: str) -> dict[str, str]:
        """login: Either the salary number or the phone number.
        password: Password for the account."""
        self.__ensure_session_id()
        data = {
            "action": "disy_login",
            "remember_loennr": "0",
            "language": "da",
            "loennr": str(user),
            "password": password,
        }
        headers = {
            "X-Requested-With": "XMLHttpRequest",
            "Content-Type": "application/x-www-form-urlencoded;charset=utf-8",
        }
        response = self.__session.post(LOGIN_URL, data=data, headers=headers)
        try:
            response_json: dict[str, Any] = response.json()
        except JSONDecodeError:
            raise InternalException("invalid response from api")

        if response.ok:
            if not response_json.get("success"):
                raise InvalidCredentialsError(f"invalid user or password")
        else:
            raise InternalException(
                f"unhandled response code {response.status_code} from server"
            )

        self.__user = str(user)
        self.__password = password
        self.__worker_type = response_json.get("medarbejdertype")
        self.__is_logged_in = True

        return {
            "user": self.__user,
            "password": self.__password,
            "worker_type": self.__worker_type,
        }

    def __ensure_logged_in(self) -> None:
        if not self.__is_logged_in:
            raise LoginRequiredError("you have to be logged in to do this action")
        if not self.has_session_id:
            raise LoginRequiredError("you have no session id, try to login again")

    def __ensure_session_id(self) -> None:
        if not self.has_session_id:
            self.__session.get(
                LOGIN_URL
            )  # going to the login page retrieves a session id

    @property
    def has_session_id(self) -> bool:
        return "PHPSESSID" in self.__session.cookies.keys()

    @property
    def user(self) -> str:
        return self.__user

    @property
    def password(self) -> str:
        return self.__password

    @property
    def earned_points(self) -> int:
        return self.get_earned_points()

    @property
    def worker_type(self) -> str:
        return self.__worker_type

    @property
    def http_session(self) -> Session:
        return self.__session

    @property
    def is_logged_in(self) -> bool:
        return self.__is_logged_in
