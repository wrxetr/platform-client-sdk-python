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

class ScimV2Group(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        ScimV2Group - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'schemas': 'list[str]',
            'display_name': 'str',
            'members': 'list[ScimV2MemberReference]',
            'meta': 'ScimMetadata'
        }

        self.attribute_map = {
            'id': 'id',
            'schemas': 'schemas',
            'display_name': 'displayName',
            'members': 'members',
            'meta': 'meta'
        }

        self._id = None
        self._schemas = None
        self._display_name = None
        self._members = None
        self._meta = None

    @property
    def id(self):
        """
        Gets the id of this ScimV2Group.
        SCIM Resource identifier

        :return: The id of this ScimV2Group.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ScimV2Group.
        SCIM Resource identifier

        :param id: The id of this ScimV2Group.
        :type: str
        """
        
        self._id = id

    @property
    def schemas(self):
        """
        Gets the schemas of this ScimV2Group.
        schemas supported

        :return: The schemas of this ScimV2Group.
        :rtype: list[str]
        """
        return self._schemas

    @schemas.setter
    def schemas(self, schemas):
        """
        Sets the schemas of this ScimV2Group.
        schemas supported

        :param schemas: The schemas of this ScimV2Group.
        :type: list[str]
        """
        
        self._schemas = schemas

    @property
    def display_name(self):
        """
        Gets the display_name of this ScimV2Group.
        The display name for the group.

        :return: The display_name of this ScimV2Group.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this ScimV2Group.
        The display name for the group.

        :param display_name: The display_name of this ScimV2Group.
        :type: str
        """
        
        self._display_name = display_name

    @property
    def members(self):
        """
        Gets the members of this ScimV2Group.
        A list of members in a SCIM group.

        :return: The members of this ScimV2Group.
        :rtype: list[ScimV2MemberReference]
        """
        return self._members

    @members.setter
    def members(self, members):
        """
        Sets the members of this ScimV2Group.
        A list of members in a SCIM group.

        :param members: The members of this ScimV2Group.
        :type: list[ScimV2MemberReference]
        """
        
        self._members = members

    @property
    def meta(self):
        """
        Gets the meta of this ScimV2Group.
        Resource SCIM meta

        :return: The meta of this ScimV2Group.
        :rtype: ScimMetadata
        """
        return self._meta

    @meta.setter
    def meta(self, meta):
        """
        Sets the meta of this ScimV2Group.
        Resource SCIM meta

        :param meta: The meta of this ScimV2Group.
        :type: ScimMetadata
        """
        
        self._meta = meta

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

