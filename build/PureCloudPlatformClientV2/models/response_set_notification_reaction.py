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


class ResponseSetNotificationReaction(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        ResponseSetNotificationReaction - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'data': 'str',
            'name': 'str',
            'reaction_type': 'str',
            'additional_properties': 'object'
        }

        self.attribute_map = {
            'data': 'data',
            'name': 'name',
            'reaction_type': 'reactionType',
            'additional_properties': 'additionalProperties'
        }

        self._data = None
        self._name = None
        self._reaction_type = None
        self._additional_properties = None

    @property
    def data(self):
        """
        Gets the data of this ResponseSetNotificationReaction.


        :return: The data of this ResponseSetNotificationReaction.
        :rtype: str
        """
        return self._data

    @data.setter
    def data(self, data):
        """
        Sets the data of this ResponseSetNotificationReaction.


        :param data: The data of this ResponseSetNotificationReaction.
        :type: str
        """
        
        self._data = data

    @property
    def name(self):
        """
        Gets the name of this ResponseSetNotificationReaction.


        :return: The name of this ResponseSetNotificationReaction.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this ResponseSetNotificationReaction.


        :param name: The name of this ResponseSetNotificationReaction.
        :type: str
        """
        
        self._name = name

    @property
    def reaction_type(self):
        """
        Gets the reaction_type of this ResponseSetNotificationReaction.


        :return: The reaction_type of this ResponseSetNotificationReaction.
        :rtype: str
        """
        return self._reaction_type

    @reaction_type.setter
    def reaction_type(self, reaction_type):
        """
        Sets the reaction_type of this ResponseSetNotificationReaction.


        :param reaction_type: The reaction_type of this ResponseSetNotificationReaction.
        :type: str
        """
        allowed_values = ["HANGUP", "TRANSFER", "TRANSFER_FLOW", "PLAY_FILE"]
        if reaction_type.lower() not in map(str.lower, allowed_values):
            # print "Invalid value for reaction_type -> " + reaction_type
            self._reaction_type = "outdated_sdk_version"
        else:
            self._reaction_type = reaction_type.lower()

    @property
    def additional_properties(self):
        """
        Gets the additional_properties of this ResponseSetNotificationReaction.


        :return: The additional_properties of this ResponseSetNotificationReaction.
        :rtype: object
        """
        return self._additional_properties

    @additional_properties.setter
    def additional_properties(self, additional_properties):
        """
        Sets the additional_properties of this ResponseSetNotificationReaction.


        :param additional_properties: The additional_properties of this ResponseSetNotificationReaction.
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

