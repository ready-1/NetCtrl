# DownloadStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**state** | **int** | Firmware update state:   * &#x60;0&#x60; &#x3D; NONE   * &#x60;1&#x60; &#x3D; IN_PROGRESS   * &#x60;2&#x60; &#x3D; DOWNLOAD_START   * &#x60;3&#x60; &#x3D; DOWNLOAD_TIMEOUT   * &#x60;4&#x60; &#x3D; DOWNLOAD_FAILED   * &#x60;5&#x60; &#x3D; DOWNLOAD_SUCCESS   * &#x60;6&#x60; &#x3D; VALIDATION_UPGRADE_START   * &#x60;7&#x60; &#x3D; VALIDATION_UPGRADE_FAILED   * &#x60;8&#x60; &#x3D; VALIDATION_UPGRADE_SUCCESS   * &#x60;9&#x60; &#x3D; OPEN_API_FAILED   * &#x60;10&#x60; &#x3D; DEVICE_REBOOT_FAILED   * &#x60;11&#x60; &#x3D; DEVICE_REBOOT_SUCCESS  | [optional] [default to 0]
**message** | **str** | Firmware update status message | [optional] [default to 'Download Status None']
**dwld_progress** | **str** | Firmware download progress in percent for HTTP or HTTPS | [optional]

## Example

```python
from openapi_client.models.download_status import DownloadStatus

# TODO update the JSON string below
json = "{}"
# create an instance of DownloadStatus from a JSON string
download_status_instance = DownloadStatus.from_json(json)
# print the JSON string representation of the object
print(DownloadStatus.to_json())

# convert the object into a dict
download_status_dict = download_status_instance.to_dict()
# create an instance of DownloadStatus from a dict
download_status_from_dict = DownloadStatus.from_dict(download_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
