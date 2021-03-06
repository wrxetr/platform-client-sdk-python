# coding: utf-8

"""
SpeechTextAnalyticsApi.py
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


class SpeechTextAnalyticsApi(object):
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

    def get_conversation_transcriptproperty(self, conversation_id, communication_id, **kwargs):
        """
        Get the pre-signed S3 URL for the transcript of a specific communication of a conversation
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_conversation_transcriptproperty(conversation_id, communication_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str conversation_id: Conversation ID (required)
        :param str communication_id: Communication ID (required)
        :return: TranscriptProperty
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['conversation_id', 'communication_id']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_conversation_transcriptproperty" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'conversation_id' is set
        if ('conversation_id' not in params) or (params['conversation_id'] is None):
            raise ValueError("Missing the required parameter `conversation_id` when calling `get_conversation_transcriptproperty`")
        # verify the required parameter 'communication_id' is set
        if ('communication_id' not in params) or (params['communication_id'] is None):
            raise ValueError("Missing the required parameter `communication_id` when calling `get_conversation_transcriptproperty`")


        resource_path = '/api/v2/conversations/{conversationId}/transcriptproperties/{communicationId}'.replace('{format}', 'json')
        path_params = {}
        if 'conversation_id' in params:
            path_params['conversationId'] = params['conversation_id']
        if 'communication_id' in params:
            path_params['communicationId'] = params['communication_id']

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
        auth_settings = ['PureCloud OAuth']

        response = self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='TranscriptProperty',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response
