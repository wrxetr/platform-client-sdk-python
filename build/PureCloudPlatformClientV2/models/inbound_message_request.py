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


class InboundMessageRequest(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        InboundMessageRequest - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'queue_id': 'str',
            'flow_id': 'str',
            'provider': 'str',
            'skill_ids': 'list[str]',
            'language_id': 'str',
            'priority': 'int',
            'attributes': 'dict(str, str)',
            'to_address': 'str',
            'to_name': 'str',
            'from_address': 'str',
            'from_name': 'str',
            'subject': 'str'
        }

        self.attribute_map = {
            'queue_id': 'queueId',
            'flow_id': 'flowId',
            'provider': 'provider',
            'skill_ids': 'skillIds',
            'language_id': 'languageId',
            'priority': 'priority',
            'attributes': 'attributes',
            'to_address': 'toAddress',
            'to_name': 'toName',
            'from_address': 'fromAddress',
            'from_name': 'fromName',
            'subject': 'subject'
        }

        self._queue_id = None
        self._flow_id = None
        self._provider = None
        self._skill_ids = None
        self._language_id = None
        self._priority = None
        self._attributes = None
        self._to_address = None
        self._to_name = None
        self._from_address = None
        self._from_name = None
        self._subject = None

    @property
    def queue_id(self):
        """
        Gets the queue_id of this InboundMessageRequest.
        The ID of the queue to use for routing the email conversation. This field is mutually exclusive with flowId

        :return: The queue_id of this InboundMessageRequest.
        :rtype: str
        """
        return self._queue_id

    @queue_id.setter
    def queue_id(self, queue_id):
        """
        Sets the queue_id of this InboundMessageRequest.
        The ID of the queue to use for routing the email conversation. This field is mutually exclusive with flowId

        :param queue_id: The queue_id of this InboundMessageRequest.
        :type: str
        """
        
        self._queue_id = queue_id

    @property
    def flow_id(self):
        """
        Gets the flow_id of this InboundMessageRequest.
        The ID of the flow to use for routing email conversation. This field is mutually exclusive with queueId

        :return: The flow_id of this InboundMessageRequest.
        :rtype: str
        """
        return self._flow_id

    @flow_id.setter
    def flow_id(self, flow_id):
        """
        Sets the flow_id of this InboundMessageRequest.
        The ID of the flow to use for routing email conversation. This field is mutually exclusive with queueId

        :param flow_id: The flow_id of this InboundMessageRequest.
        :type: str
        """
        
        self._flow_id = flow_id

    @property
    def provider(self):
        """
        Gets the provider of this InboundMessageRequest.
        The name of the provider that is sourcing the email such as Oracle, Salesforce, etc.

        :return: The provider of this InboundMessageRequest.
        :rtype: str
        """
        return self._provider

    @provider.setter
    def provider(self, provider):
        """
        Sets the provider of this InboundMessageRequest.
        The name of the provider that is sourcing the email such as Oracle, Salesforce, etc.

        :param provider: The provider of this InboundMessageRequest.
        :type: str
        """
        
        self._provider = provider

    @property
    def skill_ids(self):
        """
        Gets the skill_ids of this InboundMessageRequest.
        The list of skill ID's to use for routing.

        :return: The skill_ids of this InboundMessageRequest.
        :rtype: list[str]
        """
        return self._skill_ids

    @skill_ids.setter
    def skill_ids(self, skill_ids):
        """
        Sets the skill_ids of this InboundMessageRequest.
        The list of skill ID's to use for routing.

        :param skill_ids: The skill_ids of this InboundMessageRequest.
        :type: list[str]
        """
        
        self._skill_ids = skill_ids

    @property
    def language_id(self):
        """
        Gets the language_id of this InboundMessageRequest.
        The ID of the language to use for routing.

        :return: The language_id of this InboundMessageRequest.
        :rtype: str
        """
        return self._language_id

    @language_id.setter
    def language_id(self, language_id):
        """
        Sets the language_id of this InboundMessageRequest.
        The ID of the language to use for routing.

        :param language_id: The language_id of this InboundMessageRequest.
        :type: str
        """
        
        self._language_id = language_id

    @property
    def priority(self):
        """
        Gets the priority of this InboundMessageRequest.
        The priority to assign to the conversation for routing.

        :return: The priority of this InboundMessageRequest.
        :rtype: int
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        """
        Sets the priority of this InboundMessageRequest.
        The priority to assign to the conversation for routing.

        :param priority: The priority of this InboundMessageRequest.
        :type: int
        """
        
        self._priority = priority

    @property
    def attributes(self):
        """
        Gets the attributes of this InboundMessageRequest.
        The list of attributes to associate with the customer participant.

        :return: The attributes of this InboundMessageRequest.
        :rtype: dict(str, str)
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """
        Sets the attributes of this InboundMessageRequest.
        The list of attributes to associate with the customer participant.

        :param attributes: The attributes of this InboundMessageRequest.
        :type: dict(str, str)
        """
        
        self._attributes = attributes

    @property
    def to_address(self):
        """
        Gets the to_address of this InboundMessageRequest.
        The email address of the recipient of the email.

        :return: The to_address of this InboundMessageRequest.
        :rtype: str
        """
        return self._to_address

    @to_address.setter
    def to_address(self, to_address):
        """
        Sets the to_address of this InboundMessageRequest.
        The email address of the recipient of the email.

        :param to_address: The to_address of this InboundMessageRequest.
        :type: str
        """
        
        self._to_address = to_address

    @property
    def to_name(self):
        """
        Gets the to_name of this InboundMessageRequest.
        The name of the recipient of the email.

        :return: The to_name of this InboundMessageRequest.
        :rtype: str
        """
        return self._to_name

    @to_name.setter
    def to_name(self, to_name):
        """
        Sets the to_name of this InboundMessageRequest.
        The name of the recipient of the email.

        :param to_name: The to_name of this InboundMessageRequest.
        :type: str
        """
        
        self._to_name = to_name

    @property
    def from_address(self):
        """
        Gets the from_address of this InboundMessageRequest.
        The email address of the sender of the email.

        :return: The from_address of this InboundMessageRequest.
        :rtype: str
        """
        return self._from_address

    @from_address.setter
    def from_address(self, from_address):
        """
        Sets the from_address of this InboundMessageRequest.
        The email address of the sender of the email.

        :param from_address: The from_address of this InboundMessageRequest.
        :type: str
        """
        
        self._from_address = from_address

    @property
    def from_name(self):
        """
        Gets the from_name of this InboundMessageRequest.
        The name of the sender of the email.

        :return: The from_name of this InboundMessageRequest.
        :rtype: str
        """
        return self._from_name

    @from_name.setter
    def from_name(self, from_name):
        """
        Sets the from_name of this InboundMessageRequest.
        The name of the sender of the email.

        :param from_name: The from_name of this InboundMessageRequest.
        :type: str
        """
        
        self._from_name = from_name

    @property
    def subject(self):
        """
        Gets the subject of this InboundMessageRequest.
        The subject of the email

        :return: The subject of this InboundMessageRequest.
        :rtype: str
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        """
        Sets the subject of this InboundMessageRequest.
        The subject of the email

        :param subject: The subject of this InboundMessageRequest.
        :type: str
        """
        
        self._subject = subject

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

