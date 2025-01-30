# openapi_client.DiagnosticsApi

All URIs are relative to *https://127.0.0.1:8443/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**device_cable_test_get**](DiagnosticsApi.md#device_cable_test_get) | **GET** /device_cable_test |
[**ping_test_start_post**](DiagnosticsApi.md#ping_test_start_post) | **POST** /ping_test_start |
[**ping_test_status_get**](DiagnosticsApi.md#ping_test_status_get) | **GET** /ping_test_status |
[**sw_portmirroring_delete**](DiagnosticsApi.md#sw_portmirroring_delete) | **DELETE** /sw_portmirroring |
[**sw_portmirroring_get**](DiagnosticsApi.md#sw_portmirroring_get) | **GET** /sw_portmirroring |
[**sw_portmirroring_post**](DiagnosticsApi.md#sw_portmirroring_post) | **POST** /sw_portmirroring |
[**traceroute_start_post**](DiagnosticsApi.md#traceroute_start_post) | **POST** /traceroute_start |
[**traceroute_status_get**](DiagnosticsApi.md#traceroute_status_get) | **GET** /traceroute_status |


# **device_cable_test_get**
> DeviceCableTestGet200Response device_cable_test_get(portid)



Get device cable test results

### Example

* Bearer Authentication (bearerAuth):

```python
import openapi_client
from openapi_client.models.device_cable_test_get200_response import DeviceCableTestGet200Response
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
    api_instance = openapi_client.DiagnosticsApi(api_client)
    portid = 1 # int | Port ID

    try:
        api_response = api_instance.device_cable_test_get(portid)
        print("The response of DiagnosticsApi->device_cable_test_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DiagnosticsApi->device_cable_test_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **portid** | **int**| Port ID |

### Return type

[**DeviceCableTestGet200Response**](DeviceCableTestGet200Response.md)

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

# **ping_test_start_post**
> LogoutPost200Response ping_test_start_post(ping_test_start_post_request)



Ping test

### Example

* Bearer Authentication (bearerAuth):

```python
import openapi_client
from openapi_client.models.logout_post200_response import LogoutPost200Response
from openapi_client.models.ping_test_start_post_request import PingTestStartPostRequest
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
    api_instance = openapi_client.DiagnosticsApi(api_client)
    ping_test_start_post_request = openapi_client.PingTestStartPostRequest() # PingTestStartPostRequest |

    try:
        api_response = api_instance.ping_test_start_post(ping_test_start_post_request)
        print("The response of DiagnosticsApi->ping_test_start_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DiagnosticsApi->ping_test_start_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ping_test_start_post_request** | [**PingTestStartPostRequest**](PingTestStartPostRequest.md)|  |

### Return type

[**LogoutPost200Response**](LogoutPost200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ping_test_status_get**
> PingTestStatusGet200Response ping_test_status_get()



Get ping test status

### Example

* Bearer Authentication (bearerAuth):

```python
import openapi_client
from openapi_client.models.ping_test_status_get200_response import PingTestStatusGet200Response
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
    api_instance = openapi_client.DiagnosticsApi(api_client)

    try:
        api_response = api_instance.ping_test_status_get()
        print("The response of DiagnosticsApi->ping_test_status_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DiagnosticsApi->ping_test_status_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**PingTestStatusGet200Response**](PingTestStatusGet200Response.md)

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

# **sw_portmirroring_delete**
> LogoutPost200Response sw_portmirroring_delete(session_num)



Delete Port Mirroring Configuration Session

### Example

* Bearer Authentication (bearerAuth):

```python
import openapi_client
from openapi_client.models.logout_post200_response import LogoutPost200Response
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
    api_instance = openapi_client.DiagnosticsApi(api_client)
    session_num = 1 # int | Port mirring session number

    try:
        api_response = api_instance.sw_portmirroring_delete(session_num)
        print("The response of DiagnosticsApi->sw_portmirroring_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DiagnosticsApi->sw_portmirroring_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_num** | **int**| Port mirring session number |

### Return type

[**LogoutPost200Response**](LogoutPost200Response.md)

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

# **sw_portmirroring_get**
> SwPortmirroringGet200Response sw_portmirroring_get(session_num)



Get Port Mirroring Configuration

### Example

* Bearer Authentication (bearerAuth):

```python
import openapi_client
from openapi_client.models.sw_portmirroring_get200_response import SwPortmirroringGet200Response
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
    api_instance = openapi_client.DiagnosticsApi(api_client)
    session_num = 1 # int | Port mirroring session number

    try:
        api_response = api_instance.sw_portmirroring_get(session_num)
        print("The response of DiagnosticsApi->sw_portmirroring_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DiagnosticsApi->sw_portmirroring_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_num** | **int**| Port mirroring session number |

### Return type

[**SwPortmirroringGet200Response**](SwPortmirroringGet200Response.md)

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

# **sw_portmirroring_post**
> LogoutPost200Response sw_portmirroring_post(session_num, sw_portmirroring_post_request)



Set Port Mirroring Configuration

### Example

* Bearer Authentication (bearerAuth):

```python
import openapi_client
from openapi_client.models.logout_post200_response import LogoutPost200Response
from openapi_client.models.sw_portmirroring_post_request import SwPortmirroringPostRequest
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
    api_instance = openapi_client.DiagnosticsApi(api_client)
    session_num = 1 # int | Port mirroring session number
    sw_portmirroring_post_request = openapi_client.SwPortmirroringPostRequest() # SwPortmirroringPostRequest |

    try:
        api_response = api_instance.sw_portmirroring_post(session_num, sw_portmirroring_post_request)
        print("The response of DiagnosticsApi->sw_portmirroring_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DiagnosticsApi->sw_portmirroring_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_num** | **int**| Port mirroring session number |
 **sw_portmirroring_post_request** | [**SwPortmirroringPostRequest**](SwPortmirroringPostRequest.md)|  |

### Return type

[**LogoutPost200Response**](LogoutPost200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **traceroute_start_post**
> LogoutPost200Response traceroute_start_post(traceroute_start_post_request)



Traceroute start and stop

### Example

* Bearer Authentication (bearerAuth):

```python
import openapi_client
from openapi_client.models.logout_post200_response import LogoutPost200Response
from openapi_client.models.traceroute_start_post_request import TracerouteStartPostRequest
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
    api_instance = openapi_client.DiagnosticsApi(api_client)
    traceroute_start_post_request = openapi_client.TracerouteStartPostRequest() # TracerouteStartPostRequest |

    try:
        api_response = api_instance.traceroute_start_post(traceroute_start_post_request)
        print("The response of DiagnosticsApi->traceroute_start_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DiagnosticsApi->traceroute_start_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **traceroute_start_post_request** | [**TracerouteStartPostRequest**](TracerouteStartPostRequest.md)|  |

### Return type

[**LogoutPost200Response**](LogoutPost200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **traceroute_status_get**
> TracerouteStatusGet200Response traceroute_status_get()



Traceroute results

### Example

* Bearer Authentication (bearerAuth):

```python
import openapi_client
from openapi_client.models.traceroute_status_get200_response import TracerouteStatusGet200Response
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
    api_instance = openapi_client.DiagnosticsApi(api_client)

    try:
        api_response = api_instance.traceroute_status_get()
        print("The response of DiagnosticsApi->traceroute_status_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DiagnosticsApi->traceroute_status_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**TracerouteStatusGet200Response**](TracerouteStatusGet200Response.md)

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
