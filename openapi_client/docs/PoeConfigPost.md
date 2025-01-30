# PoeConfigPost


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pse_main_operation_status** | **str** | Main PoE Status |
**usage_threshold** | **int** | Limit PoE usage with a threshold in percentage | [default to 95]
**power_managment_mode** | **str** | PoE power management mode |
**power_detection_mode** | **int** | PoE Detection Mode:  * &#x60;0&#x60; &#x3D; Invalid  * &#x60;1&#x60; &#x3D; Legacy  * &#x60;2&#x60; &#x3D; 4pt 802.3af  * &#x60;3&#x60; &#x3D; 4pt 802.3af and legacy  * &#x60;4&#x60; &#x3D; 2pt 802.3af  * &#x60;5&#x60; &#x3D; 2pt 802.3af and legacy  * &#x60;6&#x60; &#x3D; None  * &#x60;7&#x60; &#x3D; Count  |
**traps** | **str** |  |

## Example

```python
from openapi_client.models.poe_config_post import PoeConfigPost

# TODO update the JSON string below
json = "{}"
# create an instance of PoeConfigPost from a JSON string
poe_config_post_instance = PoeConfigPost.from_json(json)
# print the JSON string representation of the object
print(PoeConfigPost.to_json())

# convert the object into a dict
poe_config_post_dict = poe_config_post_instance.to_dict()
# create an instance of PoeConfigPost from a dict
poe_config_post_from_dict = PoeConfigPost.from_dict(poe_config_post_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
