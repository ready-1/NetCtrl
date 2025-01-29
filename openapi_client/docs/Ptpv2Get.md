# Ptpv2Get


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**admin_mode** | **str** | Port PTPv2 configuration status | 
**opera_mode** | **str** | Port PTPv2 operational status | 

## Example

```python
from openapi_client.models.ptpv2_get import Ptpv2Get

# TODO update the JSON string below
json = "{}"
# create an instance of Ptpv2Get from a JSON string
ptpv2_get_instance = Ptpv2Get.from_json(json)
# print the JSON string representation of the object
print(Ptpv2Get.to_json())

# convert the object into a dict
ptpv2_get_dict = ptpv2_get_instance.to_dict()
# create an instance of Ptpv2Get from a dict
ptpv2_get_from_dict = Ptpv2Get.from_dict(ptpv2_get_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


