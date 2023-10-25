import base64
from importlib.metadata import version
from typing import Any, Dict, List, Optional, Tuple

import cattrs
import requests
from typeguard import typechecked

import viqubox_sdk._util as utils
from viqubox_sdk.exceptions import APIRequestError, AuthException
from viqubox_sdk.models import Job, ProcessingRequest


class Authentication:
    """Class representing ViQuBox API client authentication object."""

    @typechecked
    def __init__(
        self,
        username: str = "",
        password: str = "",
        api_key: str = "",
    ) -> None:
        self.api_key = api_key
        self.username = username
        self.password = password

        if not any((api_key, username, password)):
            raise AuthException(
                "must provide at least api_key or username and password for authentication"
            )

    @property
    def username(self) -> str:
        return self._username

    @username.setter
    def username(self, user_name: str) -> None:
        if not self.api_key and not isinstance(user_name, str):
            raise ValueError(f"Username must be a string: {user_name}")
        if ":" in user_name:
            raise ValueError(
                "Username cannot contain ':' symbols. According to RFC 7617 specification"
            )
        self._username = user_name

    @property
    def password(self) -> str:
        return self._password

    @password.setter
    def password(self, passwrd: str) -> None:
        if not self.api_key and not isinstance(passwrd, str):
            raise ValueError(f"Password must be a string: {passwrd}")
        self._password = passwrd

    def _to_base64(self) -> str:
        final = f"{self.username}:{self.password}"
        byte_str = base64.b64encode(bytes(final, "utf-8"))
        return byte_str.decode("utf-8")

    @property
    def header(self) -> Dict[str, str]:
        if self.api_key:
            auth_val = self.api_key
        else:
            auth_val = f"Basic {self._to_base64()}"

        return {"Authorization": auth_val}


class ViquboxClient:
    """Class that represents the ViQuBox API data processing client.
    Authentication can be provided using the :class:`Authentication` class
    or by just supplying a `username` and `password` keyword arguments.

    Usage::
        >>> ViquboxClient(username="user1", password="pass1")
        >>> ViquboxClient(authentication=Authentication(username="user1", password="pass1"))
    """

    def __init__(
        self,
        authentication: Optional[Authentication] = None,
        username: str = "",
        password: str = "",
        api_key: str = "",
        base_url: str = "https://api.viqubox.com/api/v1",
    ) -> None:
        self._api_base_url = base_url
        self._authentication = authentication or Authentication(
            username, password, api_key
        )
        self._session = requests.Session()
        self._session.headers["User-Agent"] = f"viqubox-sdk-python/{version(__package__)}"
        if self._authentication is not None:
            self._session.headers.update(self._authentication.header)

    def _get(self, endpoint: str, **kwargs: Any) -> requests.Response:
        res = self._session.get(f"{self._api_base_url}{endpoint}", **kwargs)
        if not res.ok:
            raise APIRequestError(res.content)
        return res

    def _post(self, endpoint: str, **kwargs: Any) -> requests.Response:
        res = self._session.post(f"{self._api_base_url}{endpoint}", **kwargs)
        if not res.ok:
            raise APIRequestError(res.content)
        return res

    @typechecked
    def processing_create(
        self, processing_request: ProcessingRequest
    ) -> ProcessingRequest:
        """Send a POST request to /processing endpoint to create a processing request.

        :param processing_request: processing request model.
        :return: Same type of class with filles `id` and `jobs` attributes.
        """
        json_req = cattrs.unstructure(processing_request)
        res = self._post("/processing", json=json_req)
        return cattrs.structure(res.json(), ProcessingRequest)

    @typechecked
    def processing_list(self) -> List[ProcessingRequest]:
        """Send a GET request to `/processing` endpoint to get all the processing request
        details along with jobs and ids.

        :return: A list of processing requests.
        """
        res = self._get("/processing")
        return cattrs.structure(res.json(), List[ProcessingRequest])

    @typechecked
    def processing_get(self, processing_id: str) -> ProcessingRequest:
        """Send a GET request to `/processing/:processing_id` endpoint to get
        the processing request details along with jobs and ids.

        :param processing_id: The processing request ID.
        :return: The processing request object.
        """
        res = self._get(f"/processing/{processing_id}")
        return cattrs.structure(res.json(), ProcessingRequest)

    @typechecked
    def processing_get_jobs(self, processing_id: str) -> List[Job]:
        """Send a GET request to `/processing/:processing_id/jobs` to get the job
        statuses and results if present.

        :param processing_id: The processing request id.
        :return: Jobs with their IDs, statuses and if job is finished.
        """
        res = self._get(f"/processing/{processing_id}/jobs")
        return cattrs.structure(res.json(), List[Job])

    @typechecked
    def processing_get_job(self, processing_id: str, job_id: str) -> Job:
        """Send a GET request to `/processing/:processing_id/jobs/:job_id` to get
        information about a single job.

        :param processing_id: Job processing request ID.
        :param job_id: Processing job ID.
        :return: Single job with it's information.
        """
        res = self._get(f"/processing/{processing_id}/jobs/{job_id}")
        return cattrs.structure(res.json(), Job)

    @typechecked
    def audio_shortcut(
        self,
        audio_pairs: List[Tuple[str, str]],
        query_string: dict = {"metric": "polqa", "mode": "wideband"},
        ignore_missing: bool = False,
    ) -> Tuple[str, list]:
        """Pre-process and validate audio file pairs and send them to API for audio processing.

        :param audio_pairs: Local system paths leading to files in format List[Tuple(reference: str, degraded: str)]
        :param query_string: _description_, defaults to {"metric": "polqa", "mode": "wideband"}
        :param ignore_missing: Continue flow if some paths are not found on local system, defaults to False
        :return: A tuple containing (processing id, input file mapping to API input file names)
        """

        input_files, translation = utils.prepare_audio_pairs(
            audio_pairs, ignore_missing=ignore_missing
        )
        response = self._post("/processing/audio", files=input_files, params=query_string)
        return (response.json()["id"], translation)
