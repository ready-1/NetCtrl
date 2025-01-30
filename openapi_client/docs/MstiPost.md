# MstiPost


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vlanid** | **int** | VLAN ID |
**priority** | **int** | msti priority | [default to 128]

## Example

```python
from openapi_client.models.msti_post import MstiPost

# TODO update the JSON string below
json = "{}"
# create an instance of MstiPost from a JSON string
msti_post_instance = MstiPost.from_json(json)
# print the JSON string representation of the object
print(MstiPost.to_json())

# convert the object into a dict
msti_post_dict = msti_post_instance.to_dict()
# create an instance of MstiPost from a dict
msti_post_from_dict = MstiPost.from_dict(msti_post_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
