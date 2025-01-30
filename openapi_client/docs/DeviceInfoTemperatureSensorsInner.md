# DeviceInfoTemperatureSensorsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sensor_num** | **int** | Temperature sensor SKU | [optional]
**sensor_desc** | **int** | Description of the temperature sensor | [optional]
**sensor_temp** | **str** | Temperature sensor temperature in Celcius | [optional]
**sensor_state** | **str** | Temperature sensor state:   * &#x60;0&#x60; &#x3D; NONE   * &#x60;1&#x60; &#x3D; NORMAL   * &#x60;2&#x60; &#x3D; WARNING   * &#x60;3&#x60; &#x3D; CRITICAL   * &#x60;4&#x60; &#x3D; SHUTDOWN   * &#x60;5&#x60; &#x3D; NOT PRESENT   * &#x60;6&#x60; &#x3D; NOT OPERATIONAL  | [optional]

## Example

```python
from openapi_client.models.device_info_temperature_sensors_inner import DeviceInfoTemperatureSensorsInner

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceInfoTemperatureSensorsInner from a JSON string
device_info_temperature_sensors_inner_instance = DeviceInfoTemperatureSensorsInner.from_json(json)
# print the JSON string representation of the object
print(DeviceInfoTemperatureSensorsInner.to_json())

# convert the object into a dict
device_info_temperature_sensors_inner_dict = device_info_temperature_sensors_inner_instance.to_dict()
# create an instance of DeviceInfoTemperatureSensorsInner from a dict
device_info_temperature_sensors_inner_from_dict = DeviceInfoTemperatureSensorsInner.from_dict(device_info_temperature_sensors_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
