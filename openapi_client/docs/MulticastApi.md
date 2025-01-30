# openapi_client.MulticastApi

All URIs are relative to *https://127.0.0.1:8443/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**snooping_config_get**](MulticastApi.md#snooping_config_get) | **GET** /snooping_config |
[**snooping_config_post**](MulticastApi.md#snooping_config_post) | **POST** /snooping_config |
[**snooping_interfaces_get**](MulticastApi.md#snooping_interfaces_get) | **GET** /snooping_interfaces |
[**snooping_interfaces_post**](MulticastApi.md#snooping_interfaces_post) | **POST** /snooping_interfaces |
[**snooping_queriers_get**](MulticastApi.md#snooping_queriers_get) | **GET** /snooping_queriers |
[**snooping_queriers_post**](MulticastApi.md#snooping_queriers_post) | **POST** /snooping_queriers |
[**snooping_vlan_get**](MulticastApi.md#snooping_vlan_get) | **GET** /snooping_vlan |


# **snooping_config_get**
> SnoopingConfigGet200Response snooping_config_get(family)



Get Snooping Configuration

### Example

* Bearer Authentication (bearerAuth):

```python
import openapi_client
from openapi_client.models.snooping_config_get200_response import SnoopingConfigGet200Response
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
    api_instance = openapi_client.MulticastApi(api_client)
    family = 'igmp' # str | Snooping family

    try:
        api_response = api_instance.snooping_config_get(family)
        print("The response of MulticastApi->snooping_config_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MulticastApi->snooping_config_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **family** | **str**| Snooping family |

### Return type

[**SnoopingConfigGet200Response**](SnoopingConfigGet200Response.md)

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

# **snooping_config_post**
> LogoutPost200Response snooping_config_post(family, snooping_config_post_request)



Set Snooping Configuration

### Example

* Bearer Authentication (bearerAuth):

```python
import openapi_client
from openapi_client.models.logout_post200_response import LogoutPost200Response
from openapi_client.models.snooping_config_post_request import SnoopingConfigPostRequest
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
    api_instance = openapi_client.MulticastApi(api_client)
    family = 'igmp' # str | Snooping family
    snooping_config_post_request = openapi_client.SnoopingConfigPostRequest() # SnoopingConfigPostRequest |

    try:
        api_response = api_instance.snooping_config_post(family, snooping_config_post_request)
        print("The response of MulticastApi->snooping_config_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MulticastApi->snooping_config_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **family** | **str**| Snooping family |
 **snooping_config_post_request** | [**SnoopingConfigPostRequest**](SnoopingConfigPostRequest.md)|  |

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

# **snooping_interfaces_get**
> SnoopingInterfacesGet200Response snooping_interfaces_get(family)



Get Snooping Interface Configuration

### Example

* Bearer Authentication (bearerAuth):

```python
import openapi_client
from openapi_client.models.snooping_interfaces_get200_response import SnoopingInterfacesGet200Response
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
    api_instance = openapi_client.MulticastApi(api_client)
    family = 'igmp' # str | Snooping family

    try:
        api_response = api_instance.snooping_interfaces_get(family)
        print("The response of MulticastApi->snooping_interfaces_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MulticastApi->snooping_interfaces_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **family** | **str**| Snooping family |

### Return type

[**SnoopingInterfacesGet200Response**](SnoopingInterfacesGet200Response.md)

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

# **snooping_interfaces_post**
> LogoutPost200Response snooping_interfaces_post(interface, snooping_interfaces_post_request)



Set Snooping Interface Configuration

### Example

* Bearer Authentication (bearerAuth):

```python
import openapi_client
from openapi_client.models.logout_post200_response import LogoutPost200Response
from openapi_client.models.snooping_interfaces_post_request import SnoopingInterfacesPostRequest
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
    api_instance = openapi_client.MulticastApi(api_client)
    interface = 1 # int | Port interface ID
    snooping_interfaces_post_request = openapi_client.SnoopingInterfacesPostRequest() # SnoopingInterfacesPostRequest |

    try:
        api_response = api_instance.snooping_interfaces_post(interface, snooping_interfaces_post_request)
        print("The response of MulticastApi->snooping_interfaces_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MulticastApi->snooping_interfaces_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **interface** | **int**| Port interface ID |
 **snooping_interfaces_post_request** | [**SnoopingInterfacesPostRequest**](SnoopingInterfacesPostRequest.md)|  |

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

# **snooping_queriers_get**
> SnoopingQueriersGet200Response snooping_queriers_get(family, vlanid)



Get Snooping Querier Configuration

### Example

* Bearer Authentication (bearerAuth):

```python
import openapi_client
from openapi_client.models.snooping_queriers_get200_response import SnoopingQueriersGet200Response
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
    api_instance = openapi_client.MulticastApi(api_client)
    family = 'igmp' # str | Snooping family
    vlanid = 1 # int | VLAN ID

    try:
        api_response = api_instance.snooping_queriers_get(family, vlanid)
        print("The response of MulticastApi->snooping_queriers_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MulticastApi->snooping_queriers_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **family** | **str**| Snooping family |
 **vlanid** | **int**| VLAN ID |

### Return type

[**SnoopingQueriersGet200Response**](SnoopingQueriersGet200Response.md)

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

# **snooping_queriers_post**
> LogoutPost200Response snooping_queriers_post(family, vlanid, snooping_queriers_post_request)



Set Snooping Querier Configuration

### Example

* Bearer Authentication (bearerAuth):

```python
import openapi_client
from openapi_client.models.logout_post200_response import LogoutPost200Response
from openapi_client.models.snooping_queriers_post_request import SnoopingQueriersPostRequest
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
    api_instance = openapi_client.MulticastApi(api_client)
    family = 'igmp' # str | Snooping family
    vlanid = 1 # int | VLAN ID
    snooping_queriers_post_request = openapi_client.SnoopingQueriersPostRequest() # SnoopingQueriersPostRequest |

    try:
        api_response = api_instance.snooping_queriers_post(family, vlanid, snooping_queriers_post_request)
        print("The response of MulticastApi->snooping_queriers_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MulticastApi->snooping_queriers_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **family** | **str**| Snooping family |
 **vlanid** | **int**| VLAN ID |
 **snooping_queriers_post_request** | [**SnoopingQueriersPostRequest**](SnoopingQueriersPostRequest.md)|  |

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

# **snooping_vlan_get**
> SnoopingVlanGet200Response snooping_vlan_get(family)



Get Snooping VLAN Configuration

### Example

* Bearer Authentication (bearerAuth):

```python
import openapi_client
from openapi_client.models.snooping_vlan_get200_response import SnoopingVlanGet200Response
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
    api_instance = openapi_client.MulticastApi(api_client)
    family = 'igmp' # str | Snooping family

    try:
        api_response = api_instance.snooping_vlan_get(family)
        print("The response of MulticastApi->snooping_vlan_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MulticastApi->snooping_vlan_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **family** | **str**| Snooping family |

### Return type

[**SnoopingVlanGet200Response**](SnoopingVlanGet200Response.md)

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
