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


class CallbackConversationNotificationParticipants(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        CallbackConversationNotificationParticipants - a model defined in Swagger

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
            'user': 'DependencyTrackingBuildNotificationNotificationUser',
            'queue': 'CallbackConversationNotificationUriReference',
            'attributes': 'dict(str, str)',
            'error_info': 'CallbackConversationNotificationErrorInfo',
            'script': 'CallbackConversationNotificationUriReference',
            'wrapup_timeout_ms': 'int',
            'wrapup_skipped': 'bool',
            'provider': 'str',
            'external_contact': 'CallbackConversationNotificationUriReference',
            'external_organization': 'CallbackConversationNotificationUriReference',
            'wrapup': 'ConversationNotificationWrapup',
            'outbound_preview': 'ConversationNotificationDialerPreview',
            'callback_numbers': 'list[str]',
            'callback_user_name': 'str',
            'skip_enabled': 'bool',
            'timeout_seconds': 'int',
            'callback_scheduled_time': 'datetime',
            'automated_callback_config_id': 'str'
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
            'outbound_preview': 'outboundPreview',
            'callback_numbers': 'callbackNumbers',
            'callback_user_name': 'callbackUserName',
            'skip_enabled': 'skipEnabled',
            'timeout_seconds': 'timeoutSeconds',
            'callback_scheduled_time': 'callbackScheduledTime',
            'automated_callback_config_id': 'automatedCallbackConfigId'
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
        self._outbound_preview = None
        self._callback_numbers = None
        self._callback_user_name = None
        self._skip_enabled = None
        self._timeout_seconds = None
        self._callback_scheduled_time = None
        self._automated_callback_config_id = None

    @property
    def id(self):
        """
        Gets the id of this CallbackConversationNotificationParticipants.


        :return: The id of this CallbackConversationNotificationParticipants.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this CallbackConversationNotificationParticipants.


        :param id: The id of this CallbackConversationNotificationParticipants.
        :type: str
        """
        
        self._id = id

    @property
    def name(self):
        """
        Gets the name of this CallbackConversationNotificationParticipants.


        :return: The name of this CallbackConversationNotificationParticipants.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this CallbackConversationNotificationParticipants.


        :param name: The name of this CallbackConversationNotificationParticipants.
        :type: str
        """
        
        self._name = name

    @property
    def address(self):
        """
        Gets the address of this CallbackConversationNotificationParticipants.


        :return: The address of this CallbackConversationNotificationParticipants.
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """
        Sets the address of this CallbackConversationNotificationParticipants.


        :param address: The address of this CallbackConversationNotificationParticipants.
        :type: str
        """
        
        self._address = address

    @property
    def start_time(self):
        """
        Gets the start_time of this CallbackConversationNotificationParticipants.


        :return: The start_time of this CallbackConversationNotificationParticipants.
        :rtype: datetime
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """
        Sets the start_time of this CallbackConversationNotificationParticipants.


        :param start_time: The start_time of this CallbackConversationNotificationParticipants.
        :type: datetime
        """
        
        self._start_time = start_time

    @property
    def connected_time(self):
        """
        Gets the connected_time of this CallbackConversationNotificationParticipants.


        :return: The connected_time of this CallbackConversationNotificationParticipants.
        :rtype: datetime
        """
        return self._connected_time

    @connected_time.setter
    def connected_time(self, connected_time):
        """
        Sets the connected_time of this CallbackConversationNotificationParticipants.


        :param connected_time: The connected_time of this CallbackConversationNotificationParticipants.
        :type: datetime
        """
        
        self._connected_time = connected_time

    @property
    def end_time(self):
        """
        Gets the end_time of this CallbackConversationNotificationParticipants.


        :return: The end_time of this CallbackConversationNotificationParticipants.
        :rtype: datetime
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """
        Sets the end_time of this CallbackConversationNotificationParticipants.


        :param end_time: The end_time of this CallbackConversationNotificationParticipants.
        :type: datetime
        """
        
        self._end_time = end_time

    @property
    def start_hold_time(self):
        """
        Gets the start_hold_time of this CallbackConversationNotificationParticipants.


        :return: The start_hold_time of this CallbackConversationNotificationParticipants.
        :rtype: datetime
        """
        return self._start_hold_time

    @start_hold_time.setter
    def start_hold_time(self, start_hold_time):
        """
        Sets the start_hold_time of this CallbackConversationNotificationParticipants.


        :param start_hold_time: The start_hold_time of this CallbackConversationNotificationParticipants.
        :type: datetime
        """
        
        self._start_hold_time = start_hold_time

    @property
    def purpose(self):
        """
        Gets the purpose of this CallbackConversationNotificationParticipants.


        :return: The purpose of this CallbackConversationNotificationParticipants.
        :rtype: str
        """
        return self._purpose

    @purpose.setter
    def purpose(self, purpose):
        """
        Sets the purpose of this CallbackConversationNotificationParticipants.


        :param purpose: The purpose of this CallbackConversationNotificationParticipants.
        :type: str
        """
        
        self._purpose = purpose

    @property
    def state(self):
        """
        Gets the state of this CallbackConversationNotificationParticipants.


        :return: The state of this CallbackConversationNotificationParticipants.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """
        Sets the state of this CallbackConversationNotificationParticipants.


        :param state: The state of this CallbackConversationNotificationParticipants.
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
        Gets the direction of this CallbackConversationNotificationParticipants.


        :return: The direction of this CallbackConversationNotificationParticipants.
        :rtype: str
        """
        return self._direction

    @direction.setter
    def direction(self, direction):
        """
        Sets the direction of this CallbackConversationNotificationParticipants.


        :param direction: The direction of this CallbackConversationNotificationParticipants.
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
        Gets the disconnect_type of this CallbackConversationNotificationParticipants.


        :return: The disconnect_type of this CallbackConversationNotificationParticipants.
        :rtype: str
        """
        return self._disconnect_type

    @disconnect_type.setter
    def disconnect_type(self, disconnect_type):
        """
        Sets the disconnect_type of this CallbackConversationNotificationParticipants.


        :param disconnect_type: The disconnect_type of this CallbackConversationNotificationParticipants.
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
        Gets the held of this CallbackConversationNotificationParticipants.


        :return: The held of this CallbackConversationNotificationParticipants.
        :rtype: bool
        """
        return self._held

    @held.setter
    def held(self, held):
        """
        Sets the held of this CallbackConversationNotificationParticipants.


        :param held: The held of this CallbackConversationNotificationParticipants.
        :type: bool
        """
        
        self._held = held

    @property
    def wrapup_required(self):
        """
        Gets the wrapup_required of this CallbackConversationNotificationParticipants.


        :return: The wrapup_required of this CallbackConversationNotificationParticipants.
        :rtype: bool
        """
        return self._wrapup_required

    @wrapup_required.setter
    def wrapup_required(self, wrapup_required):
        """
        Sets the wrapup_required of this CallbackConversationNotificationParticipants.


        :param wrapup_required: The wrapup_required of this CallbackConversationNotificationParticipants.
        :type: bool
        """
        
        self._wrapup_required = wrapup_required

    @property
    def wrapup_prompt(self):
        """
        Gets the wrapup_prompt of this CallbackConversationNotificationParticipants.


        :return: The wrapup_prompt of this CallbackConversationNotificationParticipants.
        :rtype: str
        """
        return self._wrapup_prompt

    @wrapup_prompt.setter
    def wrapup_prompt(self, wrapup_prompt):
        """
        Sets the wrapup_prompt of this CallbackConversationNotificationParticipants.


        :param wrapup_prompt: The wrapup_prompt of this CallbackConversationNotificationParticipants.
        :type: str
        """
        
        self._wrapup_prompt = wrapup_prompt

    @property
    def user(self):
        """
        Gets the user of this CallbackConversationNotificationParticipants.


        :return: The user of this CallbackConversationNotificationParticipants.
        :rtype: DependencyTrackingBuildNotificationNotificationUser
        """
        return self._user

    @user.setter
    def user(self, user):
        """
        Sets the user of this CallbackConversationNotificationParticipants.


        :param user: The user of this CallbackConversationNotificationParticipants.
        :type: DependencyTrackingBuildNotificationNotificationUser
        """
        
        self._user = user

    @property
    def queue(self):
        """
        Gets the queue of this CallbackConversationNotificationParticipants.


        :return: The queue of this CallbackConversationNotificationParticipants.
        :rtype: CallbackConversationNotificationUriReference
        """
        return self._queue

    @queue.setter
    def queue(self, queue):
        """
        Sets the queue of this CallbackConversationNotificationParticipants.


        :param queue: The queue of this CallbackConversationNotificationParticipants.
        :type: CallbackConversationNotificationUriReference
        """
        
        self._queue = queue

    @property
    def attributes(self):
        """
        Gets the attributes of this CallbackConversationNotificationParticipants.


        :return: The attributes of this CallbackConversationNotificationParticipants.
        :rtype: dict(str, str)
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """
        Sets the attributes of this CallbackConversationNotificationParticipants.


        :param attributes: The attributes of this CallbackConversationNotificationParticipants.
        :type: dict(str, str)
        """
        
        self._attributes = attributes

    @property
    def error_info(self):
        """
        Gets the error_info of this CallbackConversationNotificationParticipants.


        :return: The error_info of this CallbackConversationNotificationParticipants.
        :rtype: CallbackConversationNotificationErrorInfo
        """
        return self._error_info

    @error_info.setter
    def error_info(self, error_info):
        """
        Sets the error_info of this CallbackConversationNotificationParticipants.


        :param error_info: The error_info of this CallbackConversationNotificationParticipants.
        :type: CallbackConversationNotificationErrorInfo
        """
        
        self._error_info = error_info

    @property
    def script(self):
        """
        Gets the script of this CallbackConversationNotificationParticipants.


        :return: The script of this CallbackConversationNotificationParticipants.
        :rtype: CallbackConversationNotificationUriReference
        """
        return self._script

    @script.setter
    def script(self, script):
        """
        Sets the script of this CallbackConversationNotificationParticipants.


        :param script: The script of this CallbackConversationNotificationParticipants.
        :type: CallbackConversationNotificationUriReference
        """
        
        self._script = script

    @property
    def wrapup_timeout_ms(self):
        """
        Gets the wrapup_timeout_ms of this CallbackConversationNotificationParticipants.


        :return: The wrapup_timeout_ms of this CallbackConversationNotificationParticipants.
        :rtype: int
        """
        return self._wrapup_timeout_ms

    @wrapup_timeout_ms.setter
    def wrapup_timeout_ms(self, wrapup_timeout_ms):
        """
        Sets the wrapup_timeout_ms of this CallbackConversationNotificationParticipants.


        :param wrapup_timeout_ms: The wrapup_timeout_ms of this CallbackConversationNotificationParticipants.
        :type: int
        """
        
        self._wrapup_timeout_ms = wrapup_timeout_ms

    @property
    def wrapup_skipped(self):
        """
        Gets the wrapup_skipped of this CallbackConversationNotificationParticipants.


        :return: The wrapup_skipped of this CallbackConversationNotificationParticipants.
        :rtype: bool
        """
        return self._wrapup_skipped

    @wrapup_skipped.setter
    def wrapup_skipped(self, wrapup_skipped):
        """
        Sets the wrapup_skipped of this CallbackConversationNotificationParticipants.


        :param wrapup_skipped: The wrapup_skipped of this CallbackConversationNotificationParticipants.
        :type: bool
        """
        
        self._wrapup_skipped = wrapup_skipped

    @property
    def provider(self):
        """
        Gets the provider of this CallbackConversationNotificationParticipants.


        :return: The provider of this CallbackConversationNotificationParticipants.
        :rtype: str
        """
        return self._provider

    @provider.setter
    def provider(self, provider):
        """
        Sets the provider of this CallbackConversationNotificationParticipants.


        :param provider: The provider of this CallbackConversationNotificationParticipants.
        :type: str
        """
        
        self._provider = provider

    @property
    def external_contact(self):
        """
        Gets the external_contact of this CallbackConversationNotificationParticipants.


        :return: The external_contact of this CallbackConversationNotificationParticipants.
        :rtype: CallbackConversationNotificationUriReference
        """
        return self._external_contact

    @external_contact.setter
    def external_contact(self, external_contact):
        """
        Sets the external_contact of this CallbackConversationNotificationParticipants.


        :param external_contact: The external_contact of this CallbackConversationNotificationParticipants.
        :type: CallbackConversationNotificationUriReference
        """
        
        self._external_contact = external_contact

    @property
    def external_organization(self):
        """
        Gets the external_organization of this CallbackConversationNotificationParticipants.


        :return: The external_organization of this CallbackConversationNotificationParticipants.
        :rtype: CallbackConversationNotificationUriReference
        """
        return self._external_organization

    @external_organization.setter
    def external_organization(self, external_organization):
        """
        Sets the external_organization of this CallbackConversationNotificationParticipants.


        :param external_organization: The external_organization of this CallbackConversationNotificationParticipants.
        :type: CallbackConversationNotificationUriReference
        """
        
        self._external_organization = external_organization

    @property
    def wrapup(self):
        """
        Gets the wrapup of this CallbackConversationNotificationParticipants.


        :return: The wrapup of this CallbackConversationNotificationParticipants.
        :rtype: ConversationNotificationWrapup
        """
        return self._wrapup

    @wrapup.setter
    def wrapup(self, wrapup):
        """
        Sets the wrapup of this CallbackConversationNotificationParticipants.


        :param wrapup: The wrapup of this CallbackConversationNotificationParticipants.
        :type: ConversationNotificationWrapup
        """
        
        self._wrapup = wrapup

    @property
    def outbound_preview(self):
        """
        Gets the outbound_preview of this CallbackConversationNotificationParticipants.


        :return: The outbound_preview of this CallbackConversationNotificationParticipants.
        :rtype: ConversationNotificationDialerPreview
        """
        return self._outbound_preview

    @outbound_preview.setter
    def outbound_preview(self, outbound_preview):
        """
        Sets the outbound_preview of this CallbackConversationNotificationParticipants.


        :param outbound_preview: The outbound_preview of this CallbackConversationNotificationParticipants.
        :type: ConversationNotificationDialerPreview
        """
        
        self._outbound_preview = outbound_preview

    @property
    def callback_numbers(self):
        """
        Gets the callback_numbers of this CallbackConversationNotificationParticipants.


        :return: The callback_numbers of this CallbackConversationNotificationParticipants.
        :rtype: list[str]
        """
        return self._callback_numbers

    @callback_numbers.setter
    def callback_numbers(self, callback_numbers):
        """
        Sets the callback_numbers of this CallbackConversationNotificationParticipants.


        :param callback_numbers: The callback_numbers of this CallbackConversationNotificationParticipants.
        :type: list[str]
        """
        
        self._callback_numbers = callback_numbers

    @property
    def callback_user_name(self):
        """
        Gets the callback_user_name of this CallbackConversationNotificationParticipants.


        :return: The callback_user_name of this CallbackConversationNotificationParticipants.
        :rtype: str
        """
        return self._callback_user_name

    @callback_user_name.setter
    def callback_user_name(self, callback_user_name):
        """
        Sets the callback_user_name of this CallbackConversationNotificationParticipants.


        :param callback_user_name: The callback_user_name of this CallbackConversationNotificationParticipants.
        :type: str
        """
        
        self._callback_user_name = callback_user_name

    @property
    def skip_enabled(self):
        """
        Gets the skip_enabled of this CallbackConversationNotificationParticipants.


        :return: The skip_enabled of this CallbackConversationNotificationParticipants.
        :rtype: bool
        """
        return self._skip_enabled

    @skip_enabled.setter
    def skip_enabled(self, skip_enabled):
        """
        Sets the skip_enabled of this CallbackConversationNotificationParticipants.


        :param skip_enabled: The skip_enabled of this CallbackConversationNotificationParticipants.
        :type: bool
        """
        
        self._skip_enabled = skip_enabled

    @property
    def timeout_seconds(self):
        """
        Gets the timeout_seconds of this CallbackConversationNotificationParticipants.


        :return: The timeout_seconds of this CallbackConversationNotificationParticipants.
        :rtype: int
        """
        return self._timeout_seconds

    @timeout_seconds.setter
    def timeout_seconds(self, timeout_seconds):
        """
        Sets the timeout_seconds of this CallbackConversationNotificationParticipants.


        :param timeout_seconds: The timeout_seconds of this CallbackConversationNotificationParticipants.
        :type: int
        """
        
        self._timeout_seconds = timeout_seconds

    @property
    def callback_scheduled_time(self):
        """
        Gets the callback_scheduled_time of this CallbackConversationNotificationParticipants.


        :return: The callback_scheduled_time of this CallbackConversationNotificationParticipants.
        :rtype: datetime
        """
        return self._callback_scheduled_time

    @callback_scheduled_time.setter
    def callback_scheduled_time(self, callback_scheduled_time):
        """
        Sets the callback_scheduled_time of this CallbackConversationNotificationParticipants.


        :param callback_scheduled_time: The callback_scheduled_time of this CallbackConversationNotificationParticipants.
        :type: datetime
        """
        
        self._callback_scheduled_time = callback_scheduled_time

    @property
    def automated_callback_config_id(self):
        """
        Gets the automated_callback_config_id of this CallbackConversationNotificationParticipants.


        :return: The automated_callback_config_id of this CallbackConversationNotificationParticipants.
        :rtype: str
        """
        return self._automated_callback_config_id

    @automated_callback_config_id.setter
    def automated_callback_config_id(self, automated_callback_config_id):
        """
        Sets the automated_callback_config_id of this CallbackConversationNotificationParticipants.


        :param automated_callback_config_id: The automated_callback_config_id of this CallbackConversationNotificationParticipants.
        :type: str
        """
        
        self._automated_callback_config_id = automated_callback_config_id

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

