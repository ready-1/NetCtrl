# Stp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **bool** | STP/RSTP/MST enabled status | [default to True]
**root_bridge_priority** | **int** | Bridge priority | [default to 32768]
**stp_mode** | **int** | Selection STP state:   * &#x60;0&#x60; &#x3D; STP   * &#x60;1&#x60; &#x3D; Unused   * &#x60;2&#x60; &#x3D; RSTP   * &#x60;3&#x60; &#x3D; MST  | [default to 2]
**root_bridge_id** | **str** | Root bridge MAC address | 
**ports** | **List[int]** | Ports with STP enabled | 
**lag_group_id** | **List[int]** | Lag Group IDs. | 

## Example

```python
from openapi_client.models.stp import Stp

# TODO update the JSON string below
json = "{}"
# create an instance of Stp from a JSON string
stp_instance = Stp.from_json(json)
# print the JSON string representation of the object
print(Stp.to_json())

# convert the object into a dict
stp_dict = stp_instance.to_dict()
# create an instance of Stp from a dict
stp_from_dict = Stp.from_dict(stp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


