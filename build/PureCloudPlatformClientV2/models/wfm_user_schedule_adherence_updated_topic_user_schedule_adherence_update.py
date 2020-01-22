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

class WfmUserScheduleAdherenceUpdatedTopicUserScheduleAdherenceUpdate(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        WfmUserScheduleAdherenceUpdatedTopicUserScheduleAdherenceUpdate - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'user': 'WfmUserScheduleAdherenceUpdatedTopicUserReference',
            'management_unit_id': 'str',
            'scheduled_activity_category': 'str',
            'system_presence': 'str',
            'organization_secondary_presence_id': 'str',
            'routing_status': 'str',
            'actual_activity_category': 'str',
            'is_out_of_office': 'bool',
            'adherence_state': 'str',
            'impact': 'str',
            'adherence_change_time': 'datetime',
            'presence_update_time': 'datetime',
            'active_queues': 'list[WfmUserScheduleAdherenceUpdatedTopicQueueReference]',
            'active_queues_modified_time': 'datetime',
            'removed_from_management_unit': 'bool'
        }

        self.attribute_map = {
            'user': 'user',
            'management_unit_id': 'managementUnitId',
            'scheduled_activity_category': 'scheduledActivityCategory',
            'system_presence': 'systemPresence',
            'organization_secondary_presence_id': 'organizationSecondaryPresenceId',
            'routing_status': 'routingStatus',
            'actual_activity_category': 'actualActivityCategory',
            'is_out_of_office': 'isOutOfOffice',
            'adherence_state': 'adherenceState',
            'impact': 'impact',
            'adherence_change_time': 'adherenceChangeTime',
            'presence_update_time': 'presenceUpdateTime',
            'active_queues': 'activeQueues',
            'active_queues_modified_time': 'activeQueuesModifiedTime',
            'removed_from_management_unit': 'removedFromManagementUnit'
        }

        self._user = None
        self._management_unit_id = None
        self._scheduled_activity_category = None
        self._system_presence = None
        self._organization_secondary_presence_id = None
        self._routing_status = None
        self._actual_activity_category = None
        self._is_out_of_office = None
        self._adherence_state = None
        self._impact = None
        self._adherence_change_time = None
        self._presence_update_time = None
        self._active_queues = None
        self._active_queues_modified_time = None
        self._removed_from_management_unit = None

    @property
    def user(self):
        """
        Gets the user of this WfmUserScheduleAdherenceUpdatedTopicUserScheduleAdherenceUpdate.


        :return: The user of this WfmUserScheduleAdherenceUpdatedTopicUserScheduleAdherenceUpdate.
        :rtype: WfmUserScheduleAdherenceUpdatedTopicUserReference
        """
        return self._user

    @user.setter
    def user(self, user):
        """
        Sets the user of this WfmUserScheduleAdherenceUpdatedTopicUserScheduleAdherenceUpdate.


        :param user: The user of this WfmUserScheduleAdherenceUpdatedTopicUserScheduleAdherenceUpdate.
        :type: WfmUserScheduleAdherenceUpdatedTopicUserReference
        """
        
        self._user = user

    @property
    def management_unit_id(self):
        """
        Gets the management_unit_id of this WfmUserScheduleAdherenceUpdatedTopicUserScheduleAdherenceUpdate.


        :return: The management_unit_id of this WfmUserScheduleAdherenceUpdatedTopicUserScheduleAdherenceUpdate.
        :rtype: str
        """
        return self._management_unit_id

    @management_unit_id.setter
    def management_unit_id(self, management_unit_id):
        """
        Sets the management_unit_id of this WfmUserScheduleAdherenceUpdatedTopicUserScheduleAdherenceUpdate.


        :param management_unit_id: The management_unit_id of this WfmUserScheduleAdherenceUpdatedTopicUserScheduleAdherenceUpdate.
        :type: str
        """
        
        self._management_unit_id = management_unit_id

    @property
    def scheduled_activity_category(self):
        """
        Gets the scheduled_activity_category of this WfmUserScheduleAdherenceUpdatedTopicUserScheduleAdherenceUpdate.


        :return: The scheduled_activity_category of this WfmUserScheduleAdherenceUpdatedTopicUserScheduleAdherenceUpdate.
        :rtype: str
        """
        return self._scheduled_activity_category

    @scheduled_activity_category.setter
    def scheduled_activity_category(self, scheduled_activity_category):
        """
        Sets the scheduled_activity_category of this WfmUserScheduleAdherenceUpdatedTopicUserScheduleAdherenceUpdate.


        :param scheduled_activity_category: The scheduled_activity_category of this WfmUserScheduleAdherenceUpdatedTopicUserScheduleAdherenceUpdate.
        :type: str
        """
        
        self._scheduled_activity_category = scheduled_activity_category

    @property
    def system_presence(self):
        """
        Gets the system_presence of this WfmUserScheduleAdherenceUpdatedTopicUserScheduleAdherenceUpdate.


        :return: The system_presence of this WfmUserScheduleAdherenceUpdatedTopicUserScheduleAdherenceUpdate.
        :rtype: str
        """
        return self._system_presence

    @system_presence.setter
    def system_presence(self, system_presence):
        """
        Sets the system_presence of this WfmUserScheduleAdherenceUpdatedTopicUserScheduleAdherenceUpdate.


        :param system_presence: The system_presence of this WfmUserScheduleAdherenceUpdatedTopicUserScheduleAdherenceUpdate.
        :type: str
        """
        
        self._system_presence = system_presence

    @property
    def organization_secondary_presence_id(self):
        """
        Gets the organization_secondary_presence_id of this WfmUserScheduleAdherenceUpdatedTopicUserScheduleAdherenceUpdate.


        :return: The organization_secondary_presence_id of this WfmUserScheduleAdherenceUpdatedTopicUserScheduleAdherenceUpdate.
        :rtype: str
        """
        return self._organization_secondary_presence_id

    @organization_secondary_presence_id.setter
    def organization_secondary_presence_id(self, organization_secondary_presence_id):
        """
        Sets the organization_secondary_presence_id of this WfmUserScheduleAdherenceUpdatedTopicUserScheduleAdherenceUpdate.


        :param organization_secondary_presence_id: The organization_secondary_presence_id of this WfmUserScheduleAdherenceUpdatedTopicUserScheduleAdherenceUpdate.
        :type: str
        """
        
        self._organization_secondary_presence_id = organization_secondary_presence_id

    @property
    def routing_status(self):
        """
        Gets the routing_status of this WfmUserScheduleAdherenceUpdatedTopicUserScheduleAdherenceUpdate.


        :return: The routing_status of this WfmUserScheduleAdherenceUpdatedTopicUserScheduleAdherenceUpdate.
        :rtype: str
        """
        return self._routing_status

    @routing_status.setter
    def routing_status(self, routing_status):
        """
        Sets the routing_status of this WfmUserScheduleAdherenceUpdatedTopicUserScheduleAdherenceUpdate.


        :param routing_status: The routing_status of this WfmUserScheduleAdherenceUpdatedTopicUserScheduleAdherenceUpdate.
        :type: str
        """
        allowed_values = ["__EMPTY__", "OFF_QUEUE", "IDLE", "INTERACTING", "NOT_RESPONDING", "COMMUNICATING", "OFFLINE"]
        if routing_status.lower() not in map(str.lower, allowed_values):
            # print "Invalid value for routing_status -> " + routing_status
            self._routing_status = "outdated_sdk_version"
        else:
            self._routing_status = routing_status

    @property
    def actual_activity_category(self):
        """
        Gets the actual_activity_category of this WfmUserScheduleAdherenceUpdatedTopicUserScheduleAdherenceUpdate.


        :return: The actual_activity_category of this WfmUserScheduleAdherenceUpdatedTopicUserScheduleAdherenceUpdate.
        :rtype: str
        """
        return self._actual_activity_category

    @actual_activity_category.setter
    def actual_activity_category(self, actual_activity_category):
        """
        Sets the actual_activity_category of this WfmUserScheduleAdherenceUpdatedTopicUserScheduleAdherenceUpdate.


        :param actual_activity_category: The actual_activity_category of this WfmUserScheduleAdherenceUpdatedTopicUserScheduleAdherenceUpdate.
        :type: str
        """
        
        self._actual_activity_category = actual_activity_category

    @property
    def is_out_of_office(self):
        """
        Gets the is_out_of_office of this WfmUserScheduleAdherenceUpdatedTopicUserScheduleAdherenceUpdate.


        :return: The is_out_of_office of this WfmUserScheduleAdherenceUpdatedTopicUserScheduleAdherenceUpdate.
        :rtype: bool
        """
        return self._is_out_of_office

    @is_out_of_office.setter
    def is_out_of_office(self, is_out_of_office):
        """
        Sets the is_out_of_office of this WfmUserScheduleAdherenceUpdatedTopicUserScheduleAdherenceUpdate.


        :param is_out_of_office: The is_out_of_office of this WfmUserScheduleAdherenceUpdatedTopicUserScheduleAdherenceUpdate.
        :type: bool
        """
        
        self._is_out_of_office = is_out_of_office

    @property
    def adherence_state(self):
        """
        Gets the adherence_state of this WfmUserScheduleAdherenceUpdatedTopicUserScheduleAdherenceUpdate.


        :return: The adherence_state of this WfmUserScheduleAdherenceUpdatedTopicUserScheduleAdherenceUpdate.
        :rtype: str
        """
        return self._adherence_state

    @adherence_state.setter
    def adherence_state(self, adherence_state):
        """
        Sets the adherence_state of this WfmUserScheduleAdherenceUpdatedTopicUserScheduleAdherenceUpdate.


        :param adherence_state: The adherence_state of this WfmUserScheduleAdherenceUpdatedTopicUserScheduleAdherenceUpdate.
        :type: str
        """
        allowed_values = ["InAdherence", "OutOfAdherence", "Unscheduled", "Unknown", "Ignored"]
        if adherence_state.lower() not in map(str.lower, allowed_values):
            # print "Invalid value for adherence_state -> " + adherence_state
            self._adherence_state = "outdated_sdk_version"
        else:
            self._adherence_state = adherence_state

    @property
    def impact(self):
        """
        Gets the impact of this WfmUserScheduleAdherenceUpdatedTopicUserScheduleAdherenceUpdate.


        :return: The impact of this WfmUserScheduleAdherenceUpdatedTopicUserScheduleAdherenceUpdate.
        :rtype: str
        """
        return self._impact

    @impact.setter
    def impact(self, impact):
        """
        Sets the impact of this WfmUserScheduleAdherenceUpdatedTopicUserScheduleAdherenceUpdate.


        :param impact: The impact of this WfmUserScheduleAdherenceUpdatedTopicUserScheduleAdherenceUpdate.
        :type: str
        """
        
        self._impact = impact

    @property
    def adherence_change_time(self):
        """
        Gets the adherence_change_time of this WfmUserScheduleAdherenceUpdatedTopicUserScheduleAdherenceUpdate.


        :return: The adherence_change_time of this WfmUserScheduleAdherenceUpdatedTopicUserScheduleAdherenceUpdate.
        :rtype: datetime
        """
        return self._adherence_change_time

    @adherence_change_time.setter
    def adherence_change_time(self, adherence_change_time):
        """
        Sets the adherence_change_time of this WfmUserScheduleAdherenceUpdatedTopicUserScheduleAdherenceUpdate.


        :param adherence_change_time: The adherence_change_time of this WfmUserScheduleAdherenceUpdatedTopicUserScheduleAdherenceUpdate.
        :type: datetime
        """
        
        self._adherence_change_time = adherence_change_time

    @property
    def presence_update_time(self):
        """
        Gets the presence_update_time of this WfmUserScheduleAdherenceUpdatedTopicUserScheduleAdherenceUpdate.


        :return: The presence_update_time of this WfmUserScheduleAdherenceUpdatedTopicUserScheduleAdherenceUpdate.
        :rtype: datetime
        """
        return self._presence_update_time

    @presence_update_time.setter
    def presence_update_time(self, presence_update_time):
        """
        Sets the presence_update_time of this WfmUserScheduleAdherenceUpdatedTopicUserScheduleAdherenceUpdate.


        :param presence_update_time: The presence_update_time of this WfmUserScheduleAdherenceUpdatedTopicUserScheduleAdherenceUpdate.
        :type: datetime
        """
        
        self._presence_update_time = presence_update_time

    @property
    def active_queues(self):
        """
        Gets the active_queues of this WfmUserScheduleAdherenceUpdatedTopicUserScheduleAdherenceUpdate.


        :return: The active_queues of this WfmUserScheduleAdherenceUpdatedTopicUserScheduleAdherenceUpdate.
        :rtype: list[WfmUserScheduleAdherenceUpdatedTopicQueueReference]
        """
        return self._active_queues

    @active_queues.setter
    def active_queues(self, active_queues):
        """
        Sets the active_queues of this WfmUserScheduleAdherenceUpdatedTopicUserScheduleAdherenceUpdate.


        :param active_queues: The active_queues of this WfmUserScheduleAdherenceUpdatedTopicUserScheduleAdherenceUpdate.
        :type: list[WfmUserScheduleAdherenceUpdatedTopicQueueReference]
        """
        
        self._active_queues = active_queues

    @property
    def active_queues_modified_time(self):
        """
        Gets the active_queues_modified_time of this WfmUserScheduleAdherenceUpdatedTopicUserScheduleAdherenceUpdate.


        :return: The active_queues_modified_time of this WfmUserScheduleAdherenceUpdatedTopicUserScheduleAdherenceUpdate.
        :rtype: datetime
        """
        return self._active_queues_modified_time

    @active_queues_modified_time.setter
    def active_queues_modified_time(self, active_queues_modified_time):
        """
        Sets the active_queues_modified_time of this WfmUserScheduleAdherenceUpdatedTopicUserScheduleAdherenceUpdate.


        :param active_queues_modified_time: The active_queues_modified_time of this WfmUserScheduleAdherenceUpdatedTopicUserScheduleAdherenceUpdate.
        :type: datetime
        """
        
        self._active_queues_modified_time = active_queues_modified_time

    @property
    def removed_from_management_unit(self):
        """
        Gets the removed_from_management_unit of this WfmUserScheduleAdherenceUpdatedTopicUserScheduleAdherenceUpdate.


        :return: The removed_from_management_unit of this WfmUserScheduleAdherenceUpdatedTopicUserScheduleAdherenceUpdate.
        :rtype: bool
        """
        return self._removed_from_management_unit

    @removed_from_management_unit.setter
    def removed_from_management_unit(self, removed_from_management_unit):
        """
        Sets the removed_from_management_unit of this WfmUserScheduleAdherenceUpdatedTopicUserScheduleAdherenceUpdate.


        :param removed_from_management_unit: The removed_from_management_unit of this WfmUserScheduleAdherenceUpdatedTopicUserScheduleAdherenceUpdate.
        :type: bool
        """
        
        self._removed_from_management_unit = removed_from_management_unit

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

