# Download


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**protocol** | **str** | Protocol to by used for file transfer |
**fw_url** | **str** | tftp, http or https link to firmware image or configuration file to be upgrade. |
**fw_download_timeout** | **int** | Firmware iamge download time-out value in seconds from http or https link. | [default to 600]
**reboot_now** | **bool** | Indicates when to reboot:   * &#x60;true&#x60; &#x3D; immediate reboot   * &#x60;false&#x60; &#x3D; reboot manually by admin  | [default to True]
**type** | **str** | Type of file being downloaded to the switch:   * &#x60;backup-config&#x60; &#x3D; Configuration file saved to the backup configuration settings   * &#x60;firmware&#x60; &#x3D; Firmware image saved to the specified image number.  |
**image** | **int** | Specify image firmware will be downloaded:   * &#x60;1&#x60; &#x3D; Image 1   * &#x60;2&#x60; &#x3D; Image 2  |

## Example

```python
from openapi_client.models.download import Download

# TODO update the JSON string below
json = "{}"
# create an instance of Download from a JSON string
download_instance = Download.from_json(json)
# print the JSON string representation of the object
print(Download.to_json())

# convert the object into a dict
download_dict = download_instance.to_dict()
# create an instance of Download from a dict
download_from_dict = Download.from_dict(download_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
