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


class ManagementUnitSettings(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        ManagementUnitSettings - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'adherence': 'AdherenceSettings',
            'short_term_forecasting': 'ShortTermForecastingSettings',
            'time_off': 'TimeOffRequestSettings',
            'scheduling': 'SchedulingSettings',
            'metadata': 'WfmVersionedEntityMetadata'
        }

        self.attribute_map = {
            'adherence': 'adherence',
            'short_term_forecasting': 'shortTermForecasting',
            'time_off': 'timeOff',
            'scheduling': 'scheduling',
            'metadata': 'metadata'
        }

        self._adherence = None
        self._short_term_forecasting = None
        self._time_off = None
        self._scheduling = None
        self._metadata = None

    @property
    def adherence(self):
        """
        Gets the adherence of this ManagementUnitSettings.
        Adherence settings for this management unit

        :return: The adherence of this ManagementUnitSettings.
        :rtype: AdherenceSettings
        """
        return self._adherence

    @adherence.setter
    def adherence(self, adherence):
        """
        Sets the adherence of this ManagementUnitSettings.
        Adherence settings for this management unit

        :param adherence: The adherence of this ManagementUnitSettings.
        :type: AdherenceSettings
        """
        
        self._adherence = adherence

    @property
    def short_term_forecasting(self):
        """
        Gets the short_term_forecasting of this ManagementUnitSettings.
        Short term forecasting settings for this management unit

        :return: The short_term_forecasting of this ManagementUnitSettings.
        :rtype: ShortTermForecastingSettings
        """
        return self._short_term_forecasting

    @short_term_forecasting.setter
    def short_term_forecasting(self, short_term_forecasting):
        """
        Sets the short_term_forecasting of this ManagementUnitSettings.
        Short term forecasting settings for this management unit

        :param short_term_forecasting: The short_term_forecasting of this ManagementUnitSettings.
        :type: ShortTermForecastingSettings
        """
        
        self._short_term_forecasting = short_term_forecasting

    @property
    def time_off(self):
        """
        Gets the time_off of this ManagementUnitSettings.
        Time off request settings for this management unit

        :return: The time_off of this ManagementUnitSettings.
        :rtype: TimeOffRequestSettings
        """
        return self._time_off

    @time_off.setter
    def time_off(self, time_off):
        """
        Sets the time_off of this ManagementUnitSettings.
        Time off request settings for this management unit

        :param time_off: The time_off of this ManagementUnitSettings.
        :type: TimeOffRequestSettings
        """
        
        self._time_off = time_off

    @property
    def scheduling(self):
        """
        Gets the scheduling of this ManagementUnitSettings.
        Scheduling settings for this management unit

        :return: The scheduling of this ManagementUnitSettings.
        :rtype: SchedulingSettings
        """
        return self._scheduling

    @scheduling.setter
    def scheduling(self, scheduling):
        """
        Sets the scheduling of this ManagementUnitSettings.
        Scheduling settings for this management unit

        :param scheduling: The scheduling of this ManagementUnitSettings.
        :type: SchedulingSettings
        """
        
        self._scheduling = scheduling

    @property
    def metadata(self):
        """
        Gets the metadata of this ManagementUnitSettings.
        Version info metadata for the associated management unit

        :return: The metadata of this ManagementUnitSettings.
        :rtype: WfmVersionedEntityMetadata
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """
        Sets the metadata of this ManagementUnitSettings.
        Version info metadata for the associated management unit

        :param metadata: The metadata of this ManagementUnitSettings.
        :type: WfmVersionedEntityMetadata
        """
        
        self._metadata = metadata

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

