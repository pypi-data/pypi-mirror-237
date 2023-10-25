from __future__ import annotations

from collections import defaultdict
from enum import Enum
from typing import Any, Dict, List, Optional, Union

from attrs import define, field, validators
from attrs_strict import type_validator


class AuthenticationType(Enum):
    """Enum for authentication type, used along with :class:`AuthenticationOptions`.

    :param Enum: Name of authentication type.
    """

    HTTP_BASIC = "http_basic"
    PASSWORD = "password"


class JobStatus(Enum):
    """Enum representing the current job status, used in :class:`Job`.

    :param Enum: Status name.
    """

    QUEUED = "queued"
    LAUNCHED = "launched"
    SUCCESS = "success"
    FAILED = "failed"
    CANCELLED = "cancelled"


@define
class AuthenticationOptions:
    """Initialize authentication options.

    Usage::
        >>> from viqubox_sdk.models import AuthenticationOptions
        >>> AuthenticationOptions(opts={'username': 'admin', 'password': '123'}, type='password')
    """

    opts: Dict[str, str] = field(validator=[type_validator()])
    """Authentication options specific to the chosen type."""
    type: AuthenticationType = field(
        converter=AuthenticationType, validator=[type_validator()]
    )
    """Type of authentication. Supported: http_basic, password."""


@define
class InputFileConfig:
    """Class representing input file repository configuration."""

    paths: List[str] = field(factory=list, validator=[type_validator()])
    """A list of paths to input files, if no connection_protocol is provided, the
    protocol is taken from the path name."""
    connection_protocol: Optional[str] = field(default=None, validator=[type_validator()])
    """Connection protocol to use for download/upload, takes precendence
    over file path protocol."""
    authentication: Optional[AuthenticationOptions] = field(
        default=None, validator=[type_validator()]
    )
    """Authentication options for the file repository if there are any."""

    def add_path(self, path: str) -> None:
        """Add file path to config if it is not in it.

        :param path: Path of an input file.
        """
        self.paths.append(path)


@define
class MetricConfig:
    """Class representing configuration for a single metric processing script."""

    queue_name: Optional[str] = field(default=None, validator=[type_validator()])
    """Not used in production. Only needed in development when a worker is listening to
    a non-standard queueu."""
    options: Dict[str, str] = field(factory=dict, validator=[type_validator()])
    """Processing script options, required for all metrics, also contains the reference
    to input files."""
    args: Optional[List[str]] = field(factory=list, validator=[type_validator()])
    """Metric script additional CLI arguments. Will replace any defaults and possible to
    collide with options. Should not contain anything specified in options."""

    pre_processing: Optional[List[str]] = field(
        factory=list, validator=[type_validator()]
    )
    """Pre processing script names to execute before the metric script."""

    def add_option(self, key: str, value: str) -> None:
        """Convenience function for adding another option."""
        self.options[key] = value

    def add_args(self, args: List[str]) -> None:
        if self.args is None:
            self.args = args
        else:
            self.args.extend(*args)

    def add_pre_processing(self, pre_processing: str) -> None:
        if self.pre_processing is None:
            self.pre_processing = []

        self.pre_processing.append(pre_processing)


@define
class PreProcessingonfig:
    """Class representing configuration for a single pre processing script."""

    input_file: str = field(validator=[type_validator()])
    """Input file reference."""

    output_file: str = field(validator=[type_validator()])
    """Output file name."""

    command: str = field(validator=[type_validator()])
    """Command to execute."""

    args: List[str] = field(factory=list, validator=[type_validator()])
    """Processing script CLI arguments."""

    def add_args(self, args: List[str]) -> None:
        if self.args is None:
            self.args = args
        else:
            self.args.extend(*args)


@define
class OutputFileOptions:
    """Data class representing output file repository configuration options.

    Usage::
        >>> OutputFileOptions(path="smb://synalogy.com/uploads")"""

    path: str = field(validator=[type_validator()])
    """Remote path the directory to store result files."""
    connection_protocol: Optional[str] = field(default=None, validator=[type_validator()])
    """Connection protocol to use for file transfer."""
    compression: bool = field(default=False, validator=[type_validator()])
    """Whether to use compression. This causes the results to be sent only after
    processing all metrics where a zip file is created at the end end sent to the
    specified `OutputFileOptions.path`."""
    authentication: Optional[AuthenticationOptions] = field(
        default=None, validator=[type_validator()]
    )
    """Authentication to the `OutputFileOptions.path` if there is any."""


@define
class OutputConfig:
    """Class representing the output repository configuration.

    Usage::
        >>> OutputConfig(db=True, files=False)
        >>> # Results will be stored only in the database.
    """

    db: bool = field(default=True, validator=[type_validator()])
    """Store results in the ViQuBox results management API database."""
    files: bool = field(default=True, validator=[type_validator()])
    """Upload results to the directory where the input file was downloaded from.
    Authentication is used from the :class:`ProcessingRequest.input_file`."""
    artifacts: bool = field(default=False, validator=[type_validator()])
    """Upload test artifacts to client's output repository."""
    file_options: Optional[OutputFileOptions] = field(
        default=None, validator=[type_validator()]
    )
    """Configuration for a single output remote repository path."""


