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


class WeekScheduleListItemResponse(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        WeekScheduleListItemResponse - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'week_date': 'str',
            'description': 'str',
            'published': 'bool',
            'generation_results': 'WeekScheduleGenerationResult',
            'short_term_forecast': 'ShortTermForecastReference',
            'metadata': 'WfmVersionedEntityMetadata',
            'self_uri': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'week_date': 'weekDate',
            'description': 'description',
            'published': 'published',
            'generation_results': 'generationResults',
            'short_term_forecast': 'shortTermForecast',
            'metadata': 'metadata',
            'self_uri': 'selfUri'
        }

        self._id = None
        self._week_date = None
        self._description = None
        self._published = None
        self._generation_results = None
        self._short_term_forecast = None
        self._metadata = None
        self._self_uri = None

    @property
    def id(self):
        """
        Gets the id of this WeekScheduleListItemResponse.
        The globally unique identifier for the object.

        :return: The id of this WeekScheduleListItemResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this WeekScheduleListItemResponse.
        The globally unique identifier for the object.

        :param id: The id of this WeekScheduleListItemResponse.
        :type: str
        """
        
        self._id = id

    @property
    def week_date(self):
        """
        Gets the week_date of this WeekScheduleListItemResponse.
        First day of this week schedule in yyyy-MM-dd format

        :return: The week_date of this WeekScheduleListItemResponse.
        :rtype: str
        """
        return self._week_date

    @week_date.setter
    def week_date(self, week_date):
        """
        Sets the week_date of this WeekScheduleListItemResponse.
        First day of this week schedule in yyyy-MM-dd format

        :param week_date: The week_date of this WeekScheduleListItemResponse.
        :type: str
        """
        
        self._week_date = week_date

    @property
    def description(self):
        """
        Gets the description of this WeekScheduleListItemResponse.
        Description of the week schedule

        :return: The description of this WeekScheduleListItemResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this WeekScheduleListItemResponse.
        Description of the week schedule

        :param description: The description of this WeekScheduleListItemResponse.
        :type: str
        """
        
        self._description = description

    @property
    def published(self):
        """
        Gets the published of this WeekScheduleListItemResponse.
        Whether the week schedule is published

        :return: The published of this WeekScheduleListItemResponse.
        :rtype: bool
        """
        return self._published

    @published.setter
    def published(self, published):
        """
        Sets the published of this WeekScheduleListItemResponse.
        Whether the week schedule is published

        :param published: The published of this WeekScheduleListItemResponse.
        :type: bool
        """
        
        self._published = published

    @property
    def generation_results(self):
        """
        Gets the generation_results of this WeekScheduleListItemResponse.
        Summary of the results from the schedule run

        :return: The generation_results of this WeekScheduleListItemResponse.
        :rtype: WeekScheduleGenerationResult
        """
        return self._generation_results

    @generation_results.setter
    def generation_results(self, generation_results):
        """
        Sets the generation_results of this WeekScheduleListItemResponse.
        Summary of the results from the schedule run

        :param generation_results: The generation_results of this WeekScheduleListItemResponse.
        :type: WeekScheduleGenerationResult
        """
        
        self._generation_results = generation_results

    @property
    def short_term_forecast(self):
        """
        Gets the short_term_forecast of this WeekScheduleListItemResponse.
        Short term forecast associated with this schedule

        :return: The short_term_forecast of this WeekScheduleListItemResponse.
        :rtype: ShortTermForecastReference
        """
        return self._short_term_forecast

    @short_term_forecast.setter
    def short_term_forecast(self, short_term_forecast):
        """
        Sets the short_term_forecast of this WeekScheduleListItemResponse.
        Short term forecast associated with this schedule

        :param short_term_forecast: The short_term_forecast of this WeekScheduleListItemResponse.
        :type: ShortTermForecastReference
        """
        
        self._short_term_forecast = short_term_forecast

    @property
    def metadata(self):
        """
        Gets the metadata of this WeekScheduleListItemResponse.
        Version metadata for this work plan

        :return: The metadata of this WeekScheduleListItemResponse.
        :rtype: WfmVersionedEntityMetadata
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """
        Sets the metadata of this WeekScheduleListItemResponse.
        Version metadata for this work plan

        :param metadata: The metadata of this WeekScheduleListItemResponse.
        :type: WfmVersionedEntityMetadata
        """
        
        self._metadata = metadata

    @property
    def self_uri(self):
        """
        Gets the self_uri of this WeekScheduleListItemResponse.
        The URI for this object

        :return: The self_uri of this WeekScheduleListItemResponse.
        :rtype: str
        """
        return self._self_uri

    @self_uri.setter
    def self_uri(self, self_uri):
        """
        Sets the self_uri of this WeekScheduleListItemResponse.
        The URI for this object

        :param self_uri: The self_uri of this WeekScheduleListItemResponse.
        :type: str
        """
        
        self._self_uri = self_uri

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

