# openapi_client.DeviceSettingsApi

All URIs are relative to *https://127.0.0.1:8443/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**active_image_get**](DeviceSettingsApi.md#active_image_get) | **GET** /active_image | 
[**active_image_post**](DeviceSettingsApi.md#active_image_post) | **POST** /active_image | 
[**bonjour_get**](DeviceSettingsApi.md#bonjour_get) | **GET** /bonjour | 
[**bonjour_post**](DeviceSettingsApi.md#bonjour_post) | **POST** /bonjour | 
[**config_copy_post**](DeviceSettingsApi.md#config_copy_post) | **POST** /config_copy | 
[**config_file_compare_get**](DeviceSettingsApi.md#config_file_compare_get) | **GET** /config_file_compare | 
[**device_info_get**](DeviceSettingsApi.md#device_info_get) | **GET** /device_info | 
[**device_name_get**](DeviceSettingsApi.md#device_name_get) | **GET** /device_name | 
[**device_name_post**](DeviceSettingsApi.md#device_name_post) | **POST** /device_name | 
[**device_reboot_post**](DeviceSettingsApi.md#device_reboot_post) | **POST** /device_reboot | 
[**dual_image_status_get**](DeviceSettingsApi.md#dual_image_status_get) | **GET** /dual_image_status | 
[**lldp_remote_devices_get**](DeviceSettingsApi.md#lldp_remote_devices_get) | **GET** /lldp_remote_devices | 
[**system_config_get**](DeviceSettingsApi.md#system_config_get) | **GET** /system_config | 
[**system_config_post**](DeviceSettingsApi.md#system_config_post) | **POST** /system_config | 
[**system_rfc1213_get**](DeviceSettingsApi.md#system_rfc1213_get) | **GET** /system_rfc1213 | 
[**system_rfc1213_post**](DeviceSettingsApi.md#system_rfc1213_post) | **POST** /system_rfc1213 | 


# **active_image_get**
> ActiveImageGet200Response active_image_get()



Get device activate flash image

### Example

* Bearer Authentication (bearerAuth):

```python
import openapi_client
from openapi_client.models.active_image_get200_response import ActiveImageGet200Response
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
    api_instance = openapi_client.DeviceSettingsApi(api_client)

    try:
        api_response = api_instance.active_image_get()
        print("The response of DeviceSettingsApi->active_image_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeviceSettingsApi->active_image_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ActiveImageGet200Response**](ActiveImageGet200Response.md)

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

# **active_image_post**
> LogoutPost200Response active_image_post(active_image_post_request)



Set device active flash image

### Example

* Bearer Authentication (bearerAuth):

```python
import openapi_client
from openapi_client.models.active_image_post_request import ActiveImagePostRequest
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
    api_instance = openapi_client.DeviceSettingsApi(api_client)
    active_image_post_request = openapi_client.ActiveImagePostRequest() # ActiveImagePostRequest | 

    try:
        api_response = api_instance.active_image_post(active_image_post_request)
        print("The response of DeviceSettingsApi->active_image_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeviceSettingsApi->active_image_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **active_image_post_request** | [**ActiveImagePostRequest**](ActiveImagePostRequest.md)|  | 

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

# **bonjour_get**
> BonjourGet200Response bonjour_get()



Get the device bonjour status

### Example

* Bearer Authentication (bearerAuth):

```python
import openapi_client
from openapi_client.models.bonjour_get200_response import BonjourGet200Response
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
    api_instance = openapi_client.DeviceSettingsApi(api_client)

    try:
        api_response = api_instance.bonjour_get()
        print("The response of DeviceSettingsApi->bonjour_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeviceSettingsApi->bonjour_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**BonjourGet200Response**](BonjourGet200Response.md)

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

# **bonjour_post**
> LogoutPost200Response bonjour_post(bonjour_get200_response)



Set the device bonjour status

### Example

* Bearer Authentication (bearerAuth):

```python
import openapi_client
from openapi_client.models.bonjour_get200_response import BonjourGet200Response
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
    api_instance = openapi_client.DeviceSettingsApi(api_client)
    bonjour_get200_response = openapi_client.BonjourGet200Response() # BonjourGet200Response | 

    try:
        api_response = api_instance.bonjour_post(bonjour_get200_response)
        print("The response of DeviceSettingsApi->bonjour_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeviceSettingsApi->bonjour_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bonjour_get200_response** | [**BonjourGet200Response**](BonjourGet200Response.md)|  | 

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

# **config_copy_post**
> LogoutPost200Response config_copy_post(directive)



Copy configuration within switch

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
    api_instance = openapi_client.DeviceSettingsApi(api_client)
    directive = 'directive_example' # str | 

    try:
        api_response = api_instance.config_copy_post(directive)
        print("The response of DeviceSettingsApi->config_copy_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeviceSettingsApi->config_copy_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **directive** | **str**|  | 

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

# **config_file_compare_get**
> ConfigFileCompareGet200Response config_file_compare_get(directive)



Get configuration comparison

### Example

* Bearer Authentication (bearerAuth):

```python
import openapi_client
from openapi_client.models.config_file_compare_get200_response import ConfigFileCompareGet200Response
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
    api_instance = openapi_client.DeviceSettingsApi(api_client)
    directive = 'directive_example' # str | 

    try:
        api_response = api_instance.config_file_compare_get(directive)
        print("The response of DeviceSettingsApi->config_file_compare_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeviceSettingsApi->config_file_compare_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **directive** | **str**|  | 

### Return type

[**ConfigFileCompareGet200Response**](ConfigFileCompareGet200Response.md)

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

# **device_info_get**
> DeviceInfoGet200Response device_info_get()



Get the device information

### Example

* Bearer Authentication (bearerAuth):

```python
import openapi_client
from openapi_client.models.device_info_get200_response import DeviceInfoGet200Response
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
    api_instance = openapi_client.DeviceSettingsApi(api_client)

    try:
        api_response = api_instance.device_info_get()
        print("The response of DeviceSettingsApi->device_info_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeviceSettingsApi->device_info_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**DeviceInfoGet200Response**](DeviceInfoGet200Response.md)

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

# **device_name_get**
> DeviceNameGet200Response device_name_get()



Get the device name

### Example

* Bearer Authentication (bearerAuth):

```python
import openapi_client
from openapi_client.models.device_name_get200_response import DeviceNameGet200Response
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
    api_instance = openapi_client.DeviceSettingsApi(api_client)

    try:
        api_response = api_instance.device_name_get()
        print("The response of DeviceSettingsApi->device_name_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeviceSettingsApi->device_name_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**DeviceNameGet200Response**](DeviceNameGet200Response.md)

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

# **device_name_post**
> LogoutPost200Response device_name_post(device_name_post_request)



Set the device name

### Example

* Bearer Authentication (bearerAuth):

```python
import openapi_client
from openapi_client.models.device_name_post_request import DeviceNamePostRequest
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
    api_instance = openapi_client.DeviceSettingsApi(api_client)
    device_name_post_request = openapi_client.DeviceNamePostRequest() # DeviceNamePostRequest | 

    try:
        api_response = api_instance.device_name_post(device_name_post_request)
        print("The response of DeviceSettingsApi->device_name_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeviceSettingsApi->device_name_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_name_post_request** | [**DeviceNamePostRequest**](DeviceNamePostRequest.md)|  | 

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

# **device_reboot_post**
> LogoutPost200Response device_reboot_post(device_reboot_post_request)



Reboot switch

### Example

* Bearer Authentication (bearerAuth):

```python
import openapi_client
from openapi_client.models.device_reboot_post_request import DeviceRebootPostRequest
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
    api_instance = openapi_client.DeviceSettingsApi(api_client)
    device_reboot_post_request = openapi_client.DeviceRebootPostRequest() # DeviceRebootPostRequest | 

    try:
        api_response = api_instance.device_reboot_post(device_reboot_post_request)
        print("The response of DeviceSettingsApi->device_reboot_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeviceSettingsApi->device_reboot_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_reboot_post_request** | [**DeviceRebootPostRequest**](DeviceRebootPostRequest.md)|  | 

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

# **dual_image_status_get**
> DualImageStatusGet200Response dual_image_status_get()



Get the device flash image status

### Example

* Bearer Authentication (bearerAuth):

```python
import openapi_client
from openapi_client.models.dual_image_status_get200_response import DualImageStatusGet200Response
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
    api_instance = openapi_client.DeviceSettingsApi(api_client)

    try:
        api_response = api_instance.dual_image_status_get()
        print("The response of DeviceSettingsApi->dual_image_status_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeviceSettingsApi->dual_image_status_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**DualImageStatusGet200Response**](DualImageStatusGet200Response.md)

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

# **lldp_remote_devices_get**
> LldpRemoteDevicesGet200Response lldp_remote_devices_get()



Get remote device lldp information

### Example

* Bearer Authentication (bearerAuth):

```python
import openapi_client
from openapi_client.models.lldp_remote_devices_get200_response import LldpRemoteDevicesGet200Response
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
    api_instance = openapi_client.DeviceSettingsApi(api_client)

    try:
        api_response = api_instance.lldp_remote_devices_get()
        print("The response of DeviceSettingsApi->lldp_remote_devices_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeviceSettingsApi->lldp_remote_devices_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**LldpRemoteDevicesGet200Response**](LldpRemoteDevicesGet200Response.md)

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

# **system_config_get**
> SystemConfigGet200Response system_config_get()



Get device console and telnet settings

### Example

* Bearer Authentication (bearerAuth):

```python
import openapi_client
from openapi_client.models.system_config_get200_response import SystemConfigGet200Response
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
    api_instance = openapi_client.DeviceSettingsApi(api_client)

    try:
        api_response = api_instance.system_config_get()
        print("The response of DeviceSettingsApi->system_config_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeviceSettingsApi->system_config_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**SystemConfigGet200Response**](SystemConfigGet200Response.md)

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

# **system_config_post**
> LogoutPost200Response system_config_post(access_line, system_config_post_request)



Set device console and telnet settings

### Example

* Bearer Authentication (bearerAuth):

```python
import openapi_client
from openapi_client.models.logout_post200_response import LogoutPost200Response
from openapi_client.models.system_config_post_request import SystemConfigPostRequest
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
    api_instance = openapi_client.DeviceSettingsApi(api_client)
    access_line = 'access_line_example' # str | 
    system_config_post_request = openapi_client.SystemConfigPostRequest() # SystemConfigPostRequest | 

    try:
        api_response = api_instance.system_config_post(access_line, system_config_post_request)
        print("The response of DeviceSettingsApi->system_config_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeviceSettingsApi->system_config_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_line** | **str**|  | 
 **system_config_post_request** | [**SystemConfigPostRequest**](SystemConfigPostRequest.md)|  | 

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

# **system_rfc1213_get**
> SystemRfc1213Get200Response system_rfc1213_get()



Get device name, description, location and contact

### Example

* Bearer Authentication (bearerAuth):

```python
import openapi_client
from openapi_client.models.system_rfc1213_get200_response import SystemRfc1213Get200Response
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
    api_instance = openapi_client.DeviceSettingsApi(api_client)

    try:
        api_response = api_instance.system_rfc1213_get()
        print("The response of DeviceSettingsApi->system_rfc1213_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeviceSettingsApi->system_rfc1213_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**SystemRfc1213Get200Response**](SystemRfc1213Get200Response.md)

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

# **system_rfc1213_post**
> LogoutPost200Response system_rfc1213_post(system_rfc1213_post_request)



Set device name, location and contact

### Example

* Bearer Authentication (bearerAuth):

```python
import openapi_client
from openapi_client.models.logout_post200_response import LogoutPost200Response
from openapi_client.models.system_rfc1213_post_request import SystemRfc1213PostRequest
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
    api_instance = openapi_client.DeviceSettingsApi(api_client)
    system_rfc1213_post_request = openapi_client.SystemRfc1213PostRequest() # SystemRfc1213PostRequest | 

    try:
        api_response = api_instance.system_rfc1213_post(system_rfc1213_post_request)
        print("The response of DeviceSettingsApi->system_rfc1213_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeviceSettingsApi->system_rfc1213_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_rfc1213_post_request** | [**SystemRfc1213PostRequest**](SystemRfc1213PostRequest.md)|  | 

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

