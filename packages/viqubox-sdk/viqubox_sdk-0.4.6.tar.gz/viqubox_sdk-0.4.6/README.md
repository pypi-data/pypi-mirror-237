# ViQuBox-SDK

SDK for interacting with the Data Processing API.

## Setup

Requirements:

- Python 3.8+
- API token generated from the ViQuBox front-end or given by the ViQuBox team.

### Using `pip`

```python
python -m venv venv
. venv/bin/activate

pip install viqubox-sdk
```

## Usage

To create a processing request and get the jobs, use the following code:

```python
from viqubox_sdk.client import Authentication, ViquboxClient
from viqubox_sdk.models import (
    AuthenticationOptions,
    AuthenticationType,
    InputFileConfig,
    MetricConfig,
    OutputConfig,
    ProcessingRequest,
)

input_files = InputFileConfig(
    authentication=AuthenticationOptions(
        opts={"username": "admin", "password": "123"},
        type=AuthenticationType.PASSWORD,
    ),
    connection_protocol="smb",
    paths=["smb://some/path/test_video_1.mp4"],
)
output = OutputConfig(db=True, files=False)
brisque_metric = MetricConfig()
brisque_metric.add_option("video", "@test_video")
brisque_metric.add_option("model", "portrait")
brisque_metric.add_option("marker_num", "9000")
brisque_metric.add_option("scale", "400")
brisque_metric.add_option("roi", "1.2:0:1:1")

request = ProcessingRequest(test_id="t1", output=output)
request.add_files("test_video", input_files)
request.add_metric("brisque", brisque_metric)

client = ViquboxClient(Authentication(api_key="{REDACTED}"))
req = client.processing_create(request)
jobs = client.processing_get_jobs(req.id)
```
