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


class VoicemailGroupPolicy(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        VoicemailGroupPolicy - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'name': 'str',
            'group': 'Group',
            'enabled': 'bool',
            'send_email_notifications': 'bool',
            'rotate_calls_secs': 'int',
            'stop_ringing_after_rotations': 'int',
            'overflow_group_id': 'str',
            'group_alert_type': 'str'
        }

        self.attribute_map = {
            'name': 'name',
            'group': 'group',
            'enabled': 'enabled',
            'send_email_notifications': 'sendEmailNotifications',
            'rotate_calls_secs': 'rotateCallsSecs',
            'stop_ringing_after_rotations': 'stopRingingAfterRotations',
            'overflow_group_id': 'overflowGroupId',
            'group_alert_type': 'groupAlertType'
        }

        self._name = None
        self._group = None
        self._enabled = None
        self._send_email_notifications = None
        self._rotate_calls_secs = None
        self._stop_ringing_after_rotations = None
        self._overflow_group_id = None
        self._group_alert_type = None

    @property
    def name(self):
        """
        Gets the name of this VoicemailGroupPolicy.


        :return: The name of this VoicemailGroupPolicy.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this VoicemailGroupPolicy.


        :param name: The name of this VoicemailGroupPolicy.
        :type: str
        """
        
        self._name = name

    @property
    def group(self):
        """
        Gets the group of this VoicemailGroupPolicy.
        The group associated with the policy

        :return: The group of this VoicemailGroupPolicy.
        :rtype: Group
        """
        return self._group

    @group.setter
    def group(self, group):
        """
        Sets the group of this VoicemailGroupPolicy.
        The group associated with the policy

        :param group: The group of this VoicemailGroupPolicy.
        :type: Group
        """
        
        self._group = group

    @property
    def enabled(self):
        """
        Gets the enabled of this VoicemailGroupPolicy.
        Whether voicemail is enabled for the group

        :return: The enabled of this VoicemailGroupPolicy.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """
        Sets the enabled of this VoicemailGroupPolicy.
        Whether voicemail is enabled for the group

        :param enabled: The enabled of this VoicemailGroupPolicy.
        :type: bool
        """
        
        self._enabled = enabled

    @property
    def send_email_notifications(self):
        """
        Gets the send_email_notifications of this VoicemailGroupPolicy.
        Whether email notifications are sent to group members when a new voicemail is received

        :return: The send_email_notifications of this VoicemailGroupPolicy.
        :rtype: bool
        """
        return self._send_email_notifications

    @send_email_notifications.setter
    def send_email_notifications(self, send_email_notifications):
        """
        Sets the send_email_notifications of this VoicemailGroupPolicy.
        Whether email notifications are sent to group members when a new voicemail is received

        :param send_email_notifications: The send_email_notifications of this VoicemailGroupPolicy.
        :type: bool
        """
        
        self._send_email_notifications = send_email_notifications

    @property
    def rotate_calls_secs(self):
        """
        Gets the rotate_calls_secs of this VoicemailGroupPolicy.
        How many seconds to ring before rotating to the next member in the group

        :return: The rotate_calls_secs of this VoicemailGroupPolicy.
        :rtype: int
        """
        return self._rotate_calls_secs

    @rotate_calls_secs.setter
    def rotate_calls_secs(self, rotate_calls_secs):
        """
        Sets the rotate_calls_secs of this VoicemailGroupPolicy.
        How many seconds to ring before rotating to the next member in the group

        :param rotate_calls_secs: The rotate_calls_secs of this VoicemailGroupPolicy.
        :type: int
        """
        
        self._rotate_calls_secs = rotate_calls_secs

    @property
    def stop_ringing_after_rotations(self):
        """
        Gets the stop_ringing_after_rotations of this VoicemailGroupPolicy.
        How many rotations to go through

        :return: The stop_ringing_after_rotations of this VoicemailGroupPolicy.
        :rtype: int
        """
        return self._stop_ringing_after_rotations

    @stop_ringing_after_rotations.setter
    def stop_ringing_after_rotations(self, stop_ringing_after_rotations):
        """
        Sets the stop_ringing_after_rotations of this VoicemailGroupPolicy.
        How many rotations to go through

        :param stop_ringing_after_rotations: The stop_ringing_after_rotations of this VoicemailGroupPolicy.
        :type: int
        """
        
        self._stop_ringing_after_rotations = stop_ringing_after_rotations

    @property
    def overflow_group_id(self):
        """
        Gets the overflow_group_id of this VoicemailGroupPolicy.
         A fallback group to contact when all of the members in this group did not answer the call.

        :return: The overflow_group_id of this VoicemailGroupPolicy.
        :rtype: str
        """
        return self._overflow_group_id

    @overflow_group_id.setter
    def overflow_group_id(self, overflow_group_id):
        """
        Sets the overflow_group_id of this VoicemailGroupPolicy.
         A fallback group to contact when all of the members in this group did not answer the call.

        :param overflow_group_id: The overflow_group_id of this VoicemailGroupPolicy.
        :type: str
        """
        
        self._overflow_group_id = overflow_group_id

    @property
    def group_alert_type(self):
        """
        Gets the group_alert_type of this VoicemailGroupPolicy.
        Specifies if the members in this group should be contacted randomly, in a specific order, or by round-robin.

        :return: The group_alert_type of this VoicemailGroupPolicy.
        :rtype: str
        """
        return self._group_alert_type

    @group_alert_type.setter
    def group_alert_type(self, group_alert_type):
        """
        Sets the group_alert_type of this VoicemailGroupPolicy.
        Specifies if the members in this group should be contacted randomly, in a specific order, or by round-robin.

        :param group_alert_type: The group_alert_type of this VoicemailGroupPolicy.
        :type: str
        """
        allowed_values = ["RANDOM", "ROUND_ROBIN", "SEQUENTIAL"]
        if group_alert_type.lower() not in map(str.lower, allowed_values):
            # print "Invalid value for group_alert_type -> " + group_alert_type
            self._group_alert_type = "outdated_sdk_version"
        else:
            self._group_alert_type = group_alert_type

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

