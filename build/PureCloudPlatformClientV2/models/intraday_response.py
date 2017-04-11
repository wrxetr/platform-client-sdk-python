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


class IntradayResponse(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        IntradayResponse - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'start_date': 'datetime',
            'end_date': 'datetime',
            'interval_length_minutes': 'int',
            'number_of_intervals': 'int',
            'metrics': 'list[IntradayMetric]',
            'no_data_reason': 'str',
            'queue_ids': 'list[str]',
            'intraday_data_groupings': 'list[IntradayDataGroup]'
        }

        self.attribute_map = {
            'start_date': 'startDate',
            'end_date': 'endDate',
            'interval_length_minutes': 'intervalLengthMinutes',
            'number_of_intervals': 'numberOfIntervals',
            'metrics': 'metrics',
            'no_data_reason': 'noDataReason',
            'queue_ids': 'queueIds',
            'intraday_data_groupings': 'intradayDataGroupings'
        }

        self._start_date = None
        self._end_date = None
        self._interval_length_minutes = None
        self._number_of_intervals = None
        self._metrics = None
        self._no_data_reason = None
        self._queue_ids = None
        self._intraday_data_groupings = None

    @property
    def start_date(self):
        """
        Gets the start_date of this IntradayResponse.
        The start of the date range for which this data applies.  This is also the start reference point for the intervals represented in the various arrays. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ

        :return: The start_date of this IntradayResponse.
        :rtype: datetime
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """
        Sets the start_date of this IntradayResponse.
        The start of the date range for which this data applies.  This is also the start reference point for the intervals represented in the various arrays. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ

        :param start_date: The start_date of this IntradayResponse.
        :type: datetime
        """
        
        self._start_date = start_date

    @property
    def end_date(self):
        """
        Gets the end_date of this IntradayResponse.
        The end of the date range for which this data applies. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ

        :return: The end_date of this IntradayResponse.
        :rtype: datetime
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """
        Sets the end_date of this IntradayResponse.
        The end of the date range for which this data applies. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ

        :param end_date: The end_date of this IntradayResponse.
        :type: datetime
        """
        
        self._end_date = end_date

    @property
    def interval_length_minutes(self):
        """
        Gets the interval_length_minutes of this IntradayResponse.
        The aggregation period in minutes, which determines the interval duration of the returned data

        :return: The interval_length_minutes of this IntradayResponse.
        :rtype: int
        """
        return self._interval_length_minutes

    @interval_length_minutes.setter
    def interval_length_minutes(self, interval_length_minutes):
        """
        Sets the interval_length_minutes of this IntradayResponse.
        The aggregation period in minutes, which determines the interval duration of the returned data

        :param interval_length_minutes: The interval_length_minutes of this IntradayResponse.
        :type: int
        """
        
        self._interval_length_minutes = interval_length_minutes

    @property
    def number_of_intervals(self):
        """
        Gets the number_of_intervals of this IntradayResponse.
        The total number of time intervals represented by this data

        :return: The number_of_intervals of this IntradayResponse.
        :rtype: int
        """
        return self._number_of_intervals

    @number_of_intervals.setter
    def number_of_intervals(self, number_of_intervals):
        """
        Sets the number_of_intervals of this IntradayResponse.
        The total number of time intervals represented by this data

        :param number_of_intervals: The number_of_intervals of this IntradayResponse.
        :type: int
        """
        
        self._number_of_intervals = number_of_intervals

    @property
    def metrics(self):
        """
        Gets the metrics of this IntradayResponse.
        The metrics to which this data corresponds

        :return: The metrics of this IntradayResponse.
        :rtype: list[IntradayMetric]
        """
        return self._metrics

    @metrics.setter
    def metrics(self, metrics):
        """
        Sets the metrics of this IntradayResponse.
        The metrics to which this data corresponds

        :param metrics: The metrics of this IntradayResponse.
        :type: list[IntradayMetric]
        """
        
        self._metrics = metrics

    @property
    def no_data_reason(self):
        """
        Gets the no_data_reason of this IntradayResponse.
        If not null, the reason there was no data for the request

        :return: The no_data_reason of this IntradayResponse.
        :rtype: str
        """
        return self._no_data_reason

    @no_data_reason.setter
    def no_data_reason(self, no_data_reason):
        """
        Sets the no_data_reason of this IntradayResponse.
        If not null, the reason there was no data for the request

        :param no_data_reason: The no_data_reason of this IntradayResponse.
        :type: str
        """
        allowed_values = ["NoWeekData", "NoPublishedSchedule", "NoSourceForecast"]
        if no_data_reason.lower() not in map(str.lower, allowed_values):
            # print "Invalid value for no_data_reason -> " + no_data_reason
            self._no_data_reason = "outdated_sdk_version"
        else:
            self._no_data_reason = no_data_reason.lower()

    @property
    def queue_ids(self):
        """
        Gets the queue_ids of this IntradayResponse.
        The IDs of the queues this data corresponds to

        :return: The queue_ids of this IntradayResponse.
        :rtype: list[str]
        """
        return self._queue_ids

    @queue_ids.setter
    def queue_ids(self, queue_ids):
        """
        Sets the queue_ids of this IntradayResponse.
        The IDs of the queues this data corresponds to

        :param queue_ids: The queue_ids of this IntradayResponse.
        :type: list[str]
        """
        
        self._queue_ids = queue_ids

    @property
    def intraday_data_groupings(self):
        """
        Gets the intraday_data_groupings of this IntradayResponse.
        Intraday data grouped by a single media type and set of queue IDs

        :return: The intraday_data_groupings of this IntradayResponse.
        :rtype: list[IntradayDataGroup]
        """
        return self._intraday_data_groupings

    @intraday_data_groupings.setter
    def intraday_data_groupings(self, intraday_data_groupings):
        """
        Sets the intraday_data_groupings of this IntradayResponse.
        Intraday data grouped by a single media type and set of queue IDs

        :param intraday_data_groupings: The intraday_data_groupings of this IntradayResponse.
        :type: list[IntradayDataGroup]
        """
        
        self._intraday_data_groupings = intraday_data_groupings

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

