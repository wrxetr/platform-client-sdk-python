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


class ConversationNotificationScreenshares(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        ConversationNotificationScreenshares - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'state': 'str',
            'pcSelf': 'ConversationNotificationAddress',
            'id': 'str',
            'context': 'str',
            'sharing': 'bool',
            'provider': 'str',
            'disconnect_type': 'str',
            'connected_time': 'datetime',
            'disconnected_time': 'datetime',
            'additional_properties': 'object'
        }

        self.attribute_map = {
            'state': 'state',
            'pcSelf': 'self',
            'id': 'id',
            'context': 'context',
            'sharing': 'sharing',
            'provider': 'provider',
            'disconnect_type': 'disconnectType',
            'connected_time': 'connectedTime',
            'disconnected_time': 'disconnectedTime',
            'additional_properties': 'additionalProperties'
        }

        self._state = None
        self._pcSelf = None
        self._id = None
        self._context = None
        self._sharing = None
        self._provider = None
        self._disconnect_type = None
        self._connected_time = None
        self._disconnected_time = None
        self._additional_properties = None

    @property
    def state(self):
        """
        Gets the state of this ConversationNotificationScreenshares.


        :return: The state of this ConversationNotificationScreenshares.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """
        Sets the state of this ConversationNotificationScreenshares.


        :param state: The state of this ConversationNotificationScreenshares.
        :type: str
        """
        allowed_values = ["ALERTING", "DIALING", "CONTACTING", "OFFERING", "CONNECTED", "DISCONNECTED", "TERMINATED", "NONE"]
        if state.lower() not in map(str.lower, allowed_values):
            # print "Invalid value for state -> " + state
            self._state = "outdated_sdk_version"
        else:
            self._state = state.lower()

    @property
    def pcSelf(self):
        """
        Gets the pcSelf of this ConversationNotificationScreenshares.


        :return: The pcSelf of this ConversationNotificationScreenshares.
        :rtype: ConversationNotificationAddress
        """
        return self._pcSelf

    @pcSelf.setter
    def pcSelf(self, pcSelf):
        """
        Sets the pcSelf of this ConversationNotificationScreenshares.


        :param pcSelf: The pcSelf of this ConversationNotificationScreenshares.
        :type: ConversationNotificationAddress
        """
        
        self._pcSelf = pcSelf

    @property
    def id(self):
        """
        Gets the id of this ConversationNotificationScreenshares.


        :return: The id of this ConversationNotificationScreenshares.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ConversationNotificationScreenshares.


        :param id: The id of this ConversationNotificationScreenshares.
        :type: str
        """
        
        self._id = id

    @property
    def context(self):
        """
        Gets the context of this ConversationNotificationScreenshares.


        :return: The context of this ConversationNotificationScreenshares.
        :rtype: str
        """
        return self._context

    @context.setter
    def context(self, context):
        """
        Sets the context of this ConversationNotificationScreenshares.


        :param context: The context of this ConversationNotificationScreenshares.
        :type: str
        """
        
        self._context = context

    @property
    def sharing(self):
        """
        Gets the sharing of this ConversationNotificationScreenshares.


        :return: The sharing of this ConversationNotificationScreenshares.
        :rtype: bool
        """
        return self._sharing

    @sharing.setter
    def sharing(self, sharing):
        """
        Sets the sharing of this ConversationNotificationScreenshares.


        :param sharing: The sharing of this ConversationNotificationScreenshares.
        :type: bool
        """
        
        self._sharing = sharing

    @property
    def provider(self):
        """
        Gets the provider of this ConversationNotificationScreenshares.


        :return: The provider of this ConversationNotificationScreenshares.
        :rtype: str
        """
        return self._provider

    @provider.setter
    def provider(self, provider):
        """
        Sets the provider of this ConversationNotificationScreenshares.


        :param provider: The provider of this ConversationNotificationScreenshares.
        :type: str
        """
        
        self._provider = provider

    @property
    def disconnect_type(self):
        """
        Gets the disconnect_type of this ConversationNotificationScreenshares.


        :return: The disconnect_type of this ConversationNotificationScreenshares.
        :rtype: str
        """
        return self._disconnect_type

    @disconnect_type.setter
    def disconnect_type(self, disconnect_type):
        """
        Sets the disconnect_type of this ConversationNotificationScreenshares.


        :param disconnect_type: The disconnect_type of this ConversationNotificationScreenshares.
        :type: str
        """
        allowed_values = ["ENDPOINT", "CLIENT", "SYSTEM", "TIMEOUT", "TRANSFER", "TRANSFER_CONFERENCE", "TRANSFER_CONSULT", "TRANSFER_FORWARD", "TRANSFER_NOANSWER", "TRANSFER_NOTAVAILABLE", "TRANSPORT_FAILURE", "ERROR", "PEER", "OTHER", "SPAM", "UNCALLABLE"]
        if disconnect_type.lower() not in map(str.lower, allowed_values):
            # print "Invalid value for disconnect_type -> " + disconnect_type
            self._disconnect_type = "outdated_sdk_version"
        else:
            self._disconnect_type = disconnect_type.lower()

    @property
    def connected_time(self):
        """
        Gets the connected_time of this ConversationNotificationScreenshares.


        :return: The connected_time of this ConversationNotificationScreenshares.
        :rtype: datetime
        """
        return self._connected_time

    @connected_time.setter
    def connected_time(self, connected_time):
        """
        Sets the connected_time of this ConversationNotificationScreenshares.


        :param connected_time: The connected_time of this ConversationNotificationScreenshares.
        :type: datetime
        """
        
        self._connected_time = connected_time

    @property
    def disconnected_time(self):
        """
        Gets the disconnected_time of this ConversationNotificationScreenshares.


        :return: The disconnected_time of this ConversationNotificationScreenshares.
        :rtype: datetime
        """
        return self._disconnected_time

    @disconnected_time.setter
    def disconnected_time(self, disconnected_time):
        """
        Sets the disconnected_time of this ConversationNotificationScreenshares.


        :param disconnected_time: The disconnected_time of this ConversationNotificationScreenshares.
        :type: datetime
        """
        
        self._disconnected_time = disconnected_time

    @property
    def additional_properties(self):
        """
        Gets the additional_properties of this ConversationNotificationScreenshares.


        :return: The additional_properties of this ConversationNotificationScreenshares.
        :rtype: object
        """
        return self._additional_properties

    @additional_properties.setter
    def additional_properties(self, additional_properties):
        """
        Sets the additional_properties of this ConversationNotificationScreenshares.


        :param additional_properties: The additional_properties of this ConversationNotificationScreenshares.
        :type: object
        """
        
        self._additional_properties = additional_properties

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

