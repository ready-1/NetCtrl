# FiberOptics


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**port** | **str** | Port interface | [optional] 
**temp** | **str** | Temperature of the module in celsius | [optional] 
**voltage** | **str** | Voltage usage of the module | [optional] 
**current** | **str** | Current usage of the module in milliamps | [optional] 
**output_power** | **str** | Power output of the module in decibel-milliwatts | [optional] 
**input_power** | **str** | Power input of the module in decibel-milliwatts | [optional] 
**tx_fault** | **str** | Transmitter fault | [optional] 
**los** | **str** | Loss of signal | [optional] 
**fault_status** | **str** | Fault status | [optional] 
**vendor_name** | **str** | Vender name of the module | [optional] 
**link_length_50_um** | **str** | Link length in meters | [optional] 
**link_length_62_5_um** | **str** | Link length in meters | [optional] 
**link_length** | **str** | Link length in meters | [optional] 
**serial_number** | **str** | Serial number of the module | [optional] 
**part_number** | **str** | Part number of the module | [optional] 
**nominal_bit_rate** | **str** | Nominal bit rate in Mbps | [optional] 
**rev** | **str** | Vendor revision | [optional] 
**compliance** | **str** | Module compliance type | [optional] 
**supported** | **str** | Support status | [optional] 
**possible_speed_detected** | **str** | Possible speed detected | [optional] 

## Example

```python
from openapi_client.models.fiber_optics import FiberOptics

# TODO update the JSON string below
json = "{}"
# create an instance of FiberOptics from a JSON string
fiber_optics_instance = FiberOptics.from_json(json)
# print the JSON string representation of the object
print(FiberOptics.to_json())

# convert the object into a dict
fiber_optics_dict = fiber_optics_instance.to_dict()
# create an instance of FiberOptics from a dict
fiber_optics_from_dict = FiberOptics.from_dict(fiber_optics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


