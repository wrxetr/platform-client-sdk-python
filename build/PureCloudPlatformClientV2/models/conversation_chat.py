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


class ConversationChat(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        ConversationChat - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'state': 'str',
            'id': 'str',
            'room_id': 'str',
            'recording_id': 'str',
            'segments': 'list[Segment]',
            'held': 'bool',
            'direction': 'str',
            'disconnect_type': 'str',
            'start_hold_time': 'datetime',
            'connected_time': 'datetime',
            'disconnected_time': 'datetime',
            'provider': 'str'
        }

        self.attribute_map = {
            'state': 'state',
            'id': 'id',
            'room_id': 'roomId',
            'recording_id': 'recordingId',
            'segments': 'segments',
            'held': 'held',
            'direction': 'direction',
            'disconnect_type': 'disconnectType',
            'start_hold_time': 'startHoldTime',
            'connected_time': 'connectedTime',
            'disconnected_time': 'disconnectedTime',
            'provider': 'provider'
        }

        self._state = None
        self._id = None
        self._room_id = None
        self._recording_id = None
        self._segments = None
        self._held = None
        self._direction = None
        self._disconnect_type = None
        self._start_hold_time = None
        self._connected_time = None
        self._disconnected_time = None
        self._provider = None

    @property
    def state(self):
        """
        Gets the state of this ConversationChat.
        The connection state of this communication.

        :return: The state of this ConversationChat.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """
        Sets the state of this ConversationChat.
        The connection state of this communication.

        :param state: The state of this ConversationChat.
        :type: str
        """
        allowed_values = ["alerting", "dialing", "contacting", "offering", "connected", "disconnected", "terminated", "none"]
        if state.lower() not in map(str.lower, allowed_values):
            # print "Invalid value for state -> " + state
            self._state = "outdated_sdk_version"
        else:
            self._state = state.lower()

    @property
    def id(self):
        """
        Gets the id of this ConversationChat.
        A globally unique identifier for this communication.

        :return: The id of this ConversationChat.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ConversationChat.
        A globally unique identifier for this communication.

        :param id: The id of this ConversationChat.
        :type: str
        """
        
        self._id = id

    @property
    def room_id(self):
        """
        Gets the room_id of this ConversationChat.
        The room id for the chat.

        :return: The room_id of this ConversationChat.
        :rtype: str
        """
        return self._room_id

    @room_id.setter
    def room_id(self, room_id):
        """
        Sets the room_id of this ConversationChat.
        The room id for the chat.

        :param room_id: The room_id of this ConversationChat.
        :type: str
        """
        
        self._room_id = room_id

    @property
    def recording_id(self):
        """
        Gets the recording_id of this ConversationChat.
        A globally unique identifier for the recording associated with this chat.

        :return: The recording_id of this ConversationChat.
        :rtype: str
        """
        return self._recording_id

    @recording_id.setter
    def recording_id(self, recording_id):
        """
        Sets the recording_id of this ConversationChat.
        A globally unique identifier for the recording associated with this chat.

        :param recording_id: The recording_id of this ConversationChat.
        :type: str
        """
        
        self._recording_id = recording_id

    @property
    def segments(self):
        """
        Gets the segments of this ConversationChat.
        The time line of the participant's chat, divided into activity segments.

        :return: The segments of this ConversationChat.
        :rtype: list[Segment]
        """
        return self._segments

    @segments.setter
    def segments(self, segments):
        """
        Sets the segments of this ConversationChat.
        The time line of the participant's chat, divided into activity segments.

        :param segments: The segments of this ConversationChat.
        :type: list[Segment]
        """
        
        self._segments = segments

    @property
    def held(self):
        """
        Gets the held of this ConversationChat.
        True if this call is held and the person on this side hears silence.

        :return: The held of this ConversationChat.
        :rtype: bool
        """
        return self._held

    @held.setter
    def held(self, held):
        """
        Sets the held of this ConversationChat.
        True if this call is held and the person on this side hears silence.

        :param held: The held of this ConversationChat.
        :type: bool
        """
        
        self._held = held

    @property
    def direction(self):
        """
        Gets the direction of this ConversationChat.
        The direction of the chat

        :return: The direction of this ConversationChat.
        :rtype: str
        """
        return self._direction

    @direction.setter
    def direction(self, direction):
        """
        Sets the direction of this ConversationChat.
        The direction of the chat

        :param direction: The direction of this ConversationChat.
        :type: str
        """
        allowed_values = ["inbound", "outbound"]
        if direction.lower() not in map(str.lower, allowed_values):
            # print "Invalid value for direction -> " + direction
            self._direction = "outdated_sdk_version"
        else:
            self._direction = direction.lower()

    @property
    def disconnect_type(self):
        """
        Gets the disconnect_type of this ConversationChat.
        System defined string indicating what caused the communication to disconnect. Will be null until the communication disconnects.

        :return: The disconnect_type of this ConversationChat.
        :rtype: str
        """
        return self._disconnect_type

    @disconnect_type.setter
    def disconnect_type(self, disconnect_type):
        """
        Sets the disconnect_type of this ConversationChat.
        System defined string indicating what caused the communication to disconnect. Will be null until the communication disconnects.

        :param disconnect_type: The disconnect_type of this ConversationChat.
        :type: str
        """
        allowed_values = ["endpoint", "client", "system", "transfer", "transfer.conference", "transfer.consult", "transfer.forward", "error", "peer", "other", "uncallable"]
        if disconnect_type.lower() not in map(str.lower, allowed_values):
            # print "Invalid value for disconnect_type -> " + disconnect_type
            self._disconnect_type = "outdated_sdk_version"
        else:
            self._disconnect_type = disconnect_type.lower()

    @property
    def start_hold_time(self):
        """
        Gets the start_hold_time of this ConversationChat.
        The timestamp the chat was placed on hold in the cloud clock if the chat is currently on hold. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ

        :return: The start_hold_time of this ConversationChat.
        :rtype: datetime
        """
        return self._start_hold_time

    @start_hold_time.setter
    def start_hold_time(self, start_hold_time):
        """
        Sets the start_hold_time of this ConversationChat.
        The timestamp the chat was placed on hold in the cloud clock if the chat is currently on hold. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ

        :param start_hold_time: The start_hold_time of this ConversationChat.
        :type: datetime
        """
        
        self._start_hold_time = start_hold_time

    @property
    def connected_time(self):
        """
        Gets the connected_time of this ConversationChat.
        The timestamp when this communication was connected in the cloud clock. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ

        :return: The connected_time of this ConversationChat.
        :rtype: datetime
        """
        return self._connected_time

    @connected_time.setter
    def connected_time(self, connected_time):
        """
        Sets the connected_time of this ConversationChat.
        The timestamp when this communication was connected in the cloud clock. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ

        :param connected_time: The connected_time of this ConversationChat.
        :type: datetime
        """
        
        self._connected_time = connected_time

    @property
    def disconnected_time(self):
        """
        Gets the disconnected_time of this ConversationChat.
        The timestamp when this communication disconnected from the conversation in the provider clock. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ

        :return: The disconnected_time of this ConversationChat.
        :rtype: datetime
        """
        return self._disconnected_time

    @disconnected_time.setter
    def disconnected_time(self, disconnected_time):
        """
        Sets the disconnected_time of this ConversationChat.
        The timestamp when this communication disconnected from the conversation in the provider clock. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ

        :param disconnected_time: The disconnected_time of this ConversationChat.
        :type: datetime
        """
        
        self._disconnected_time = disconnected_time

    @property
    def provider(self):
        """
        Gets the provider of this ConversationChat.
        The source provider for the email.

        :return: The provider of this ConversationChat.
        :rtype: str
        """
        return self._provider

    @provider.setter
    def provider(self, provider):
        """
        Sets the provider of this ConversationChat.
        The source provider for the email.

        :param provider: The provider of this ConversationChat.
        :type: str
        """
        
        self._provider = provider

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

