---
title: LocationsApi
---

## PureCloudPlatformClientV2.LocationsApi

All URIs are relative to *https://api.mypurecloud.com*

|Method | Description|
|------------- | -------------|
|[**get_location**](LocationsApi.html#get_location) | Get Location by ID.|
|[**get_locations**](LocationsApi.html#get_locations) | Get a list of all locations.|
|[**get_locations_search**](LocationsApi.html#get_locations_search) | Search locations using the q64 value returned from a previous search|
|[**post_locations_search**](LocationsApi.html#post_locations_search) | Search locations|
{: class="table table-striped"}

<a name="get_location"></a>

## [**LocationDefinition**](LocationDefinition.html)get_location(location_id)

Get Location by ID.



Wraps GET /api/v2/locations/{locationId} 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.LocationsApi()
location_id = 'location_id_example' # str | Location ID

try:
    # Get Location by ID.
    api_response = api_instance.get_location(location_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling LocationsApi->get_location: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **location_id** | **str**| Location ID | |
{: class="table table-striped"}

### Return type

[**LocationDefinition**](LocationDefinition.html)

<a name="get_locations"></a>

## [**list[LocationDefinition]**](LocationDefinition.html)get_locations(page_size=page_size, page_number=page_number, sort_order=sort_order)

Get a list of all locations.



Wraps GET /api/v2/locations 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.LocationsApi()
page_size = 25 # int | Page size (optional) (default to 25)
page_number = 1 # int | Page number (optional) (default to 1)
sort_order = 'sort_order_example' # str | Sort order (optional)

try:
    # Get a list of all locations.
    api_response = api_instance.get_locations(page_size=page_size, page_number=page_number, sort_order=sort_order)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling LocationsApi->get_locations: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **page_size** | **int**| Page size | [optional] [default to 25]|
| **page_number** | **int**| Page number | [optional] [default to 1]|
| **sort_order** | **str**| Sort order | [optional] |
{: class="table table-striped"}

### Return type

[**list[LocationDefinition]**](LocationDefinition.html)

<a name="get_locations_search"></a>

## [**LocationsSearchResponse**](LocationsSearchResponse.html)get_locations_search(q64, expand=expand)

Search locations using the q64 value returned from a previous search



Wraps GET /api/v2/locations/search 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.LocationsApi()
q64 = 'q64_example' # str | q64
expand = ['expand_example'] # list[str] | expand (optional)

try:
    # Search locations using the q64 value returned from a previous search
    api_response = api_instance.get_locations_search(q64, expand=expand)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling LocationsApi->get_locations_search: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **q64** | **str**| q64 | |
| **expand** | [**list[str]**](str.html)| expand | [optional] |
{: class="table table-striped"}

### Return type

[**LocationsSearchResponse**](LocationsSearchResponse.html)

<a name="post_locations_search"></a>

## [**LocationsSearchResponse**](LocationsSearchResponse.html)post_locations_search(body)

Search locations



Wraps POST /api/v2/locations/search 

### Example

~~~python
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud Auth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.LocationsApi()
body = PureCloudPlatformClientV2.LocationSearchRequest() # LocationSearchRequest | Search request options

try:
    # Search locations
    api_response = api_instance.post_locations_search(body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling LocationsApi->post_locations_search: %s\n" % e
~~~

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**LocationSearchRequest**](LocationSearchRequest.html)| Search request options | |
{: class="table table-striped"}

### Return type

[**LocationsSearchResponse**](LocationsSearchResponse.html)
