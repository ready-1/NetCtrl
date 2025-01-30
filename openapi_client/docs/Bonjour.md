# Bonjour


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | Set the bonjour status | [default to 'enabled']

## Example

```python
from openapi_client.models.bonjour import Bonjour

# TODO update the JSON string below
json = "{}"
# create an instance of Bonjour from a JSON string
bonjour_instance = Bonjour.from_json(json)
# print the JSON string representation of the object
print(Bonjour.to_json())

# convert the object into a dict
bonjour_dict = bonjour_instance.to_dict()
# create an instance of Bonjour from a dict
bonjour_from_dict = Bonjour.from_dict(bonjour_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
