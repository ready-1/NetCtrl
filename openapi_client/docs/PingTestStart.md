# PingTestStart


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **int** | Action to start ping:   * &#x60;1&#x60; &#x3D; Start   * &#x60;0&#x60; &#x3D; Stop  |
**ip_version** | **int** | IP address version:   * &#x60;4&#x60; &#x3D; IPv4   * &#x60;6&#x60; &#x3D; IPv6  | [optional] [default to 4]
**host** | **str** | Hostname/IP address |
**count** | **int** | Number of echo requests sent | [optional] [default to 3]
**size** | **int** | Size of ping packet | [optional] [default to 64]
**timeout** | **int** | Time out value in seconds | [optional] [default to 60]
**interval** | **str** | Interval between ping packets in seconds | [optional]

## Example

```python
from openapi_client.models.ping_test_start import PingTestStart

# TODO update the JSON string below
json = "{}"
# create an instance of PingTestStart from a JSON string
ping_test_start_instance = PingTestStart.from_json(json)
# print the JSON string representation of the object
print(PingTestStart.to_json())

# convert the object into a dict
ping_test_start_dict = ping_test_start_instance.to_dict()
# create an instance of PingTestStart from a dict
ping_test_start_from_dict = PingTestStart.from_dict(ping_test_start_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
