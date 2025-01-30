# openapi_client.PowerOverEthernetInformationAndSettingsApi

All URIs are relative to *https://127.0.0.1:8443/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**poe_config_get**](PowerOverEthernetInformationAndSettingsApi.md#poe_config_get) | **GET** /poe_config |
[**poe_config_post**](PowerOverEthernetInformationAndSettingsApi.md#poe_config_post) | **POST** /poe_config |
[**swcfg_poe_get**](PowerOverEthernetInformationAndSettingsApi.md#swcfg_poe_get) | **GET** /swcfg_poe |
[**swcfg_poe_post**](PowerOverEthernetInformationAndSettingsApi.md#swcfg_poe_post) | **POST** /swcfg_poe |


# **poe_config_get**
> PoeConfigGet200Response poe_config_get()



Get switch PoE settings

### Example

* Bearer Authentication (bearerAuth):

```python
import openapi_client
from openapi_client.models.poe_config_get200_response import PoeConfigGet200Response
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
    api_instance = openapi_client.PowerOverEthernetInformationAndSettingsApi(api_client)

    try:
        api_response = api_instance.poe_config_get()
        print("The response of PowerOverEthernetInformationAndSettingsApi->poe_config_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PowerOverEthernetInformationAndSettingsApi->poe_config_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**PoeConfigGet200Response**](PoeConfigGet200Response.md)

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

# **poe_config_post**
> LogoutPost200Response poe_config_post(poe_config_post_request)



Set switch PoE settings

### Example

* Bearer Authentication (bearerAuth):

```python
import openapi_client
from openapi_client.models.logout_post200_response import LogoutPost200Response
from openapi_client.models.poe_config_post_request import PoeConfigPostRequest
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
    api_instance = openapi_client.PowerOverEthernetInformationAndSettingsApi(api_client)
    poe_config_post_request = openapi_client.PoeConfigPostRequest() # PoeConfigPostRequest |

    try:
        api_response = api_instance.poe_config_post(poe_config_post_request)
        print("The response of PowerOverEthernetInformationAndSettingsApi->poe_config_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PowerOverEthernetInformationAndSettingsApi->poe_config_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **poe_config_post_request** | [**PoeConfigPostRequest**](PoeConfigPostRequest.md)|  |

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

# **swcfg_poe_get**
> SwcfgPoeGet200Response swcfg_poe_get(portid)



Get port PoE configuration

### Example

* Bearer Authentication (bearerAuth):

```python
import openapi_client
from openapi_client.models.swcfg_poe_get200_response import SwcfgPoeGet200Response
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
    api_instance = openapi_client.PowerOverEthernetInformationAndSettingsApi(api_client)
    portid = openapi_client.SwPortstatsGetPortidParameter() # SwPortstatsGetPortidParameter | Port ID Number by `<port#>` or `ALL`

    try:
        api_response = api_instance.swcfg_poe_get(portid)
        print("The response of PowerOverEthernetInformationAndSettingsApi->swcfg_poe_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PowerOverEthernetInformationAndSettingsApi->swcfg_poe_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **portid** | [**SwPortstatsGetPortidParameter**](.md)| Port ID Number by &#x60;&lt;port#&gt;&#x60; or &#x60;ALL&#x60; |

### Return type

[**SwcfgPoeGet200Response**](SwcfgPoeGet200Response.md)

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

# **swcfg_poe_post**
> LogoutPost200Response swcfg_poe_post(portid, swcfg_poe_post_request)



Set port PoE configuration

### Example

* Bearer Authentication (bearerAuth):

```python
import openapi_client
from openapi_client.models.logout_post200_response import LogoutPost200Response
from openapi_client.models.swcfg_poe_post_request import SwcfgPoePostRequest
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
    api_instance = openapi_client.PowerOverEthernetInformationAndSettingsApi(api_client)
    portid = ALL # int | Port ID Number by `<port#>` or `ALL`
    swcfg_poe_post_request = openapi_client.SwcfgPoePostRequest() # SwcfgPoePostRequest |

    try:
        api_response = api_instance.swcfg_poe_post(portid, swcfg_poe_post_request)
        print("The response of PowerOverEthernetInformationAndSettingsApi->swcfg_poe_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PowerOverEthernetInformationAndSettingsApi->swcfg_poe_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **portid** | **int**| Port ID Number by &#x60;&lt;port#&gt;&#x60; or &#x60;ALL&#x60; |
 **swcfg_poe_post_request** | [**SwcfgPoePostRequest**](SwcfgPoePostRequest.md)|  |

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
