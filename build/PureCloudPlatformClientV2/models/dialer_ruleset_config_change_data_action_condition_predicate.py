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


class DialerRulesetConfigChangeDataActionConditionPredicate(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        DialerRulesetConfigChangeDataActionConditionPredicate - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'output_field': 'str',
            'output_operator': 'str',
            'comparison_value': 'str',
            'additional_properties': 'object'
        }

        self.attribute_map = {
            'output_field': 'outputField',
            'output_operator': 'outputOperator',
            'comparison_value': 'comparisonValue',
            'additional_properties': 'additionalProperties'
        }

        self._output_field = None
        self._output_operator = None
        self._comparison_value = None
        self._additional_properties = None

    @property
    def output_field(self):
        """
        Gets the output_field of this DialerRulesetConfigChangeDataActionConditionPredicate.


        :return: The output_field of this DialerRulesetConfigChangeDataActionConditionPredicate.
        :rtype: str
        """
        return self._output_field

    @output_field.setter
    def output_field(self, output_field):
        """
        Sets the output_field of this DialerRulesetConfigChangeDataActionConditionPredicate.


        :param output_field: The output_field of this DialerRulesetConfigChangeDataActionConditionPredicate.
        :type: str
        """
        
        self._output_field = output_field

    @property
    def output_operator(self):
        """
        Gets the output_operator of this DialerRulesetConfigChangeDataActionConditionPredicate.


        :return: The output_operator of this DialerRulesetConfigChangeDataActionConditionPredicate.
        :rtype: str
        """
        return self._output_operator

    @output_operator.setter
    def output_operator(self, output_operator):
        """
        Sets the output_operator of this DialerRulesetConfigChangeDataActionConditionPredicate.


        :param output_operator: The output_operator of this DialerRulesetConfigChangeDataActionConditionPredicate.
        :type: str
        """
        allowed_values = ["EQUALS", "LESS_THAN", "LESS_THAN_EQUALS", "GREATER_THAN", "GREATER_THAN_EQUALS", "CONTAINS", "BEGINS_WITH", "ENDS_WITH", "BEFORE", "AFTER"]
        if output_operator.lower() not in map(str.lower, allowed_values):
            # print "Invalid value for output_operator -> " + output_operator
            self._output_operator = "outdated_sdk_version"
        else:
            self._output_operator = output_operator

    @property
    def comparison_value(self):
        """
        Gets the comparison_value of this DialerRulesetConfigChangeDataActionConditionPredicate.


        :return: The comparison_value of this DialerRulesetConfigChangeDataActionConditionPredicate.
        :rtype: str
        """
        return self._comparison_value

    @comparison_value.setter
    def comparison_value(self, comparison_value):
        """
        Sets the comparison_value of this DialerRulesetConfigChangeDataActionConditionPredicate.


        :param comparison_value: The comparison_value of this DialerRulesetConfigChangeDataActionConditionPredicate.
        :type: str
        """
        
        self._comparison_value = comparison_value

    @property
    def additional_properties(self):
        """
        Gets the additional_properties of this DialerRulesetConfigChangeDataActionConditionPredicate.


        :return: The additional_properties of this DialerRulesetConfigChangeDataActionConditionPredicate.
        :rtype: object
        """
        return self._additional_properties

    @additional_properties.setter
    def additional_properties(self, additional_properties):
        """
        Sets the additional_properties of this DialerRulesetConfigChangeDataActionConditionPredicate.


        :param additional_properties: The additional_properties of this DialerRulesetConfigChangeDataActionConditionPredicate.
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

