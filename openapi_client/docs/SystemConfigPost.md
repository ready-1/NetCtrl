# SystemConfigPost


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sys_line_terminal_default_len** | **int** | System access type setting | 
**sys_line_terminal_len** | **int** | Set terminal length of an access line to default. | 
**sys_serial_time_out_default** | **int** | Set serial timeout to default value. | 
**sys_serial_time_out** | **int** | Serial timeout. | 
**sys_telnet_server_admin_mode** | **str** | Telnet server admin mode | 
**sys_transfer_bytes_completed** | **int** | Bytes transferred for the file. | 

## Example

```python
from openapi_client.models.system_config_post import SystemConfigPost

# TODO update the JSON string below
json = "{}"
# create an instance of SystemConfigPost from a JSON string
system_config_post_instance = SystemConfigPost.from_json(json)
# print the JSON string representation of the object
print(SystemConfigPost.to_json())

# convert the object into a dict
system_config_post_dict = system_config_post_instance.to_dict()
# create an instance of SystemConfigPost from a dict
system_config_post_from_dict = SystemConfigPost.from_dict(system_config_post_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


