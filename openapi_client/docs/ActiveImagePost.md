# ActiveImagePost


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** | Set the activated image:   * &#x60;image1&#x60;   * &#x60;image2&#x60;  |

## Example

```python
from openapi_client.models.active_image_post import ActiveImagePost

# TODO update the JSON string below
json = "{}"
# create an instance of ActiveImagePost from a JSON string
active_image_post_instance = ActiveImagePost.from_json(json)
# print the JSON string representation of the object
print(ActiveImagePost.to_json())

# convert the object into a dict
active_image_post_dict = active_image_post_instance.to_dict()
# create an instance of ActiveImagePost from a dict
active_image_post_from_dict = ActiveImagePost.from_dict(active_image_post_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
