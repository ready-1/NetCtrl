# IpRouteTableGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resp** | [**GeneralResponsesCode**](GeneralResponsesCode.md) |  | [optional] 
**ip_route_table** | [**List[IpRouteTable]**](IpRouteTable.md) |  | [optional] 

## Example

```python
from openapi_client.models.ip_route_table_get200_response import IpRouteTableGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of IpRouteTableGet200Response from a JSON string
ip_route_table_get200_response_instance = IpRouteTableGet200Response.from_json(json)
# print the JSON string representation of the object
print(IpRouteTableGet200Response.to_json())

# convert the object into a dict
ip_route_table_get200_response_dict = ip_route_table_get200_response_instance.to_dict()
# create an instance of IpRouteTableGet200Response from a dict
ip_route_table_get200_response_from_dict = IpRouteTableGet200Response.from_dict(ip_route_table_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


