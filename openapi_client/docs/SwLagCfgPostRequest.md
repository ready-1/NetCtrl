# SwLagCfgPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**switch_config_lag_group** | [**SwLagCfg**](SwLagCfg.md) |  | [optional]

## Example

```python
from openapi_client.models.sw_lag_cfg_post_request import SwLagCfgPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SwLagCfgPostRequest from a JSON string
sw_lag_cfg_post_request_instance = SwLagCfgPostRequest.from_json(json)
# print the JSON string representation of the object
print(SwLagCfgPostRequest.to_json())

# convert the object into a dict
sw_lag_cfg_post_request_dict = sw_lag_cfg_post_request_instance.to_dict()
# create an instance of SwLagCfgPostRequest from a dict
sw_lag_cfg_post_request_from_dict = SwLagCfgPostRequest.from_dict(sw_lag_cfg_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
