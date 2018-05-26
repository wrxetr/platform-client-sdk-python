# coding: utf-8

"""
NotificationsApi.py
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


class NotificationsApi(object):
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

    def delete_notifications_channel_subscriptions(self, channel_id, **kwargs):
        """
        Remove all subscriptions
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_notifications_channel_subscriptions(channel_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str channel_id: Channel ID (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['channel_id']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_notifications_channel_subscriptions" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'channel_id' is set
        if ('channel_id' not in params) or (params['channel_id'] is None):
            raise ValueError("Missing the required parameter `channel_id` when calling `delete_notifications_channel_subscriptions`")


        resource_path = '/api/v2/notifications/channels/{channelId}/subscriptions'.replace('{format}', 'json')
        path_params = {}
        if 'channel_id' in params:
            path_params['channelId'] = params['channel_id']

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

    def get_notifications_availabletopics(self, **kwargs):
        """
        Get available notification topics.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_notifications_availabletopics(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param list[str] expand: Which fields, if any, to expand
        :return: AvailableTopicEntityListing
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['expand']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_notifications_availabletopics" % key
                )
            params[key] = val
        del params['kwargs']



        resource_path = '/api/v2/notifications/availabletopics'.replace('{format}', 'json')
        path_params = {}

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
                                            response_type='AvailableTopicEntityListing',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_notifications_channel_subscriptions(self, channel_id, **kwargs):
        """
        The list of all subscriptions for this channel
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_notifications_channel_subscriptions(channel_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str channel_id: Channel ID (required)
        :return: ChannelTopicEntityListing
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['channel_id']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_notifications_channel_subscriptions" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'channel_id' is set
        if ('channel_id' not in params) or (params['channel_id'] is None):
            raise ValueError("Missing the required parameter `channel_id` when calling `get_notifications_channel_subscriptions`")


        resource_path = '/api/v2/notifications/channels/{channelId}/subscriptions'.replace('{format}', 'json')
        path_params = {}
        if 'channel_id' in params:
            path_params['channelId'] = params['channel_id']

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
                                            response_type='ChannelTopicEntityListing',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_notifications_channels(self, **kwargs):
        """
        The list of existing channels
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_notifications_channels(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str includechannels: Show user's channels for this specific token or across all tokens for this user and app.  Channel Ids for other access tokens will not be shown, but will be presented to show their existence.
        :return: ChannelEntityListing
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['includechannels']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_notifications_channels" % key
                )
            params[key] = val
        del params['kwargs']



        resource_path = '/api/v2/notifications/channels'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'includechannels' in params:
            query_params['includechannels'] = params['includechannels']

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
                                            response_type='ChannelEntityListing',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def post_notifications_channel_subscriptions(self, channel_id, body, **kwargs):
        """
        Add a list of subscriptions to the existing list of subscriptions
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_notifications_channel_subscriptions(channel_id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str channel_id: Channel ID (required)
        :param list[ChannelTopic] body: Body (required)
        :return: ChannelTopicEntityListing
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['channel_id', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_notifications_channel_subscriptions" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'channel_id' is set
        if ('channel_id' not in params) or (params['channel_id'] is None):
            raise ValueError("Missing the required parameter `channel_id` when calling `post_notifications_channel_subscriptions`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `post_notifications_channel_subscriptions`")


        resource_path = '/api/v2/notifications/channels/{channelId}/subscriptions'.replace('{format}', 'json')
        path_params = {}
        if 'channel_id' in params:
            path_params['channelId'] = params['channel_id']

        query_params = {}

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

        response = self.api_client.call_api(resource_path, 'POST',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='ChannelTopicEntityListing',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def post_notifications_channels(self, **kwargs):
        """
        Create a new channel
        There is a limit of 5 channels per user/app combination. Creating a 6th channel will remove the channel with oldest last used date.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_notifications_channels(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :return: Channel
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
                    " to method post_notifications_channels" % key
                )
            params[key] = val
        del params['kwargs']



        resource_path = '/api/v2/notifications/channels'.replace('{format}', 'json')
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

        response = self.api_client.call_api(resource_path, 'POST',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='Channel',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def put_notifications_channel_subscriptions(self, channel_id, body, **kwargs):
        """
        Replace the current list of subscriptions with a new list.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.put_notifications_channel_subscriptions(channel_id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str channel_id: Channel ID (required)
        :param list[ChannelTopic] body: Body (required)
        :return: ChannelTopicEntityListing
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['channel_id', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method put_notifications_channel_subscriptions" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'channel_id' is set
        if ('channel_id' not in params) or (params['channel_id'] is None):
            raise ValueError("Missing the required parameter `channel_id` when calling `put_notifications_channel_subscriptions`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `put_notifications_channel_subscriptions`")


        resource_path = '/api/v2/notifications/channels/{channelId}/subscriptions'.replace('{format}', 'json')
        path_params = {}
        if 'channel_id' in params:
            path_params['channelId'] = params['channel_id']

        query_params = {}

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
                                            response_type='ChannelTopicEntityListing',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response
