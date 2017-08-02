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


class VoicemailRetentionPolicy(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        VoicemailRetentionPolicy - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'voicemail_retention_policy_type': 'str',
            'number_of_days': 'int'
        }

        self.attribute_map = {
            'voicemail_retention_policy_type': 'voicemailRetentionPolicyType',
            'number_of_days': 'numberOfDays'
        }

        self._voicemail_retention_policy_type = None
        self._number_of_days = None

    @property
    def voicemail_retention_policy_type(self):
        """
        Gets the voicemail_retention_policy_type of this VoicemailRetentionPolicy.
        The retention policy type

        :return: The voicemail_retention_policy_type of this VoicemailRetentionPolicy.
        :rtype: str
        """
        return self._voicemail_retention_policy_type

    @voicemail_retention_policy_type.setter
    def voicemail_retention_policy_type(self, voicemail_retention_policy_type):
        """
        Sets the voicemail_retention_policy_type of this VoicemailRetentionPolicy.
        The retention policy type

        :param voicemail_retention_policy_type: The voicemail_retention_policy_type of this VoicemailRetentionPolicy.
        :type: str
        """
        allowed_values = ["RETAIN_INDEFINITELY", "RETAIN_WITH_TTL", "IMMEDIATE_DELETE"]
        if voicemail_retention_policy_type.lower() not in map(str.lower, allowed_values):
            # print "Invalid value for voicemail_retention_policy_type -> " + voicemail_retention_policy_type
            self._voicemail_retention_policy_type = "outdated_sdk_version"
        else:
            self._voicemail_retention_policy_type = voicemail_retention_policy_type

    @property
    def number_of_days(self):
        """
        Gets the number_of_days of this VoicemailRetentionPolicy.
        If retentionPolicyType == RETAIN_WITH_TTL, then this value represents the number of days for the TTL

        :return: The number_of_days of this VoicemailRetentionPolicy.
        :rtype: int
        """
        return self._number_of_days

    @number_of_days.setter
    def number_of_days(self, number_of_days):
        """
        Sets the number_of_days of this VoicemailRetentionPolicy.
        If retentionPolicyType == RETAIN_WITH_TTL, then this value represents the number of days for the TTL

        :param number_of_days: The number_of_days of this VoicemailRetentionPolicy.
        :type: int
        """
        
        self._number_of_days = number_of_days

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

