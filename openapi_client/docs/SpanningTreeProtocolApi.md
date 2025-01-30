# openapi_client.SpanningTreeProtocolApi

All URIs are relative to *https://127.0.0.1:8443/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**dot1d_stp_config_get**](SpanningTreeProtocolApi.md#dot1d_stp_config_get) | **GET** /dot1d_stp_config |
[**dot1d_stp_entries_get**](SpanningTreeProtocolApi.md#dot1d_stp_entries_get) | **GET** /dot1d_stp_entries |
[**dot1s_interfaces_get**](SpanningTreeProtocolApi.md#dot1s_interfaces_get) | **GET** /dot1s_interfaces |
[**dot1s_interfaces_post**](SpanningTreeProtocolApi.md#dot1s_interfaces_post) | **POST** /dot1s_interfaces |
[**msti_delete**](SpanningTreeProtocolApi.md#msti_delete) | **DELETE** /msti |
[**msti_get**](SpanningTreeProtocolApi.md#msti_get) | **GET** /msti |
[**msti_post**](SpanningTreeProtocolApi.md#msti_post) | **POST** /msti |
[**stp_get**](SpanningTreeProtocolApi.md#stp_get) | **GET** /stp |
[**stp_post**](SpanningTreeProtocolApi.md#stp_post) | **POST** /stp |


# **dot1d_stp_config_get**
> Dot1dStpConfigGet200Response dot1d_stp_config_get()



Get Spanning Tree Protocol (STP) configuration

### Example

* Bearer Authentication (bearerAuth):

```python
import openapi_client
from openapi_client.models.dot1d_stp_config_get200_response import Dot1dStpConfigGet200Response
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
    api_instance = openapi_client.SpanningTreeProtocolApi(api_client)

    try:
        api_response = api_instance.dot1d_stp_config_get()
        print("The response of SpanningTreeProtocolApi->dot1d_stp_config_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SpanningTreeProtocolApi->dot1d_stp_config_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**Dot1dStpConfigGet200Response**](Dot1dStpConfigGet200Response.md)

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

# **dot1d_stp_entries_get**
> Dot1dStpEntriesGet200Response dot1d_stp_entries_get()



Get Spanning Tree Protocol (STP) entries

### Example

* Bearer Authentication (bearerAuth):

```python
import openapi_client
from openapi_client.models.dot1d_stp_entries_get200_response import Dot1dStpEntriesGet200Response
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
    api_instance = openapi_client.SpanningTreeProtocolApi(api_client)

    try:
        api_response = api_instance.dot1d_stp_entries_get()
        print("The response of SpanningTreeProtocolApi->dot1d_stp_entries_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SpanningTreeProtocolApi->dot1d_stp_entries_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**Dot1dStpEntriesGet200Response**](Dot1dStpEntriesGet200Response.md)

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

# **dot1s_interfaces_get**
> Dot1sInterfacesGet200Response dot1s_interfaces_get()



Get Multiple Spanning Tree Protocol (MSTP) interface configuration

### Example

* Bearer Authentication (bearerAuth):

```python
import openapi_client
from openapi_client.models.dot1s_interfaces_get200_response import Dot1sInterfacesGet200Response
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
    api_instance = openapi_client.SpanningTreeProtocolApi(api_client)

    try:
        api_response = api_instance.dot1s_interfaces_get()
        print("The response of SpanningTreeProtocolApi->dot1s_interfaces_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SpanningTreeProtocolApi->dot1s_interfaces_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**Dot1sInterfacesGet200Response**](Dot1sInterfacesGet200Response.md)

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

# **dot1s_interfaces_post**
> LogoutPost200Response dot1s_interfaces_post(interface, dot1s_interfaces_post_request)



Set Multiple Spanning Tree Protocol (MSTP) interface configuration

### Example

* Bearer Authentication (bearerAuth):

```python
import openapi_client
from openapi_client.models.dot1s_interfaces_post_request import Dot1sInterfacesPostRequest
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
    api_instance = openapi_client.SpanningTreeProtocolApi(api_client)
    interface = 1 # int | Port Interface Number
    dot1s_interfaces_post_request = openapi_client.Dot1sInterfacesPostRequest() # Dot1sInterfacesPostRequest |

    try:
        api_response = api_instance.dot1s_interfaces_post(interface, dot1s_interfaces_post_request)
        print("The response of SpanningTreeProtocolApi->dot1s_interfaces_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SpanningTreeProtocolApi->dot1s_interfaces_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **interface** | **int**| Port Interface Number |
 **dot1s_interfaces_post_request** | [**Dot1sInterfacesPostRequest**](Dot1sInterfacesPostRequest.md)|  |

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

# **msti_delete**
> LogoutPost200Response msti_delete(mstid)



Delete MST ID

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
    api_instance = openapi_client.SpanningTreeProtocolApi(api_client)
    mstid = 1 # int | MST ID

    try:
        api_response = api_instance.msti_delete(mstid)
        print("The response of SpanningTreeProtocolApi->msti_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SpanningTreeProtocolApi->msti_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mstid** | **int**| MST ID |

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

# **msti_get**
> MstiGet200Response msti_get()



Get Multiple Spanning Tree (MST) ID

### Example

* Bearer Authentication (bearerAuth):

```python
import openapi_client
from openapi_client.models.msti_get200_response import MstiGet200Response
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
    api_instance = openapi_client.SpanningTreeProtocolApi(api_client)

    try:
        api_response = api_instance.msti_get()
        print("The response of SpanningTreeProtocolApi->msti_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SpanningTreeProtocolApi->msti_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**MstiGet200Response**](MstiGet200Response.md)

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

# **msti_post**
> LogoutPost200Response msti_post(msti_post_request, mstid=mstid)



Set Multiple Spanning Tree (MST) ID

### Example

* Bearer Authentication (bearerAuth):

```python
import openapi_client
from openapi_client.models.logout_post200_response import LogoutPost200Response
from openapi_client.models.msti_post_request import MstiPostRequest
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
    api_instance = openapi_client.SpanningTreeProtocolApi(api_client)
    msti_post_request = openapi_client.MstiPostRequest() # MstiPostRequest |
    mstid = 1 # int | Multiple Spanning Tree (MST) ID (optional)

    try:
        api_response = api_instance.msti_post(msti_post_request, mstid=mstid)
        print("The response of SpanningTreeProtocolApi->msti_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SpanningTreeProtocolApi->msti_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **msti_post_request** | [**MstiPostRequest**](MstiPostRequest.md)|  |
 **mstid** | **int**| Multiple Spanning Tree (MST) ID | [optional]

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

# **stp_get**
> StpGet200Response stp_get()



Get STP information

### Example

* Bearer Authentication (bearerAuth):

```python
import openapi_client
from openapi_client.models.stp_get200_response import StpGet200Response
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
    api_instance = openapi_client.SpanningTreeProtocolApi(api_client)

    try:
        api_response = api_instance.stp_get()
        print("The response of SpanningTreeProtocolApi->stp_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SpanningTreeProtocolApi->stp_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**StpGet200Response**](StpGet200Response.md)

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

# **stp_post**
> LogoutPost200Response stp_post(stp_post_request)



Set STP information

### Example

* Bearer Authentication (bearerAuth):

```python
import openapi_client
from openapi_client.models.logout_post200_response import LogoutPost200Response
from openapi_client.models.stp_post_request import StpPostRequest
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
    api_instance = openapi_client.SpanningTreeProtocolApi(api_client)
    stp_post_request = openapi_client.StpPostRequest() # StpPostRequest |

    try:
        api_response = api_instance.stp_post(stp_post_request)
        print("The response of SpanningTreeProtocolApi->stp_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SpanningTreeProtocolApi->stp_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stp_post_request** | [**StpPostRequest**](StpPostRequest.md)|  |

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
