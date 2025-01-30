# DeviceLogReader


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**logs** | **List[str]** | Device Logs in buffer | [optional]

## Example

```python
from openapi_client.models.device_log_reader import DeviceLogReader

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceLogReader from a JSON string
device_log_reader_instance = DeviceLogReader.from_json(json)
# print the JSON string representation of the object
print(DeviceLogReader.to_json())

# convert the object into a dict
device_log_reader_dict = device_log_reader_instance.to_dict()
# create an instance of DeviceLogReader from a dict
device_log_reader_from_dict = DeviceLogReader.from_dict(device_log_reader_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
