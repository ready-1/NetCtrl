# Dot1dTpPortEntriesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**port** | **int** | Port Interface Number | [optional]
**max_info** | **int** | Maximum size of the information field this port can receive or transmit. | [optional]
**in_frames** | **int** | Number of frames received by this port from its segment. | [optional]
**out_frames** | **int** | Number of frames transmitted by this port to its segment. | [optional]
**in_discards** | **int** | Count of valid frames received which were discarded by the forwarding process. | [optional]

## Example

```python
from openapi_client.models.dot1d_tp_port_entries_inner import Dot1dTpPortEntriesInner

# TODO update the JSON string below
json = "{}"
# create an instance of Dot1dTpPortEntriesInner from a JSON string
dot1d_tp_port_entries_inner_instance = Dot1dTpPortEntriesInner.from_json(json)
# print the JSON string representation of the object
print(Dot1dTpPortEntriesInner.to_json())

# convert the object into a dict
dot1d_tp_port_entries_inner_dict = dot1d_tp_port_entries_inner_instance.to_dict()
# create an instance of Dot1dTpPortEntriesInner from a dict
dot1d_tp_port_entries_inner_from_dict = Dot1dTpPortEntriesInner.from_dict(dot1d_tp_port_entries_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
