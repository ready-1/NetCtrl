# openapi_client.LoggingApi

All URIs are relative to *https://127.0.0.1:8443/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**device_log_reader_get**](LoggingApi.md#device_log_reader_get) | **GET** /device_log_reader | 


# **device_log_reader_get**
> DeviceLogReaderGet200Response device_log_reader_get(num_logs)



Get device log reader

### Example

* Bearer Authentication (bearerAuth):

```python
import openapi_client
from openapi_client.models.device_log_reader_get200_response import DeviceLogReaderGet200Response
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
    api_instance = openapi_client.LoggingApi(api_client)
    num_logs = 2 # int | Number of logs pulled

    try:
        api_response = api_instance.device_log_reader_get(num_logs)
        print("The response of LoggingApi->device_log_reader_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LoggingApi->device_log_reader_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **num_logs** | **int**| Number of logs pulled | 

### Return type

[**DeviceLogReaderGet200Response**](DeviceLogReaderGet200Response.md)

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

