# PoeConfigGet


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**firmware_version** | **str** | PoE Firmware Version | [optional] 
**pse_main_operation_status** | **str** | Power Sourcing Equipment main operation status | [optional] 
**total_power_consumed_watts** | **str** | Total power consumed in watts | [optional] 
**power_managment_mode** | **str** | PoE power management mode | [optional] 
**traps** | **str** |  | [optional] 
**power_detection_mode** | **int** | PoE Detection Mode:  * &#x60;0&#x60; &#x3D; Invalid  * &#x60;1&#x60; &#x3D; Legacy  * &#x60;2&#x60; &#x3D; 4pt 802.3af  * &#x60;3&#x60; &#x3D; 4pt 802.3af and legacy  * &#x60;4&#x60; &#x3D; 2pt 802.3af  * &#x60;5&#x60; &#x3D; 2pt 802.3af and legacy  * &#x60;6&#x60; &#x3D; None  * &#x60;7&#x60; &#x3D; Count  | [optional] 

## Example

```python
from openapi_client.models.poe_config_get import PoeConfigGet

# TODO update the JSON string below
json = "{}"
# create an instance of PoeConfigGet from a JSON string
poe_config_get_instance = PoeConfigGet.from_json(json)
# print the JSON string representation of the object
print(PoeConfigGet.to_json())

# convert the object into a dict
poe_config_get_dict = poe_config_get_instance.to_dict()
# create an instance of PoeConfigGet from a dict
poe_config_get_from_dict = PoeConfigGet.from_dict(poe_config_get_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


