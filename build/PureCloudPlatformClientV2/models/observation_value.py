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


class ObservationValue(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        ObservationValue - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'observation_date': 'datetime',
            'conversation_id': 'str',
            'session_id': 'str',
            'requested_routing_skill_ids': 'list[str]',
            'requested_language_id': 'str',
            'participant_name': 'str',
            'user_id': 'str',
            'direction': 'str',
            'converted_from': 'str',
            'converted_to': 'str',
            'address_from': 'str',
            'address_to': 'str',
            'ani': 'str',
            'dnis': 'str'
        }

        self.attribute_map = {
            'observation_date': 'observationDate',
            'conversation_id': 'conversationId',
            'session_id': 'sessionId',
            'requested_routing_skill_ids': 'requestedRoutingSkillIds',
            'requested_language_id': 'requestedLanguageId',
            'participant_name': 'participantName',
            'user_id': 'userId',
            'direction': 'direction',
            'converted_from': 'convertedFrom',
            'converted_to': 'convertedTo',
            'address_from': 'addressFrom',
            'address_to': 'addressTo',
            'ani': 'ani',
            'dnis': 'dnis'
        }

        self._observation_date = None
        self._conversation_id = None
        self._session_id = None
        self._requested_routing_skill_ids = None
        self._requested_language_id = None
        self._participant_name = None
        self._user_id = None
        self._direction = None
        self._converted_from = None
        self._converted_to = None
        self._address_from = None
        self._address_to = None
        self._ani = None
        self._dnis = None

    @property
    def observation_date(self):
        """
        Gets the observation_date of this ObservationValue.
        The time at which the observation occurred. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ

        :return: The observation_date of this ObservationValue.
        :rtype: datetime
        """
        return self._observation_date

    @observation_date.setter
    def observation_date(self, observation_date):
        """
        Sets the observation_date of this ObservationValue.
        The time at which the observation occurred. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ

        :param observation_date: The observation_date of this ObservationValue.
        :type: datetime
        """
        
        self._observation_date = observation_date

    @property
    def conversation_id(self):
        """
        Gets the conversation_id of this ObservationValue.
        Unique identifier for the conversation

        :return: The conversation_id of this ObservationValue.
        :rtype: str
        """
        return self._conversation_id

    @conversation_id.setter
    def conversation_id(self, conversation_id):
        """
        Sets the conversation_id of this ObservationValue.
        Unique identifier for the conversation

        :param conversation_id: The conversation_id of this ObservationValue.
        :type: str
        """
        
        self._conversation_id = conversation_id

    @property
    def session_id(self):
        """
        Gets the session_id of this ObservationValue.
        The unique identifier of this session

        :return: The session_id of this ObservationValue.
        :rtype: str
        """
        return self._session_id

    @session_id.setter
    def session_id(self, session_id):
        """
        Sets the session_id of this ObservationValue.
        The unique identifier of this session

        :param session_id: The session_id of this ObservationValue.
        :type: str
        """
        
        self._session_id = session_id

    @property
    def requested_routing_skill_ids(self):
        """
        Gets the requested_routing_skill_ids of this ObservationValue.
        Unique identifier for a skill requested for an interaction

        :return: The requested_routing_skill_ids of this ObservationValue.
        :rtype: list[str]
        """
        return self._requested_routing_skill_ids

    @requested_routing_skill_ids.setter
    def requested_routing_skill_ids(self, requested_routing_skill_ids):
        """
        Sets the requested_routing_skill_ids of this ObservationValue.
        Unique identifier for a skill requested for an interaction

        :param requested_routing_skill_ids: The requested_routing_skill_ids of this ObservationValue.
        :type: list[str]
        """
        
        self._requested_routing_skill_ids = requested_routing_skill_ids

    @property
    def requested_language_id(self):
        """
        Gets the requested_language_id of this ObservationValue.
        Unique identifier for the language requested for an interaction

        :return: The requested_language_id of this ObservationValue.
        :rtype: str
        """
        return self._requested_language_id

    @requested_language_id.setter
    def requested_language_id(self, requested_language_id):
        """
        Sets the requested_language_id of this ObservationValue.
        Unique identifier for the language requested for an interaction

        :param requested_language_id: The requested_language_id of this ObservationValue.
        :type: str
        """
        
        self._requested_language_id = requested_language_id

    @property
    def participant_name(self):
        """
        Gets the participant_name of this ObservationValue.
        A human readable name identifying the participant

        :return: The participant_name of this ObservationValue.
        :rtype: str
        """
        return self._participant_name

    @participant_name.setter
    def participant_name(self, participant_name):
        """
        Sets the participant_name of this ObservationValue.
        A human readable name identifying the participant

        :param participant_name: The participant_name of this ObservationValue.
        :type: str
        """
        
        self._participant_name = participant_name

    @property
    def user_id(self):
        """
        Gets the user_id of this ObservationValue.
        Unique identifier for the user

        :return: The user_id of this ObservationValue.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """
        Sets the user_id of this ObservationValue.
        Unique identifier for the user

        :param user_id: The user_id of this ObservationValue.
        :type: str
        """
        
        self._user_id = user_id

    @property
    def direction(self):
        """
        Gets the direction of this ObservationValue.
        The direction of the communication

        :return: The direction of this ObservationValue.
        :rtype: str
        """
        return self._direction

    @direction.setter
    def direction(self, direction):
        """
        Sets the direction of this ObservationValue.
        The direction of the communication

        :param direction: The direction of this ObservationValue.
        :type: str
        """
        allowed_values = ["inbound", "outbound"]
        if direction.lower() not in map(str.lower, allowed_values):
            # print "Invalid value for direction -> " + direction
            self._direction = "outdated_sdk_version"
        else:
            self._direction = direction

    @property
    def converted_from(self):
        """
        Gets the converted_from of this ObservationValue.
        Session media type that was converted from in case of a media type conversion

        :return: The converted_from of this ObservationValue.
        :rtype: str
        """
        return self._converted_from

    @converted_from.setter
    def converted_from(self, converted_from):
        """
        Sets the converted_from of this ObservationValue.
        Session media type that was converted from in case of a media type conversion

        :param converted_from: The converted_from of this ObservationValue.
        :type: str
        """
        
        self._converted_from = converted_from

    @property
    def converted_to(self):
        """
        Gets the converted_to of this ObservationValue.
        Session media type that was converted to in case of a media type conversion

        :return: The converted_to of this ObservationValue.
        :rtype: str
        """
        return self._converted_to

    @converted_to.setter
    def converted_to(self, converted_to):
        """
        Sets the converted_to of this ObservationValue.
        Session media type that was converted to in case of a media type conversion

        :param converted_to: The converted_to of this ObservationValue.
        :type: str
        """
        
        self._converted_to = converted_to

    @property
    def address_from(self):
        """
        Gets the address_from of this ObservationValue.
        The address that initiated an action

        :return: The address_from of this ObservationValue.
        :rtype: str
        """
        return self._address_from

    @address_from.setter
    def address_from(self, address_from):
        """
        Sets the address_from of this ObservationValue.
        The address that initiated an action

        :param address_from: The address_from of this ObservationValue.
        :type: str
        """
        
        self._address_from = address_from

    @property
    def address_to(self):
        """
        Gets the address_to of this ObservationValue.
        The address receiving an action

        :return: The address_to of this ObservationValue.
        :rtype: str
        """
        return self._address_to

    @address_to.setter
    def address_to(self, address_to):
        """
        Sets the address_to of this ObservationValue.
        The address receiving an action

        :param address_to: The address_to of this ObservationValue.
        :type: str
        """
        
        self._address_to = address_to

    @property
    def ani(self):
        """
        Gets the ani of this ObservationValue.
        Automatic Number Identification (caller's number)

        :return: The ani of this ObservationValue.
        :rtype: str
        """
        return self._ani

    @ani.setter
    def ani(self, ani):
        """
        Sets the ani of this ObservationValue.
        Automatic Number Identification (caller's number)

        :param ani: The ani of this ObservationValue.
        :type: str
        """
        
        self._ani = ani

    @property
    def dnis(self):
        """
        Gets the dnis of this ObservationValue.
        Dialed number identification service (number dialed by the calling party)

        :return: The dnis of this ObservationValue.
        :rtype: str
        """
        return self._dnis

    @dnis.setter
    def dnis(self, dnis):
        """
        Sets the dnis of this ObservationValue.
        Dialed number identification service (number dialed by the calling party)

        :param dnis: The dnis of this ObservationValue.
        :type: str
        """
        
        self._dnis = dnis

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

