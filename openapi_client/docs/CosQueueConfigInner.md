# CosQueueConfigInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**CosQueueConfigInnerId**](CosQueueConfigInnerId.md) |  | [optional] 
**min_bw** | [**CosQueueConfigInnerMinBw**](CosQueueConfigInnerMinBw.md) |  | [optional] 
**mgmt_type** | **str** | CoS Management Type | [optional] 
**schedule_type** | **str** | CoS Schedule Type | [optional] 

## Example

```python
from openapi_client.models.cos_queue_config_inner import CosQueueConfigInner

# TODO update the JSON string below
json = "{}"
# create an instance of CosQueueConfigInner from a JSON string
cos_queue_config_inner_instance = CosQueueConfigInner.from_json(json)
# print the JSON string representation of the object
print(CosQueueConfigInner.to_json())

# convert the object into a dict
cos_queue_config_inner_dict = cos_queue_config_inner_instance.to_dict()
# create an instance of CosQueueConfigInner from a dict
cos_queue_config_inner_from_dict = CosQueueConfigInner.from_dict(cos_queue_config_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


