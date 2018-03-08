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


class MessageConversationNotificationMessageMediaParticipant(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        MessageConversationNotificationMessageMediaParticipant - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'name': 'str',
            'address': 'str',
            'start_time': 'datetime',
            'connected_time': 'datetime',
            'end_time': 'datetime',
            'start_hold_time': 'datetime',
            'purpose': 'str',
            'state': 'str',
            'direction': 'str',
            'disconnect_type': 'str',
            'held': 'bool',
            'wrapup_required': 'bool',
            'wrapup_prompt': 'str',
            'user': 'DocumentDataV2NotificationCreatedBy',
            'queue': 'MessageConversationNotificationUriReference',
            'attributes': 'dict(str, str)',
            'error_info': 'MessageConversationNotificationErrorInfo',
            'script': 'MessageConversationNotificationUriReference',
            'wrapup_timeout_ms': 'int',
            'wrapup_skipped': 'bool',
            'provider': 'str',
            'external_contact': 'MessageConversationNotificationUriReference',
            'external_organization': 'MessageConversationNotificationUriReference',
            'wrapup': 'ConversationNotificationWrapup',
            'peer': 'str',
            'screen_recording_state': 'str',
            'messages': 'list[MessageConversationNotificationMessages]',
            'type': 'str',
            'recipient_country': 'str',
            'recipient_type': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'address': 'address',
            'start_time': 'startTime',
            'connected_time': 'connectedTime',
            'end_time': 'endTime',
            'start_hold_time': 'startHoldTime',
            'purpose': 'purpose',
            'state': 'state',
            'direction': 'direction',
            'disconnect_type': 'disconnectType',
            'held': 'held',
            'wrapup_required': 'wrapupRequired',
            'wrapup_prompt': 'wrapupPrompt',
            'user': 'user',
            'queue': 'queue',
            'attributes': 'attributes',
            'error_info': 'errorInfo',
            'script': 'script',
            'wrapup_timeout_ms': 'wrapupTimeoutMs',
            'wrapup_skipped': 'wrapupSkipped',
            'provider': 'provider',
            'external_contact': 'externalContact',
            'external_organization': 'externalOrganization',
            'wrapup': 'wrapup',
            'peer': 'peer',
            'screen_recording_state': 'screenRecordingState',
            'messages': 'messages',
            'type': 'type',
            'recipient_country': 'recipientCountry',
            'recipient_type': 'recipientType'
        }

        self._id = None
        self._name = None
        self._address = None
        self._start_time = None
        self._connected_time = None
        self._end_time = None
        self._start_hold_time = None
        self._purpose = None
        self._state = None
        self._direction = None
        self._disconnect_type = None
        self._held = None
        self._wrapup_required = None
        self._wrapup_prompt = None
        self._user = None
        self._queue = None
        self._attributes = None
        self._error_info = None
        self._script = None
        self._wrapup_timeout_ms = None
        self._wrapup_skipped = None
        self._provider = None
        self._external_contact = None
        self._external_organization = None
        self._wrapup = None
        self._peer = None
        self._screen_recording_state = None
        self._messages = None
        self._type = None
        self._recipient_country = None
        self._recipient_type = None

    @property
    def id(self):
        """
        Gets the id of this MessageConversationNotificationMessageMediaParticipant.


        :return: The id of this MessageConversationNotificationMessageMediaParticipant.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this MessageConversationNotificationMessageMediaParticipant.


        :param id: The id of this MessageConversationNotificationMessageMediaParticipant.
        :type: str
        """
        
        self._id = id

    @property
    def name(self):
        """
        Gets the name of this MessageConversationNotificationMessageMediaParticipant.


        :return: The name of this MessageConversationNotificationMessageMediaParticipant.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this MessageConversationNotificationMessageMediaParticipant.


        :param name: The name of this MessageConversationNotificationMessageMediaParticipant.
        :type: str
        """
        
        self._name = name

    @property
    def address(self):
        """
        Gets the address of this MessageConversationNotificationMessageMediaParticipant.


        :return: The address of this MessageConversationNotificationMessageMediaParticipant.
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """
        Sets the address of this MessageConversationNotificationMessageMediaParticipant.


        :param address: The address of this MessageConversationNotificationMessageMediaParticipant.
        :type: str
        """
        
        self._address = address

    @property
    def start_time(self):
        """
        Gets the start_time of this MessageConversationNotificationMessageMediaParticipant.


        :return: The start_time of this MessageConversationNotificationMessageMediaParticipant.
        :rtype: datetime
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """
        Sets the start_time of this MessageConversationNotificationMessageMediaParticipant.


        :param start_time: The start_time of this MessageConversationNotificationMessageMediaParticipant.
        :type: datetime
        """
        
        self._start_time = start_time

    @property
    def connected_time(self):
        """
        Gets the connected_time of this MessageConversationNotificationMessageMediaParticipant.


        :return: The connected_time of this MessageConversationNotificationMessageMediaParticipant.
        :rtype: datetime
        """
        return self._connected_time

    @connected_time.setter
    def connected_time(self, connected_time):
        """
        Sets the connected_time of this MessageConversationNotificationMessageMediaParticipant.


        :param connected_time: The connected_time of this MessageConversationNotificationMessageMediaParticipant.
        :type: datetime
        """
        
        self._connected_time = connected_time

    @property
    def end_time(self):
        """
        Gets the end_time of this MessageConversationNotificationMessageMediaParticipant.


        :return: The end_time of this MessageConversationNotificationMessageMediaParticipant.
        :rtype: datetime
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """
        Sets the end_time of this MessageConversationNotificationMessageMediaParticipant.


        :param end_time: The end_time of this MessageConversationNotificationMessageMediaParticipant.
        :type: datetime
        """
        
        self._end_time = end_time

    @property
    def start_hold_time(self):
        """
        Gets the start_hold_time of this MessageConversationNotificationMessageMediaParticipant.


        :return: The start_hold_time of this MessageConversationNotificationMessageMediaParticipant.
        :rtype: datetime
        """
        return self._start_hold_time

    @start_hold_time.setter
    def start_hold_time(self, start_hold_time):
        """
        Sets the start_hold_time of this MessageConversationNotificationMessageMediaParticipant.


        :param start_hold_time: The start_hold_time of this MessageConversationNotificationMessageMediaParticipant.
        :type: datetime
        """
        
        self._start_hold_time = start_hold_time

    @property
    def purpose(self):
        """
        Gets the purpose of this MessageConversationNotificationMessageMediaParticipant.


        :return: The purpose of this MessageConversationNotificationMessageMediaParticipant.
        :rtype: str
        """
        return self._purpose

    @purpose.setter
    def purpose(self, purpose):
        """
        Sets the purpose of this MessageConversationNotificationMessageMediaParticipant.


        :param purpose: The purpose of this MessageConversationNotificationMessageMediaParticipant.
        :type: str
        """
        
        self._purpose = purpose

    @property
    def state(self):
        """
        Gets the state of this MessageConversationNotificationMessageMediaParticipant.


        :return: The state of this MessageConversationNotificationMessageMediaParticipant.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """
        Sets the state of this MessageConversationNotificationMessageMediaParticipant.


        :param state: The state of this MessageConversationNotificationMessageMediaParticipant.
        :type: str
        """
        allowed_values = ["alerting", "dialing", "contacting", "offering", "connected", "disconnected", "terminated", "converting", "uploading", "transmitting", "scheduled", "none"]
        if state.lower() not in map(str.lower, allowed_values):
            # print "Invalid value for state -> " + state
            self._state = "outdated_sdk_version"
        else:
            self._state = state

    @property
    def direction(self):
        """
        Gets the direction of this MessageConversationNotificationMessageMediaParticipant.


        :return: The direction of this MessageConversationNotificationMessageMediaParticipant.
        :rtype: str
        """
        return self._direction

    @direction.setter
    def direction(self, direction):
        """
        Sets the direction of this MessageConversationNotificationMessageMediaParticipant.


        :param direction: The direction of this MessageConversationNotificationMessageMediaParticipant.
        :type: str
        """
        allowed_values = ["inbound", "outbound"]
        if direction.lower() not in map(str.lower, allowed_values):
            # print "Invalid value for direction -> " + direction
            self._direction = "outdated_sdk_version"
        else:
            self._direction = direction

    @property
    def disconnect_type(self):
        """
        Gets the disconnect_type of this MessageConversationNotificationMessageMediaParticipant.


        :return: The disconnect_type of this MessageConversationNotificationMessageMediaParticipant.
        :rtype: str
        """
        return self._disconnect_type

    @disconnect_type.setter
    def disconnect_type(self, disconnect_type):
        """
        Sets the disconnect_type of this MessageConversationNotificationMessageMediaParticipant.


        :param disconnect_type: The disconnect_type of this MessageConversationNotificationMessageMediaParticipant.
        :type: str
        """
        allowed_values = ["endpoint", "client", "system", "transfer", "timeout", "transfer.conference", "transfer.consult", "transfer.forward", "transfer.noanswer", "transfer.notavailable", "transport.failure", "error", "peer", "other", "spam", "uncallable"]
        if disconnect_type.lower() not in map(str.lower, allowed_values):
            # print "Invalid value for disconnect_type -> " + disconnect_type
            self._disconnect_type = "outdated_sdk_version"
        else:
            self._disconnect_type = disconnect_type

    @property
    def held(self):
        """
        Gets the held of this MessageConversationNotificationMessageMediaParticipant.


        :return: The held of this MessageConversationNotificationMessageMediaParticipant.
        :rtype: bool
        """
        return self._held

    @held.setter
    def held(self, held):
        """
        Sets the held of this MessageConversationNotificationMessageMediaParticipant.


        :param held: The held of this MessageConversationNotificationMessageMediaParticipant.
        :type: bool
        """
        
        self._held = held

    @property
    def wrapup_required(self):
        """
        Gets the wrapup_required of this MessageConversationNotificationMessageMediaParticipant.


        :return: The wrapup_required of this MessageConversationNotificationMessageMediaParticipant.
        :rtype: bool
        """
        return self._wrapup_required

    @wrapup_required.setter
    def wrapup_required(self, wrapup_required):
        """
        Sets the wrapup_required of this MessageConversationNotificationMessageMediaParticipant.


        :param wrapup_required: The wrapup_required of this MessageConversationNotificationMessageMediaParticipant.
        :type: bool
        """
        
        self._wrapup_required = wrapup_required

    @property
    def wrapup_prompt(self):
        """
        Gets the wrapup_prompt of this MessageConversationNotificationMessageMediaParticipant.


        :return: The wrapup_prompt of this MessageConversationNotificationMessageMediaParticipant.
        :rtype: str
        """
        return self._wrapup_prompt

    @wrapup_prompt.setter
    def wrapup_prompt(self, wrapup_prompt):
        """
        Sets the wrapup_prompt of this MessageConversationNotificationMessageMediaParticipant.


        :param wrapup_prompt: The wrapup_prompt of this MessageConversationNotificationMessageMediaParticipant.
        :type: str
        """
        
        self._wrapup_prompt = wrapup_prompt

    @property
    def user(self):
        """
        Gets the user of this MessageConversationNotificationMessageMediaParticipant.


        :return: The user of this MessageConversationNotificationMessageMediaParticipant.
        :rtype: DocumentDataV2NotificationCreatedBy
        """
        return self._user

    @user.setter
    def user(self, user):
        """
        Sets the user of this MessageConversationNotificationMessageMediaParticipant.


        :param user: The user of this MessageConversationNotificationMessageMediaParticipant.
        :type: DocumentDataV2NotificationCreatedBy
        """
        
        self._user = user

    @property
    def queue(self):
        """
        Gets the queue of this MessageConversationNotificationMessageMediaParticipant.


        :return: The queue of this MessageConversationNotificationMessageMediaParticipant.
        :rtype: MessageConversationNotificationUriReference
        """
        return self._queue

    @queue.setter
    def queue(self, queue):
        """
        Sets the queue of this MessageConversationNotificationMessageMediaParticipant.


        :param queue: The queue of this MessageConversationNotificationMessageMediaParticipant.
        :type: MessageConversationNotificationUriReference
        """
        
        self._queue = queue

    @property
    def attributes(self):
        """
        Gets the attributes of this MessageConversationNotificationMessageMediaParticipant.


        :return: The attributes of this MessageConversationNotificationMessageMediaParticipant.
        :rtype: dict(str, str)
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """
        Sets the attributes of this MessageConversationNotificationMessageMediaParticipant.


        :param attributes: The attributes of this MessageConversationNotificationMessageMediaParticipant.
        :type: dict(str, str)
        """
        
        self._attributes = attributes

    @property
    def error_info(self):
        """
        Gets the error_info of this MessageConversationNotificationMessageMediaParticipant.


        :return: The error_info of this MessageConversationNotificationMessageMediaParticipant.
        :rtype: MessageConversationNotificationErrorInfo
        """
        return self._error_info

    @error_info.setter
    def error_info(self, error_info):
        """
        Sets the error_info of this MessageConversationNotificationMessageMediaParticipant.


        :param error_info: The error_info of this MessageConversationNotificationMessageMediaParticipant.
        :type: MessageConversationNotificationErrorInfo
        """
        
        self._error_info = error_info

    @property
    def script(self):
        """
        Gets the script of this MessageConversationNotificationMessageMediaParticipant.


        :return: The script of this MessageConversationNotificationMessageMediaParticipant.
        :rtype: MessageConversationNotificationUriReference
        """
        return self._script

    @script.setter
    def script(self, script):
        """
        Sets the script of this MessageConversationNotificationMessageMediaParticipant.


        :param script: The script of this MessageConversationNotificationMessageMediaParticipant.
        :type: MessageConversationNotificationUriReference
        """
        
        self._script = script

    @property
    def wrapup_timeout_ms(self):
        """
        Gets the wrapup_timeout_ms of this MessageConversationNotificationMessageMediaParticipant.


        :return: The wrapup_timeout_ms of this MessageConversationNotificationMessageMediaParticipant.
        :rtype: int
        """
        return self._wrapup_timeout_ms

    @wrapup_timeout_ms.setter
    def wrapup_timeout_ms(self, wrapup_timeout_ms):
        """
        Sets the wrapup_timeout_ms of this MessageConversationNotificationMessageMediaParticipant.


        :param wrapup_timeout_ms: The wrapup_timeout_ms of this MessageConversationNotificationMessageMediaParticipant.
        :type: int
        """
        
        self._wrapup_timeout_ms = wrapup_timeout_ms

    @property
    def wrapup_skipped(self):
        """
        Gets the wrapup_skipped of this MessageConversationNotificationMessageMediaParticipant.


        :return: The wrapup_skipped of this MessageConversationNotificationMessageMediaParticipant.
        :rtype: bool
        """
        return self._wrapup_skipped

    @wrapup_skipped.setter
    def wrapup_skipped(self, wrapup_skipped):
        """
        Sets the wrapup_skipped of this MessageConversationNotificationMessageMediaParticipant.


        :param wrapup_skipped: The wrapup_skipped of this MessageConversationNotificationMessageMediaParticipant.
        :type: bool
        """
        
        self._wrapup_skipped = wrapup_skipped

    @property
    def provider(self):
        """
        Gets the provider of this MessageConversationNotificationMessageMediaParticipant.


        :return: The provider of this MessageConversationNotificationMessageMediaParticipant.
        :rtype: str
        """
        return self._provider

    @provider.setter
    def provider(self, provider):
        """
        Sets the provider of this MessageConversationNotificationMessageMediaParticipant.


        :param provider: The provider of this MessageConversationNotificationMessageMediaParticipant.
        :type: str
        """
        
        self._provider = provider

    @property
    def external_contact(self):
        """
        Gets the external_contact of this MessageConversationNotificationMessageMediaParticipant.


        :return: The external_contact of this MessageConversationNotificationMessageMediaParticipant.
        :rtype: MessageConversationNotificationUriReference
        """
        return self._external_contact

    @external_contact.setter
    def external_contact(self, external_contact):
        """
        Sets the external_contact of this MessageConversationNotificationMessageMediaParticipant.


        :param external_contact: The external_contact of this MessageConversationNotificationMessageMediaParticipant.
        :type: MessageConversationNotificationUriReference
        """
        
        self._external_contact = external_contact

    @property
    def external_organization(self):
        """
        Gets the external_organization of this MessageConversationNotificationMessageMediaParticipant.


        :return: The external_organization of this MessageConversationNotificationMessageMediaParticipant.
        :rtype: MessageConversationNotificationUriReference
        """
        return self._external_organization

    @external_organization.setter
    def external_organization(self, external_organization):
        """
        Sets the external_organization of this MessageConversationNotificationMessageMediaParticipant.


        :param external_organization: The external_organization of this MessageConversationNotificationMessageMediaParticipant.
        :type: MessageConversationNotificationUriReference
        """
        
        self._external_organization = external_organization

    @property
    def wrapup(self):
        """
        Gets the wrapup of this MessageConversationNotificationMessageMediaParticipant.


        :return: The wrapup of this MessageConversationNotificationMessageMediaParticipant.
        :rtype: ConversationNotificationWrapup
        """
        return self._wrapup

    @wrapup.setter
    def wrapup(self, wrapup):
        """
        Sets the wrapup of this MessageConversationNotificationMessageMediaParticipant.


        :param wrapup: The wrapup of this MessageConversationNotificationMessageMediaParticipant.
        :type: ConversationNotificationWrapup
        """
        
        self._wrapup = wrapup

    @property
    def peer(self):
        """
        Gets the peer of this MessageConversationNotificationMessageMediaParticipant.


        :return: The peer of this MessageConversationNotificationMessageMediaParticipant.
        :rtype: str
        """
        return self._peer

    @peer.setter
    def peer(self, peer):
        """
        Sets the peer of this MessageConversationNotificationMessageMediaParticipant.


        :param peer: The peer of this MessageConversationNotificationMessageMediaParticipant.
        :type: str
        """
        
        self._peer = peer

    @property
    def screen_recording_state(self):
        """
        Gets the screen_recording_state of this MessageConversationNotificationMessageMediaParticipant.


        :return: The screen_recording_state of this MessageConversationNotificationMessageMediaParticipant.
        :rtype: str
        """
        return self._screen_recording_state

    @screen_recording_state.setter
    def screen_recording_state(self, screen_recording_state):
        """
        Sets the screen_recording_state of this MessageConversationNotificationMessageMediaParticipant.


        :param screen_recording_state: The screen_recording_state of this MessageConversationNotificationMessageMediaParticipant.
        :type: str
        """
        
        self._screen_recording_state = screen_recording_state

    @property
    def messages(self):
        """
        Gets the messages of this MessageConversationNotificationMessageMediaParticipant.


        :return: The messages of this MessageConversationNotificationMessageMediaParticipant.
        :rtype: list[MessageConversationNotificationMessages]
        """
        return self._messages

    @messages.setter
    def messages(self, messages):
        """
        Sets the messages of this MessageConversationNotificationMessageMediaParticipant.


        :param messages: The messages of this MessageConversationNotificationMessageMediaParticipant.
        :type: list[MessageConversationNotificationMessages]
        """
        
        self._messages = messages

    @property
    def type(self):
        """
        Gets the type of this MessageConversationNotificationMessageMediaParticipant.


        :return: The type of this MessageConversationNotificationMessageMediaParticipant.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this MessageConversationNotificationMessageMediaParticipant.


        :param type: The type of this MessageConversationNotificationMessageMediaParticipant.
        :type: str
        """
        allowed_values = ["SMS", "TWITTER", "FACEBOOK", "LINE", "VIBER", "WECHAT"]
        if type.lower() not in map(str.lower, allowed_values):
            # print "Invalid value for type -> " + type
            self._type = "outdated_sdk_version"
        else:
            self._type = type

    @property
    def recipient_country(self):
        """
        Gets the recipient_country of this MessageConversationNotificationMessageMediaParticipant.


        :return: The recipient_country of this MessageConversationNotificationMessageMediaParticipant.
        :rtype: str
        """
        return self._recipient_country

    @recipient_country.setter
    def recipient_country(self, recipient_country):
        """
        Sets the recipient_country of this MessageConversationNotificationMessageMediaParticipant.


        :param recipient_country: The recipient_country of this MessageConversationNotificationMessageMediaParticipant.
        :type: str
        """
        
        self._recipient_country = recipient_country

    @property
    def recipient_type(self):
        """
        Gets the recipient_type of this MessageConversationNotificationMessageMediaParticipant.


        :return: The recipient_type of this MessageConversationNotificationMessageMediaParticipant.
        :rtype: str
        """
        return self._recipient_type

    @recipient_type.setter
    def recipient_type(self, recipient_type):
        """
        Sets the recipient_type of this MessageConversationNotificationMessageMediaParticipant.


        :param recipient_type: The recipient_type of this MessageConversationNotificationMessageMediaParticipant.
        :type: str
        """
        
        self._recipient_type = recipient_type

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

