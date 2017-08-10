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


class EventLog(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        EventLog - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'name': 'str',
            'error_entity': 'UriReference',
            'related_entity': 'UriReference',
            'timestamp': 'datetime',
            'level': 'str',
            'category': 'str',
            'correlation_id': 'str',
            'event_message': 'EventMessage',
            'self_uri': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'error_entity': 'errorEntity',
            'related_entity': 'relatedEntity',
            'timestamp': 'timestamp',
            'level': 'level',
            'category': 'category',
            'correlation_id': 'correlationId',
            'event_message': 'eventMessage',
            'self_uri': 'selfUri'
        }

        self._id = None
        self._name = None
        self._error_entity = None
        self._related_entity = None
        self._timestamp = None
        self._level = None
        self._category = None
        self._correlation_id = None
        self._event_message = None
        self._self_uri = None

    @property
    def id(self):
        """
        Gets the id of this EventLog.
        The globally unique identifier for the object.

        :return: The id of this EventLog.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this EventLog.
        The globally unique identifier for the object.

        :param id: The id of this EventLog.
        :type: str
        """
        
        self._id = id

    @property
    def name(self):
        """
        Gets the name of this EventLog.


        :return: The name of this EventLog.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this EventLog.


        :param name: The name of this EventLog.
        :type: str
        """
        
        self._name = name

    @property
    def error_entity(self):
        """
        Gets the error_entity of this EventLog.


        :return: The error_entity of this EventLog.
        :rtype: UriReference
        """
        return self._error_entity

    @error_entity.setter
    def error_entity(self, error_entity):
        """
        Sets the error_entity of this EventLog.


        :param error_entity: The error_entity of this EventLog.
        :type: UriReference
        """
        
        self._error_entity = error_entity

    @property
    def related_entity(self):
        """
        Gets the related_entity of this EventLog.


        :return: The related_entity of this EventLog.
        :rtype: UriReference
        """
        return self._related_entity

    @related_entity.setter
    def related_entity(self, related_entity):
        """
        Sets the related_entity of this EventLog.


        :param related_entity: The related_entity of this EventLog.
        :type: UriReference
        """
        
        self._related_entity = related_entity

    @property
    def timestamp(self):
        """
        Gets the timestamp of this EventLog.
        Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ

        :return: The timestamp of this EventLog.
        :rtype: datetime
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """
        Sets the timestamp of this EventLog.
        Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ

        :param timestamp: The timestamp of this EventLog.
        :type: datetime
        """
        
        self._timestamp = timestamp

    @property
    def level(self):
        """
        Gets the level of this EventLog.


        :return: The level of this EventLog.
        :rtype: str
        """
        return self._level

    @level.setter
    def level(self, level):
        """
        Sets the level of this EventLog.


        :param level: The level of this EventLog.
        :type: str
        """
        allowed_values = ["INFO", "WARNING", "ERROR"]
        if level.lower() not in map(str.lower, allowed_values):
            # print "Invalid value for level -> " + level
            self._level = "outdated_sdk_version"
        else:
            self._level = level

    @property
    def category(self):
        """
        Gets the category of this EventLog.


        :return: The category of this EventLog.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """
        Sets the category of this EventLog.


        :param category: The category of this EventLog.
        :type: str
        """
        allowed_values = ["CALLBACK", "CALL_RESTRICTION", "CALL_RULE", "CAMPAIGN", "CAMPAIGN_RULE", "CONTACT_LIST_FILTER", "ENTITY_LIMIT", "IMPORT_ERROR", "ORGANIZATION_CONFIGURATION", "SCHEDULE"]
        if category.lower() not in map(str.lower, allowed_values):
            # print "Invalid value for category -> " + category
            self._category = "outdated_sdk_version"
        else:
            self._category = category

    @property
    def correlation_id(self):
        """
        Gets the correlation_id of this EventLog.


        :return: The correlation_id of this EventLog.
        :rtype: str
        """
        return self._correlation_id

    @correlation_id.setter
    def correlation_id(self, correlation_id):
        """
        Sets the correlation_id of this EventLog.


        :param correlation_id: The correlation_id of this EventLog.
        :type: str
        """
        
        self._correlation_id = correlation_id

    @property
    def event_message(self):
        """
        Gets the event_message of this EventLog.


        :return: The event_message of this EventLog.
        :rtype: EventMessage
        """
        return self._event_message

    @event_message.setter
    def event_message(self, event_message):
        """
        Sets the event_message of this EventLog.


        :param event_message: The event_message of this EventLog.
        :type: EventMessage
        """
        
        self._event_message = event_message

    @property
    def self_uri(self):
        """
        Gets the self_uri of this EventLog.
        The URI for this object

        :return: The self_uri of this EventLog.
        :rtype: str
        """
        return self._self_uri

    @self_uri.setter
    def self_uri(self, self_uri):
        """
        Sets the self_uri of this EventLog.
        The URI for this object

        :param self_uri: The self_uri of this EventLog.
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

