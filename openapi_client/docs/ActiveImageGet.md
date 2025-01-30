# ActiveImageGet


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** | Active image label | [optional]
**image_descr** | **str** | Active image description | [optional]

## Example

```python
from openapi_client.models.active_image_get import ActiveImageGet

# TODO update the JSON string below
json = "{}"
# create an instance of ActiveImageGet from a JSON string
active_image_get_instance = ActiveImageGet.from_json(json)
# print the JSON string representation of the object
print(ActiveImageGet.to_json())

# convert the object into a dict
active_image_get_dict = active_image_get_instance.to_dict()
# create an instance of ActiveImageGet from a dict
active_image_get_from_dict = ActiveImageGet.from_dict(active_image_get_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
