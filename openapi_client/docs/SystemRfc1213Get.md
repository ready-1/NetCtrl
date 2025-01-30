# SystemRfc1213Get


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sys_descr** | **str** | Description of the system | [optional]
**sys_name** | **str** | Name of the system | [optional]
**sys_location** | **str** | Physical location of the system | [optional]
**sys_contact** | **str** | System administrator contact information | [optional]

## Example

```python
from openapi_client.models.system_rfc1213_get import SystemRfc1213Get

# TODO update the JSON string below
json = "{}"
# create an instance of SystemRfc1213Get from a JSON string
system_rfc1213_get_instance = SystemRfc1213Get.from_json(json)
# print the JSON string representation of the object
print(SystemRfc1213Get.to_json())

# convert the object into a dict
system_rfc1213_get_dict = system_rfc1213_get_instance.to_dict()
# create an instance of SystemRfc1213Get from a dict
system_rfc1213_get_from_dict = SystemRfc1213Get.from_dict(system_rfc1213_get_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
