# TracerouteStart


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **int** | Traceroute action:   * &#x60;1&#x60; &#x3D; Start   * &#x60;0&#x60; &#x3D; Stop  | 
**host** | **str** | Traceroute host or IP | [default to 'www.netgear.com']
**size** | **int** | Size of probe packets | [optional] [default to 38]
**ip_version** | **int** | IP address version:   * &#x60;4&#x60; &#x3D; IPv4   * &#x60;6&#x60; &#x3D; IPv6  | [optional] [default to 4]
**init_ttl** | **int** | Initial Time To Live to be used | [optional] [default to 1]
**max_ttl** | **int** | Maximum Time To Live for the destination | [optional] [default to 30]
**port** | **int** | UDP destination port for probe packets | [optional] [default to 33434]
**n_queries** | **int** | Number of probes per hop | [optional] [default to 3]
**wait** | **int** | Time between probes in seconds | [optional] [default to 3]

## Example

```python
from openapi_client.models.traceroute_start import TracerouteStart

# TODO update the JSON string below
json = "{}"
# create an instance of TracerouteStart from a JSON string
traceroute_start_instance = TracerouteStart.from_json(json)
# print the JSON string representation of the object
print(TracerouteStart.to_json())

# convert the object into a dict
traceroute_start_dict = traceroute_start_instance.to_dict()
# create an instance of TracerouteStart from a dict
traceroute_start_from_dict = TracerouteStart.from_dict(traceroute_start_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


