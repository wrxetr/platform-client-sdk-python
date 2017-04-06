---
title: PresenceApi
---

## PureCloudPlatformClientV2.PresenceApi

All URIs are relative to *https://api.mypurecloud.com*

|Method | Description|
|------------- | -------------|
|[**delete_presencedefinition**](PresenceApi.html#delete_presencedefinition) | Delete a Presence Definition|
|[**get_presencedefinition**](PresenceApi.html#get_presencedefinition) | Get a Presence Definition|
|[**get_presencedefinitions**](PresenceApi.html#get_presencedefinitions) | Get an Organization&#39;s list of Presence Definitions|
|[**get_systempresences**](PresenceApi.html#get_systempresences) | Get the list of SystemPresences|
|[**get_user_presence**](PresenceApi.html#get_user_presence) | Get a user&#39;s Presence|
|[**patch_user_presence**](PresenceApi.html#patch_user_presence) | Patch a user&#39;s Presence|
|[**post_presencedefinitions**](PresenceApi.html#post_presencedefinitions) | Create a Presence Definition|
|[**put_presencedefinition**](PresenceApi.html#put_presencedefinition) | Update a Presence Definition|
{: class="table table-striped"}

<a name="delete_presencedefinition"></a>

## delete_presencedefinition(presence_id)

Delete a Presence Definition



Wraps DELETE /api/v2/presencedefinitions/{presenceId} 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.PresenceApi()
presence_id = 'presence_id_example' # str | Organization Presence ID

try:
    # Delete a Presence Definition
    api_instance.delete_presencedefinition(presence_id)
except ApiException as e:
    print "Exception when calling PresenceApi->delete_presencedefinition: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **presence_id** | **str**| Organization Presence ID | |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="get_presencedefinition"></a>

## [**OrganizationPresence**](OrganizationPresence.html)get_presencedefinition(presence_id, locale_code=locale_code)

Get a Presence Definition



Wraps GET /api/v2/presencedefinitions/{presenceId} 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.PresenceApi()
presence_id = 'presence_id_example' # str | Organization Presence ID
locale_code = 'locale_code_example' # str | The locale code to fetch for the presence definition. Use ALL to fetch everything. (optional)

try:
    # Get a Presence Definition
    api_response = api_instance.get_presencedefinition(presence_id, locale_code=locale_code)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling PresenceApi->get_presencedefinition: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **presence_id** | **str**| Organization Presence ID | |
| **locale_code** | **str**| The locale code to fetch for the presence definition. Use ALL to fetch everything. | [optional] |
{: class="table table-striped"}

### Return type

[**OrganizationPresence**](OrganizationPresence.html)

<a name="get_presencedefinitions"></a>

## [**OrganizationPresenceEntityListing**](OrganizationPresenceEntityListing.html)get_presencedefinitions(page_number=page_number, page_size=page_size, deleted=deleted, locale_code=locale_code)

Get an Organization's list of Presence Definitions



Wraps GET /api/v2/presencedefinitions 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.PresenceApi()
page_number = 1 # int | Page number (optional) (default to 1)
page_size = 25 # int | Page size (optional) (default to 25)
deleted = 'false' # str | Deleted query can be TRUE, FALSE or ALL (optional) (default to false)
locale_code = 'locale_code_example' # str | The locale code to fetch for each presence definition. Use ALL to fetch everything. (optional)

try:
    # Get an Organization's list of Presence Definitions
    api_response = api_instance.get_presencedefinitions(page_number=page_number, page_size=page_size, deleted=deleted, locale_code=locale_code)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling PresenceApi->get_presencedefinitions: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **page_number** | **int**| Page number | [optional] [default to 1]|
| **page_size** | **int**| Page size | [optional] [default to 25]|
| **deleted** | **str**| Deleted query can be TRUE, FALSE or ALL | [optional] [default to false]|
| **locale_code** | **str**| The locale code to fetch for each presence definition. Use ALL to fetch everything. | [optional] |
{: class="table table-striped"}

### Return type

[**OrganizationPresenceEntityListing**](OrganizationPresenceEntityListing.html)

<a name="get_systempresences"></a>

## [**list[SystemPresence]**](SystemPresence.html)get_systempresences()

Get the list of SystemPresences



Wraps GET /api/v2/systempresences 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.PresenceApi()

try:
    # Get the list of SystemPresences
    api_response = api_instance.get_systempresences()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling PresenceApi->get_systempresences: %s\n" % e
~~~

### Parameters

This endpoint does not need any parameter.
{: class="table table-striped"}

### Return type

[**list[SystemPresence]**](SystemPresence.html)

<a name="get_user_presence"></a>

## [**UserPresence**](UserPresence.html)get_user_presence(user_id, source_id)

Get a user's Presence



Wraps GET /api/v2/users/{userId}/presences/{sourceId} 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.PresenceApi()
user_id = 'user_id_example' # str | user Id
source_id = 'source_id_example' # str | Source

try:
    # Get a user's Presence
    api_response = api_instance.get_user_presence(user_id, source_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling PresenceApi->get_user_presence: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **user_id** | **str**| user Id | |
| **source_id** | **str**| Source | |
{: class="table table-striped"}

### Return type

[**UserPresence**](UserPresence.html)

<a name="patch_user_presence"></a>

## [**UserPresence**](UserPresence.html)patch_user_presence(user_id, source_id, body)

Patch a user's Presence

The presence object can be patched one of three ways. Option 1: Set the 'primary' property to true. This will set the 'source' defined in the path as the user's primary presence source. Option 2: Provide the presenceDefinition value. The 'id' is the only value required within the presenceDefinition. Option 3: Provide the message value. Option 1 can be combined with Option 2 and/or Option 3.

Wraps PATCH /api/v2/users/{userId}/presences/{sourceId} 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.PresenceApi()
user_id = 'user_id_example' # str | user Id
source_id = 'source_id_example' # str | Source
body = PureCloudPlatformClientV2.UserPresence() # UserPresence | User presence

try:
    # Patch a user's Presence
    api_response = api_instance.patch_user_presence(user_id, source_id, body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling PresenceApi->patch_user_presence: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **user_id** | **str**| user Id | |
| **source_id** | **str**| Source | |
| **body** | [**UserPresence**](UserPresence.html)| User presence | |
{: class="table table-striped"}

### Return type

[**UserPresence**](UserPresence.html)

<a name="post_presencedefinitions"></a>

## [**OrganizationPresence**](OrganizationPresence.html)post_presencedefinitions(body)

Create a Presence Definition



Wraps POST /api/v2/presencedefinitions 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.PresenceApi()
body = PureCloudPlatformClientV2.OrganizationPresence() # OrganizationPresence | The Presence Definition to create

try:
    # Create a Presence Definition
    api_response = api_instance.post_presencedefinitions(body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling PresenceApi->post_presencedefinitions: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**OrganizationPresence**](OrganizationPresence.html)| The Presence Definition to create | |
{: class="table table-striped"}

### Return type

[**OrganizationPresence**](OrganizationPresence.html)

<a name="put_presencedefinition"></a>

## [**OrganizationPresence**](OrganizationPresence.html)put_presencedefinition(presence_id, body)

Update a Presence Definition



Wraps PUT /api/v2/presencedefinitions/{presenceId} 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.PresenceApi()
presence_id = 'presence_id_example' # str | Organization Presence ID
body = PureCloudPlatformClientV2.OrganizationPresence() # OrganizationPresence | The OrganizationPresence to update

try:
    # Update a Presence Definition
    api_response = api_instance.put_presencedefinition(presence_id, body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling PresenceApi->put_presencedefinition: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **presence_id** | **str**| Organization Presence ID | |
| **body** | [**OrganizationPresence**](OrganizationPresence.html)| The OrganizationPresence to update | |
{: class="table table-striped"}

### Return type

[**OrganizationPresence**](OrganizationPresence.html)
