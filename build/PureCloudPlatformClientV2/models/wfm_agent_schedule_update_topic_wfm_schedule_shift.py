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


class WfmAgentScheduleUpdateTopicWfmScheduleShift(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        WfmAgentScheduleUpdateTopicWfmScheduleShift - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'week_date': 'str',
            'week_schedule_id': 'str',
            'id': 'str',
            'start_date': 'datetime',
            'length_in_minutes': 'int',
            'activities': 'list[WfmAgentScheduleUpdateTopicWfmScheduleActivity]'
        }

        self.attribute_map = {
            'week_date': 'weekDate',
            'week_schedule_id': 'weekScheduleId',
            'id': 'id',
            'start_date': 'startDate',
            'length_in_minutes': 'lengthInMinutes',
            'activities': 'activities'
        }

        self._week_date = None
        self._week_schedule_id = None
        self._id = None
        self._start_date = None
        self._length_in_minutes = None
        self._activities = None

    @property
    def week_date(self):
        """
        Gets the week_date of this WfmAgentScheduleUpdateTopicWfmScheduleShift.


        :return: The week_date of this WfmAgentScheduleUpdateTopicWfmScheduleShift.
        :rtype: str
        """
        return self._week_date

    @week_date.setter
    def week_date(self, week_date):
        """
        Sets the week_date of this WfmAgentScheduleUpdateTopicWfmScheduleShift.


        :param week_date: The week_date of this WfmAgentScheduleUpdateTopicWfmScheduleShift.
        :type: str
        """
        
        self._week_date = week_date

    @property
    def week_schedule_id(self):
        """
        Gets the week_schedule_id of this WfmAgentScheduleUpdateTopicWfmScheduleShift.


        :return: The week_schedule_id of this WfmAgentScheduleUpdateTopicWfmScheduleShift.
        :rtype: str
        """
        return self._week_schedule_id

    @week_schedule_id.setter
    def week_schedule_id(self, week_schedule_id):
        """
        Sets the week_schedule_id of this WfmAgentScheduleUpdateTopicWfmScheduleShift.


        :param week_schedule_id: The week_schedule_id of this WfmAgentScheduleUpdateTopicWfmScheduleShift.
        :type: str
        """
        
        self._week_schedule_id = week_schedule_id

    @property
    def id(self):
        """
        Gets the id of this WfmAgentScheduleUpdateTopicWfmScheduleShift.


        :return: The id of this WfmAgentScheduleUpdateTopicWfmScheduleShift.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this WfmAgentScheduleUpdateTopicWfmScheduleShift.


        :param id: The id of this WfmAgentScheduleUpdateTopicWfmScheduleShift.
        :type: str
        """
        
        self._id = id

    @property
    def start_date(self):
        """
        Gets the start_date of this WfmAgentScheduleUpdateTopicWfmScheduleShift.


        :return: The start_date of this WfmAgentScheduleUpdateTopicWfmScheduleShift.
        :rtype: datetime
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """
        Sets the start_date of this WfmAgentScheduleUpdateTopicWfmScheduleShift.


        :param start_date: The start_date of this WfmAgentScheduleUpdateTopicWfmScheduleShift.
        :type: datetime
        """
        
        self._start_date = start_date

    @property
    def length_in_minutes(self):
        """
        Gets the length_in_minutes of this WfmAgentScheduleUpdateTopicWfmScheduleShift.


        :return: The length_in_minutes of this WfmAgentScheduleUpdateTopicWfmScheduleShift.
        :rtype: int
        """
        return self._length_in_minutes

    @length_in_minutes.setter
    def length_in_minutes(self, length_in_minutes):
        """
        Sets the length_in_minutes of this WfmAgentScheduleUpdateTopicWfmScheduleShift.


        :param length_in_minutes: The length_in_minutes of this WfmAgentScheduleUpdateTopicWfmScheduleShift.
        :type: int
        """
        
        self._length_in_minutes = length_in_minutes

    @property
    def activities(self):
        """
        Gets the activities of this WfmAgentScheduleUpdateTopicWfmScheduleShift.


        :return: The activities of this WfmAgentScheduleUpdateTopicWfmScheduleShift.
        :rtype: list[WfmAgentScheduleUpdateTopicWfmScheduleActivity]
        """
        return self._activities

    @activities.setter
    def activities(self, activities):
        """
        Sets the activities of this WfmAgentScheduleUpdateTopicWfmScheduleShift.


        :param activities: The activities of this WfmAgentScheduleUpdateTopicWfmScheduleShift.
        :type: list[WfmAgentScheduleUpdateTopicWfmScheduleActivity]
        """
        
        self._activities = activities

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

