# SwPortmirroring


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**session_num** | **int** | Port mirroring session number |
**session_mode** | **bool** | Port mirroring admin mode configuration |
**dest_port** | **int** | Destination or probe port ID. No ports selected when set to &#x60;0&#x60;. |
**src_port** | [**List[SwPortmirroringSrcPortInner]**](SwPortmirroringSrcPortInner.md) |  | [optional]

## Example

```python
from openapi_client.models.sw_portmirroring import SwPortmirroring

# TODO update the JSON string below
json = "{}"
# create an instance of SwPortmirroring from a JSON string
sw_portmirroring_instance = SwPortmirroring.from_json(json)
# print the JSON string representation of the object
print(SwPortmirroring.to_json())

# convert the object into a dict
sw_portmirroring_dict = sw_portmirroring_instance.to_dict()
# create an instance of SwPortmirroring from a dict
sw_portmirroring_from_dict = SwPortmirroring.from_dict(sw_portmirroring_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
