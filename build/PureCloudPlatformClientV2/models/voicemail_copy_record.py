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


class VoicemailCopyRecord(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        VoicemailCopyRecord - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'user': 'User',
            'group': 'Group',
            'date': 'datetime'
        }

        self.attribute_map = {
            'user': 'user',
            'group': 'group',
            'date': 'date'
        }

        self._user = None
        self._group = None
        self._date = None

    @property
    def user(self):
        """
        Gets the user of this VoicemailCopyRecord.
        The user that the voicemail message was copied to/from

        :return: The user of this VoicemailCopyRecord.
        :rtype: User
        """
        return self._user

    @user.setter
    def user(self, user):
        """
        Sets the user of this VoicemailCopyRecord.
        The user that the voicemail message was copied to/from

        :param user: The user of this VoicemailCopyRecord.
        :type: User
        """
        
        self._user = user

    @property
    def group(self):
        """
        Gets the group of this VoicemailCopyRecord.
        The group that the voicemail message was copied to/from

        :return: The group of this VoicemailCopyRecord.
        :rtype: Group
        """
        return self._group

    @group.setter
    def group(self, group):
        """
        Sets the group of this VoicemailCopyRecord.
        The group that the voicemail message was copied to/from

        :param group: The group of this VoicemailCopyRecord.
        :type: Group
        """
        
        self._group = group

    @property
    def date(self):
        """
        Gets the date of this VoicemailCopyRecord.
        The date when the voicemail was copied. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ

        :return: The date of this VoicemailCopyRecord.
        :rtype: datetime
        """
        return self._date

    @date.setter
    def date(self, date):
        """
        Sets the date of this VoicemailCopyRecord.
        The date when the voicemail was copied. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ

        :param date: The date of this VoicemailCopyRecord.
        :type: datetime
        """
        
        self._date = date

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
