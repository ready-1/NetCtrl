# openapi_client.LinkAggregrationGroupSettingsApi

All URIs are relative to *https://127.0.0.1:8443/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sw_lag_cfg_get**](LinkAggregrationGroupSettingsApi.md#sw_lag_cfg_get) | **GET** /sw_lag_cfg | 
[**sw_lag_cfg_post**](LinkAggregrationGroupSettingsApi.md#sw_lag_cfg_post) | **POST** /sw_lag_cfg | 


# **sw_lag_cfg_get**
> SwLagCfgGet200Response sw_lag_cfg_get(lag_group)



Get Link Aggregration Group settings

### Example

* Bearer Authentication (bearerAuth):

```python
import openapi_client
from openapi_client.models.sw_lag_cfg_get200_response import SwLagCfgGet200Response
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
    api_instance = openapi_client.LinkAggregrationGroupSettingsApi(api_client)
    lag_group = openapi_client.SwPortstatsGetPortidParameter() # SwPortstatsGetPortidParameter | LAG Group ID# or `ALL`

    try:
        api_response = api_instance.sw_lag_cfg_get(lag_group)
        print("The response of LinkAggregrationGroupSettingsApi->sw_lag_cfg_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LinkAggregrationGroupSettingsApi->sw_lag_cfg_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lag_group** | [**SwPortstatsGetPortidParameter**](.md)| LAG Group ID# or &#x60;ALL&#x60; | 

### Return type

[**SwLagCfgGet200Response**](SwLagCfgGet200Response.md)

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

# **sw_lag_cfg_post**
> LogoutPost200Response sw_lag_cfg_post(lag_group, sw_lag_cfg_post_request)



Set Link Aggregration Group settings

### Example

* Bearer Authentication (bearerAuth):

```python
import openapi_client
from openapi_client.models.logout_post200_response import LogoutPost200Response
from openapi_client.models.sw_lag_cfg_post_request import SwLagCfgPostRequest
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
    api_instance = openapi_client.LinkAggregrationGroupSettingsApi(api_client)
    lag_group = 1 # int | LAG Group ID
    sw_lag_cfg_post_request = openapi_client.SwLagCfgPostRequest() # SwLagCfgPostRequest | 

    try:
        api_response = api_instance.sw_lag_cfg_post(lag_group, sw_lag_cfg_post_request)
        print("The response of LinkAggregrationGroupSettingsApi->sw_lag_cfg_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LinkAggregrationGroupSettingsApi->sw_lag_cfg_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lag_group** | **int**| LAG Group ID | 
 **sw_lag_cfg_post_request** | [**SwLagCfgPostRequest**](SwLagCfgPostRequest.md)|  | 

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

