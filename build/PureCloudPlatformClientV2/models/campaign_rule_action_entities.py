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


class CampaignRuleActionEntities(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        CampaignRuleActionEntities - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'campaigns': 'list[UriReference]',
            'sequences': 'list[UriReference]',
            'use_triggering_entity': 'bool'
        }

        self.attribute_map = {
            'campaigns': 'campaigns',
            'sequences': 'sequences',
            'use_triggering_entity': 'useTriggeringEntity'
        }

        self._campaigns = None
        self._sequences = None
        self._use_triggering_entity = None

    @property
    def campaigns(self):
        """
        Gets the campaigns of this CampaignRuleActionEntities.
        The list of campaigns for a CampaignRule to monitor. Required if the CampaignRule has any conditions that run on a campaign.

        :return: The campaigns of this CampaignRuleActionEntities.
        :rtype: list[UriReference]
        """
        return self._campaigns

    @campaigns.setter
    def campaigns(self, campaigns):
        """
        Sets the campaigns of this CampaignRuleActionEntities.
        The list of campaigns for a CampaignRule to monitor. Required if the CampaignRule has any conditions that run on a campaign.

        :param campaigns: The campaigns of this CampaignRuleActionEntities.
        :type: list[UriReference]
        """
        
        self._campaigns = campaigns

    @property
    def sequences(self):
        """
        Gets the sequences of this CampaignRuleActionEntities.
        The list of sequences for a CampaignRule to monitor. Required if the CampaignRule has any conditions that run on a sequence.

        :return: The sequences of this CampaignRuleActionEntities.
        :rtype: list[UriReference]
        """
        return self._sequences

    @sequences.setter
    def sequences(self, sequences):
        """
        Sets the sequences of this CampaignRuleActionEntities.
        The list of sequences for a CampaignRule to monitor. Required if the CampaignRule has any conditions that run on a sequence.

        :param sequences: The sequences of this CampaignRuleActionEntities.
        :type: list[UriReference]
        """
        
        self._sequences = sequences

    @property
    def use_triggering_entity(self):
        """
        Gets the use_triggering_entity of this CampaignRuleActionEntities.
        If true, the CampaignRuleAction will apply to the same entity that triggered the CampaignRuleCondition.

        :return: The use_triggering_entity of this CampaignRuleActionEntities.
        :rtype: bool
        """
        return self._use_triggering_entity

    @use_triggering_entity.setter
    def use_triggering_entity(self, use_triggering_entity):
        """
        Sets the use_triggering_entity of this CampaignRuleActionEntities.
        If true, the CampaignRuleAction will apply to the same entity that triggered the CampaignRuleCondition.

        :param use_triggering_entity: The use_triggering_entity of this CampaignRuleActionEntities.
        :type: bool
        """
        
        self._use_triggering_entity = use_triggering_entity

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

