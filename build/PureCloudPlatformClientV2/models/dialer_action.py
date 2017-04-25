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


class DialerAction(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        DialerAction - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'type': 'str',
            'action_type_name': 'str',
            'update_option': 'str',
            'properties': 'dict(str, str)'
        }

        self.attribute_map = {
            'type': 'type',
            'action_type_name': 'actionTypeName',
            'update_option': 'updateOption',
            'properties': 'properties'
        }

        self._type = None
        self._action_type_name = None
        self._update_option = None
        self._properties = None

    @property
    def type(self):
        """
        Gets the type of this DialerAction.
        Type of the action

        :return: The type of this DialerAction.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this DialerAction.
        Type of the action

        :param type: The type of this DialerAction.
        :type: str
        """
        allowed_values = ["Action", "modifyContactAttribute"]
        if type.lower() not in map(str.lower, allowed_values):
            # print "Invalid value for type -> " + type
            self._type = "outdated_sdk_version"
        else:
            self._type = type

    @property
    def action_type_name(self):
        """
        Gets the action_type_name of this DialerAction.
        Identifier of the action

        :return: The action_type_name of this DialerAction.
        :rtype: str
        """
        return self._action_type_name

    @action_type_name.setter
    def action_type_name(self, action_type_name):
        """
        Sets the action_type_name of this DialerAction.
        Identifier of the action

        :param action_type_name: The action_type_name of this DialerAction.
        :type: str
        """
        allowed_values = ["DO_NOT_DIAL", "MODIFY_CONTACT_ATTRIBUTE", "SWITCH_TO_PREVIEW", "APPEND_NUMBER_TO_DNC_LIST", "SCHEDULE_CALLBACK", "CONTACT_UNCALLABLE", "NUMBER_UNCALLABLE"]
        if action_type_name.lower() not in map(str.lower, allowed_values):
            # print "Invalid value for action_type_name -> " + action_type_name
            self._action_type_name = "outdated_sdk_version"
        else:
            self._action_type_name = action_type_name

    @property
    def update_option(self):
        """
        Gets the update_option of this DialerAction.
        Indicator of the type of update action (applicable only to certain types of actions)

        :return: The update_option of this DialerAction.
        :rtype: str
        """
        return self._update_option

    @update_option.setter
    def update_option(self, update_option):
        """
        Sets the update_option of this DialerAction.
        Indicator of the type of update action (applicable only to certain types of actions)

        :param update_option: The update_option of this DialerAction.
        :type: str
        """
        allowed_values = ["SET", "INCREMENT", "DECREMENT", "CURRENT_TIME"]
        if update_option.lower() not in map(str.lower, allowed_values):
            # print "Invalid value for update_option -> " + update_option
            self._update_option = "outdated_sdk_version"
        else:
            self._update_option = update_option

    @property
    def properties(self):
        """
        Gets the properties of this DialerAction.
        Map of key-value pairs pertinent to the action (different actions require different properties)

        :return: The properties of this DialerAction.
        :rtype: dict(str, str)
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """
        Sets the properties of this DialerAction.
        Map of key-value pairs pertinent to the action (different actions require different properties)

        :param properties: The properties of this DialerAction.
        :type: dict(str, str)
        """
        
        self._properties = properties

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

