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


class DomainCapabilities(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        DomainCapabilities - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'enabled': 'bool',
            'dhcp': 'bool',
            'metric': 'int',
            'auto_metric': 'bool',
            'supports_metric': 'bool',
            'ping_enabled': 'bool'
        }

        self.attribute_map = {
            'enabled': 'enabled',
            'dhcp': 'dhcp',
            'metric': 'metric',
            'auto_metric': 'autoMetric',
            'supports_metric': 'supportsMetric',
            'ping_enabled': 'pingEnabled'
        }

        self._enabled = None
        self._dhcp = None
        self._metric = None
        self._auto_metric = None
        self._supports_metric = None
        self._ping_enabled = None

    @property
    def enabled(self):
        """
        Gets the enabled of this DomainCapabilities.
        True if this address family on the interface is enabled.

        :return: The enabled of this DomainCapabilities.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """
        Sets the enabled of this DomainCapabilities.
        True if this address family on the interface is enabled.

        :param enabled: The enabled of this DomainCapabilities.
        :type: bool
        """
        
        self._enabled = enabled

    @property
    def dhcp(self):
        """
        Gets the dhcp of this DomainCapabilities.
        True if this address family on the interface is using DHCP.

        :return: The dhcp of this DomainCapabilities.
        :rtype: bool
        """
        return self._dhcp

    @dhcp.setter
    def dhcp(self, dhcp):
        """
        Sets the dhcp of this DomainCapabilities.
        True if this address family on the interface is using DHCP.

        :param dhcp: The dhcp of this DomainCapabilities.
        :type: bool
        """
        
        self._dhcp = dhcp

    @property
    def metric(self):
        """
        Gets the metric of this DomainCapabilities.
        The metric being used for the address family on this interface. Lower values will have a higher priority. If autoMetric is true, this value will be the automatically calculated metric. To set this value be sure autoMetric is false. If no value is returned, metric configuration is not supported on this Edge.

        :return: The metric of this DomainCapabilities.
        :rtype: int
        """
        return self._metric

    @metric.setter
    def metric(self, metric):
        """
        Sets the metric of this DomainCapabilities.
        The metric being used for the address family on this interface. Lower values will have a higher priority. If autoMetric is true, this value will be the automatically calculated metric. To set this value be sure autoMetric is false. If no value is returned, metric configuration is not supported on this Edge.

        :param metric: The metric of this DomainCapabilities.
        :type: int
        """
        
        self._metric = metric

    @property
    def auto_metric(self):
        """
        Gets the auto_metric of this DomainCapabilities.
        True if the metric is being calculated automatically for the address family on this interface.

        :return: The auto_metric of this DomainCapabilities.
        :rtype: bool
        """
        return self._auto_metric

    @auto_metric.setter
    def auto_metric(self, auto_metric):
        """
        Sets the auto_metric of this DomainCapabilities.
        True if the metric is being calculated automatically for the address family on this interface.

        :param auto_metric: The auto_metric of this DomainCapabilities.
        :type: bool
        """
        
        self._auto_metric = auto_metric

    @property
    def supports_metric(self):
        """
        Gets the supports_metric of this DomainCapabilities.
        True if metric configuration is supported.

        :return: The supports_metric of this DomainCapabilities.
        :rtype: bool
        """
        return self._supports_metric

    @supports_metric.setter
    def supports_metric(self, supports_metric):
        """
        Sets the supports_metric of this DomainCapabilities.
        True if metric configuration is supported.

        :param supports_metric: The supports_metric of this DomainCapabilities.
        :type: bool
        """
        
        self._supports_metric = supports_metric

    @property
    def ping_enabled(self):
        """
        Gets the ping_enabled of this DomainCapabilities.
        Set to true to enable this address family on this interface to respond to ping requests.

        :return: The ping_enabled of this DomainCapabilities.
        :rtype: bool
        """
        return self._ping_enabled

    @ping_enabled.setter
    def ping_enabled(self, ping_enabled):
        """
        Sets the ping_enabled of this DomainCapabilities.
        Set to true to enable this address family on this interface to respond to ping requests.

        :param ping_enabled: The ping_enabled of this DomainCapabilities.
        :type: bool
        """
        
        self._ping_enabled = ping_enabled

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
