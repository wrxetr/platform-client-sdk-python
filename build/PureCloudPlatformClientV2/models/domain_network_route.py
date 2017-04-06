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


class DomainNetworkRoute(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        DomainNetworkRoute - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'prefix': 'str',
            'nexthop': 'str',
            'persistent': 'bool',
            'metric': 'int',
            'family': 'int'
        }

        self.attribute_map = {
            'prefix': 'prefix',
            'nexthop': 'nexthop',
            'persistent': 'persistent',
            'metric': 'metric',
            'family': 'family'
        }

        self._prefix = None
        self._nexthop = None
        self._persistent = None
        self._metric = None
        self._family = None

    @property
    def prefix(self):
        """
        Gets the prefix of this DomainNetworkRoute.
        The IPv4 or IPv6 route prefix in CIDR notation.

        :return: The prefix of this DomainNetworkRoute.
        :rtype: str
        """
        return self._prefix

    @prefix.setter
    def prefix(self, prefix):
        """
        Sets the prefix of this DomainNetworkRoute.
        The IPv4 or IPv6 route prefix in CIDR notation.

        :param prefix: The prefix of this DomainNetworkRoute.
        :type: str
        """
        
        self._prefix = prefix

    @property
    def nexthop(self):
        """
        Gets the nexthop of this DomainNetworkRoute.
        The IPv4 or IPv6 nexthop IP address.

        :return: The nexthop of this DomainNetworkRoute.
        :rtype: str
        """
        return self._nexthop

    @nexthop.setter
    def nexthop(self, nexthop):
        """
        Sets the nexthop of this DomainNetworkRoute.
        The IPv4 or IPv6 nexthop IP address.

        :param nexthop: The nexthop of this DomainNetworkRoute.
        :type: str
        """
        
        self._nexthop = nexthop

    @property
    def persistent(self):
        """
        Gets the persistent of this DomainNetworkRoute.
        True if this route will persist on Edge restart.  Routes assigned by DHCP will be returned as false.

        :return: The persistent of this DomainNetworkRoute.
        :rtype: bool
        """
        return self._persistent

    @persistent.setter
    def persistent(self, persistent):
        """
        Sets the persistent of this DomainNetworkRoute.
        True if this route will persist on Edge restart.  Routes assigned by DHCP will be returned as false.

        :param persistent: The persistent of this DomainNetworkRoute.
        :type: bool
        """
        
        self._persistent = persistent

    @property
    def metric(self):
        """
        Gets the metric of this DomainNetworkRoute.
        The metric being used for route. Lower values will have a higher priority.

        :return: The metric of this DomainNetworkRoute.
        :rtype: int
        """
        return self._metric

    @metric.setter
    def metric(self, metric):
        """
        Sets the metric of this DomainNetworkRoute.
        The metric being used for route. Lower values will have a higher priority.

        :param metric: The metric of this DomainNetworkRoute.
        :type: int
        """
        
        self._metric = metric

    @property
    def family(self):
        """
        Gets the family of this DomainNetworkRoute.
        The address family for this route.

        :return: The family of this DomainNetworkRoute.
        :rtype: int
        """
        return self._family

    @family.setter
    def family(self, family):
        """
        Sets the family of this DomainNetworkRoute.
        The address family for this route.

        :param family: The family of this DomainNetworkRoute.
        :type: int
        """
        allowed_values = ["2", "23"]
        if family.lower() not in map(str.lower, allowed_values):
            # print "Invalid value for family -> " + family
            self._family = "outdated_sdk_version"
        else:
            self._family = family.lower()

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

