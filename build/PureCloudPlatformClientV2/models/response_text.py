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


class ResponseText(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        ResponseText - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'content': 'str',
            'content_type': 'str'
        }

        self.attribute_map = {
            'content': 'content',
            'content_type': 'contentType'
        }

        self._content = None
        self._content_type = None

    @property
    def content(self):
        """
        Gets the content of this ResponseText.
        Response text content.

        :return: The content of this ResponseText.
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        """
        Sets the content of this ResponseText.
        Response text content.

        :param content: The content of this ResponseText.
        :type: str
        """
        
        self._content = content

    @property
    def content_type(self):
        """
        Gets the content_type of this ResponseText.
        Response text content type.

        :return: The content_type of this ResponseText.
        :rtype: str
        """
        return self._content_type

    @content_type.setter
    def content_type(self, content_type):
        """
        Sets the content_type of this ResponseText.
        Response text content type.

        :param content_type: The content_type of this ResponseText.
        :type: str
        """
        allowed_values = ["text/plain", "text/html"]
        if content_type.lower() not in map(str.lower, allowed_values):
            # print "Invalid value for content_type -> " + content_type
            self._content_type = "outdated_sdk_version"
        else:
            self._content_type = content_type.lower()

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

