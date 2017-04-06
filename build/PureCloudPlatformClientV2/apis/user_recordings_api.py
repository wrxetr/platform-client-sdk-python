# coding: utf-8

"""
UserRecordingsApi.py
Copyright 2016 SmartBear Software

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
"""

from __future__ import absolute_import

import sys
import os
import re

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient


class UserRecordingsApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def delete_userrecording(self, recording_id, **kwargs):
        """
        Delete a user recording.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_userrecording(recording_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str recording_id: User Recording ID (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['recording_id']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_userrecording" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'recording_id' is set
        if ('recording_id' not in params) or (params['recording_id'] is None):
            raise ValueError("Missing the required parameter `recording_id` when calling `delete_userrecording`")


        resource_path = '/api/v2/userrecordings/{recordingId}'.replace('{format}', 'json')
        path_params = {}
        if 'recording_id' in params:
            path_params['recordingId'] = params['recording_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['PureCloud Auth']

        response = self.api_client.call_api(resource_path, 'DELETE',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type=None,
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_userrecording(self, recording_id, **kwargs):
        """
        Get a user recording.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_userrecording(recording_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str recording_id: User Recording ID (required)
        :param list[str] expand: Which fields, if any, to expand.
        :return: UserRecording
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['recording_id', 'expand']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_userrecording" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'recording_id' is set
        if ('recording_id' not in params) or (params['recording_id'] is None):
            raise ValueError("Missing the required parameter `recording_id` when calling `get_userrecording`")


        resource_path = '/api/v2/userrecordings/{recordingId}'.replace('{format}', 'json')
        path_params = {}
        if 'recording_id' in params:
            path_params['recordingId'] = params['recording_id']

        query_params = {}
        if 'expand' in params:
            query_params['expand'] = params['expand']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['PureCloud Auth']

        response = self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='UserRecording',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_userrecording_media(self, recording_id, **kwargs):
        """
        Download a user recording.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_userrecording_media(recording_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str recording_id: User Recording ID (required)
        :param str format_id: The desired media format.
        :return: DownloadResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['recording_id', 'format_id']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_userrecording_media" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'recording_id' is set
        if ('recording_id' not in params) or (params['recording_id'] is None):
            raise ValueError("Missing the required parameter `recording_id` when calling `get_userrecording_media`")


        resource_path = '/api/v2/userrecordings/{recordingId}/media'.replace('{format}', 'json')
        path_params = {}
        if 'recording_id' in params:
            path_params['recordingId'] = params['recording_id']

        query_params = {}
        if 'format_id' in params:
            query_params['formatId'] = params['format_id']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['PureCloud Auth']

        response = self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='DownloadResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_userrecordings(self, **kwargs):
        """
        Get a list of user recordings.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_userrecordings(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int page_size: Page size
        :param int page_number: Page number
        :param list[str] expand: Which fields, if any, to expand.
        :return: UserRecordingEntityListing
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['page_size', 'page_number', 'expand']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_userrecordings" % key
                )
            params[key] = val
        del params['kwargs']



        resource_path = '/api/v2/userrecordings'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'page_size' in params:
            query_params['pageSize'] = params['page_size']
        if 'page_number' in params:
            query_params['pageNumber'] = params['page_number']
        if 'expand' in params:
            query_params['expand'] = params['expand']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['PureCloud Auth']

        response = self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='UserRecordingEntityListing',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_userrecordings_summary(self, **kwargs):
        """
        Get user recording summary
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_userrecordings_summary(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :return: FaxSummary
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_userrecordings_summary" % key
                )
            params[key] = val
        del params['kwargs']



        resource_path = '/api/v2/userrecordings/summary'.replace('{format}', 'json')
        path_params = {}

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['PureCloud Auth']

        response = self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='FaxSummary',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def put_userrecording(self, recording_id, body, **kwargs):
        """
        Update a user recording.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.put_userrecording(recording_id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str recording_id: User Recording ID (required)
        :param UserRecording body: UserRecording (required)
        :param list[str] expand: Which fields, if any, to expand.
        :return: UserRecording
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['recording_id', 'body', 'expand']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method put_userrecording" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'recording_id' is set
        if ('recording_id' not in params) or (params['recording_id'] is None):
            raise ValueError("Missing the required parameter `recording_id` when calling `put_userrecording`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `put_userrecording`")


        resource_path = '/api/v2/userrecordings/{recordingId}'.replace('{format}', 'json')
        path_params = {}
        if 'recording_id' in params:
            path_params['recordingId'] = params['recording_id']

        query_params = {}
        if 'expand' in params:
            query_params['expand'] = params['expand']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['PureCloud Auth']

        response = self.api_client.call_api(resource_path, 'PUT',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='UserRecording',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response
