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


class DomainNetworkAddress(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        DomainNetworkAddress - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'type': 'str',
            'address': 'str',
            'persistent': 'bool',
            'family': 'int'
        }

        self.attribute_map = {
            'type': 'type',
            'address': 'address',
            'persistent': 'persistent',
            'family': 'family'
        }

        self._type = None
        self._address = None
        self._persistent = None
        self._family = None

    @property
    def type(self):
        """
        Gets the type of this DomainNetworkAddress.
        The type of address.

        :return: The type of this DomainNetworkAddress.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this DomainNetworkAddress.
        The type of address.

        :param type: The type of this DomainNetworkAddress.
        :type: str
        """
        allowed_values = ["ip", "dns", "gateway", "tdm"]
        if type.lower() not in map(str.lower, allowed_values):
            # print "Invalid value for type -> " + type
            self._type = "outdated_sdk_version"
        else:
            self._type = type.lower()

    @property
    def address(self):
        """
        Gets the address of this DomainNetworkAddress.
        An IPv4 or IPv6 IP address. When specifying an address of type \"ip\", use CIDR format for the subnet mask.

        :return: The address of this DomainNetworkAddress.
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """
        Sets the address of this DomainNetworkAddress.
        An IPv4 or IPv6 IP address. When specifying an address of type \"ip\", use CIDR format for the subnet mask.

        :param address: The address of this DomainNetworkAddress.
        :type: str
        """
        
        self._address = address

    @property
    def persistent(self):
        """
        Gets the persistent of this DomainNetworkAddress.
        True if this address will persist on Edge restart.  Addresses assigned by DHCP will be returned as false.

        :return: The persistent of this DomainNetworkAddress.
        :rtype: bool
        """
        return self._persistent

    @persistent.setter
    def persistent(self, persistent):
        """
        Sets the persistent of this DomainNetworkAddress.
        True if this address will persist on Edge restart.  Addresses assigned by DHCP will be returned as false.

        :param persistent: The persistent of this DomainNetworkAddress.
        :type: bool
        """
        
        self._persistent = persistent

    @property
    def family(self):
        """
        Gets the family of this DomainNetworkAddress.
        The address family for this address.

        :return: The family of this DomainNetworkAddress.
        :rtype: int
        """
        return self._family

    @family.setter
    def family(self, family):
        """
        Sets the family of this DomainNetworkAddress.
        The address family for this address.

        :param family: The family of this DomainNetworkAddress.
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

