# DeviceCableTest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **int** | Status of the cable test:   * &#x60;0&#x60; &#x3D; Untested   * &#x60;1&#x60; &#x3D; Fail   * &#x60;2&#x60; &#x3D; Normal   * &#x60;3&#x60; &#x3D; Open   * &#x60;4&#x60; &#x3D; Short   * &#x60;5&#x60; &#x3D; Open Short   * &#x60;6&#x60; &#x3D; Cross Talk   * &#x60;7&#x60; &#x3D; No Cable  | [optional]
**len_known** | **int** | Length of Cable in meters. (0 if not known) | [optional]
**shortest_len** | **int** | Cable length range shorter limit in meters. | [optional]
**longest_len** | **int** | Cable length range longer limit in meters. | [optional]
**cable_failure_len** | **int** | Distance along cable to detected fault. | [optional]

## Example

```python
from openapi_client.models.device_cable_test import DeviceCableTest

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceCableTest from a JSON string
device_cable_test_instance = DeviceCableTest.from_json(json)
# print the JSON string representation of the object
print(DeviceCableTest.to_json())

# convert the object into a dict
device_cable_test_dict = device_cable_test_instance.to_dict()
# create an instance of DeviceCableTest from a dict
device_cable_test_from_dict = DeviceCableTest.from_dict(device_cable_test_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
