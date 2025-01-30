# SwPortmirroringGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resp** | [**GeneralResponsesCode**](GeneralResponsesCode.md) |  | [optional]
**switch_rstp_port_config** | [**SwPortmirroring**](SwPortmirroring.md) |  | [optional]

## Example

```python
from openapi_client.models.sw_portmirroring_get200_response import SwPortmirroringGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of SwPortmirroringGet200Response from a JSON string
sw_portmirroring_get200_response_instance = SwPortmirroringGet200Response.from_json(json)
# print the JSON string representation of the object
print(SwPortmirroringGet200Response.to_json())

# convert the object into a dict
sw_portmirroring_get200_response_dict = sw_portmirroring_get200_response_instance.to_dict()
# create an instance of SwPortmirroringGet200Response from a dict
sw_portmirroring_get200_response_from_dict = SwPortmirroringGet200Response.from_dict(sw_portmirroring_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
