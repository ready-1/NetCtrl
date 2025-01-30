# SystemConfigGet


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sys_access_line** | **str** | System access type setting | [optional]
**sys_line_terminal_len** | **int** | Terminal length of an access line. | [optional]
**sys_serial_time_out** | **int** | Serial timeout. | [optional]
**sys_telnet_server_admin_mode** | **str** | Telnet server admin mode. | [optional]

## Example

```python
from openapi_client.models.system_config_get import SystemConfigGet

# TODO update the JSON string below
json = "{}"
# create an instance of SystemConfigGet from a JSON string
system_config_get_instance = SystemConfigGet.from_json(json)
# print the JSON string representation of the object
print(SystemConfigGet.to_json())

# convert the object into a dict
system_config_get_dict = system_config_get_instance.to_dict()
# create an instance of SystemConfigGet from a dict
system_config_get_from_dict = SystemConfigGet.from_dict(system_config_get_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
