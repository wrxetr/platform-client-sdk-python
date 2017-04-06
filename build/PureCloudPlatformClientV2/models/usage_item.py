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


class UsageItem(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        UsageItem - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'type': 'str',
            'total_document_byte_count': 'int',
            'total_document_count': 'int'
        }

        self.attribute_map = {
            'type': 'type',
            'total_document_byte_count': 'totalDocumentByteCount',
            'total_document_count': 'totalDocumentCount'
        }

        self._type = None
        self._total_document_byte_count = None
        self._total_document_count = None

    @property
    def type(self):
        """
        Gets the type of this UsageItem.


        :return: The type of this UsageItem.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this UsageItem.


        :param type: The type of this UsageItem.
        :type: str
        """
        allowed_values = ["RECORDING", "FAX", "DOCUMENT", "ALL"]
        if type.lower() not in map(str.lower, allowed_values):
            # print "Invalid value for type -> " + type
            self._type = "outdated_sdk_version"
        else:
            self._type = type.lower()

    @property
    def total_document_byte_count(self):
        """
        Gets the total_document_byte_count of this UsageItem.


        :return: The total_document_byte_count of this UsageItem.
        :rtype: int
        """
        return self._total_document_byte_count

    @total_document_byte_count.setter
    def total_document_byte_count(self, total_document_byte_count):
        """
        Sets the total_document_byte_count of this UsageItem.


        :param total_document_byte_count: The total_document_byte_count of this UsageItem.
        :type: int
        """
        
        self._total_document_byte_count = total_document_byte_count

    @property
    def total_document_count(self):
        """
        Gets the total_document_count of this UsageItem.


        :return: The total_document_count of this UsageItem.
        :rtype: int
        """
        return self._total_document_count

    @total_document_count.setter
    def total_document_count(self, total_document_count):
        """
        Sets the total_document_count of this UsageItem.


        :param total_document_count: The total_document_count of this UsageItem.
        :type: int
        """
        
        self._total_document_count = total_document_count

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

