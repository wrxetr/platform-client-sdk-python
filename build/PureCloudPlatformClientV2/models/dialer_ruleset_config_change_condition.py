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


class DialerRulesetConfigChangeCondition(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        DialerRulesetConfigChangeCondition - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'type': 'str',
            'inverted': 'bool',
            'attribute_name': 'str',
            'value': 'str',
            'value_type': 'str',
            'operator': 'str',
            'codes': 'list[str]',
            'property_type': 'str',
            'pcProperty': 'str',
            'additional_properties': 'object'
        }

        self.attribute_map = {
            'type': 'type',
            'inverted': 'inverted',
            'attribute_name': 'attributeName',
            'value': 'value',
            'value_type': 'valueType',
            'operator': 'operator',
            'codes': 'codes',
            'property_type': 'propertyType',
            'pcProperty': 'property',
            'additional_properties': 'additionalProperties'
        }

        self._type = None
        self._inverted = None
        self._attribute_name = None
        self._value = None
        self._value_type = None
        self._operator = None
        self._codes = None
        self._property_type = None
        self._pcProperty = None
        self._additional_properties = None

    @property
    def type(self):
        """
        Gets the type of this DialerRulesetConfigChangeCondition.


        :return: The type of this DialerRulesetConfigChangeCondition.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this DialerRulesetConfigChangeCondition.


        :param type: The type of this DialerRulesetConfigChangeCondition.
        :type: str
        """
        
        self._type = type

    @property
    def inverted(self):
        """
        Gets the inverted of this DialerRulesetConfigChangeCondition.


        :return: The inverted of this DialerRulesetConfigChangeCondition.
        :rtype: bool
        """
        return self._inverted

    @inverted.setter
    def inverted(self, inverted):
        """
        Sets the inverted of this DialerRulesetConfigChangeCondition.


        :param inverted: The inverted of this DialerRulesetConfigChangeCondition.
        :type: bool
        """
        
        self._inverted = inverted

    @property
    def attribute_name(self):
        """
        Gets the attribute_name of this DialerRulesetConfigChangeCondition.


        :return: The attribute_name of this DialerRulesetConfigChangeCondition.
        :rtype: str
        """
        return self._attribute_name

    @attribute_name.setter
    def attribute_name(self, attribute_name):
        """
        Sets the attribute_name of this DialerRulesetConfigChangeCondition.


        :param attribute_name: The attribute_name of this DialerRulesetConfigChangeCondition.
        :type: str
        """
        
        self._attribute_name = attribute_name

    @property
    def value(self):
        """
        Gets the value of this DialerRulesetConfigChangeCondition.


        :return: The value of this DialerRulesetConfigChangeCondition.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of this DialerRulesetConfigChangeCondition.


        :param value: The value of this DialerRulesetConfigChangeCondition.
        :type: str
        """
        
        self._value = value

    @property
    def value_type(self):
        """
        Gets the value_type of this DialerRulesetConfigChangeCondition.


        :return: The value_type of this DialerRulesetConfigChangeCondition.
        :rtype: str
        """
        return self._value_type

    @value_type.setter
    def value_type(self, value_type):
        """
        Sets the value_type of this DialerRulesetConfigChangeCondition.


        :param value_type: The value_type of this DialerRulesetConfigChangeCondition.
        :type: str
        """
        allowed_values = ["STRING", "NUMERIC", "DATETIME", "PERIOD"]
        if value_type.lower() not in map(str.lower, allowed_values):
            # print "Invalid value for value_type -> " + value_type
            self._value_type = "outdated_sdk_version"
        else:
            self._value_type = value_type

    @property
    def operator(self):
        """
        Gets the operator of this DialerRulesetConfigChangeCondition.


        :return: The operator of this DialerRulesetConfigChangeCondition.
        :rtype: str
        """
        return self._operator

    @operator.setter
    def operator(self, operator):
        """
        Sets the operator of this DialerRulesetConfigChangeCondition.


        :param operator: The operator of this DialerRulesetConfigChangeCondition.
        :type: str
        """
        allowed_values = ["EQUALS", "LESS_THAN", "LESS_THAN_EQUALS", "GREATER_THAN", "GREATER_THAN_EQUALS", "CONTAINS", "BEGINS_WITH", "ENDS_WITH", "BEFORE", "AFTER"]
        if operator.lower() not in map(str.lower, allowed_values):
            # print "Invalid value for operator -> " + operator
            self._operator = "outdated_sdk_version"
        else:
            self._operator = operator

    @property
    def codes(self):
        """
        Gets the codes of this DialerRulesetConfigChangeCondition.


        :return: The codes of this DialerRulesetConfigChangeCondition.
        :rtype: list[str]
        """
        return self._codes

    @codes.setter
    def codes(self, codes):
        """
        Sets the codes of this DialerRulesetConfigChangeCondition.


        :param codes: The codes of this DialerRulesetConfigChangeCondition.
        :type: list[str]
        """
        
        self._codes = codes

    @property
    def property_type(self):
        """
        Gets the property_type of this DialerRulesetConfigChangeCondition.


        :return: The property_type of this DialerRulesetConfigChangeCondition.
        :rtype: str
        """
        return self._property_type

    @property_type.setter
    def property_type(self, property_type):
        """
        Sets the property_type of this DialerRulesetConfigChangeCondition.


        :param property_type: The property_type of this DialerRulesetConfigChangeCondition.
        :type: str
        """
        allowed_values = ["LAST_ATTEMPT_BY_COLUMN", "LAST_ATTEMPT_OVERALL", "LAST_RESULT_BY_COLUMN", "LAST_RESULT_OVERALL"]
        if property_type.lower() not in map(str.lower, allowed_values):
            # print "Invalid value for property_type -> " + property_type
            self._property_type = "outdated_sdk_version"
        else:
            self._property_type = property_type

    @property
    def pcProperty(self):
        """
        Gets the pcProperty of this DialerRulesetConfigChangeCondition.


        :return: The pcProperty of this DialerRulesetConfigChangeCondition.
        :rtype: str
        """
        return self._pcProperty

    @pcProperty.setter
    def pcProperty(self, pcProperty):
        """
        Sets the pcProperty of this DialerRulesetConfigChangeCondition.


        :param pcProperty: The pcProperty of this DialerRulesetConfigChangeCondition.
        :type: str
        """
        
        self._pcProperty = pcProperty

    @property
    def additional_properties(self):
        """
        Gets the additional_properties of this DialerRulesetConfigChangeCondition.


        :return: The additional_properties of this DialerRulesetConfigChangeCondition.
        :rtype: object
        """
        return self._additional_properties

    @additional_properties.setter
    def additional_properties(self, additional_properties):
        """
        Sets the additional_properties of this DialerRulesetConfigChangeCondition.


        :param additional_properties: The additional_properties of this DialerRulesetConfigChangeCondition.
        :type: object
        """
        
        self._additional_properties = additional_properties

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
