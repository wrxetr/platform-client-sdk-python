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


class ContactSort(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        ContactSort - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'field_name': 'str',
            'direction': 'str',
            'numeric': 'bool'
        }

        self.attribute_map = {
            'field_name': 'fieldName',
            'direction': 'direction',
            'numeric': 'numeric'
        }

        self._field_name = None
        self._direction = None
        self._numeric = None

    @property
    def field_name(self):
        """
        Gets the field_name of this ContactSort.


        :return: The field_name of this ContactSort.
        :rtype: str
        """
        return self._field_name

    @field_name.setter
    def field_name(self, field_name):
        """
        Sets the field_name of this ContactSort.


        :param field_name: The field_name of this ContactSort.
        :type: str
        """
        
        self._field_name = field_name

    @property
    def direction(self):
        """
        Gets the direction of this ContactSort.
        The direction in which to sort contacts.

        :return: The direction of this ContactSort.
        :rtype: str
        """
        return self._direction

    @direction.setter
    def direction(self, direction):
        """
        Sets the direction of this ContactSort.
        The direction in which to sort contacts.

        :param direction: The direction of this ContactSort.
        :type: str
        """
        allowed_values = ["ASC", "DESC"]
        if direction.lower() not in map(str.lower, allowed_values):
            # print "Invalid value for direction -> " + direction
            self._direction = "outdated_sdk_version"
        else:
            self._direction = direction

    @property
    def numeric(self):
        """
        Gets the numeric of this ContactSort.
        Whether or not the column contains numeric data.

        :return: The numeric of this ContactSort.
        :rtype: bool
        """
        return self._numeric

    @numeric.setter
    def numeric(self, numeric):
        """
        Sets the numeric of this ContactSort.
        Whether or not the column contains numeric data.

        :param numeric: The numeric of this ContactSort.
        :type: bool
        """
        
        self._numeric = numeric

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

