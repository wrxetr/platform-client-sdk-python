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


class IntradayQueryDataCommand(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        IntradayQueryDataCommand - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'start_date': 'datetime',
            'end_date': 'datetime',
            'metrics': 'list[IntradayMetric]',
            'queue_ids': 'list[str]',
            'interval_length_minutes': 'int'
        }

        self.attribute_map = {
            'start_date': 'startDate',
            'end_date': 'endDate',
            'metrics': 'metrics',
            'queue_ids': 'queueIds',
            'interval_length_minutes': 'intervalLengthMinutes'
        }

        self._start_date = None
        self._end_date = None
        self._metrics = None
        self._queue_ids = None
        self._interval_length_minutes = None

    @property
    def start_date(self):
        """
        Gets the start_date of this IntradayQueryDataCommand.
        Start date of the requested date range in ISO-8601 format

        :return: The start_date of this IntradayQueryDataCommand.
        :rtype: datetime
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """
        Sets the start_date of this IntradayQueryDataCommand.
        Start date of the requested date range in ISO-8601 format

        :param start_date: The start_date of this IntradayQueryDataCommand.
        :type: datetime
        """
        
        self._start_date = start_date

    @property
    def end_date(self):
        """
        Gets the end_date of this IntradayQueryDataCommand.
        End date of the requested date range in ISO-8601 format.  Must be within the same 7 day schedule week as defined by the management unit's start day of week

        :return: The end_date of this IntradayQueryDataCommand.
        :rtype: datetime
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """
        Sets the end_date of this IntradayQueryDataCommand.
        End date of the requested date range in ISO-8601 format.  Must be within the same 7 day schedule week as defined by the management unit's start day of week

        :param end_date: The end_date of this IntradayQueryDataCommand.
        :type: datetime
        """
        
        self._end_date = end_date

    @property
    def metrics(self):
        """
        Gets the metrics of this IntradayQueryDataCommand.
        The metrics to validate

        :return: The metrics of this IntradayQueryDataCommand.
        :rtype: list[IntradayMetric]
        """
        return self._metrics

    @metrics.setter
    def metrics(self, metrics):
        """
        Sets the metrics of this IntradayQueryDataCommand.
        The metrics to validate

        :param metrics: The metrics of this IntradayQueryDataCommand.
        :type: list[IntradayMetric]
        """
        
        self._metrics = metrics

    @property
    def queue_ids(self):
        """
        Gets the queue_ids of this IntradayQueryDataCommand.
        The queue IDs for which to fetch data.  Omitting or passing an empty list will return all available queues

        :return: The queue_ids of this IntradayQueryDataCommand.
        :rtype: list[str]
        """
        return self._queue_ids

    @queue_ids.setter
    def queue_ids(self, queue_ids):
        """
        Sets the queue_ids of this IntradayQueryDataCommand.
        The queue IDs for which to fetch data.  Omitting or passing an empty list will return all available queues

        :param queue_ids: The queue_ids of this IntradayQueryDataCommand.
        :type: list[str]
        """
        
        self._queue_ids = queue_ids

    @property
    def interval_length_minutes(self):
        """
        Gets the interval_length_minutes of this IntradayQueryDataCommand.
        The period/interval for which to aggregate the data.  Optional, defaults to 15

        :return: The interval_length_minutes of this IntradayQueryDataCommand.
        :rtype: int
        """
        return self._interval_length_minutes

    @interval_length_minutes.setter
    def interval_length_minutes(self, interval_length_minutes):
        """
        Sets the interval_length_minutes of this IntradayQueryDataCommand.
        The period/interval for which to aggregate the data.  Optional, defaults to 15

        :param interval_length_minutes: The interval_length_minutes of this IntradayQueryDataCommand.
        :type: int
        """
        
        self._interval_length_minutes = interval_length_minutes

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

