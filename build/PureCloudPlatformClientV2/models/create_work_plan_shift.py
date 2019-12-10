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
import json

from ..utils import sanitize_for_serialization

class CreateWorkPlanShift(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        CreateWorkPlanShift - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'name': 'str',
            'days': 'SetWrapperDayOfWeek',
            'flexible_start_time': 'bool',
            'exact_start_time_minutes_from_midnight': 'int',
            'earliest_start_time_minutes_from_midnight': 'int',
            'latest_start_time_minutes_from_midnight': 'int',
            'constrain_stop_time': 'bool',
            'constrain_latest_stop_time': 'bool',
            'latest_stop_time_minutes_from_midnight': 'int',
            'start_increment_minutes': 'int',
            'flexible_paid_time': 'bool',
            'exact_paid_time_minutes': 'int',
            'minimum_paid_time_minutes': 'int',
            'maximum_paid_time_minutes': 'int',
            'constrain_contiguous_work_time': 'bool',
            'minimum_contiguous_work_time_minutes': 'int',
            'maximum_contiguous_work_time_minutes': 'int',
            'activities': 'list[CreateWorkPlanActivity]'
        }

        self.attribute_map = {
            'name': 'name',
            'days': 'days',
            'flexible_start_time': 'flexibleStartTime',
            'exact_start_time_minutes_from_midnight': 'exactStartTimeMinutesFromMidnight',
            'earliest_start_time_minutes_from_midnight': 'earliestStartTimeMinutesFromMidnight',
            'latest_start_time_minutes_from_midnight': 'latestStartTimeMinutesFromMidnight',
            'constrain_stop_time': 'constrainStopTime',
            'constrain_latest_stop_time': 'constrainLatestStopTime',
            'latest_stop_time_minutes_from_midnight': 'latestStopTimeMinutesFromMidnight',
            'start_increment_minutes': 'startIncrementMinutes',
            'flexible_paid_time': 'flexiblePaidTime',
            'exact_paid_time_minutes': 'exactPaidTimeMinutes',
            'minimum_paid_time_minutes': 'minimumPaidTimeMinutes',
            'maximum_paid_time_minutes': 'maximumPaidTimeMinutes',
            'constrain_contiguous_work_time': 'constrainContiguousWorkTime',
            'minimum_contiguous_work_time_minutes': 'minimumContiguousWorkTimeMinutes',
            'maximum_contiguous_work_time_minutes': 'maximumContiguousWorkTimeMinutes',
            'activities': 'activities'
        }

        self._name = None
        self._days = None
        self._flexible_start_time = None
        self._exact_start_time_minutes_from_midnight = None
        self._earliest_start_time_minutes_from_midnight = None
        self._latest_start_time_minutes_from_midnight = None
        self._constrain_stop_time = None
        self._constrain_latest_stop_time = None
        self._latest_stop_time_minutes_from_midnight = None
        self._start_increment_minutes = None
        self._flexible_paid_time = None
        self._exact_paid_time_minutes = None
        self._minimum_paid_time_minutes = None
        self._maximum_paid_time_minutes = None
        self._constrain_contiguous_work_time = None
        self._minimum_contiguous_work_time_minutes = None
        self._maximum_contiguous_work_time_minutes = None
        self._activities = None

    @property
    def name(self):
        """
        Gets the name of this CreateWorkPlanShift.
        Name of the shift

        :return: The name of this CreateWorkPlanShift.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this CreateWorkPlanShift.
        Name of the shift

        :param name: The name of this CreateWorkPlanShift.
        :type: str
        """
        
        self._name = name

    @property
    def days(self):
        """
        Gets the days of this CreateWorkPlanShift.
        Days of the week applicable for this shift

        :return: The days of this CreateWorkPlanShift.
        :rtype: SetWrapperDayOfWeek
        """
        return self._days

    @days.setter
    def days(self, days):
        """
        Sets the days of this CreateWorkPlanShift.
        Days of the week applicable for this shift

        :param days: The days of this CreateWorkPlanShift.
        :type: SetWrapperDayOfWeek
        """
        
        self._days = days

    @property
    def flexible_start_time(self):
        """
        Gets the flexible_start_time of this CreateWorkPlanShift.
        Whether the start time of the shift is flexible

        :return: The flexible_start_time of this CreateWorkPlanShift.
        :rtype: bool
        """
        return self._flexible_start_time

    @flexible_start_time.setter
    def flexible_start_time(self, flexible_start_time):
        """
        Sets the flexible_start_time of this CreateWorkPlanShift.
        Whether the start time of the shift is flexible

        :param flexible_start_time: The flexible_start_time of this CreateWorkPlanShift.
        :type: bool
        """
        
        self._flexible_start_time = flexible_start_time

    @property
    def exact_start_time_minutes_from_midnight(self):
        """
        Gets the exact_start_time_minutes_from_midnight of this CreateWorkPlanShift.
        Exact start time of the shift defined as offset minutes from midnight. Used if flexibleStartTime == false

        :return: The exact_start_time_minutes_from_midnight of this CreateWorkPlanShift.
        :rtype: int
        """
        return self._exact_start_time_minutes_from_midnight

    @exact_start_time_minutes_from_midnight.setter
    def exact_start_time_minutes_from_midnight(self, exact_start_time_minutes_from_midnight):
        """
        Sets the exact_start_time_minutes_from_midnight of this CreateWorkPlanShift.
        Exact start time of the shift defined as offset minutes from midnight. Used if flexibleStartTime == false

        :param exact_start_time_minutes_from_midnight: The exact_start_time_minutes_from_midnight of this CreateWorkPlanShift.
        :type: int
        """
        
        self._exact_start_time_minutes_from_midnight = exact_start_time_minutes_from_midnight

    @property
    def earliest_start_time_minutes_from_midnight(self):
        """
        Gets the earliest_start_time_minutes_from_midnight of this CreateWorkPlanShift.
        Earliest start time of the shift defined as offset minutes from midnight. Used if flexibleStartTime == true

        :return: The earliest_start_time_minutes_from_midnight of this CreateWorkPlanShift.
        :rtype: int
        """
        return self._earliest_start_time_minutes_from_midnight

    @earliest_start_time_minutes_from_midnight.setter
    def earliest_start_time_minutes_from_midnight(self, earliest_start_time_minutes_from_midnight):
        """
        Sets the earliest_start_time_minutes_from_midnight of this CreateWorkPlanShift.
        Earliest start time of the shift defined as offset minutes from midnight. Used if flexibleStartTime == true

        :param earliest_start_time_minutes_from_midnight: The earliest_start_time_minutes_from_midnight of this CreateWorkPlanShift.
        :type: int
        """
        
        self._earliest_start_time_minutes_from_midnight = earliest_start_time_minutes_from_midnight

    @property
    def latest_start_time_minutes_from_midnight(self):
        """
        Gets the latest_start_time_minutes_from_midnight of this CreateWorkPlanShift.
        Latest start time of the shift defined as offset minutes from midnight. Used if flexibleStartTime == true

        :return: The latest_start_time_minutes_from_midnight of this CreateWorkPlanShift.
        :rtype: int
        """
        return self._latest_start_time_minutes_from_midnight

    @latest_start_time_minutes_from_midnight.setter
    def latest_start_time_minutes_from_midnight(self, latest_start_time_minutes_from_midnight):
        """
        Sets the latest_start_time_minutes_from_midnight of this CreateWorkPlanShift.
        Latest start time of the shift defined as offset minutes from midnight. Used if flexibleStartTime == true

        :param latest_start_time_minutes_from_midnight: The latest_start_time_minutes_from_midnight of this CreateWorkPlanShift.
        :type: int
        """
        
        self._latest_start_time_minutes_from_midnight = latest_start_time_minutes_from_midnight

    @property
    def constrain_stop_time(self):
        """
        Gets the constrain_stop_time of this CreateWorkPlanShift.
        Whether the latest stop time constraint for the shift is enabled

        :return: The constrain_stop_time of this CreateWorkPlanShift.
        :rtype: bool
        """
        return self._constrain_stop_time

    @constrain_stop_time.setter
    def constrain_stop_time(self, constrain_stop_time):
        """
        Sets the constrain_stop_time of this CreateWorkPlanShift.
        Whether the latest stop time constraint for the shift is enabled

        :param constrain_stop_time: The constrain_stop_time of this CreateWorkPlanShift.
        :type: bool
        """
        
        self._constrain_stop_time = constrain_stop_time

    @property
    def constrain_latest_stop_time(self):
        """
        Gets the constrain_latest_stop_time of this CreateWorkPlanShift.
        Whether the latest stop time constraint for the shift is enabled

        :return: The constrain_latest_stop_time of this CreateWorkPlanShift.
        :rtype: bool
        """
        return self._constrain_latest_stop_time

    @constrain_latest_stop_time.setter
    def constrain_latest_stop_time(self, constrain_latest_stop_time):
        """
        Sets the constrain_latest_stop_time of this CreateWorkPlanShift.
        Whether the latest stop time constraint for the shift is enabled

        :param constrain_latest_stop_time: The constrain_latest_stop_time of this CreateWorkPlanShift.
        :type: bool
        """
        
        self._constrain_latest_stop_time = constrain_latest_stop_time

    @property
    def latest_stop_time_minutes_from_midnight(self):
        """
        Gets the latest_stop_time_minutes_from_midnight of this CreateWorkPlanShift.
        Latest stop time of the shift defined as offset minutes from midnight. Used if constrainStopTime == true

        :return: The latest_stop_time_minutes_from_midnight of this CreateWorkPlanShift.
        :rtype: int
        """
        return self._latest_stop_time_minutes_from_midnight

    @latest_stop_time_minutes_from_midnight.setter
    def latest_stop_time_minutes_from_midnight(self, latest_stop_time_minutes_from_midnight):
        """
        Sets the latest_stop_time_minutes_from_midnight of this CreateWorkPlanShift.
        Latest stop time of the shift defined as offset minutes from midnight. Used if constrainStopTime == true

        :param latest_stop_time_minutes_from_midnight: The latest_stop_time_minutes_from_midnight of this CreateWorkPlanShift.
        :type: int
        """
        
        self._latest_stop_time_minutes_from_midnight = latest_stop_time_minutes_from_midnight

    @property
    def start_increment_minutes(self):
        """
        Gets the start_increment_minutes of this CreateWorkPlanShift.
        Increment in offset minutes that would contribute to different possible start times for the shift. Used if flexibleStartTime == true

        :return: The start_increment_minutes of this CreateWorkPlanShift.
        :rtype: int
        """
        return self._start_increment_minutes

    @start_increment_minutes.setter
    def start_increment_minutes(self, start_increment_minutes):
        """
        Sets the start_increment_minutes of this CreateWorkPlanShift.
        Increment in offset minutes that would contribute to different possible start times for the shift. Used if flexibleStartTime == true

        :param start_increment_minutes: The start_increment_minutes of this CreateWorkPlanShift.
        :type: int
        """
        
        self._start_increment_minutes = start_increment_minutes

    @property
    def flexible_paid_time(self):
        """
        Gets the flexible_paid_time of this CreateWorkPlanShift.
        Whether the paid time setting for the shift is flexible

        :return: The flexible_paid_time of this CreateWorkPlanShift.
        :rtype: bool
        """
        return self._flexible_paid_time

    @flexible_paid_time.setter
    def flexible_paid_time(self, flexible_paid_time):
        """
        Sets the flexible_paid_time of this CreateWorkPlanShift.
        Whether the paid time setting for the shift is flexible

        :param flexible_paid_time: The flexible_paid_time of this CreateWorkPlanShift.
        :type: bool
        """
        
        self._flexible_paid_time = flexible_paid_time

    @property
    def exact_paid_time_minutes(self):
        """
        Gets the exact_paid_time_minutes of this CreateWorkPlanShift.
        Exact paid time in minutes configured for the shift. Used if flexiblePaidTime == false

        :return: The exact_paid_time_minutes of this CreateWorkPlanShift.
        :rtype: int
        """
        return self._exact_paid_time_minutes

    @exact_paid_time_minutes.setter
    def exact_paid_time_minutes(self, exact_paid_time_minutes):
        """
        Sets the exact_paid_time_minutes of this CreateWorkPlanShift.
        Exact paid time in minutes configured for the shift. Used if flexiblePaidTime == false

        :param exact_paid_time_minutes: The exact_paid_time_minutes of this CreateWorkPlanShift.
        :type: int
        """
        
        self._exact_paid_time_minutes = exact_paid_time_minutes

    @property
    def minimum_paid_time_minutes(self):
        """
        Gets the minimum_paid_time_minutes of this CreateWorkPlanShift.
        Minimum paid time in minutes configured for the shift. Used if flexiblePaidTime == true

        :return: The minimum_paid_time_minutes of this CreateWorkPlanShift.
        :rtype: int
        """
        return self._minimum_paid_time_minutes

    @minimum_paid_time_minutes.setter
    def minimum_paid_time_minutes(self, minimum_paid_time_minutes):
        """
        Sets the minimum_paid_time_minutes of this CreateWorkPlanShift.
        Minimum paid time in minutes configured for the shift. Used if flexiblePaidTime == true

        :param minimum_paid_time_minutes: The minimum_paid_time_minutes of this CreateWorkPlanShift.
        :type: int
        """
        
        self._minimum_paid_time_minutes = minimum_paid_time_minutes

    @property
    def maximum_paid_time_minutes(self):
        """
        Gets the maximum_paid_time_minutes of this CreateWorkPlanShift.
        Maximum paid time in minutes configured for the shift. Used if flexiblePaidTime == true

        :return: The maximum_paid_time_minutes of this CreateWorkPlanShift.
        :rtype: int
        """
        return self._maximum_paid_time_minutes

    @maximum_paid_time_minutes.setter
    def maximum_paid_time_minutes(self, maximum_paid_time_minutes):
        """
        Sets the maximum_paid_time_minutes of this CreateWorkPlanShift.
        Maximum paid time in minutes configured for the shift. Used if flexiblePaidTime == true

        :param maximum_paid_time_minutes: The maximum_paid_time_minutes of this CreateWorkPlanShift.
        :type: int
        """
        
        self._maximum_paid_time_minutes = maximum_paid_time_minutes

    @property
    def constrain_contiguous_work_time(self):
        """
        Gets the constrain_contiguous_work_time of this CreateWorkPlanShift.
        Whether the contiguous time constraint for the shift is enabled

        :return: The constrain_contiguous_work_time of this CreateWorkPlanShift.
        :rtype: bool
        """
        return self._constrain_contiguous_work_time

    @constrain_contiguous_work_time.setter
    def constrain_contiguous_work_time(self, constrain_contiguous_work_time):
        """
        Sets the constrain_contiguous_work_time of this CreateWorkPlanShift.
        Whether the contiguous time constraint for the shift is enabled

        :param constrain_contiguous_work_time: The constrain_contiguous_work_time of this CreateWorkPlanShift.
        :type: bool
        """
        
        self._constrain_contiguous_work_time = constrain_contiguous_work_time

    @property
    def minimum_contiguous_work_time_minutes(self):
        """
        Gets the minimum_contiguous_work_time_minutes of this CreateWorkPlanShift.
        Minimum contiguous time in minutes configured for the shift. Used if constrainContiguousWorkTime == true

        :return: The minimum_contiguous_work_time_minutes of this CreateWorkPlanShift.
        :rtype: int
        """
        return self._minimum_contiguous_work_time_minutes

    @minimum_contiguous_work_time_minutes.setter
    def minimum_contiguous_work_time_minutes(self, minimum_contiguous_work_time_minutes):
        """
        Sets the minimum_contiguous_work_time_minutes of this CreateWorkPlanShift.
        Minimum contiguous time in minutes configured for the shift. Used if constrainContiguousWorkTime == true

        :param minimum_contiguous_work_time_minutes: The minimum_contiguous_work_time_minutes of this CreateWorkPlanShift.
        :type: int
        """
        
        self._minimum_contiguous_work_time_minutes = minimum_contiguous_work_time_minutes

    @property
    def maximum_contiguous_work_time_minutes(self):
        """
        Gets the maximum_contiguous_work_time_minutes of this CreateWorkPlanShift.
        Maximum contiguous time in minutes configured for the shift. Used if constrainContiguousWorkTime == true

        :return: The maximum_contiguous_work_time_minutes of this CreateWorkPlanShift.
        :rtype: int
        """
        return self._maximum_contiguous_work_time_minutes

    @maximum_contiguous_work_time_minutes.setter
    def maximum_contiguous_work_time_minutes(self, maximum_contiguous_work_time_minutes):
        """
        Sets the maximum_contiguous_work_time_minutes of this CreateWorkPlanShift.
        Maximum contiguous time in minutes configured for the shift. Used if constrainContiguousWorkTime == true

        :param maximum_contiguous_work_time_minutes: The maximum_contiguous_work_time_minutes of this CreateWorkPlanShift.
        :type: int
        """
        
        self._maximum_contiguous_work_time_minutes = maximum_contiguous_work_time_minutes

    @property
    def activities(self):
        """
        Gets the activities of this CreateWorkPlanShift.
        Activities configured for this shift

        :return: The activities of this CreateWorkPlanShift.
        :rtype: list[CreateWorkPlanActivity]
        """
        return self._activities

    @activities.setter
    def activities(self, activities):
        """
        Sets the activities of this CreateWorkPlanShift.
        Activities configured for this shift

        :param activities: The activities of this CreateWorkPlanShift.
        :type: list[CreateWorkPlanActivity]
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

    def to_json(self):
        """
        Returns the model as raw JSON
        """
        return json.dumps(sanitize_for_serialization(self.to_dict()))

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