@define
class ProcessingRequest:
    """Class representing a job request to the Data Processing API."""

    test_id: str = field(validator=[type_validator()])
    """Required parameter when creating a processing request."""
    output: OutputConfig = field(validator=[type_validator()])
    """Processing result output repository configuration."""
    input_files: Dict[str, List[InputFileConfig]] = field(
        factory=lambda: defaultdict(list), validator=[type_validator()]
    )
    """Input file configuration mapping to references used in metrics."""
    metrics: Dict[str, MetricConfig] = field(factory=dict, validator=[type_validator()])
    """Metrics to process the jobs."""

    pre_processing: Optional[Dict[str, PreProcessingonfig]] = field(
        default=None, validator=[type_validator()]
    )
    """Post processing configuration."""

    team_id: Optional[str] = field(default=None, validator=[type_validator()])
    """Team ID associated to the team that the request was created from."""

    created_at: Optional[str] = field(default=None, validator=[type_validator()])
    """(API filled.) Date when the processing request was created."""
    jobs: Optional[List[str]] = field(default=None, validator=[type_validator()])
    """(API filled.) Processing request related jobs."""
    id: Optional[str] = field(default=None, validator=[type_validator()])
    """(API filled.) Optional parameter filled after creating a processing request or
    sending a get request for a specific request."""

    def add_metric(self, name: Union[str, str], metric: MetricConfig) -> None:
        """Add the given metric config to all :class:`ProcessingRequest` metrics.

        :param name: Name of the metric.
        :param metric: Metric configuration for the metric to add.
        """
        self.metrics[name] = metric

    def add_files(self, name: str, input_file: InputFileConfig) -> None:
        self.input_files[name].append(input_file)

    def add_pre_processing(self, name: str, pre_processing: PreProcessingonfig) -> None:
        if self.pre_processing is None:
            self.pre_processing = {}
        self.pre_processing[name] = pre_processing

    def __str__(self) -> str:
        return f"id: {self.test_id}, metrics: {self.metrics}"


@define
class Data:
    """Class representing a single data entry. Received from API job requests."""

    value: Optional[float] = field(default=None, validator=[type_validator()])
    """Numeric value of data point."""
    error: Optional[str] = field(default=None, validator=[type_validator()])
    """Error description in case processing failed."""


@define
class Results:
    """Class representing a metric result object for a single job. Received after
    creating a processing request and listing a jobs or getting a single job."""

    info: Dict[str, Any] = field(validator=[type_validator()])
    """Info/metadata block of the metric results."""
    data: List[Data] = field(factory=list, validator=[type_validator()])
    """Numeric data from processed input files."""


@define
class InputFileConfigSingle:
    """Class representing input file repository configuration for a single path.
    Created by the API after sending a processing request."""

    path: str = field(validator=[type_validator()])
    """Remote path to a single input file."""
    connection_protocol: Optional[str] = field(default=None, validator=[type_validator()])
    """Connection protocol to use for download/upload, takes precendence over file path protocol."""
    authentication: Optional[AuthenticationOptions] = field(
        default=None, validator=validators.optional([type_validator()])
    )
    """Authentication options for the file repository if there are any."""


@define
class MetricStatus:
    status: str = field(validator=[type_validator()])
    error: str = field(validator=[type_validator()])


@define
class Job:
    """Class representing a single processing job after creating a processing request.
    Multiple jobs can be created from a single processing request. One metric and input
    file count up to one processing job for a single worker.

    Received after sending get requests to job endpoints."""

    job_id: str = field(validator=[type_validator()])
    """ID of the job."""
    processing_id: str = field(validator=[type_validator()])
    """Processing request ID."""
    output: OutputConfig = field(validator=[type_validator()])
    """Output config from the created :class:`ProcessingRequest`."""
    status: str = field(validator=[type_validator()])
    """Current status of the job in processing."""
    metric_status: Dict[str, MetricStatus] = field(
        factory=dict, validator=[type_validator()]
    )
    """Each of the metric statuses."""
    metrics: Dict[str, MetricConfig] = field(factory=dict, validator=[type_validator()])
    """Metric config from the created :class:`ProcessingRequest`."""
    input_files: Dict[str, InputFileConfigSingle] = field(
        factory=dict, validator=[type_validator()]
    )
    """Input file config from the created :class:`ProcessingRequest`."""
    results: List[Results] = field(factory=list, validator=[type_validator()])
    """Metric processing results after the processing has been completed."""
    error: Optional[str] = field(default=None, validator=[type_validator()])
    """Error in case a single metric processing task had failed."""
