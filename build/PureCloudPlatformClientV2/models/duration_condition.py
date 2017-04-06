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


class DurationCondition(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        DurationCondition - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'duration_target': 'str',
            'duration_operator': 'str',
            'duration_range': 'str'
        }

        self.attribute_map = {
            'duration_target': 'durationTarget',
            'duration_operator': 'durationOperator',
            'duration_range': 'durationRange'
        }

        self._duration_target = None
        self._duration_operator = None
        self._duration_range = None

    @property
    def duration_target(self):
        """
        Gets the duration_target of this DurationCondition.


        :return: The duration_target of this DurationCondition.
        :rtype: str
        """
        return self._duration_target

    @duration_target.setter
    def duration_target(self, duration_target):
        """
        Sets the duration_target of this DurationCondition.


        :param duration_target: The duration_target of this DurationCondition.
        :type: str
        """
        allowed_values = ["DURATION", "DURATION_RANGE"]
        if duration_target.lower() not in map(str.lower, allowed_values):
            # print "Invalid value for duration_target -> " + duration_target
            self._duration_target = "outdated_sdk_version"
        else:
            self._duration_target = duration_target.lower()

    @property
    def duration_operator(self):
        """
        Gets the duration_operator of this DurationCondition.


        :return: The duration_operator of this DurationCondition.
        :rtype: str
        """
        return self._duration_operator

    @duration_operator.setter
    def duration_operator(self, duration_operator):
        """
        Sets the duration_operator of this DurationCondition.


        :param duration_operator: The duration_operator of this DurationCondition.
        :type: str
        """
        
        self._duration_operator = duration_operator

    @property
    def duration_range(self):
        """
        Gets the duration_range of this DurationCondition.


        :return: The duration_range of this DurationCondition.
        :rtype: str
        """
        return self._duration_range

    @duration_range.setter
    def duration_range(self, duration_range):
        """
        Sets the duration_range of this DurationCondition.


        :param duration_range: The duration_range of this DurationCondition.
        :type: str
        """
        
        self._duration_range = duration_range

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

