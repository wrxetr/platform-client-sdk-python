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


class TrunkMetrics(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        TrunkMetrics - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'event_time': 'datetime',
            'logical_interface': 'UriReference',
            'trunk': 'UriReference',
            'calls': 'TrunkMetricsCalls',
            'qos': 'TrunkMetricsQoS'
        }

        self.attribute_map = {
            'event_time': 'eventTime',
            'logical_interface': 'logicalInterface',
            'trunk': 'trunk',
            'calls': 'calls',
            'qos': 'qos'
        }

        self._event_time = None
        self._logical_interface = None
        self._trunk = None
        self._calls = None
        self._qos = None

    @property
    def event_time(self):
        """
        Gets the event_time of this TrunkMetrics.
        Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ

        :return: The event_time of this TrunkMetrics.
        :rtype: datetime
        """
        return self._event_time

    @event_time.setter
    def event_time(self, event_time):
        """
        Sets the event_time of this TrunkMetrics.
        Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ

        :param event_time: The event_time of this TrunkMetrics.
        :type: datetime
        """
        
        self._event_time = event_time

    @property
    def logical_interface(self):
        """
        Gets the logical_interface of this TrunkMetrics.


        :return: The logical_interface of this TrunkMetrics.
        :rtype: UriReference
        """
        return self._logical_interface

    @logical_interface.setter
    def logical_interface(self, logical_interface):
        """
        Sets the logical_interface of this TrunkMetrics.


        :param logical_interface: The logical_interface of this TrunkMetrics.
        :type: UriReference
        """
        
        self._logical_interface = logical_interface

    @property
    def trunk(self):
        """
        Gets the trunk of this TrunkMetrics.


        :return: The trunk of this TrunkMetrics.
        :rtype: UriReference
        """
        return self._trunk

    @trunk.setter
    def trunk(self, trunk):
        """
        Sets the trunk of this TrunkMetrics.


        :param trunk: The trunk of this TrunkMetrics.
        :type: UriReference
        """
        
        self._trunk = trunk

    @property
    def calls(self):
        """
        Gets the calls of this TrunkMetrics.


        :return: The calls of this TrunkMetrics.
        :rtype: TrunkMetricsCalls
        """
        return self._calls

    @calls.setter
    def calls(self, calls):
        """
        Sets the calls of this TrunkMetrics.


        :param calls: The calls of this TrunkMetrics.
        :type: TrunkMetricsCalls
        """
        
        self._calls = calls

    @property
    def qos(self):
        """
        Gets the qos of this TrunkMetrics.


        :return: The qos of this TrunkMetrics.
        :rtype: TrunkMetricsQoS
        """
        return self._qos

    @qos.setter
    def qos(self, qos):
        """
        Sets the qos of this TrunkMetrics.


        :param qos: The qos of this TrunkMetrics.
        :type: TrunkMetricsQoS
        """
        
        self._qos = qos

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

