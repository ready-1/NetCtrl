# openapi_client.PortInformationAndSettingsApi

All URIs are relative to *https://127.0.0.1:8443/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**device_reset_counters_post**](PortInformationAndSettingsApi.md#device_reset_counters_post) | **POST** /device_reset_counters | 
[**dot1d_base_config_get**](PortInformationAndSettingsApi.md#dot1d_base_config_get) | **GET** /dot1d_base_config | 
[**dot1d_tp_config_get**](PortInformationAndSettingsApi.md#dot1d_tp_config_get) | **GET** /dot1d_tp_config | 
[**dot1d_tp_config_post**](PortInformationAndSettingsApi.md#dot1d_tp_config_post) | **POST** /dot1d_tp_config | 
[**dot1d_tp_port_entries_get**](PortInformationAndSettingsApi.md#dot1d_tp_port_entries_get) | **GET** /dot1d_tp_port_entries | 
[**fdb_stats_get**](PortInformationAndSettingsApi.md#fdb_stats_get) | **GET** /fdb_stats | 
[**fdb_stats_post**](PortInformationAndSettingsApi.md#fdb_stats_post) | **POST** /fdb_stats | 
[**fdbs_delete**](PortInformationAndSettingsApi.md#fdbs_delete) | **DELETE** /fdbs | 
[**fdbs_get**](PortInformationAndSettingsApi.md#fdbs_get) | **GET** /fdbs | 
[**fiber_optics_get**](PortInformationAndSettingsApi.md#fiber_optics_get) | **GET** /fiber_optics | 
[**ptpv2_get**](PortInformationAndSettingsApi.md#ptpv2_get) | **GET** /ptpv2 | 
[**ptpv2_global_get**](PortInformationAndSettingsApi.md#ptpv2_global_get) | **GET** /ptpv2_global | 
[**ptpv2_global_post**](PortInformationAndSettingsApi.md#ptpv2_global_post) | **POST** /ptpv2_global | 
[**ptpv2_post**](PortInformationAndSettingsApi.md#ptpv2_post) | **POST** /ptpv2 | 
[**sw_portstats_get**](PortInformationAndSettingsApi.md#sw_portstats_get) | **GET** /sw_portstats | 
[**swcfg_port_get**](PortInformationAndSettingsApi.md#swcfg_port_get) | **GET** /swcfg_port | 
[**swcfg_port_post**](PortInformationAndSettingsApi.md#swcfg_port_post) | **POST** /swcfg_port | 


# **device_reset_counters_post**
> LogoutPost200Response device_reset_counters_post(portid)



Reset interface coutnters of device

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
    api_instance = openapi_client.PortInformationAndSettingsApi(api_client)
    portid = openapi_client.SwPortstatsGetPortidParameter() # SwPortstatsGetPortidParameter | Port ID Number by `<port#>` or `ALL`

    try:
        api_response = api_instance.device_reset_counters_post(portid)
        print("The response of PortInformationAndSettingsApi->device_reset_counters_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortInformationAndSettingsApi->device_reset_counters_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **portid** | [**SwPortstatsGetPortidParameter**](.md)| Port ID Number by &#x60;&lt;port#&gt;&#x60; or &#x60;ALL&#x60; | 

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

# **dot1d_base_config_get**
> Dot1dBaseConfigGet200Response dot1d_base_config_get()



Get Bridge Base Configuration

### Example

* Bearer Authentication (bearerAuth):

```python
import openapi_client
from openapi_client.models.dot1d_base_config_get200_response import Dot1dBaseConfigGet200Response
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
    api_instance = openapi_client.PortInformationAndSettingsApi(api_client)

    try:
        api_response = api_instance.dot1d_base_config_get()
        print("The response of PortInformationAndSettingsApi->dot1d_base_config_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortInformationAndSettingsApi->dot1d_base_config_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**Dot1dBaseConfigGet200Response**](Dot1dBaseConfigGet200Response.md)

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

# **dot1d_tp_config_get**
> Dot1dTpConfigGet200Response dot1d_tp_config_get()



Get bridge timeout period for aging out dynamically learned forwarding information

### Example

* Bearer Authentication (bearerAuth):

```python
import openapi_client
from openapi_client.models.dot1d_tp_config_get200_response import Dot1dTpConfigGet200Response
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
    api_instance = openapi_client.PortInformationAndSettingsApi(api_client)

    try:
        api_response = api_instance.dot1d_tp_config_get()
        print("The response of PortInformationAndSettingsApi->dot1d_tp_config_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortInformationAndSettingsApi->dot1d_tp_config_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**Dot1dTpConfigGet200Response**](Dot1dTpConfigGet200Response.md)

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

# **dot1d_tp_config_post**
> LogoutPost200Response dot1d_tp_config_post(dot1d_tp_config_post_request)



Set bridge timeout period for aging out dynamically learned forwarding information

### Example

* Bearer Authentication (bearerAuth):

```python
import openapi_client
from openapi_client.models.dot1d_tp_config_post_request import Dot1dTpConfigPostRequest
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
    api_instance = openapi_client.PortInformationAndSettingsApi(api_client)
    dot1d_tp_config_post_request = openapi_client.Dot1dTpConfigPostRequest() # Dot1dTpConfigPostRequest | 

    try:
        api_response = api_instance.dot1d_tp_config_post(dot1d_tp_config_post_request)
        print("The response of PortInformationAndSettingsApi->dot1d_tp_config_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortInformationAndSettingsApi->dot1d_tp_config_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dot1d_tp_config_post_request** | [**Dot1dTpConfigPostRequest**](Dot1dTpConfigPostRequest.md)|  | 

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

# **dot1d_tp_port_entries_get**
> Dot1dTpPortEntriesGet200Response dot1d_tp_port_entries_get()



Get bridge timeout period port entries

### Example

* Bearer Authentication (bearerAuth):

```python
import openapi_client
from openapi_client.models.dot1d_tp_port_entries_get200_response import Dot1dTpPortEntriesGet200Response
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
    api_instance = openapi_client.PortInformationAndSettingsApi(api_client)

    try:
        api_response = api_instance.dot1d_tp_port_entries_get()
        print("The response of PortInformationAndSettingsApi->dot1d_tp_port_entries_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortInformationAndSettingsApi->dot1d_tp_port_entries_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**Dot1dTpPortEntriesGet200Response**](Dot1dTpPortEntriesGet200Response.md)

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

# **fdb_stats_get**
> FdbStatsGet200Response fdb_stats_get()



Get forwarding database (fdb) statistics

### Example

* Bearer Authentication (bearerAuth):

```python
import openapi_client
from openapi_client.models.fdb_stats_get200_response import FdbStatsGet200Response
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
    api_instance = openapi_client.PortInformationAndSettingsApi(api_client)

    try:
        api_response = api_instance.fdb_stats_get()
        print("The response of PortInformationAndSettingsApi->fdb_stats_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortInformationAndSettingsApi->fdb_stats_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**FdbStatsGet200Response**](FdbStatsGet200Response.md)

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

# **fdb_stats_post**
> LogoutPost200Response fdb_stats_post(fdb_stats_post_request)



Reset forwarding database (fdb) table entries

### Example

* Bearer Authentication (bearerAuth):

```python
import openapi_client
from openapi_client.models.fdb_stats_post_request import FdbStatsPostRequest
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
    api_instance = openapi_client.PortInformationAndSettingsApi(api_client)
    fdb_stats_post_request = openapi_client.FdbStatsPostRequest() # FdbStatsPostRequest | 

    try:
        api_response = api_instance.fdb_stats_post(fdb_stats_post_request)
        print("The response of PortInformationAndSettingsApi->fdb_stats_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortInformationAndSettingsApi->fdb_stats_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fdb_stats_post_request** | [**FdbStatsPostRequest**](FdbStatsPostRequest.md)|  | 

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

# **fdbs_delete**
> LogoutPost200Response fdbs_delete(mac)



Delete forwarding database (fdb) MAC address entry

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
    api_instance = openapi_client.PortInformationAndSettingsApi(api_client)
    mac = 'mac_example' # str | Delete all learned MAC entries in the forwarding database

    try:
        api_response = api_instance.fdbs_delete(mac)
        print("The response of PortInformationAndSettingsApi->fdbs_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortInformationAndSettingsApi->fdbs_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mac** | **str**| Delete all learned MAC entries in the forwarding database | 

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

# **fdbs_get**
> FdbsGet200Response fdbs_get()



Get forwarding database (fdb) information

### Example

* Bearer Authentication (bearerAuth):

```python
import openapi_client
from openapi_client.models.fdbs_get200_response import FdbsGet200Response
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
    api_instance = openapi_client.PortInformationAndSettingsApi(api_client)

    try:
        api_response = api_instance.fdbs_get()
        print("The response of PortInformationAndSettingsApi->fdbs_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortInformationAndSettingsApi->fdbs_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**FdbsGet200Response**](FdbsGet200Response.md)

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

# **fiber_optics_get**
> FiberOpticsGet200Response fiber_optics_get()



Get bridge base configuration

### Example

* Bearer Authentication (bearerAuth):

```python
import openapi_client
from openapi_client.models.fiber_optics_get200_response import FiberOpticsGet200Response
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
    api_instance = openapi_client.PortInformationAndSettingsApi(api_client)

    try:
        api_response = api_instance.fiber_optics_get()
        print("The response of PortInformationAndSettingsApi->fiber_optics_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortInformationAndSettingsApi->fiber_optics_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**FiberOpticsGet200Response**](FiberOpticsGet200Response.md)

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

# **ptpv2_get**
> Ptpv2Get200Response ptpv2_get(portid)



Get switch's PTPv2 status configuration

### Example

* Bearer Authentication (bearerAuth):

```python
import openapi_client
from openapi_client.models.ptpv2_get200_response import Ptpv2Get200Response
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
    api_instance = openapi_client.PortInformationAndSettingsApi(api_client)
    portid = 'portid_example' # str | Port interface ID number by `<port#>` or `All`

    try:
        api_response = api_instance.ptpv2_get(portid)
        print("The response of PortInformationAndSettingsApi->ptpv2_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortInformationAndSettingsApi->ptpv2_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **portid** | **str**| Port interface ID number by &#x60;&lt;port#&gt;&#x60; or &#x60;All&#x60; | 

### Return type

[**Ptpv2Get200Response**](Ptpv2Get200Response.md)

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

# **ptpv2_global_get**
> Ptpv2GlobalGet200Response ptpv2_global_get()



Get switch's PTPv2 status configuration

### Example

* Bearer Authentication (bearerAuth):

```python
import openapi_client
from openapi_client.models.ptpv2_global_get200_response import Ptpv2GlobalGet200Response
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
    api_instance = openapi_client.PortInformationAndSettingsApi(api_client)

    try:
        api_response = api_instance.ptpv2_global_get()
        print("The response of PortInformationAndSettingsApi->ptpv2_global_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortInformationAndSettingsApi->ptpv2_global_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**Ptpv2GlobalGet200Response**](Ptpv2GlobalGet200Response.md)

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

# **ptpv2_global_post**
> LogoutPost200Response ptpv2_global_post(ptpv2_global_post_request)



Set switch's PTPv2 status configuration

### Example

* Bearer Authentication (bearerAuth):

```python
import openapi_client
from openapi_client.models.logout_post200_response import LogoutPost200Response
from openapi_client.models.ptpv2_global_post_request import Ptpv2GlobalPostRequest
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
    api_instance = openapi_client.PortInformationAndSettingsApi(api_client)
    ptpv2_global_post_request = openapi_client.Ptpv2GlobalPostRequest() # Ptpv2GlobalPostRequest | 

    try:
        api_response = api_instance.ptpv2_global_post(ptpv2_global_post_request)
        print("The response of PortInformationAndSettingsApi->ptpv2_global_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortInformationAndSettingsApi->ptpv2_global_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ptpv2_global_post_request** | [**Ptpv2GlobalPostRequest**](Ptpv2GlobalPostRequest.md)|  | 

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

# **ptpv2_post**
> LogoutPost200Response ptpv2_post(portid, ptpv2_post_request)



Set switch's PTPv2 status configuration

### Example

* Bearer Authentication (bearerAuth):

```python
import openapi_client
from openapi_client.models.logout_post200_response import LogoutPost200Response
from openapi_client.models.ptpv2_post_request import Ptpv2PostRequest
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
    api_instance = openapi_client.PortInformationAndSettingsApi(api_client)
    portid = 'portid_example' # str | Port interface ID
    ptpv2_post_request = openapi_client.Ptpv2PostRequest() # Ptpv2PostRequest | 

    try:
        api_response = api_instance.ptpv2_post(portid, ptpv2_post_request)
        print("The response of PortInformationAndSettingsApi->ptpv2_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortInformationAndSettingsApi->ptpv2_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **portid** | **str**| Port interface ID | 
 **ptpv2_post_request** | [**Ptpv2PostRequest**](Ptpv2PostRequest.md)|  | 

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

# **sw_portstats_get**
> SwPortstatsGet200Response sw_portstats_get(portid)



Get port statistics

### Example

* Bearer Authentication (bearerAuth):

```python
import openapi_client
from openapi_client.models.sw_portstats_get200_response import SwPortstatsGet200Response
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
    api_instance = openapi_client.PortInformationAndSettingsApi(api_client)
    portid = openapi_client.SwPortstatsGetPortidParameter() # SwPortstatsGetPortidParameter | Port ID Number by `<port#>` or `ALL`

    try:
        api_response = api_instance.sw_portstats_get(portid)
        print("The response of PortInformationAndSettingsApi->sw_portstats_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortInformationAndSettingsApi->sw_portstats_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **portid** | [**SwPortstatsGetPortidParameter**](.md)| Port ID Number by &#x60;&lt;port#&gt;&#x60; or &#x60;ALL&#x60; | 

### Return type

[**SwPortstatsGet200Response**](SwPortstatsGet200Response.md)

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

# **swcfg_port_get**
> SwcfgPortGet200Response swcfg_port_get(portid)



Get port configuration

### Example

* Bearer Authentication (bearerAuth):

```python
import openapi_client
from openapi_client.models.swcfg_port_get200_response import SwcfgPortGet200Response
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
    api_instance = openapi_client.PortInformationAndSettingsApi(api_client)
    portid = 1 # int | Port ID Number

    try:
        api_response = api_instance.swcfg_port_get(portid)
        print("The response of PortInformationAndSettingsApi->swcfg_port_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortInformationAndSettingsApi->swcfg_port_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **portid** | **int**| Port ID Number | 

### Return type

[**SwcfgPortGet200Response**](SwcfgPortGet200Response.md)

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

# **swcfg_port_post**
> LogoutPost200Response swcfg_port_post(portid, swcfg_port_get200_response)



Set port configuration

### Example

* Bearer Authentication (bearerAuth):

```python
import openapi_client
from openapi_client.models.logout_post200_response import LogoutPost200Response
from openapi_client.models.swcfg_port_get200_response import SwcfgPortGet200Response
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
    api_instance = openapi_client.PortInformationAndSettingsApi(api_client)
    portid = 1 # int | Port ID Number
    swcfg_port_get200_response = openapi_client.SwcfgPortGet200Response() # SwcfgPortGet200Response | 

    try:
        api_response = api_instance.swcfg_port_post(portid, swcfg_port_get200_response)
        print("The response of PortInformationAndSettingsApi->swcfg_port_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortInformationAndSettingsApi->swcfg_port_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **portid** | **int**| Port ID Number | 
 **swcfg_port_get200_response** | [**SwcfgPortGet200Response**](SwcfgPortGet200Response.md)|  | 

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

