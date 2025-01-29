# SwcfgPoe


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**portid** | **int** | Port ID | [optional] 
**enable** | **bool** | Enable PoE power | 
**power_limit_mode** | **int** | Power limit mode:   * &#x60;0&#x60; &#x3D; Invalid   * &#x60;1&#x60; &#x3D; DOT3AF   * &#x60;2&#x60; &#x3D; USER   * &#x60;3&#x60; &#x3D; NONE   * &#x60;4&#x60; &#x3D; COUNT  | 
**classification** | **int** | PoE power classification:   * &#x60;0&#x60; &#x3D; Invalid   * &#x60;1&#x60; &#x3D; Class 0   * &#x60;2&#x60; &#x3D; Class 1   * &#x60;3&#x60; &#x3D; Class 2   * &#x60;4&#x60; &#x3D; Class 3  | 
**current_power** | **int** | Current power used in milliwatts | [optional] 
**power_limit** | **int** | Power limit in milliwatts | 
**status** | **int** | PoE status:   * &#x60;-1&#x60; &#x3D; Invalid   * &#x60;0&#x60; &#x3D; Disabled   * &#x60;1&#x60; &#x3D; Searching   * &#x60;2&#x60; &#x3D; Delivering Power   * &#x60;3&#x60; &#x3D; Test   * &#x60;4&#x60; &#x3D; Fault   * &#x60;5&#x60; &#x3D; Other Fault   * &#x60;6&#x60; &#x3D; Requesting Power   * &#x60;7&#x60; &#x3D; Overload  | [optional] 
**reset** | **bool** | PoE port power cycle | [optional] 

## Example

```python
from openapi_client.models.swcfg_poe import SwcfgPoe

# TODO update the JSON string below
json = "{}"
# create an instance of SwcfgPoe from a JSON string
swcfg_poe_instance = SwcfgPoe.from_json(json)
# print the JSON string representation of the object
print(SwcfgPoe.to_json())

# convert the object into a dict
swcfg_poe_dict = swcfg_poe_instance.to_dict()
# create an instance of SwcfgPoe from a dict
swcfg_poe_from_dict = SwcfgPoe.from_dict(swcfg_poe_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


