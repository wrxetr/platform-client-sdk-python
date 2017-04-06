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


class UserPresenceAlert(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        UserPresenceAlert - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'name': 'str',
            'presence_user': 'User',
            'presence_type': 'str',
            'presence_value': 'str',
            'presence_limit_in_seconds': 'int',
            'rule_id': 'str',
            'start_date': 'datetime',
            'end_date': 'datetime',
            'notification_users': 'list[User]',
            'alert_types': 'list[str]',
            'rule_uri': 'str',
            'self_uri': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'presence_user': 'presenceUser',
            'presence_type': 'presenceType',
            'presence_value': 'presenceValue',
            'presence_limit_in_seconds': 'presenceLimitInSeconds',
            'rule_id': 'ruleId',
            'start_date': 'startDate',
            'end_date': 'endDate',
            'notification_users': 'notificationUsers',
            'alert_types': 'alertTypes',
            'rule_uri': 'ruleUri',
            'self_uri': 'selfUri'
        }

        self._id = None
        self._name = None
        self._presence_user = None
        self._presence_type = None
        self._presence_value = None
        self._presence_limit_in_seconds = None
        self._rule_id = None
        self._start_date = None
        self._end_date = None
        self._notification_users = None
        self._alert_types = None
        self._rule_uri = None
        self._self_uri = None

    @property
    def id(self):
        """
        Gets the id of this UserPresenceAlert.
        The globally unique identifier for the object.

        :return: The id of this UserPresenceAlert.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this UserPresenceAlert.
        The globally unique identifier for the object.

        :param id: The id of this UserPresenceAlert.
        :type: str
        """
        
        self._id = id

    @property
    def name(self):
        """
        Gets the name of this UserPresenceAlert.
        Name of the rule

        :return: The name of this UserPresenceAlert.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this UserPresenceAlert.
        Name of the rule

        :param name: The name of this UserPresenceAlert.
        :type: str
        """
        
        self._name = name

    @property
    def presence_user(self):
        """
        Gets the presence_user of this UserPresenceAlert.
        The user whose presence will be watched.

        :return: The presence_user of this UserPresenceAlert.
        :rtype: User
        """
        return self._presence_user

    @presence_user.setter
    def presence_user(self, presence_user):
        """
        Sets the presence_user of this UserPresenceAlert.
        The user whose presence will be watched.

        :param presence_user: The presence_user of this UserPresenceAlert.
        :type: User
        """
        
        self._presence_user = presence_user

    @property
    def presence_type(self):
        """
        Gets the presence_type of this UserPresenceAlert.
        Indicates to which presence type the presence value belongs.

        :return: The presence_type of this UserPresenceAlert.
        :rtype: str
        """
        return self._presence_type

    @presence_type.setter
    def presence_type(self, presence_type):
        """
        Sets the presence_type of this UserPresenceAlert.
        Indicates to which presence type the presence value belongs.

        :param presence_type: The presence_type of this UserPresenceAlert.
        :type: str
        """
        allowed_values = ["SYSTEM", "ORGANIZATION"]
        if presence_type.lower() not in map(str.lower, allowed_values):
            # print "Invalid value for presence_type -> " + presence_type
            self._presence_type = "outdated_sdk_version"
        else:
            self._presence_type = presence_type.lower()

    @property
    def presence_value(self):
        """
        Gets the presence_value of this UserPresenceAlert.
        The Org's UUID or Systems enum constance indicating the presence of concern.

        :return: The presence_value of this UserPresenceAlert.
        :rtype: str
        """
        return self._presence_value

    @presence_value.setter
    def presence_value(self, presence_value):
        """
        Sets the presence_value of this UserPresenceAlert.
        The Org's UUID or Systems enum constance indicating the presence of concern.

        :param presence_value: The presence_value of this UserPresenceAlert.
        :type: str
        """
        
        self._presence_value = presence_value

    @property
    def presence_limit_in_seconds(self):
        """
        Gets the presence_limit_in_seconds of this UserPresenceAlert.
        The number of seconds to wait before alerting based upon the user's presence.

        :return: The presence_limit_in_seconds of this UserPresenceAlert.
        :rtype: int
        """
        return self._presence_limit_in_seconds

    @presence_limit_in_seconds.setter
    def presence_limit_in_seconds(self, presence_limit_in_seconds):
        """
        Sets the presence_limit_in_seconds of this UserPresenceAlert.
        The number of seconds to wait before alerting based upon the user's presence.

        :param presence_limit_in_seconds: The presence_limit_in_seconds of this UserPresenceAlert.
        :type: int
        """
        
        self._presence_limit_in_seconds = presence_limit_in_seconds

    @property
    def rule_id(self):
        """
        Gets the rule_id of this UserPresenceAlert.
        The id of the rule.

        :return: The rule_id of this UserPresenceAlert.
        :rtype: str
        """
        return self._rule_id

    @rule_id.setter
    def rule_id(self, rule_id):
        """
        Sets the rule_id of this UserPresenceAlert.
        The id of the rule.

        :param rule_id: The rule_id of this UserPresenceAlert.
        :type: str
        """
        
        self._rule_id = rule_id

    @property
    def start_date(self):
        """
        Gets the start_date of this UserPresenceAlert.
        The date/time the alert was created. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ

        :return: The start_date of this UserPresenceAlert.
        :rtype: datetime
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """
        Sets the start_date of this UserPresenceAlert.
        The date/time the alert was created. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ

        :param start_date: The start_date of this UserPresenceAlert.
        :type: datetime
        """
        
        self._start_date = start_date

    @property
    def end_date(self):
        """
        Gets the end_date of this UserPresenceAlert.
        The date/time the owning rule exiting in alarm status. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ

        :return: The end_date of this UserPresenceAlert.
        :rtype: datetime
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """
        Sets the end_date of this UserPresenceAlert.
        The date/time the owning rule exiting in alarm status. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ

        :param end_date: The end_date of this UserPresenceAlert.
        :type: datetime
        """
        
        self._end_date = end_date

    @property
    def notification_users(self):
        """
        Gets the notification_users of this UserPresenceAlert.
        The ids of users who were notified of alarm state change.

        :return: The notification_users of this UserPresenceAlert.
        :rtype: list[User]
        """
        return self._notification_users

    @notification_users.setter
    def notification_users(self, notification_users):
        """
        Sets the notification_users of this UserPresenceAlert.
        The ids of users who were notified of alarm state change.

        :param notification_users: The notification_users of this UserPresenceAlert.
        :type: list[User]
        """
        
        self._notification_users = notification_users

    @property
    def alert_types(self):
        """
        Gets the alert_types of this UserPresenceAlert.
        A collection of notification methods.

        :return: The alert_types of this UserPresenceAlert.
        :rtype: list[str]
        """
        return self._alert_types

    @alert_types.setter
    def alert_types(self, alert_types):
        """
        Sets the alert_types of this UserPresenceAlert.
        A collection of notification methods.

        :param alert_types: The alert_types of this UserPresenceAlert.
        :type: list[str]
        """
        
        self._alert_types = alert_types

    @property
    def rule_uri(self):
        """
        Gets the rule_uri of this UserPresenceAlert.


        :return: The rule_uri of this UserPresenceAlert.
        :rtype: str
        """
        return self._rule_uri

    @rule_uri.setter
    def rule_uri(self, rule_uri):
        """
        Sets the rule_uri of this UserPresenceAlert.


        :param rule_uri: The rule_uri of this UserPresenceAlert.
        :type: str
        """
        
        self._rule_uri = rule_uri

    @property
    def self_uri(self):
        """
        Gets the self_uri of this UserPresenceAlert.
        The URI for this object

        :return: The self_uri of this UserPresenceAlert.
        :rtype: str
        """
        return self._self_uri

    @self_uri.setter
    def self_uri(self, self_uri):
        """
        Sets the self_uri of this UserPresenceAlert.
        The URI for this object

        :param self_uri: The self_uri of this UserPresenceAlert.
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
