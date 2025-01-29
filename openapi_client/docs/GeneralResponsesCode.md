# GeneralResponsesCode


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | [optional] 
**resp_code** | **int** |  | [optional] 
**resp_msg** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.general_responses_code import GeneralResponsesCode

# TODO update the JSON string below
json = "{}"
# create an instance of GeneralResponsesCode from a JSON string
general_responses_code_instance = GeneralResponsesCode.from_json(json)
# print the JSON string representation of the object
print(GeneralResponsesCode.to_json())

# convert the object into a dict
general_responses_code_dict = general_responses_code_instance.to_dict()
# create an instance of GeneralResponsesCode from a dict
general_responses_code_from_dict = GeneralResponsesCode.from_dict(general_responses_code_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


