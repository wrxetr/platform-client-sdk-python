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


class GroupContact(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        GroupContact - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'address': 'str',
            'display': 'str',
            'type': 'str',
            'media_type': 'str'
        }

        self.attribute_map = {
            'address': 'address',
            'display': 'display',
            'type': 'type',
            'media_type': 'mediaType'
        }

        self._address = None
        self._display = None
        self._type = None
        self._media_type = None

    @property
    def address(self):
        """
        Gets the address of this GroupContact.
        Phone number for this contact type

        :return: The address of this GroupContact.
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """
        Sets the address of this GroupContact.
        Phone number for this contact type

        :param address: The address of this GroupContact.
        :type: str
        """
        
        self._address = address

    @property
    def display(self):
        """
        Gets the display of this GroupContact.
        Formatted version of the address property

        :return: The display of this GroupContact.
        :rtype: str
        """
        return self._display

    @display.setter
    def display(self, display):
        """
        Sets the display of this GroupContact.
        Formatted version of the address property

        :param display: The display of this GroupContact.
        :type: str
        """
        
        self._display = display

    @property
    def type(self):
        """
        Gets the type of this GroupContact.
        Contact type of the address

        :return: The type of this GroupContact.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this GroupContact.
        Contact type of the address

        :param type: The type of this GroupContact.
        :type: str
        """
        allowed_values = ["GROUPRING", "GROUPPHONE"]
        if type.lower() not in map(str.lower, allowed_values):
            # print "Invalid value for type -> " + type
            self._type = "outdated_sdk_version"
        else:
            self._type = type

    @property
    def media_type(self):
        """
        Gets the media_type of this GroupContact.
        Media type of the address

        :return: The media_type of this GroupContact.
        :rtype: str
        """
        return self._media_type

    @media_type.setter
    def media_type(self, media_type):
        """
        Sets the media_type of this GroupContact.
        Media type of the address

        :param media_type: The media_type of this GroupContact.
        :type: str
        """
        allowed_values = ["PHONE"]
        if media_type.lower() not in map(str.lower, allowed_values):
            # print "Invalid value for media_type -> " + media_type
            self._media_type = "outdated_sdk_version"
        else:
            self._media_type = media_type

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

