# Costrust


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mode** | **str** | Trust mode of COS - Global/ALL/Per Interface:   * dot1p   * untrusted   * ip-dscp  | 

## Example

```python
from openapi_client.models.costrust import Costrust

# TODO update the JSON string below
json = "{}"
# create an instance of Costrust from a JSON string
costrust_instance = Costrust.from_json(json)
# print the JSON string representation of the object
print(Costrust.to_json())

# convert the object into a dict
costrust_dict = costrust_instance.to_dict()
# create an instance of Costrust from a dict
costrust_from_dict = Costrust.from_dict(costrust_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


