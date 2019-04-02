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


class CurrentUserScheduleRequestBody(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        CurrentUserScheduleRequestBody - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'start_date': 'datetime',
            'end_date': 'datetime',
            'load_full_weeks': 'bool'
        }

        self.attribute_map = {
            'start_date': 'startDate',
            'end_date': 'endDate',
            'load_full_weeks': 'loadFullWeeks'
        }

        self._start_date = None
        self._end_date = None
        self._load_full_weeks = None

    @property
    def start_date(self):
        """
        Gets the start_date of this CurrentUserScheduleRequestBody.
        Beginning of the range of schedules to fetch, in ISO-8601 format

        :return: The start_date of this CurrentUserScheduleRequestBody.
        :rtype: datetime
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """
        Sets the start_date of this CurrentUserScheduleRequestBody.
        Beginning of the range of schedules to fetch, in ISO-8601 format

        :param start_date: The start_date of this CurrentUserScheduleRequestBody.
        :type: datetime
        """
        
        self._start_date = start_date

    @property
    def end_date(self):
        """
        Gets the end_date of this CurrentUserScheduleRequestBody.
        End of the range of schedules to fetch, in ISO-8601 format

        :return: The end_date of this CurrentUserScheduleRequestBody.
        :rtype: datetime
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """
        Sets the end_date of this CurrentUserScheduleRequestBody.
        End of the range of schedules to fetch, in ISO-8601 format

        :param end_date: The end_date of this CurrentUserScheduleRequestBody.
        :type: datetime
        """
        
        self._end_date = end_date

    @property
    def load_full_weeks(self):
        """
        Gets the load_full_weeks of this CurrentUserScheduleRequestBody.
        Whether to load the full week's schedule (for the current user) of any week overlapping the start/end date query parameters, defaults to false

        :return: The load_full_weeks of this CurrentUserScheduleRequestBody.
        :rtype: bool
        """
        return self._load_full_weeks

    @load_full_weeks.setter
    def load_full_weeks(self, load_full_weeks):
        """
        Sets the load_full_weeks of this CurrentUserScheduleRequestBody.
        Whether to load the full week's schedule (for the current user) of any week overlapping the start/end date query parameters, defaults to false

        :param load_full_weeks: The load_full_weeks of this CurrentUserScheduleRequestBody.
        :type: bool
        """
        
        self._load_full_weeks = load_full_weeks

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

