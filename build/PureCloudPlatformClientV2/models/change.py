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


class Change(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        Change - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'entity': 'AuditEntity',
            'pcProperty': 'str',
            'old_values': 'list[str]',
            'new_values': 'list[str]'
        }

        self.attribute_map = {
            'entity': 'entity',
            'pcProperty': 'property',
            'old_values': 'oldValues',
            'new_values': 'newValues'
        }

        self._entity = None
        self._pcProperty = None
        self._old_values = None
        self._new_values = None

    @property
    def entity(self):
        """
        Gets the entity of this Change.


        :return: The entity of this Change.
        :rtype: AuditEntity
        """
        return self._entity

    @entity.setter
    def entity(self, entity):
        """
        Sets the entity of this Change.


        :param entity: The entity of this Change.
        :type: AuditEntity
        """
        
        self._entity = entity

    @property
    def pcProperty(self):
        """
        Gets the pcProperty of this Change.
        The property that was changed

        :return: The pcProperty of this Change.
        :rtype: str
        """
        return self._pcProperty

    @pcProperty.setter
    def pcProperty(self, pcProperty):
        """
        Sets the pcProperty of this Change.
        The property that was changed

        :param pcProperty: The pcProperty of this Change.
        :type: str
        """
        
        self._pcProperty = pcProperty

    @property
    def old_values(self):
        """
        Gets the old_values of this Change.
        The old values which were modified and/or removed by this action.

        :return: The old_values of this Change.
        :rtype: list[str]
        """
        return self._old_values

    @old_values.setter
    def old_values(self, old_values):
        """
        Sets the old_values of this Change.
        The old values which were modified and/or removed by this action.

        :param old_values: The old_values of this Change.
        :type: list[str]
        """
        
        self._old_values = old_values

    @property
    def new_values(self):
        """
        Gets the new_values of this Change.
        The new values which were modified and/or added by this action.

        :return: The new_values of this Change.
        :rtype: list[str]
        """
        return self._new_values

    @new_values.setter
    def new_values(self, new_values):
        """
        Sets the new_values of this Change.
        The new values which were modified and/or added by this action.

        :param new_values: The new_values of this Change.
        :type: list[str]
        """
        
        self._new_values = new_values

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

