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

class CreateServiceGoalGroupRequest(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        CreateServiceGoalGroupRequest - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'name': 'str',
            'goals': 'ServiceGoalGroupGoals',
            'queue_media_associations': 'list[CreateQueueMediaAssociationRequest]'
        }

        self.attribute_map = {
            'name': 'name',
            'goals': 'goals',
            'queue_media_associations': 'queueMediaAssociations'
        }

        self._name = None
        self._goals = None
        self._queue_media_associations = None

    @property
    def name(self):
        """
        Gets the name of this CreateServiceGoalGroupRequest.
        name

        :return: The name of this CreateServiceGoalGroupRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this CreateServiceGoalGroupRequest.
        name

        :param name: The name of this CreateServiceGoalGroupRequest.
        :type: str
        """
        
        self._name = name

    @property
    def goals(self):
        """
        Gets the goals of this CreateServiceGoalGroupRequest.
        Goals defined for this service goal group

        :return: The goals of this CreateServiceGoalGroupRequest.
        :rtype: ServiceGoalGroupGoals
        """
        return self._goals

    @goals.setter
    def goals(self, goals):
        """
        Sets the goals of this CreateServiceGoalGroupRequest.
        Goals defined for this service goal group

        :param goals: The goals of this CreateServiceGoalGroupRequest.
        :type: ServiceGoalGroupGoals
        """
        
        self._goals = goals

    @property
    def queue_media_associations(self):
        """
        Gets the queue_media_associations of this CreateServiceGoalGroupRequest.
        List of queues and media types from that queue to associate with this service goal group

        :return: The queue_media_associations of this CreateServiceGoalGroupRequest.
        :rtype: list[CreateQueueMediaAssociationRequest]
        """
        return self._queue_media_associations

    @queue_media_associations.setter
    def queue_media_associations(self, queue_media_associations):
        """
        Sets the queue_media_associations of this CreateServiceGoalGroupRequest.
        List of queues and media types from that queue to associate with this service goal group

        :param queue_media_associations: The queue_media_associations of this CreateServiceGoalGroupRequest.
        :type: list[CreateQueueMediaAssociationRequest]
        """
        
        self._queue_media_associations = queue_media_associations

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

