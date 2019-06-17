# coding: utf-8

"""
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

    Ref: https://github.com/swagger-api/swagger-codegen
"""

from pprint import pformat
from six import iteritems
import re


class CreateWebChatMessageRequest(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        CreateWebChatMessageRequest - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'body': 'str',
            'body_type': 'str'
        }

        self.attribute_map = {
            'body': 'body',
            'body_type': 'bodyType'
        }

        self._body = None
        self._body_type = None

    @property
    def body(self):
        """
        Gets the body of this CreateWebChatMessageRequest.
        The message body. Note that message bodies are limited to 4,000 characters.

        :return: The body of this CreateWebChatMessageRequest.
        :rtype: str
        """
        return self._body

    @body.setter
    def body(self, body):
        """
        Sets the body of this CreateWebChatMessageRequest.
        The message body. Note that message bodies are limited to 4,000 characters.

        :param body: The body of this CreateWebChatMessageRequest.
        :type: str
        """
        
        self._body = body

    @property
    def body_type(self):
        """
        Gets the body_type of this CreateWebChatMessageRequest.
        The purpose of the message within the conversation, such as a standard text entry versus a greeting.

        :return: The body_type of this CreateWebChatMessageRequest.
        :rtype: str
        """
        return self._body_type

    @body_type.setter
    def body_type(self, body_type):
        """
        Sets the body_type of this CreateWebChatMessageRequest.
        The purpose of the message within the conversation, such as a standard text entry versus a greeting.

        :param body_type: The body_type of this CreateWebChatMessageRequest.
        :type: str
        """
        allowed_values = ["standard", "notice", "member-join", "member-leave", "media-request"]
        if body_type.lower() not in map(str.lower, allowed_values):
            # print "Invalid value for body_type -> " + body_type
            self._body_type = "outdated_sdk_version"
        else:
            self._body_type = body_type

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

