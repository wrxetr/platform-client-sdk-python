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

class UserDetailsQuery(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        UserDetailsQuery - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'interval': 'str',
            'user_filters': 'list[UserDetailQueryFilter]',
            'routing_status_filters': 'list[RoutingStatusDetailQueryFilter]',
            'order': 'str',
            'presence_aggregations': 'list[AnalyticsQueryAggregation]',
            'routing_status_aggregations': 'list[AnalyticsQueryAggregation]',
            'paging': 'PagingSpec',
            'presence_detail_filters': 'list[PresenceDetailQueryFilter]'
        }

        self.attribute_map = {
            'interval': 'interval',
            'user_filters': 'userFilters',
            'routing_status_filters': 'routingStatusFilters',
            'order': 'order',
            'presence_aggregations': 'presenceAggregations',
            'routing_status_aggregations': 'routingStatusAggregations',
            'paging': 'paging',
            'presence_detail_filters': 'presenceDetailFilters'
        }

        self._interval = None
        self._user_filters = None
        self._routing_status_filters = None
        self._order = None
        self._presence_aggregations = None
        self._routing_status_aggregations = None
        self._paging = None
        self._presence_detail_filters = None

    @property
    def interval(self):
        """
        Gets the interval of this UserDetailsQuery.
        Specifies the date and time range of data being queried. Conversations MUST have started within this time range to potentially be included within the result set. Intervals are represented as an ISO-8601 string. For example: YYYY-MM-DDThh:mm:ss/YYYY-MM-DDThh:mm:ss

        :return: The interval of this UserDetailsQuery.
        :rtype: str
        """
        return self._interval

    @interval.setter
    def interval(self, interval):
        """
        Sets the interval of this UserDetailsQuery.
        Specifies the date and time range of data being queried. Conversations MUST have started within this time range to potentially be included within the result set. Intervals are represented as an ISO-8601 string. For example: YYYY-MM-DDThh:mm:ss/YYYY-MM-DDThh:mm:ss

        :param interval: The interval of this UserDetailsQuery.
        :type: str
        """
        
        self._interval = interval

    @property
    def user_filters(self):
        """
        Gets the user_filters of this UserDetailsQuery.
        Filters that target the users to retrieve data for

        :return: The user_filters of this UserDetailsQuery.
        :rtype: list[UserDetailQueryFilter]
        """
        return self._user_filters

    @user_filters.setter
    def user_filters(self, user_filters):
        """
        Sets the user_filters of this UserDetailsQuery.
        Filters that target the users to retrieve data for

        :param user_filters: The user_filters of this UserDetailsQuery.
        :type: list[UserDetailQueryFilter]
        """
        
        self._user_filters = user_filters

    @property
    def routing_status_filters(self):
        """
        Gets the routing_status_filters of this UserDetailsQuery.
        Filters that target agent routing status-level data

        :return: The routing_status_filters of this UserDetailsQuery.
        :rtype: list[RoutingStatusDetailQueryFilter]
        """
        return self._routing_status_filters

    @routing_status_filters.setter
    def routing_status_filters(self, routing_status_filters):
        """
        Sets the routing_status_filters of this UserDetailsQuery.
        Filters that target agent routing status-level data

        :param routing_status_filters: The routing_status_filters of this UserDetailsQuery.
        :type: list[RoutingStatusDetailQueryFilter]
        """
        
        self._routing_status_filters = routing_status_filters

    @property
    def order(self):
        """
        Gets the order of this UserDetailsQuery.
        Sort the result set in ascending/descending order. Default is ascending

        :return: The order of this UserDetailsQuery.
        :rtype: str
        """
        return self._order

    @order.setter
    def order(self, order):
        """
        Sets the order of this UserDetailsQuery.
        Sort the result set in ascending/descending order. Default is ascending

        :param order: The order of this UserDetailsQuery.
        :type: str
        """
        allowed_values = ["asc", "desc"]
        if order.lower() not in map(str.lower, allowed_values):
            # print "Invalid value for order -> " + order
            self._order = "outdated_sdk_version"
        else:
            self._order = order

    @property
    def presence_aggregations(self):
        """
        Gets the presence_aggregations of this UserDetailsQuery.
        Include faceted search and aggregate roll-ups of presence data in your search results. This does not function as a filter, but rather, summary data about the presence results matching your filters

        :return: The presence_aggregations of this UserDetailsQuery.
        :rtype: list[AnalyticsQueryAggregation]
        """
        return self._presence_aggregations

    @presence_aggregations.setter
    def presence_aggregations(self, presence_aggregations):
        """
        Sets the presence_aggregations of this UserDetailsQuery.
        Include faceted search and aggregate roll-ups of presence data in your search results. This does not function as a filter, but rather, summary data about the presence results matching your filters

        :param presence_aggregations: The presence_aggregations of this UserDetailsQuery.
        :type: list[AnalyticsQueryAggregation]
        """
        
        self._presence_aggregations = presence_aggregations

    @property
    def routing_status_aggregations(self):
        """
        Gets the routing_status_aggregations of this UserDetailsQuery.
        Include faceted search and aggregate roll-ups of agent routing status data in your search results. This does not function as a filter, but rather, summary data about the agent routing status results matching your filters

        :return: The routing_status_aggregations of this UserDetailsQuery.
        :rtype: list[AnalyticsQueryAggregation]
        """
        return self._routing_status_aggregations

    @routing_status_aggregations.setter
    def routing_status_aggregations(self, routing_status_aggregations):
        """
        Sets the routing_status_aggregations of this UserDetailsQuery.
        Include faceted search and aggregate roll-ups of agent routing status data in your search results. This does not function as a filter, but rather, summary data about the agent routing status results matching your filters

        :param routing_status_aggregations: The routing_status_aggregations of this UserDetailsQuery.
        :type: list[AnalyticsQueryAggregation]
        """
        
        self._routing_status_aggregations = routing_status_aggregations

    @property
    def paging(self):
        """
        Gets the paging of this UserDetailsQuery.
        Page size and number to control iterating through large result sets. Default page size is 25

        :return: The paging of this UserDetailsQuery.
        :rtype: PagingSpec
        """
        return self._paging

    @paging.setter
    def paging(self, paging):
        """
        Sets the paging of this UserDetailsQuery.
        Page size and number to control iterating through large result sets. Default page size is 25

        :param paging: The paging of this UserDetailsQuery.
        :type: PagingSpec
        """
        
        self._paging = paging

    @property
    def presence_detail_filters(self):
        """
        Gets the presence_detail_filters of this UserDetailsQuery.


        :return: The presence_detail_filters of this UserDetailsQuery.
        :rtype: list[PresenceDetailQueryFilter]
        """
        return self._presence_detail_filters

    @presence_detail_filters.setter
    def presence_detail_filters(self, presence_detail_filters):
        """
        Sets the presence_detail_filters of this UserDetailsQuery.


        :param presence_detail_filters: The presence_detail_filters of this UserDetailsQuery.
        :type: list[PresenceDetailQueryFilter]
        """
        
        self._presence_detail_filters = presence_detail_filters

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

