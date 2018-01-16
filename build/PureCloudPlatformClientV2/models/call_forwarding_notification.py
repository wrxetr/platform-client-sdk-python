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


class CallForwardingNotification(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        CallForwardingNotification - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'user': 'DocumentDataV2NotificationWorkspace',
            'enabled': 'bool',
            'calls': 'list[CallForwardingNotificationCalls]',
            'voicemail': 'str',
            'modified_date': 'datetime'
        }

        self.attribute_map = {
            'user': 'user',
            'enabled': 'enabled',
            'calls': 'calls',
            'voicemail': 'voicemail',
            'modified_date': 'modifiedDate'
        }

        self._user = None
        self._enabled = None
        self._calls = None
        self._voicemail = None
        self._modified_date = None

    @property
    def user(self):
        """
        Gets the user of this CallForwardingNotification.


        :return: The user of this CallForwardingNotification.
        :rtype: DocumentDataV2NotificationWorkspace
        """
        return self._user

    @user.setter
    def user(self, user):
        """
        Sets the user of this CallForwardingNotification.


        :param user: The user of this CallForwardingNotification.
        :type: DocumentDataV2NotificationWorkspace
        """
        
        self._user = user

    @property
    def enabled(self):
        """
        Gets the enabled of this CallForwardingNotification.


        :return: The enabled of this CallForwardingNotification.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """
        Sets the enabled of this CallForwardingNotification.


        :param enabled: The enabled of this CallForwardingNotification.
        :type: bool
        """
        
        self._enabled = enabled

    @property
    def calls(self):
        """
        Gets the calls of this CallForwardingNotification.


        :return: The calls of this CallForwardingNotification.
        :rtype: list[CallForwardingNotificationCalls]
        """
        return self._calls

    @calls.setter
    def calls(self, calls):
        """
        Sets the calls of this CallForwardingNotification.


        :param calls: The calls of this CallForwardingNotification.
        :type: list[CallForwardingNotificationCalls]
        """
        
        self._calls = calls

    @property
    def voicemail(self):
        """
        Gets the voicemail of this CallForwardingNotification.


        :return: The voicemail of this CallForwardingNotification.
        :rtype: str
        """
        return self._voicemail

    @voicemail.setter
    def voicemail(self, voicemail):
        """
        Sets the voicemail of this CallForwardingNotification.


        :param voicemail: The voicemail of this CallForwardingNotification.
        :type: str
        """
        
        self._voicemail = voicemail

    @property
    def modified_date(self):
        """
        Gets the modified_date of this CallForwardingNotification.


        :return: The modified_date of this CallForwardingNotification.
        :rtype: datetime
        """
        return self._modified_date

    @modified_date.setter
    def modified_date(self, modified_date):
        """
        Sets the modified_date of this CallForwardingNotification.


        :param modified_date: The modified_date of this CallForwardingNotification.
        :type: datetime
        """
        
        self._modified_date = modified_date

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

