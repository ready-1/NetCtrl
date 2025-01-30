# openapi_client.QualityOfServiceApi

All URIs are relative to *https://127.0.0.1:8443/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cos_queue_config_get**](QualityOfServiceApi.md#cos_queue_config_get) | **GET** /cos_queue_config |
[**cos_queue_config_post**](QualityOfServiceApi.md#cos_queue_config_post) | **POST** /cos_queue_config |
[**costrust_get**](QualityOfServiceApi.md#costrust_get) | **GET** /costrust |
[**costrust_post**](QualityOfServiceApi.md#costrust_post) | **POST** /costrust |
[**dot1p_queue_map_get**](QualityOfServiceApi.md#dot1p_queue_map_get) | **GET** /dot1p_queue_map |
[**dot1p_queue_map_post**](QualityOfServiceApi.md#dot1p_queue_map_post) | **POST** /dot1p_queue_map |
[**ipdscp_queue_map_get**](QualityOfServiceApi.md#ipdscp_queue_map_get) | **GET** /ipdscp_queue_map |
[**ipdscp_queue_map_post**](QualityOfServiceApi.md#ipdscp_queue_map_post) | **POST** /ipdscp_queue_map |


# **cos_queue_config_get**
> CosQueueConfigGet200Response cos_queue_config_get(interface)



Get Class of Service (CoS) queue configuration

### Example

* Bearer Authentication (bearerAuth):

```python
import openapi_client
from openapi_client.models.cos_queue_config_get200_response import CosQueueConfigGet200Response
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
    api_instance = openapi_client.QualityOfServiceApi(api_client)
    interface = 56 # int | Port interface ID by `<port#>`, `Global`, or `ALL`

    try:
        api_response = api_instance.cos_queue_config_get(interface)
        print("The response of QualityOfServiceApi->cos_queue_config_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualityOfServiceApi->cos_queue_config_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **interface** | **int**| Port interface ID by &#x60;&lt;port#&gt;&#x60;, &#x60;Global&#x60;, or &#x60;ALL&#x60; |

### Return type

[**CosQueueConfigGet200Response**](CosQueueConfigGet200Response.md)

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

# **cos_queue_config_post**
> LogoutPost200Response cos_queue_config_post(interface, cos_queue_config_post_request)



Set Class of Service (CoS) queue configuration

### Example

* Bearer Authentication (bearerAuth):

```python
import openapi_client
from openapi_client.models.cos_queue_config_post_request import CosQueueConfigPostRequest
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
    api_instance = openapi_client.QualityOfServiceApi(api_client)
    interface = 56 # int | Port interface ID  by `<port#>` or `Global`
    cos_queue_config_post_request = openapi_client.CosQueueConfigPostRequest() # CosQueueConfigPostRequest |

    try:
        api_response = api_instance.cos_queue_config_post(interface, cos_queue_config_post_request)
        print("The response of QualityOfServiceApi->cos_queue_config_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualityOfServiceApi->cos_queue_config_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **interface** | **int**| Port interface ID  by &#x60;&lt;port#&gt;&#x60; or &#x60;Global&#x60; |
 **cos_queue_config_post_request** | [**CosQueueConfigPostRequest**](CosQueueConfigPostRequest.md)|  |

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

# **costrust_get**
> CostrustGet200Response costrust_get(interface)



Get Class of Service (CoS) trust settings

### Example

* Bearer Authentication (bearerAuth):

```python
import openapi_client
from openapi_client.models.costrust_get200_response import CostrustGet200Response
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
    api_instance = openapi_client.QualityOfServiceApi(api_client)
    interface = openapi_client.SwPortstatsGetPortidParameter() # SwPortstatsGetPortidParameter | Port interface ID Number by `<port#>`, `ALL`, or `Global`

    try:
        api_response = api_instance.costrust_get(interface)
        print("The response of QualityOfServiceApi->costrust_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualityOfServiceApi->costrust_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **interface** | [**SwPortstatsGetPortidParameter**](.md)| Port interface ID Number by &#x60;&lt;port#&gt;&#x60;, &#x60;ALL&#x60;, or &#x60;Global&#x60; |

### Return type

[**CostrustGet200Response**](CostrustGet200Response.md)

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

# **costrust_post**
> LogoutPost200Response costrust_post(interface, costrust_post_request)



Set Class of Service (CoS) trust settings

### Example

* Bearer Authentication (bearerAuth):

```python
import openapi_client
from openapi_client.models.costrust_post_request import CostrustPostRequest
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
    api_instance = openapi_client.QualityOfServiceApi(api_client)
    interface = ALL # int | Port interface ID Number by `<port#>`, `ALL`, or `Global`
    costrust_post_request = openapi_client.CostrustPostRequest() # CostrustPostRequest |

    try:
        api_response = api_instance.costrust_post(interface, costrust_post_request)
        print("The response of QualityOfServiceApi->costrust_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualityOfServiceApi->costrust_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **interface** | **int**| Port interface ID Number by &#x60;&lt;port#&gt;&#x60;, &#x60;ALL&#x60;, or &#x60;Global&#x60; |
 **costrust_post_request** | [**CostrustPostRequest**](CostrustPostRequest.md)|  |

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

# **dot1p_queue_map_get**
> Dot1pQueueMapGet200Response dot1p_queue_map_get(interface)



Get Class of Service (CoS) 802.1p queue mapping

### Example

* Bearer Authentication (bearerAuth):

```python
import openapi_client
from openapi_client.models.dot1p_queue_map_get200_response import Dot1pQueueMapGet200Response
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
    api_instance = openapi_client.QualityOfServiceApi(api_client)
    interface = openapi_client.SwPortstatsGetPortidParameter() # SwPortstatsGetPortidParameter | Port interface ID Number by `<port#>`, `ALL`, or `Global`

    try:
        api_response = api_instance.dot1p_queue_map_get(interface)
        print("The response of QualityOfServiceApi->dot1p_queue_map_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualityOfServiceApi->dot1p_queue_map_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **interface** | [**SwPortstatsGetPortidParameter**](.md)| Port interface ID Number by &#x60;&lt;port#&gt;&#x60;, &#x60;ALL&#x60;, or &#x60;Global&#x60; |

### Return type

[**Dot1pQueueMapGet200Response**](Dot1pQueueMapGet200Response.md)

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

# **dot1p_queue_map_post**
> LogoutPost200Response dot1p_queue_map_post(interface, dot1p_queue_map_post_request)



Set Class of Service (CoS) 802.1p queue mapping

### Example

* Bearer Authentication (bearerAuth):

```python
import openapi_client
from openapi_client.models.dot1p_queue_map_post_request import Dot1pQueueMapPostRequest
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
    api_instance = openapi_client.QualityOfServiceApi(api_client)
    interface = openapi_client.SwPortstatsGetPortidParameter() # SwPortstatsGetPortidParameter | Port interface ID Number by `<port#>` or `Global`
    dot1p_queue_map_post_request = openapi_client.Dot1pQueueMapPostRequest() # Dot1pQueueMapPostRequest |

    try:
        api_response = api_instance.dot1p_queue_map_post(interface, dot1p_queue_map_post_request)
        print("The response of QualityOfServiceApi->dot1p_queue_map_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualityOfServiceApi->dot1p_queue_map_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **interface** | [**SwPortstatsGetPortidParameter**](.md)| Port interface ID Number by &#x60;&lt;port#&gt;&#x60; or &#x60;Global&#x60; |
 **dot1p_queue_map_post_request** | [**Dot1pQueueMapPostRequest**](Dot1pQueueMapPostRequest.md)|  |

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

# **ipdscp_queue_map_get**
> IpdscpQueueMapGet200Response ipdscp_queue_map_get()



Get mapping from the Differentiated Services Code Point (DSCP) to the outgoing traffic forwarding queue

### Example

* Bearer Authentication (bearerAuth):

```python
import openapi_client
from openapi_client.models.ipdscp_queue_map_get200_response import IpdscpQueueMapGet200Response
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
    api_instance = openapi_client.QualityOfServiceApi(api_client)

    try:
        api_response = api_instance.ipdscp_queue_map_get()
        print("The response of QualityOfServiceApi->ipdscp_queue_map_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualityOfServiceApi->ipdscp_queue_map_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**IpdscpQueueMapGet200Response**](IpdscpQueueMapGet200Response.md)

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

# **ipdscp_queue_map_post**
> LogoutPost200Response ipdscp_queue_map_post(ipdscp_queue_map_post_request)



Set mapping from the Differentiated Services Code Point (DSCP) to the outgoing traffic forwarding queue

### Example

* Bearer Authentication (bearerAuth):

```python
import openapi_client
from openapi_client.models.ipdscp_queue_map_post_request import IpdscpQueueMapPostRequest
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
    api_instance = openapi_client.QualityOfServiceApi(api_client)
    ipdscp_queue_map_post_request = openapi_client.IpdscpQueueMapPostRequest() # IpdscpQueueMapPostRequest |

    try:
        api_response = api_instance.ipdscp_queue_map_post(ipdscp_queue_map_post_request)
        print("The response of QualityOfServiceApi->ipdscp_queue_map_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualityOfServiceApi->ipdscp_queue_map_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ipdscp_queue_map_post_request** | [**IpdscpQueueMapPostRequest**](IpdscpQueueMapPostRequest.md)|  |

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
