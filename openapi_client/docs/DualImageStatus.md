# DualImageStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**image1_label** | **str** | image1 label | [optional] [default to 'image1']
**image1_descr** | **str** | image1 description | [optional]
**image1_version** | **str** | image1 version | [optional]
**image2_label** | **str** | image2 label | [optional] [default to 'image2']
**image2_descr** | **str** | image2 description | [optional]
**image2_version** | **str** | image2 version | [optional]
**activated_img_label** | **str** | active image label | [optional]

## Example

```python
from openapi_client.models.dual_image_status import DualImageStatus

# TODO update the JSON string below
json = "{}"
# create an instance of DualImageStatus from a JSON string
dual_image_status_instance = DualImageStatus.from_json(json)
# print the JSON string representation of the object
print(DualImageStatus.to_json())

# convert the object into a dict
dual_image_status_dict = dual_image_status_instance.to_dict()
# create an instance of DualImageStatus from a dict
dual_image_status_from_dict = DualImageStatus.from_dict(dual_image_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
