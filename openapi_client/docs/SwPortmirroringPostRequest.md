# SwPortmirroringPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**switch_rstp_port_config** | [**SwPortmirroring**](SwPortmirroring.md) |  | [optional]

## Example

```python
from openapi_client.models.sw_portmirroring_post_request import SwPortmirroringPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SwPortmirroringPostRequest from a JSON string
sw_portmirroring_post_request_instance = SwPortmirroringPostRequest.from_json(json)
# print the JSON string representation of the object
print(SwPortmirroringPostRequest.to_json())

# convert the object into a dict
sw_portmirroring_post_request_dict = sw_portmirroring_post_request_instance.to_dict()
# create an instance of SwPortmirroringPostRequest from a dict
sw_portmirroring_post_request_from_dict = SwPortmirroringPostRequest.from_dict(sw_portmirroring_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
