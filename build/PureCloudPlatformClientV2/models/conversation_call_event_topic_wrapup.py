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


class ConversationCallEventTopicWrapup(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        ConversationCallEventTopicWrapup - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'code': 'str',
            'notes': 'str',
            'tags': 'list[str]',
            'duration_seconds': 'int',
            'end_time': 'datetime',
            'additional_properties': 'object'
        }

        self.attribute_map = {
            'code': 'code',
            'notes': 'notes',
            'tags': 'tags',
            'duration_seconds': 'durationSeconds',
            'end_time': 'endTime',
            'additional_properties': 'additionalProperties'
        }

        self._code = None
        self._notes = None
        self._tags = None
        self._duration_seconds = None
        self._end_time = None
        self._additional_properties = None

    @property
    def code(self):
        """
        Gets the code of this ConversationCallEventTopicWrapup.


        :return: The code of this ConversationCallEventTopicWrapup.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """
        Sets the code of this ConversationCallEventTopicWrapup.


        :param code: The code of this ConversationCallEventTopicWrapup.
        :type: str
        """
        
        self._code = code

    @property
    def notes(self):
        """
        Gets the notes of this ConversationCallEventTopicWrapup.


        :return: The notes of this ConversationCallEventTopicWrapup.
        :rtype: str
        """
        return self._notes

    @notes.setter
    def notes(self, notes):
        """
        Sets the notes of this ConversationCallEventTopicWrapup.


        :param notes: The notes of this ConversationCallEventTopicWrapup.
        :type: str
        """
        
        self._notes = notes

    @property
    def tags(self):
        """
        Gets the tags of this ConversationCallEventTopicWrapup.


        :return: The tags of this ConversationCallEventTopicWrapup.
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """
        Sets the tags of this ConversationCallEventTopicWrapup.


        :param tags: The tags of this ConversationCallEventTopicWrapup.
        :type: list[str]
        """
        
        self._tags = tags

    @property
    def duration_seconds(self):
        """
        Gets the duration_seconds of this ConversationCallEventTopicWrapup.


        :return: The duration_seconds of this ConversationCallEventTopicWrapup.
        :rtype: int
        """
        return self._duration_seconds

    @duration_seconds.setter
    def duration_seconds(self, duration_seconds):
        """
        Sets the duration_seconds of this ConversationCallEventTopicWrapup.


        :param duration_seconds: The duration_seconds of this ConversationCallEventTopicWrapup.
        :type: int
        """
        
        self._duration_seconds = duration_seconds

    @property
    def end_time(self):
        """
        Gets the end_time of this ConversationCallEventTopicWrapup.


        :return: The end_time of this ConversationCallEventTopicWrapup.
        :rtype: datetime
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """
        Sets the end_time of this ConversationCallEventTopicWrapup.


        :param end_time: The end_time of this ConversationCallEventTopicWrapup.
        :type: datetime
        """
        
        self._end_time = end_time

    @property
    def additional_properties(self):
        """
        Gets the additional_properties of this ConversationCallEventTopicWrapup.


        :return: The additional_properties of this ConversationCallEventTopicWrapup.
        :rtype: object
        """
        return self._additional_properties

    @additional_properties.setter
    def additional_properties(self, additional_properties):
        """
        Sets the additional_properties of this ConversationCallEventTopicWrapup.


        :param additional_properties: The additional_properties of this ConversationCallEventTopicWrapup.
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

