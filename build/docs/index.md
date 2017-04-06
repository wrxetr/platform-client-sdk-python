---
title: PureCloud API SDK - Python
---

[![PyPI version](https://badge.fury.io/py/PureCloudPlatformApiSdk.svg)](https://badge.fury.io/py/PureCloudPlatformApiSdk)

Documentation can be found at [https://developer.mypurecloud.com/api/rest/client-libraries/python/latest/](https://developer.mypurecloud.com/api/rest/client-libraries/python/latest/)

## Install Using pip

~~~
pip install PureCloudPlatformApiSdk
~~~

Package info can be found at [https://pypi.python.org/pypi/PureCloudPlatformApiSdk](https://pypi.python.org/pypi/PureCloudPlatformApiSdk)

## Using the Library

### Referencing the Library

Import the package in the python script:

~~~
import PureCloudPlatformApiSdk
~~~

### Authenticating

The Python SDK does not currently contain helper methods to complete an OAuth flow. The consuming applicaiton must complete an OAuth flow to get an access token outside the scope of the SDK. Once an access token is obtained, it should be set on the SDK via `PureCloudPlatformApiSdk.configuration.access_token`. For more information about authenticating with OAuth, see the Developer Center article [Authorization](https://developer.mypurecloud.com/api/rest/authorization/index.html).

~~~
PureCloudPlatformApiSdk.configuration.access_token = 'cuQbSAf1LU4CuIaSj1D6Gm399jmTr7zLTTc3KPSyCvEyJQIo9r648h3SH8oFzLPPKxE3Mvb166lq5NcjSBoGE5A'
~~~

### Setting the Environment

If connecting to a PureCloud environment other than mypurecloud.com (e.g. mypurecloud.ie), set the new base path before constructing any API classes. The new base path should be the base path to the Platform API for your environment.

~~~
PureCloudPlatformApiSdk.configuration.host = 'https://api.mypurecloud.ie'
~~~

### Making Requests

There are two steps to making requests:

1. Instantiate one of the API classes in the ININ.PureCloudApi.Api namespace
2. Call the methods on the API object

Example of getting the authenticated user's information:

~~~
usersApi = PureCloudPlatformApiSdk.UsersApi()
print usersApi.get_me()
~~~

## SDK Source Code Generation

The SDK is automatically regenerated and published from the API's definition after each API release. For more information on the build process, see the [platform-client-sdk-common](https://github.com/MyPureCloud/platform-client-sdk-common) project.