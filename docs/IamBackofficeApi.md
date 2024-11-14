# iambackoffice.IamBackofficeApi

All URIs are relative to *https://iambackoffice.api.gogemini.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**iam_backoffice_assign_roles**](IamBackofficeApi.md#iam_backoffice_assign_roles) | **POST** /iambackoffice.IamBackoffice/AssignRoles | AUTHZ
[**iam_backoffice_assign_user_to_group**](IamBackofficeApi.md#iam_backoffice_assign_user_to_group) | **POST** /iambackoffice.IamBackoffice/AssignUserToGroup | 
[**iam_backoffice_create_group**](IamBackofficeApi.md#iam_backoffice_create_group) | **POST** /iambackoffice.IamBackoffice/CreateGroup | GROUPS
[**iam_backoffice_disable_user_mfa**](IamBackofficeApi.md#iam_backoffice_disable_user_mfa) | **POST** /iambackoffice.IamBackoffice/DisableUserMfa | 
[**iam_backoffice_enable_user_mfa**](IamBackofficeApi.md#iam_backoffice_enable_user_mfa) | **POST** /iambackoffice.IamBackoffice/EnableUserMfa | 
[**iam_backoffice_generate_secret_for_qr**](IamBackofficeApi.md#iam_backoffice_generate_secret_for_qr) | **POST** /iambackoffice.IamBackoffice/GenerateSecretForQR | MFA
[**iam_backoffice_get_user**](IamBackofficeApi.md#iam_backoffice_get_user) | **POST** /iambackoffice.IamBackoffice/GetUser | USER
[**iam_backoffice_login**](IamBackofficeApi.md#iam_backoffice_login) | **POST** /iambackoffice.IamBackoffice/Login | LOGIN
[**iam_backoffice_login_mfa**](IamBackofficeApi.md#iam_backoffice_login_mfa) | **POST** /iambackoffice.IamBackoffice/LoginMfa | LOGIN MFA
[**iam_backoffice_logout**](IamBackofficeApi.md#iam_backoffice_logout) | **POST** /iambackoffice.IamBackoffice/Logout | 
[**iam_backoffice_register**](IamBackofficeApi.md#iam_backoffice_register) | **POST** /iambackoffice.IamBackoffice/Register | REGISTRATION
[**iam_backoffice_search_groups**](IamBackofficeApi.md#iam_backoffice_search_groups) | **POST** /iambackoffice.IamBackoffice/SearchGroups | 
[**iam_backoffice_unassign_roles**](IamBackofficeApi.md#iam_backoffice_unassign_roles) | **POST** /iambackoffice.IamBackoffice/UnassignRoles | 


# **iam_backoffice_assign_roles**
> IambackofficeAssignRolesResponse iam_backoffice_assign_roles(body)

AUTHZ

### Example


```python
import iambackoffice
from iambackoffice.models.iambackoffice_assign_roles_request import IambackofficeAssignRolesRequest
from iambackoffice.models.iambackoffice_assign_roles_response import IambackofficeAssignRolesResponse
from iambackoffice.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://iambackoffice.api.gogemini.io
# See configuration.py for a list of all supported configuration parameters.
configuration = iambackoffice.Configuration(
    host = "https://iambackoffice.api.gogemini.io"
)


# Enter a context with an instance of the API client
with iambackoffice.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = iambackoffice.IamBackofficeApi(api_client)
    body = iambackoffice.IambackofficeAssignRolesRequest() # IambackofficeAssignRolesRequest | 

    try:
        # AUTHZ
        api_response = api_instance.iam_backoffice_assign_roles(body)
        print("The response of IamBackofficeApi->iam_backoffice_assign_roles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IamBackofficeApi->iam_backoffice_assign_roles: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**IambackofficeAssignRolesRequest**](IambackofficeAssignRolesRequest.md)|  | 

### Return type

[**IambackofficeAssignRolesResponse**](IambackofficeAssignRolesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **iam_backoffice_assign_user_to_group**
> object iam_backoffice_assign_user_to_group(body)



### Example


```python
import iambackoffice
from iambackoffice.models.iambackoffice_assign_user_to_group_request import IambackofficeAssignUserToGroupRequest
from iambackoffice.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://iambackoffice.api.gogemini.io
# See configuration.py for a list of all supported configuration parameters.
configuration = iambackoffice.Configuration(
    host = "https://iambackoffice.api.gogemini.io"
)


# Enter a context with an instance of the API client
with iambackoffice.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = iambackoffice.IamBackofficeApi(api_client)
    body = iambackoffice.IambackofficeAssignUserToGroupRequest() # IambackofficeAssignUserToGroupRequest | 

    try:
        api_response = api_instance.iam_backoffice_assign_user_to_group(body)
        print("The response of IamBackofficeApi->iam_backoffice_assign_user_to_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IamBackofficeApi->iam_backoffice_assign_user_to_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**IambackofficeAssignUserToGroupRequest**](IambackofficeAssignUserToGroupRequest.md)|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **iam_backoffice_create_group**
> IambackofficeCreateGroupResponse iam_backoffice_create_group(body)

GROUPS

### Example


```python
import iambackoffice
from iambackoffice.models.iambackoffice_create_group_request import IambackofficeCreateGroupRequest
from iambackoffice.models.iambackoffice_create_group_response import IambackofficeCreateGroupResponse
from iambackoffice.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://iambackoffice.api.gogemini.io
# See configuration.py for a list of all supported configuration parameters.
configuration = iambackoffice.Configuration(
    host = "https://iambackoffice.api.gogemini.io"
)


# Enter a context with an instance of the API client
with iambackoffice.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = iambackoffice.IamBackofficeApi(api_client)
    body = iambackoffice.IambackofficeCreateGroupRequest() # IambackofficeCreateGroupRequest | 

    try:
        # GROUPS
        api_response = api_instance.iam_backoffice_create_group(body)
        print("The response of IamBackofficeApi->iam_backoffice_create_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IamBackofficeApi->iam_backoffice_create_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**IambackofficeCreateGroupRequest**](IambackofficeCreateGroupRequest.md)|  | 

### Return type

[**IambackofficeCreateGroupResponse**](IambackofficeCreateGroupResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **iam_backoffice_disable_user_mfa**
> IambackofficeUserMfaResponse iam_backoffice_disable_user_mfa(body)



### Example


```python
import iambackoffice
from iambackoffice.models.iambackoffice_disable_user_mfa_request import IambackofficeDisableUserMfaRequest
from iambackoffice.models.iambackoffice_user_mfa_response import IambackofficeUserMfaResponse
from iambackoffice.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://iambackoffice.api.gogemini.io
# See configuration.py for a list of all supported configuration parameters.
configuration = iambackoffice.Configuration(
    host = "https://iambackoffice.api.gogemini.io"
)


# Enter a context with an instance of the API client
with iambackoffice.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = iambackoffice.IamBackofficeApi(api_client)
    body = iambackoffice.IambackofficeDisableUserMfaRequest() # IambackofficeDisableUserMfaRequest | 

    try:
        api_response = api_instance.iam_backoffice_disable_user_mfa(body)
        print("The response of IamBackofficeApi->iam_backoffice_disable_user_mfa:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IamBackofficeApi->iam_backoffice_disable_user_mfa: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**IambackofficeDisableUserMfaRequest**](IambackofficeDisableUserMfaRequest.md)|  | 

### Return type

[**IambackofficeUserMfaResponse**](IambackofficeUserMfaResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **iam_backoffice_enable_user_mfa**
> IambackofficeUserMfaResponse iam_backoffice_enable_user_mfa(body)



### Example


```python
import iambackoffice
from iambackoffice.models.iambackoffice_enable_user_mfa_request import IambackofficeEnableUserMfaRequest
from iambackoffice.models.iambackoffice_user_mfa_response import IambackofficeUserMfaResponse
from iambackoffice.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://iambackoffice.api.gogemini.io
# See configuration.py for a list of all supported configuration parameters.
configuration = iambackoffice.Configuration(
    host = "https://iambackoffice.api.gogemini.io"
)


# Enter a context with an instance of the API client
with iambackoffice.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = iambackoffice.IamBackofficeApi(api_client)
    body = iambackoffice.IambackofficeEnableUserMfaRequest() # IambackofficeEnableUserMfaRequest | 

    try:
        api_response = api_instance.iam_backoffice_enable_user_mfa(body)
        print("The response of IamBackofficeApi->iam_backoffice_enable_user_mfa:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IamBackofficeApi->iam_backoffice_enable_user_mfa: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**IambackofficeEnableUserMfaRequest**](IambackofficeEnableUserMfaRequest.md)|  | 

### Return type

[**IambackofficeUserMfaResponse**](IambackofficeUserMfaResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **iam_backoffice_generate_secret_for_qr**
> IambackofficeGenerateSecretForQRResponse iam_backoffice_generate_secret_for_qr(body)

MFA

### Example


```python
import iambackoffice
from iambackoffice.models.iambackoffice_generate_secret_for_qr_response import IambackofficeGenerateSecretForQRResponse
from iambackoffice.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://iambackoffice.api.gogemini.io
# See configuration.py for a list of all supported configuration parameters.
configuration = iambackoffice.Configuration(
    host = "https://iambackoffice.api.gogemini.io"
)


# Enter a context with an instance of the API client
with iambackoffice.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = iambackoffice.IamBackofficeApi(api_client)
    body = None # object | 

    try:
        # MFA
        api_response = api_instance.iam_backoffice_generate_secret_for_qr(body)
        print("The response of IamBackofficeApi->iam_backoffice_generate_secret_for_qr:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IamBackofficeApi->iam_backoffice_generate_secret_for_qr: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **object**|  | 

### Return type

[**IambackofficeGenerateSecretForQRResponse**](IambackofficeGenerateSecretForQRResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **iam_backoffice_get_user**
> IambackofficeGetUserResponse iam_backoffice_get_user(body)

USER

### Example


```python
import iambackoffice
from iambackoffice.models.iambackoffice_get_user_request import IambackofficeGetUserRequest
from iambackoffice.models.iambackoffice_get_user_response import IambackofficeGetUserResponse
from iambackoffice.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://iambackoffice.api.gogemini.io
# See configuration.py for a list of all supported configuration parameters.
configuration = iambackoffice.Configuration(
    host = "https://iambackoffice.api.gogemini.io"
)


# Enter a context with an instance of the API client
with iambackoffice.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = iambackoffice.IamBackofficeApi(api_client)
    body = iambackoffice.IambackofficeGetUserRequest() # IambackofficeGetUserRequest | 

    try:
        # USER
        api_response = api_instance.iam_backoffice_get_user(body)
        print("The response of IamBackofficeApi->iam_backoffice_get_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IamBackofficeApi->iam_backoffice_get_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**IambackofficeGetUserRequest**](IambackofficeGetUserRequest.md)|  | 

### Return type

[**IambackofficeGetUserResponse**](IambackofficeGetUserResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **iam_backoffice_login**
> IambackofficeLoginResponse iam_backoffice_login(body)

LOGIN

### Example


```python
import iambackoffice
from iambackoffice.models.iambackoffice_login_request import IambackofficeLoginRequest
from iambackoffice.models.iambackoffice_login_response import IambackofficeLoginResponse
from iambackoffice.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://iambackoffice.api.gogemini.io
# See configuration.py for a list of all supported configuration parameters.
configuration = iambackoffice.Configuration(
    host = "https://iambackoffice.api.gogemini.io"
)


# Enter a context with an instance of the API client
with iambackoffice.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = iambackoffice.IamBackofficeApi(api_client)
    body = iambackoffice.IambackofficeLoginRequest() # IambackofficeLoginRequest | 

    try:
        # LOGIN
        api_response = api_instance.iam_backoffice_login(body)
        print("The response of IamBackofficeApi->iam_backoffice_login:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IamBackofficeApi->iam_backoffice_login: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**IambackofficeLoginRequest**](IambackofficeLoginRequest.md)|  | 

### Return type

[**IambackofficeLoginResponse**](IambackofficeLoginResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **iam_backoffice_login_mfa**
> IambackofficeLoginResponse iam_backoffice_login_mfa(body)

LOGIN MFA

### Example


```python
import iambackoffice
from iambackoffice.models.iambackoffice_login_mfa_request import IambackofficeLoginMfaRequest
from iambackoffice.models.iambackoffice_login_response import IambackofficeLoginResponse
from iambackoffice.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://iambackoffice.api.gogemini.io
# See configuration.py for a list of all supported configuration parameters.
configuration = iambackoffice.Configuration(
    host = "https://iambackoffice.api.gogemini.io"
)


# Enter a context with an instance of the API client
with iambackoffice.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = iambackoffice.IamBackofficeApi(api_client)
    body = iambackoffice.IambackofficeLoginMfaRequest() # IambackofficeLoginMfaRequest | 

    try:
        # LOGIN MFA
        api_response = api_instance.iam_backoffice_login_mfa(body)
        print("The response of IamBackofficeApi->iam_backoffice_login_mfa:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IamBackofficeApi->iam_backoffice_login_mfa: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**IambackofficeLoginMfaRequest**](IambackofficeLoginMfaRequest.md)|  | 

### Return type

[**IambackofficeLoginResponse**](IambackofficeLoginResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **iam_backoffice_logout**
> IambackofficeLogoutResponse iam_backoffice_logout(body)



### Example


```python
import iambackoffice
from iambackoffice.models.iambackoffice_logout_request import IambackofficeLogoutRequest
from iambackoffice.models.iambackoffice_logout_response import IambackofficeLogoutResponse
from iambackoffice.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://iambackoffice.api.gogemini.io
# See configuration.py for a list of all supported configuration parameters.
configuration = iambackoffice.Configuration(
    host = "https://iambackoffice.api.gogemini.io"
)


# Enter a context with an instance of the API client
with iambackoffice.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = iambackoffice.IamBackofficeApi(api_client)
    body = iambackoffice.IambackofficeLogoutRequest() # IambackofficeLogoutRequest | 

    try:
        api_response = api_instance.iam_backoffice_logout(body)
        print("The response of IamBackofficeApi->iam_backoffice_logout:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IamBackofficeApi->iam_backoffice_logout: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**IambackofficeLogoutRequest**](IambackofficeLogoutRequest.md)|  | 

### Return type

[**IambackofficeLogoutResponse**](IambackofficeLogoutResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **iam_backoffice_register**
> IambackofficeRegistrationResponse iam_backoffice_register(body)

REGISTRATION

### Example


```python
import iambackoffice
from iambackoffice.models.iambackoffice_registration_request import IambackofficeRegistrationRequest
from iambackoffice.models.iambackoffice_registration_response import IambackofficeRegistrationResponse
from iambackoffice.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://iambackoffice.api.gogemini.io
# See configuration.py for a list of all supported configuration parameters.
configuration = iambackoffice.Configuration(
    host = "https://iambackoffice.api.gogemini.io"
)


# Enter a context with an instance of the API client
with iambackoffice.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = iambackoffice.IamBackofficeApi(api_client)
    body = iambackoffice.IambackofficeRegistrationRequest() # IambackofficeRegistrationRequest | 

    try:
        # REGISTRATION
        api_response = api_instance.iam_backoffice_register(body)
        print("The response of IamBackofficeApi->iam_backoffice_register:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IamBackofficeApi->iam_backoffice_register: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**IambackofficeRegistrationRequest**](IambackofficeRegistrationRequest.md)|  | 

### Return type

[**IambackofficeRegistrationResponse**](IambackofficeRegistrationResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **iam_backoffice_search_groups**
> IambackofficeSearchGroupsResponse iam_backoffice_search_groups(body)



### Example


```python
import iambackoffice
from iambackoffice.models.iambackoffice_search_groups_request import IambackofficeSearchGroupsRequest
from iambackoffice.models.iambackoffice_search_groups_response import IambackofficeSearchGroupsResponse
from iambackoffice.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://iambackoffice.api.gogemini.io
# See configuration.py for a list of all supported configuration parameters.
configuration = iambackoffice.Configuration(
    host = "https://iambackoffice.api.gogemini.io"
)


# Enter a context with an instance of the API client
with iambackoffice.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = iambackoffice.IamBackofficeApi(api_client)
    body = iambackoffice.IambackofficeSearchGroupsRequest() # IambackofficeSearchGroupsRequest | 

    try:
        api_response = api_instance.iam_backoffice_search_groups(body)
        print("The response of IamBackofficeApi->iam_backoffice_search_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IamBackofficeApi->iam_backoffice_search_groups: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**IambackofficeSearchGroupsRequest**](IambackofficeSearchGroupsRequest.md)|  | 

### Return type

[**IambackofficeSearchGroupsResponse**](IambackofficeSearchGroupsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **iam_backoffice_unassign_roles**
> IambackofficeUnassignRolesResponse iam_backoffice_unassign_roles(body)



### Example


```python
import iambackoffice
from iambackoffice.models.iambackoffice_unassign_roles_request import IambackofficeUnassignRolesRequest
from iambackoffice.models.iambackoffice_unassign_roles_response import IambackofficeUnassignRolesResponse
from iambackoffice.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://iambackoffice.api.gogemini.io
# See configuration.py for a list of all supported configuration parameters.
configuration = iambackoffice.Configuration(
    host = "https://iambackoffice.api.gogemini.io"
)


# Enter a context with an instance of the API client
with iambackoffice.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = iambackoffice.IamBackofficeApi(api_client)
    body = iambackoffice.IambackofficeUnassignRolesRequest() # IambackofficeUnassignRolesRequest | 

    try:
        api_response = api_instance.iam_backoffice_unassign_roles(body)
        print("The response of IamBackofficeApi->iam_backoffice_unassign_roles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IamBackofficeApi->iam_backoffice_unassign_roles: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**IambackofficeUnassignRolesRequest**](IambackofficeUnassignRolesRequest.md)|  | 

### Return type

[**IambackofficeUnassignRolesResponse**](IambackofficeUnassignRolesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

