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


class CampaignRuleNotificationCampaignRuleConditions(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        CampaignRuleNotificationCampaignRuleConditions - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'parameters': 'dict(str, str)',
            'condition_type': 'str',
            'additional_properties': 'object'
        }

        self.attribute_map = {
            'id': 'id',
            'parameters': 'parameters',
            'condition_type': 'conditionType',
            'additional_properties': 'additionalProperties'
        }

        self._id = None
        self._parameters = None
        self._condition_type = None
        self._additional_properties = None

    @property
    def id(self):
        """
        Gets the id of this CampaignRuleNotificationCampaignRuleConditions.


        :return: The id of this CampaignRuleNotificationCampaignRuleConditions.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this CampaignRuleNotificationCampaignRuleConditions.


        :param id: The id of this CampaignRuleNotificationCampaignRuleConditions.
        :type: str
        """
        
        self._id = id

    @property
    def parameters(self):
        """
        Gets the parameters of this CampaignRuleNotificationCampaignRuleConditions.


        :return: The parameters of this CampaignRuleNotificationCampaignRuleConditions.
        :rtype: dict(str, str)
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """
        Sets the parameters of this CampaignRuleNotificationCampaignRuleConditions.


        :param parameters: The parameters of this CampaignRuleNotificationCampaignRuleConditions.
        :type: dict(str, str)
        """
        
        self._parameters = parameters

    @property
    def condition_type(self):
        """
        Gets the condition_type of this CampaignRuleNotificationCampaignRuleConditions.


        :return: The condition_type of this CampaignRuleNotificationCampaignRuleConditions.
        :rtype: str
        """
        return self._condition_type

    @condition_type.setter
    def condition_type(self, condition_type):
        """
        Sets the condition_type of this CampaignRuleNotificationCampaignRuleConditions.


        :param condition_type: The condition_type of this CampaignRuleNotificationCampaignRuleConditions.
        :type: str
        """
        allowed_values = ["CAMPAIGN_PROGRESS", "CAMPAIGN_AGENTS"]
        if condition_type.lower() not in map(str.lower, allowed_values):
            # print "Invalid value for condition_type -> " + condition_type
            self._condition_type = "outdated_sdk_version"
        else:
            self._condition_type = condition_type

    @property
    def additional_properties(self):
        """
        Gets the additional_properties of this CampaignRuleNotificationCampaignRuleConditions.


        :return: The additional_properties of this CampaignRuleNotificationCampaignRuleConditions.
        :rtype: object
        """
        return self._additional_properties

    @additional_properties.setter
    def additional_properties(self, additional_properties):
        """
        Sets the additional_properties of this CampaignRuleNotificationCampaignRuleConditions.


        :param additional_properties: The additional_properties of this CampaignRuleNotificationCampaignRuleConditions.
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

