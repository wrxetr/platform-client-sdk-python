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

class InboundRoute(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        InboundRoute - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'name': 'str',
            'pattern': 'str',
            'queue': 'DomainEntityRef',
            'priority': 'int',
            'skills': 'list[DomainEntityRef]',
            'language': 'DomainEntityRef',
            'from_name': 'str',
            'from_email': 'str',
            'flow': 'DomainEntityRef',
            'reply_email_address': 'QueueEmailAddress',
            'auto_bcc': 'list[EmailAddress]',
            'spam_flow': 'DomainEntityRef',
            'self_uri': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'pattern': 'pattern',
            'queue': 'queue',
            'priority': 'priority',
            'skills': 'skills',
            'language': 'language',
            'from_name': 'fromName',
            'from_email': 'fromEmail',
            'flow': 'flow',
            'reply_email_address': 'replyEmailAddress',
            'auto_bcc': 'autoBcc',
            'spam_flow': 'spamFlow',
            'self_uri': 'selfUri'
        }

        self._id = None
        self._name = None
        self._pattern = None
        self._queue = None
        self._priority = None
        self._skills = None
        self._language = None
        self._from_name = None
        self._from_email = None
        self._flow = None
        self._reply_email_address = None
        self._auto_bcc = None
        self._spam_flow = None
        self._self_uri = None

    @property
    def id(self):
        """
        Gets the id of this InboundRoute.
        The globally unique identifier for the object.

        :return: The id of this InboundRoute.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this InboundRoute.
        The globally unique identifier for the object.

        :param id: The id of this InboundRoute.
        :type: str
        """
        
        self._id = id

    @property
    def name(self):
        """
        Gets the name of this InboundRoute.


        :return: The name of this InboundRoute.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this InboundRoute.


        :param name: The name of this InboundRoute.
        :type: str
        """
        
        self._name = name

    @property
    def pattern(self):
        """
        Gets the pattern of this InboundRoute.
        The search pattern that the mailbox name should match.

        :return: The pattern of this InboundRoute.
        :rtype: str
        """
        return self._pattern

    @pattern.setter
    def pattern(self, pattern):
        """
        Sets the pattern of this InboundRoute.
        The search pattern that the mailbox name should match.

        :param pattern: The pattern of this InboundRoute.
        :type: str
        """
        
        self._pattern = pattern

    @property
    def queue(self):
        """
        Gets the queue of this InboundRoute.
        The queue to route the emails to.

        :return: The queue of this InboundRoute.
        :rtype: DomainEntityRef
        """
        return self._queue

    @queue.setter
    def queue(self, queue):
        """
        Sets the queue of this InboundRoute.
        The queue to route the emails to.

        :param queue: The queue of this InboundRoute.
        :type: DomainEntityRef
        """
        
        self._queue = queue

    @property
    def priority(self):
        """
        Gets the priority of this InboundRoute.
        The priority to use for routing.

        :return: The priority of this InboundRoute.
        :rtype: int
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        """
        Sets the priority of this InboundRoute.
        The priority to use for routing.

        :param priority: The priority of this InboundRoute.
        :type: int
        """
        
        self._priority = priority

    @property
    def skills(self):
        """
        Gets the skills of this InboundRoute.
        The skills to use for routing.

        :return: The skills of this InboundRoute.
        :rtype: list[DomainEntityRef]
        """
        return self._skills

    @skills.setter
    def skills(self, skills):
        """
        Sets the skills of this InboundRoute.
        The skills to use for routing.

        :param skills: The skills of this InboundRoute.
        :type: list[DomainEntityRef]
        """
        
        self._skills = skills

    @property
    def language(self):
        """
        Gets the language of this InboundRoute.
        The language to use for routing.

        :return: The language of this InboundRoute.
        :rtype: DomainEntityRef
        """
        return self._language

    @language.setter
    def language(self, language):
        """
        Sets the language of this InboundRoute.
        The language to use for routing.

        :param language: The language of this InboundRoute.
        :type: DomainEntityRef
        """
        
        self._language = language

    @property
    def from_name(self):
        """
        Gets the from_name of this InboundRoute.
        The sender name to use for outgoing replies.

        :return: The from_name of this InboundRoute.
        :rtype: str
        """
        return self._from_name

    @from_name.setter
    def from_name(self, from_name):
        """
        Sets the from_name of this InboundRoute.
        The sender name to use for outgoing replies.

        :param from_name: The from_name of this InboundRoute.
        :type: str
        """
        
        self._from_name = from_name

    @property
    def from_email(self):
        """
        Gets the from_email of this InboundRoute.
        The sender email to use for outgoing replies.

        :return: The from_email of this InboundRoute.
        :rtype: str
        """
        return self._from_email

    @from_email.setter
    def from_email(self, from_email):
        """
        Sets the from_email of this InboundRoute.
        The sender email to use for outgoing replies.

        :param from_email: The from_email of this InboundRoute.
        :type: str
        """
        
        self._from_email = from_email

    @property
    def flow(self):
        """
        Gets the flow of this InboundRoute.
        The flow to use for processing the email.

        :return: The flow of this InboundRoute.
        :rtype: DomainEntityRef
        """
        return self._flow

    @flow.setter
    def flow(self, flow):
        """
        Sets the flow of this InboundRoute.
        The flow to use for processing the email.

        :param flow: The flow of this InboundRoute.
        :type: DomainEntityRef
        """
        
        self._flow = flow

    @property
    def reply_email_address(self):
        """
        Gets the reply_email_address of this InboundRoute.
        The route to use for email replies.

        :return: The reply_email_address of this InboundRoute.
        :rtype: QueueEmailAddress
        """
        return self._reply_email_address

    @reply_email_address.setter
    def reply_email_address(self, reply_email_address):
        """
        Sets the reply_email_address of this InboundRoute.
        The route to use for email replies.

        :param reply_email_address: The reply_email_address of this InboundRoute.
        :type: QueueEmailAddress
        """
        
        self._reply_email_address = reply_email_address

    @property
    def auto_bcc(self):
        """
        Gets the auto_bcc of this InboundRoute.
        The recipients that should be  automatically blind copied on outbound emails associated with this InboundRoute.

        :return: The auto_bcc of this InboundRoute.
        :rtype: list[EmailAddress]
        """
        return self._auto_bcc

    @auto_bcc.setter
    def auto_bcc(self, auto_bcc):
        """
        Sets the auto_bcc of this InboundRoute.
        The recipients that should be  automatically blind copied on outbound emails associated with this InboundRoute.

        :param auto_bcc: The auto_bcc of this InboundRoute.
        :type: list[EmailAddress]
        """
        
        self._auto_bcc = auto_bcc

    @property
    def spam_flow(self):
        """
        Gets the spam_flow of this InboundRoute.
        The flow to use for processing inbound emails that have been marked as spam.

        :return: The spam_flow of this InboundRoute.
        :rtype: DomainEntityRef
        """
        return self._spam_flow

    @spam_flow.setter
    def spam_flow(self, spam_flow):
        """
        Sets the spam_flow of this InboundRoute.
        The flow to use for processing inbound emails that have been marked as spam.

        :param spam_flow: The spam_flow of this InboundRoute.
        :type: DomainEntityRef
        """
        
        self._spam_flow = spam_flow

    @property
    def self_uri(self):
        """
        Gets the self_uri of this InboundRoute.
        The URI for this object

        :return: The self_uri of this InboundRoute.
        :rtype: str
        """
        return self._self_uri

    @self_uri.setter
    def self_uri(self, self_uri):
        """
        Sets the self_uri of this InboundRoute.
        The URI for this object

        :param self_uri: The self_uri of this InboundRoute.
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

