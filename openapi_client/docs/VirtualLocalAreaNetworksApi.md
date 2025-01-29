# openapi_client.VirtualLocalAreaNetworksApi

All URIs are relative to *https://127.0.0.1:8443/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**dot1q_sw_port_config_get**](VirtualLocalAreaNetworksApi.md#dot1q_sw_port_config_get) | **GET** /dot1q_sw_port_config | 
[**dot1q_sw_port_config_post**](VirtualLocalAreaNetworksApi.md#dot1q_sw_port_config_post) | **POST** /dot1q_sw_port_config | 
[**swcfg_vlan_delete**](VirtualLocalAreaNetworksApi.md#swcfg_vlan_delete) | **DELETE** /swcfg_vlan | 
[**swcfg_vlan_get**](VirtualLocalAreaNetworksApi.md#swcfg_vlan_get) | **GET** /swcfg_vlan | 
[**swcfg_vlan_membership_get**](VirtualLocalAreaNetworksApi.md#swcfg_vlan_membership_get) | **GET** /swcfg_vlan_membership | 
[**swcfg_vlan_membership_post**](VirtualLocalAreaNetworksApi.md#swcfg_vlan_membership_post) | **POST** /swcfg_vlan_membership | 
[**swcfg_vlan_post**](VirtualLocalAreaNetworksApi.md#swcfg_vlan_post) | **POST** /swcfg_vlan | 
[**vlan_ip_get**](VirtualLocalAreaNetworksApi.md#vlan_ip_get) | **GET** /vlan_ip | 
[**vlan_ip_post**](VirtualLocalAreaNetworksApi.md#vlan_ip_post) | **POST** /vlan_ip | 


# **dot1q_sw_port_config_get**
> Dot1qSwPortConfigGet200Response dot1q_sw_port_config_get(interface)



Get VLAN switchport interface configuration

### Example

* Bearer Authentication (bearerAuth):

```python
import openapi_client
from openapi_client.models.dot1q_sw_port_config_get200_response import Dot1qSwPortConfigGet200Response
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
    api_instance = openapi_client.VirtualLocalAreaNetworksApi(api_client)
    interface = 1 # int | Port Interface ID

    try:
        api_response = api_instance.dot1q_sw_port_config_get(interface)
        print("The response of VirtualLocalAreaNetworksApi->dot1q_sw_port_config_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualLocalAreaNetworksApi->dot1q_sw_port_config_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **interface** | **int**| Port Interface ID | 

### Return type

[**Dot1qSwPortConfigGet200Response**](Dot1qSwPortConfigGet200Response.md)

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

# **dot1q_sw_port_config_post**
> LogoutPost200Response dot1q_sw_port_config_post(interface, dot1q_sw_port_config_post_request)



Set VLAN switchport interface configuration

### Example

* Bearer Authentication (bearerAuth):

```python
import openapi_client
from openapi_client.models.dot1q_sw_port_config_post_request import Dot1qSwPortConfigPostRequest
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
    api_instance = openapi_client.VirtualLocalAreaNetworksApi(api_client)
    interface = 1 # int | Port Interface ID
    dot1q_sw_port_config_post_request = openapi_client.Dot1qSwPortConfigPostRequest() # Dot1qSwPortConfigPostRequest | 

    try:
        api_response = api_instance.dot1q_sw_port_config_post(interface, dot1q_sw_port_config_post_request)
        print("The response of VirtualLocalAreaNetworksApi->dot1q_sw_port_config_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualLocalAreaNetworksApi->dot1q_sw_port_config_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **interface** | **int**| Port Interface ID | 
 **dot1q_sw_port_config_post_request** | [**Dot1qSwPortConfigPostRequest**](Dot1qSwPortConfigPostRequest.md)|  | 

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

# **swcfg_vlan_delete**
> LogoutPost200Response swcfg_vlan_delete(vlanid)



Delete VLAN configuration

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
    api_instance = openapi_client.VirtualLocalAreaNetworksApi(api_client)
    vlanid = 1 # int | VLAN ID

    try:
        api_response = api_instance.swcfg_vlan_delete(vlanid)
        print("The response of VirtualLocalAreaNetworksApi->swcfg_vlan_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualLocalAreaNetworksApi->swcfg_vlan_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vlanid** | **int**| VLAN ID | 

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

# **swcfg_vlan_get**
> SwcfgVlanGet200Response swcfg_vlan_get(vlanid)



Get VLAN configuration settings

### Example

* Bearer Authentication (bearerAuth):

```python
import openapi_client
from openapi_client.models.swcfg_vlan_get200_response import SwcfgVlanGet200Response
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
    api_instance = openapi_client.VirtualLocalAreaNetworksApi(api_client)
    vlanid = 1 # int | VLAN ID

    try:
        api_response = api_instance.swcfg_vlan_get(vlanid)
        print("The response of VirtualLocalAreaNetworksApi->swcfg_vlan_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualLocalAreaNetworksApi->swcfg_vlan_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vlanid** | **int**| VLAN ID | 

### Return type

[**SwcfgVlanGet200Response**](SwcfgVlanGet200Response.md)

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

# **swcfg_vlan_membership_get**
> SwcfgVlanMembershipGet200Response swcfg_vlan_membership_get(vlanid)



Get VLAN port membership list

### Example

* Bearer Authentication (bearerAuth):

```python
import openapi_client
from openapi_client.models.swcfg_vlan_membership_get200_response import SwcfgVlanMembershipGet200Response
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
    api_instance = openapi_client.VirtualLocalAreaNetworksApi(api_client)
    vlanid = 1 # int | VLAN ID

    try:
        api_response = api_instance.swcfg_vlan_membership_get(vlanid)
        print("The response of VirtualLocalAreaNetworksApi->swcfg_vlan_membership_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualLocalAreaNetworksApi->swcfg_vlan_membership_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vlanid** | **int**| VLAN ID | 

### Return type

[**SwcfgVlanMembershipGet200Response**](SwcfgVlanMembershipGet200Response.md)

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

# **swcfg_vlan_membership_post**
> LogoutPost200Response swcfg_vlan_membership_post(swcfg_vlan_membership_post_request)



Set list of VLAN port membership

### Example

* Bearer Authentication (bearerAuth):

```python
import openapi_client
from openapi_client.models.logout_post200_response import LogoutPost200Response
from openapi_client.models.swcfg_vlan_membership_post_request import SwcfgVlanMembershipPostRequest
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
    api_instance = openapi_client.VirtualLocalAreaNetworksApi(api_client)
    swcfg_vlan_membership_post_request = openapi_client.SwcfgVlanMembershipPostRequest() # SwcfgVlanMembershipPostRequest | 

    try:
        api_response = api_instance.swcfg_vlan_membership_post(swcfg_vlan_membership_post_request)
        print("The response of VirtualLocalAreaNetworksApi->swcfg_vlan_membership_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualLocalAreaNetworksApi->swcfg_vlan_membership_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **swcfg_vlan_membership_post_request** | [**SwcfgVlanMembershipPostRequest**](SwcfgVlanMembershipPostRequest.md)|  | 

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

# **swcfg_vlan_post**
> LogoutPost200Response swcfg_vlan_post(vlanid, swcfg_vlan_post_request)



Set VLAN configuration

### Example

* Bearer Authentication (bearerAuth):

```python
import openapi_client
from openapi_client.models.logout_post200_response import LogoutPost200Response
from openapi_client.models.swcfg_vlan_post_request import SwcfgVlanPostRequest
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
    api_instance = openapi_client.VirtualLocalAreaNetworksApi(api_client)
    vlanid = 1 # int | VLAN ID
    swcfg_vlan_post_request = openapi_client.SwcfgVlanPostRequest() # SwcfgVlanPostRequest | 

    try:
        api_response = api_instance.swcfg_vlan_post(vlanid, swcfg_vlan_post_request)
        print("The response of VirtualLocalAreaNetworksApi->swcfg_vlan_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualLocalAreaNetworksApi->swcfg_vlan_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vlanid** | **int**| VLAN ID | 
 **swcfg_vlan_post_request** | [**SwcfgVlanPostRequest**](SwcfgVlanPostRequest.md)|  | 

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

# **vlan_ip_get**
> VlanIpGet200Response vlan_ip_get()



Get VLAN IP configuration

### Example

* Bearer Authentication (bearerAuth):

```python
import openapi_client
from openapi_client.models.vlan_ip_get200_response import VlanIpGet200Response
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
    api_instance = openapi_client.VirtualLocalAreaNetworksApi(api_client)

    try:
        api_response = api_instance.vlan_ip_get()
        print("The response of VirtualLocalAreaNetworksApi->vlan_ip_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualLocalAreaNetworksApi->vlan_ip_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**VlanIpGet200Response**](VlanIpGet200Response.md)

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

# **vlan_ip_post**
> LogoutPost200Response vlan_ip_post(vlan_ip_post_request)



Set VLAN IP configuration

### Example

* Bearer Authentication (bearerAuth):

```python
import openapi_client
from openapi_client.models.logout_post200_response import LogoutPost200Response
from openapi_client.models.vlan_ip_post_request import VlanIpPostRequest
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
    api_instance = openapi_client.VirtualLocalAreaNetworksApi(api_client)
    vlan_ip_post_request = openapi_client.VlanIpPostRequest() # VlanIpPostRequest | 

    try:
        api_response = api_instance.vlan_ip_post(vlan_ip_post_request)
        print("The response of VirtualLocalAreaNetworksApi->vlan_ip_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualLocalAreaNetworksApi->vlan_ip_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vlan_ip_post_request** | [**VlanIpPostRequest**](VlanIpPostRequest.md)|  | 

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

