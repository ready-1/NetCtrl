# SwLagCfgGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resp** | [**GeneralResponsesCode**](GeneralResponsesCode.md) |  | [optional]
**switch_config_lag_group** | [**SwLagCfg**](SwLagCfg.md) |  | [optional]

## Example

```python
from openapi_client.models.sw_lag_cfg_get200_response import SwLagCfgGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of SwLagCfgGet200Response from a JSON string
sw_lag_cfg_get200_response_instance = SwLagCfgGet200Response.from_json(json)
# print the JSON string representation of the object
print(SwLagCfgGet200Response.to_json())

# convert the object into a dict
sw_lag_cfg_get200_response_dict = sw_lag_cfg_get200_response_instance.to_dict()
# create an instance of SwLagCfgGet200Response from a dict
sw_lag_cfg_get200_response_from_dict = SwLagCfgGet200Response.from_dict(sw_lag_cfg_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
