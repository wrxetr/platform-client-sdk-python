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


class Filter(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        Filter - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'name': 'str',
            'type': 'str',
            'operator': 'str',
            'values': 'list[str]'
        }

        self.attribute_map = {
            'name': 'name',
            'type': 'type',
            'operator': 'operator',
            'values': 'values'
        }

        self._name = None
        self._type = None
        self._operator = None
        self._values = None

    @property
    def name(self):
        """
        Gets the name of this Filter.
        The name of the field by which to filter.

        :return: The name of this Filter.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Filter.
        The name of the field by which to filter.

        :param name: The name of this Filter.
        :type: str
        """
        
        self._name = name

    @property
    def type(self):
        """
        Gets the type of this Filter.
        The type of the filter, DATE or STRING.

        :return: The type of this Filter.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this Filter.
        The type of the filter, DATE or STRING.

        :param type: The type of this Filter.
        :type: str
        """
        
        self._type = type

    @property
    def operator(self):
        """
        Gets the operator of this Filter.
        The operation that the filter performs.

        :return: The operator of this Filter.
        :rtype: str
        """
        return self._operator

    @operator.setter
    def operator(self, operator):
        """
        Sets the operator of this Filter.
        The operation that the filter performs.

        :param operator: The operator of this Filter.
        :type: str
        """
        
        self._operator = operator

    @property
    def values(self):
        """
        Gets the values of this Filter.
        The values to make the filter comparison against.

        :return: The values of this Filter.
        :rtype: list[str]
        """
        return self._values

    @values.setter
    def values(self, values):
        """
        Sets the values of this Filter.
        The values to make the filter comparison against.

        :param values: The values of this Filter.
        :type: list[str]
        """
        
        self._values = values

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

