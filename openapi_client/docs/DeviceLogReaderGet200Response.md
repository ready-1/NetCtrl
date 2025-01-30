# DeviceLogReaderGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resp** | [**GeneralResponsesCode**](GeneralResponsesCode.md) |  | [optional]
**log_reader** | [**DeviceLogReader**](DeviceLogReader.md) |  | [optional]

## Example

```python
from openapi_client.models.device_log_reader_get200_response import DeviceLogReaderGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceLogReaderGet200Response from a JSON string
device_log_reader_get200_response_instance = DeviceLogReaderGet200Response.from_json(json)
# print the JSON string representation of the object
print(DeviceLogReaderGet200Response.to_json())

# convert the object into a dict
device_log_reader_get200_response_dict = device_log_reader_get200_response_instance.to_dict()
# create an instance of DeviceLogReaderGet200Response from a dict
device_log_reader_get200_response_from_dict = DeviceLogReaderGet200Response.from_dict(device_log_reader_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
