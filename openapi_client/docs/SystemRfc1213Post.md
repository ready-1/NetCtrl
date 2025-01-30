# SystemRfc1213Post


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sys_name** | **str** | Name of the system |
**sys_location** | **str** | Location of the system |
**sys_contact** | **str** | Contact of the system |

## Example

```python
from openapi_client.models.system_rfc1213_post import SystemRfc1213Post

# TODO update the JSON string below
json = "{}"
# create an instance of SystemRfc1213Post from a JSON string
system_rfc1213_post_instance = SystemRfc1213Post.from_json(json)
# print the JSON string representation of the object
print(SystemRfc1213Post.to_json())

# convert the object into a dict
system_rfc1213_post_dict = system_rfc1213_post_instance.to_dict()
# create an instance of SystemRfc1213Post from a dict
system_rfc1213_post_from_dict = SystemRfc1213Post.from_dict(system_rfc1213_post_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
