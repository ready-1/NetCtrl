# SwLagCfg


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lag_group** | **int** | LAG Group:   * &#x60;0&#x60; &#x3D; Create a new LAG group   * Non-zero values will modify an existing LAB group.  | [optional]
**name** | **str** | LAG description |
**group_id** | **int** | LAG Group ID |
**admin_mode** | **bool** | LAG enabled state |
**type** | **int** | LAG Type:   * &#x60;0&#x60; &#x3D; Dynamic or Static LAG   * &#x60;1&#x60; &#x3D; Static LAG  |
**members** | **List[int]** | LAG Port members |

## Example

```python
from openapi_client.models.sw_lag_cfg import SwLagCfg

# TODO update the JSON string below
json = "{}"
# create an instance of SwLagCfg from a JSON string
sw_lag_cfg_instance = SwLagCfg.from_json(json)
# print the JSON string representation of the object
print(SwLagCfg.to_json())

# convert the object into a dict
sw_lag_cfg_dict = sw_lag_cfg_instance.to_dict()
# create an instance of SwLagCfg from a dict
sw_lag_cfg_from_dict = SwLagCfg.from_dict(sw_lag_cfg_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
