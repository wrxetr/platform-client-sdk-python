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


class WfmForecastModificationAttributes(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        WfmForecastModificationAttributes - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'queues': 'list[QueueReference]',
            'media_types': 'list[str]',
            'languages': 'list[LanguageReference]',
            'skill_sets': 'list[list[RoutingSkillReference]]'
        }

        self.attribute_map = {
            'queues': 'queues',
            'media_types': 'mediaTypes',
            'languages': 'languages',
            'skill_sets': 'skillSets'
        }

        self._queues = None
        self._media_types = None
        self._languages = None
        self._skill_sets = None

    @property
    def queues(self):
        """
        Gets the queues of this WfmForecastModificationAttributes.
        The queues to which to apply a modification

        :return: The queues of this WfmForecastModificationAttributes.
        :rtype: list[QueueReference]
        """
        return self._queues

    @queues.setter
    def queues(self, queues):
        """
        Sets the queues of this WfmForecastModificationAttributes.
        The queues to which to apply a modification

        :param queues: The queues of this WfmForecastModificationAttributes.
        :type: list[QueueReference]
        """
        
        self._queues = queues

    @property
    def media_types(self):
        """
        Gets the media_types of this WfmForecastModificationAttributes.
        The media types to which to apply a modification

        :return: The media_types of this WfmForecastModificationAttributes.
        :rtype: list[str]
        """
        return self._media_types

    @media_types.setter
    def media_types(self, media_types):
        """
        Sets the media_types of this WfmForecastModificationAttributes.
        The media types to which to apply a modification

        :param media_types: The media_types of this WfmForecastModificationAttributes.
        :type: list[str]
        """
        
        self._media_types = media_types

    @property
    def languages(self):
        """
        Gets the languages of this WfmForecastModificationAttributes.
        The languages to which to apply a modification

        :return: The languages of this WfmForecastModificationAttributes.
        :rtype: list[LanguageReference]
        """
        return self._languages

    @languages.setter
    def languages(self, languages):
        """
        Sets the languages of this WfmForecastModificationAttributes.
        The languages to which to apply a modification

        :param languages: The languages of this WfmForecastModificationAttributes.
        :type: list[LanguageReference]
        """
        
        self._languages = languages

    @property
    def skill_sets(self):
        """
        Gets the skill_sets of this WfmForecastModificationAttributes.
        The skill sets to which to apply a modification

        :return: The skill_sets of this WfmForecastModificationAttributes.
        :rtype: list[list[RoutingSkillReference]]
        """
        return self._skill_sets

    @skill_sets.setter
    def skill_sets(self, skill_sets):
        """
        Sets the skill_sets of this WfmForecastModificationAttributes.
        The skill sets to which to apply a modification

        :param skill_sets: The skill_sets of this WfmForecastModificationAttributes.
        :type: list[list[RoutingSkillReference]]
        """
        
        self._skill_sets = skill_sets

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

