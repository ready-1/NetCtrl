# Dot1dStpConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**protocol_specification** | **str** | STP protocol | [optional]
**priority** | **int** | Bridge priority and displayed in multiples of 4096 | [optional]
**time_since_topology_change** | **int** | Time passed since topology change (seconds) | [optional]
**top_changes** | **int** | Number of times topology changed. | [optional]
**designated_root** | **str** | Bridge identifier of the root bridge | [optional]
**root_cost** | **int** | Value of the Root Path Cost for the common and internal spanning tree | [optional]
**root_port** | **int** | Root port identifier | [optional]
**max_age** | **int** | Maximum age | [optional]
**hello_time** | **int** | Hello time | [optional]
**hold_time** | **int** | Hold time | [optional]
**forward_delay** | **int** | Forward delay | [optional]
**bridge_max_age** | **int** | Bridge maximum age | [optional]
**bridge_hello_time** | **int** | Bridge hello time | [optional]
**bridge_forward_delay** | **int** | Bridge forward delay | [optional]

## Example

```python
from openapi_client.models.dot1d_stp_config import Dot1dStpConfig

# TODO update the JSON string below
json = "{}"
# create an instance of Dot1dStpConfig from a JSON string
dot1d_stp_config_instance = Dot1dStpConfig.from_json(json)
# print the JSON string representation of the object
print(Dot1dStpConfig.to_json())

# convert the object into a dict
dot1d_stp_config_dict = dot1d_stp_config_instance.to_dict()
# create an instance of Dot1dStpConfig from a dict
dot1d_stp_config_from_dict = Dot1dStpConfig.from_dict(dot1d_stp_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
