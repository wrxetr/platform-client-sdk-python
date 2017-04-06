---
title: GroupsApi
---

## PureCloudPlatformClientV2.GroupsApi

All URIs are relative to *https://api.mypurecloud.com*

|Method | Description|
|------------- | -------------|
|[**delete_group**](GroupsApi.html#delete_group) | Delete group|
|[**delete_group_members**](GroupsApi.html#delete_group_members) | Remove members|
|[**get_fieldconfig**](GroupsApi.html#get_fieldconfig) | Fetch field config for an entity type|
|[**get_group**](GroupsApi.html#get_group) | Get group|
|[**get_group_members**](GroupsApi.html#get_group_members) | Get group members|
|[**get_groups**](GroupsApi.html#get_groups) | Get a group list|
|[**get_groups_search**](GroupsApi.html#get_groups_search) | Search groups using the q64 value returned from a previous search|
|[**post_group_members**](GroupsApi.html#post_group_members) | Add members|
|[**post_groups**](GroupsApi.html#post_groups) | Create a group|
|[**post_groups_search**](GroupsApi.html#post_groups_search) | Search groups|
|[**put_group**](GroupsApi.html#put_group) | Update group|
{: class="table table-striped"}

<a name="delete_group"></a>

## delete_group(group_id)

Delete group



Wraps DELETE /api/v2/groups/{groupId} 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.GroupsApi()
group_id = 'group_id_example' # str | Group ID

try:
    # Delete group
    api_instance.delete_group(group_id)
except ApiException as e:
    print "Exception when calling GroupsApi->delete_group: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **group_id** | **str**| Group ID | |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="delete_group_members"></a>

## [**Empty**](Empty.html)delete_group_members(group_id, ids)

Remove members



Wraps DELETE /api/v2/groups/{groupId}/members 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.GroupsApi()
group_id = 'group_id_example' # str | Group ID
ids = 'ids_example' # str | Comma separated list of userIds to remove

try:
    # Remove members
    api_response = api_instance.delete_group_members(group_id, ids)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling GroupsApi->delete_group_members: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **group_id** | **str**| Group ID | |
| **ids** | **str**| Comma separated list of userIds to remove | |
{: class="table table-striped"}

### Return type

[**Empty**](Empty.html)

<a name="get_fieldconfig"></a>

## [**FieldConfig**](FieldConfig.html)get_fieldconfig(type)

Fetch field config for an entity type



Wraps GET /api/v2/fieldconfig 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.GroupsApi()
type = 'type_example' # str | Field type

try:
    # Fetch field config for an entity type
    api_response = api_instance.get_fieldconfig(type)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling GroupsApi->get_fieldconfig: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **type** | **str**| Field type | |
{: class="table table-striped"}

### Return type

[**FieldConfig**](FieldConfig.html)

<a name="get_group"></a>

## [**Group**](Group.html)get_group(group_id)

Get group



Wraps GET /api/v2/groups/{groupId} 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.GroupsApi()
group_id = 'group_id_example' # str | Group ID

try:
    # Get group
    api_response = api_instance.get_group(group_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling GroupsApi->get_group: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **group_id** | **str**| Group ID | |
{: class="table table-striped"}

### Return type

[**Group**](Group.html)

<a name="get_group_members"></a>

## [**UserEntityListing**](UserEntityListing.html)get_group_members(group_id, page_size=page_size, page_number=page_number, sort_order=sort_order, expand=expand)

Get group members



Wraps GET /api/v2/groups/{groupId}/members 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.GroupsApi()
group_id = 'group_id_example' # str | Group ID
page_size = 25 # int | Page size (optional) (default to 25)
page_number = 1 # int | Page number (optional) (default to 1)
sort_order = 'ASC' # str | Ascending or descending sort order (optional) (default to ASC)
expand = ['expand_example'] # list[str] | Which fields, if any, to expand (optional)

try:
    # Get group members
    api_response = api_instance.get_group_members(group_id, page_size=page_size, page_number=page_number, sort_order=sort_order, expand=expand)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling GroupsApi->get_group_members: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **group_id** | **str**| Group ID | |
| **page_size** | **int**| Page size | [optional] [default to 25]|
| **page_number** | **int**| Page number | [optional] [default to 1]|
| **sort_order** | **str**| Ascending or descending sort order | [optional] [default to ASC]|
| **expand** | [**list[str]**](str.html)| Which fields, if any, to expand | [optional] |
{: class="table table-striped"}

### Return type

[**UserEntityListing**](UserEntityListing.html)

<a name="get_groups"></a>

## [**GroupEntityListing**](GroupEntityListing.html)get_groups(page_size=page_size, page_number=page_number, sort_order=sort_order)

Get a group list



Wraps GET /api/v2/groups 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.GroupsApi()
page_size = 25 # int | Page size (optional) (default to 25)
page_number = 1 # int | Page number (optional) (default to 1)
sort_order = 'ASC' # str | Ascending or descending sort order (optional) (default to ASC)

try:
    # Get a group list
    api_response = api_instance.get_groups(page_size=page_size, page_number=page_number, sort_order=sort_order)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling GroupsApi->get_groups: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **page_size** | **int**| Page size | [optional] [default to 25]|
| **page_number** | **int**| Page number | [optional] [default to 1]|
| **sort_order** | **str**| Ascending or descending sort order | [optional] [default to ASC]|
{: class="table table-striped"}

### Return type

[**GroupEntityListing**](GroupEntityListing.html)

<a name="get_groups_search"></a>

## [**GroupsSearchResponse**](GroupsSearchResponse.html)get_groups_search(q64, expand=expand)

Search groups using the q64 value returned from a previous search



Wraps GET /api/v2/groups/search 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.GroupsApi()
q64 = 'q64_example' # str | q64
expand = ['expand_example'] # list[str] | expand (optional)

try:
    # Search groups using the q64 value returned from a previous search
    api_response = api_instance.get_groups_search(q64, expand=expand)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling GroupsApi->get_groups_search: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **q64** | **str**| q64 | |
| **expand** | [**list[str]**](str.html)| expand | [optional] |
{: class="table table-striped"}

### Return type

[**GroupsSearchResponse**](GroupsSearchResponse.html)

<a name="post_group_members"></a>

## [**Empty**](Empty.html)post_group_members(group_id, body)

Add members



Wraps POST /api/v2/groups/{groupId}/members 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.GroupsApi()
group_id = 'group_id_example' # str | Group ID
body = PureCloudPlatformClientV2.GroupMembersUpdate() # GroupMembersUpdate | Add members

try:
    # Add members
    api_response = api_instance.post_group_members(group_id, body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling GroupsApi->post_group_members: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **group_id** | **str**| Group ID | |
| **body** | [**GroupMembersUpdate**](GroupMembersUpdate.html)| Add members | |
{: class="table table-striped"}

### Return type

[**Empty**](Empty.html)

<a name="post_groups"></a>

## [**Group**](Group.html)post_groups(body)

Create a group



Wraps POST /api/v2/groups 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.GroupsApi()
body = PureCloudPlatformClientV2.Group() # Group | Group

try:
    # Create a group
    api_response = api_instance.post_groups(body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling GroupsApi->post_groups: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**Group**](Group.html)| Group | |
{: class="table table-striped"}

### Return type

[**Group**](Group.html)

<a name="post_groups_search"></a>

## [**GroupsSearchResponse**](GroupsSearchResponse.html)post_groups_search(body)

Search groups



Wraps POST /api/v2/groups/search 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.GroupsApi()
body = PureCloudPlatformClientV2.GroupSearchRequest() # GroupSearchRequest | Search request options

try:
    # Search groups
    api_response = api_instance.post_groups_search(body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling GroupsApi->post_groups_search: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**GroupSearchRequest**](GroupSearchRequest.html)| Search request options | |
{: class="table table-striped"}

### Return type

[**GroupsSearchResponse**](GroupsSearchResponse.html)

<a name="put_group"></a>

## [**Group**](Group.html)put_group(group_id, body=body)

Update group



Wraps PUT /api/v2/groups/{groupId} 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.GroupsApi()
group_id = 'group_id_example' # str | Group ID
body = PureCloudPlatformClientV2.GroupUpdate() # GroupUpdate | Group (optional)

try:
    # Update group
    api_response = api_instance.put_group(group_id, body=body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling GroupsApi->put_group: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **group_id** | **str**| Group ID | |
| **body** | [**GroupUpdate**](GroupUpdate.html)| Group | [optional] |
{: class="table table-striped"}

### Return type

[**Group**](Group.html)
