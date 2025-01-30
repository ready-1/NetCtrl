# openapi_client.RoutingSettingsApi

All URIs are relative to *https://127.0.0.1:8443/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**host_table_get**](RoutingSettingsApi.md#host_table_get) | **GET** /host_table |
[**ip_route_table_get**](RoutingSettingsApi.md#ip_route_table_get) | **GET** /ip_route_table |


# **host_table_get**
> HostTableGet200Response host_table_get()



Get Switch's Host Table

### Example

* Bearer Authentication (bearerAuth):

```python
import openapi_client
from openapi_client.models.host_table_get200_response import HostTableGet200Response
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://127.0.0.1:8443/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://127.0.0.1:8443/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearerAuth
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.RoutingSettingsApi(api_client)

    try:
        api_response = api_instance.host_table_get()
        print("The response of RoutingSettingsApi->host_table_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoutingSettingsApi->host_table_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**HostTableGet200Response**](HostTableGet200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ip_route_table_get**
> IpRouteTableGet200Response ip_route_table_get()



Get IP Routing Table

### Example

* Bearer Authentication (bearerAuth):

```python
import openapi_client
from openapi_client.models.ip_route_table_get200_response import IpRouteTableGet200Response
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://127.0.0.1:8443/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://127.0.0.1:8443/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearerAuth
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.RoutingSettingsApi(api_client)

    try:
        api_response = api_instance.ip_route_table_get()
        print("The response of RoutingSettingsApi->ip_route_table_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoutingSettingsApi->ip_route_table_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**IpRouteTableGet200Response**](IpRouteTableGet200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
