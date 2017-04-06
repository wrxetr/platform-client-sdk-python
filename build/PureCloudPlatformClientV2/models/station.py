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


class Station(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        Station - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'name': 'str',
            'description': 'str',
            'status': 'str',
            'user_id': 'str',
            'primary_edge': 'UriReference',
            'secondary_edge': 'UriReference',
            'type': 'str',
            'line_appearance_id': 'str',
            'self_uri': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'description': 'description',
            'status': 'status',
            'user_id': 'userId',
            'primary_edge': 'primaryEdge',
            'secondary_edge': 'secondaryEdge',
            'type': 'type',
            'line_appearance_id': 'lineAppearanceId',
            'self_uri': 'selfUri'
        }

        self._id = None
        self._name = None
        self._description = None
        self._status = None
        self._user_id = None
        self._primary_edge = None
        self._secondary_edge = None
        self._type = None
        self._line_appearance_id = None
        self._self_uri = None

    @property
    def id(self):
        """
        Gets the id of this Station.
        The globally unique identifier for the object.

        :return: The id of this Station.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Station.
        The globally unique identifier for the object.

        :param id: The id of this Station.
        :type: str
        """
        
        self._id = id

    @property
    def name(self):
        """
        Gets the name of this Station.


        :return: The name of this Station.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Station.


        :param name: The name of this Station.
        :type: str
        """
        
        self._name = name

    @property
    def description(self):
        """
        Gets the description of this Station.


        :return: The description of this Station.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this Station.


        :param description: The description of this Station.
        :type: str
        """
        
        self._description = description

    @property
    def status(self):
        """
        Gets the status of this Station.


        :return: The status of this Station.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this Station.


        :param status: The status of this Station.
        :type: str
        """
        allowed_values = ["AVAILABLE", "ASSOCIATED"]
        if status.lower() not in map(str.lower, allowed_values):
            # print "Invalid value for status -> " + status
            self._status = "outdated_sdk_version"
        else:
            self._status = status.lower()

    @property
    def user_id(self):
        """
        Gets the user_id of this Station.


        :return: The user_id of this Station.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """
        Sets the user_id of this Station.


        :param user_id: The user_id of this Station.
        :type: str
        """
        
        self._user_id = user_id

    @property
    def primary_edge(self):
        """
        Gets the primary_edge of this Station.


        :return: The primary_edge of this Station.
        :rtype: UriReference
        """
        return self._primary_edge

    @primary_edge.setter
    def primary_edge(self, primary_edge):
        """
        Sets the primary_edge of this Station.


        :param primary_edge: The primary_edge of this Station.
        :type: UriReference
        """
        
        self._primary_edge = primary_edge

    @property
    def secondary_edge(self):
        """
        Gets the secondary_edge of this Station.


        :return: The secondary_edge of this Station.
        :rtype: UriReference
        """
        return self._secondary_edge

    @secondary_edge.setter
    def secondary_edge(self, secondary_edge):
        """
        Sets the secondary_edge of this Station.


        :param secondary_edge: The secondary_edge of this Station.
        :type: UriReference
        """
        
        self._secondary_edge = secondary_edge

    @property
    def type(self):
        """
        Gets the type of this Station.


        :return: The type of this Station.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this Station.


        :param type: The type of this Station.
        :type: str
        """
        
        self._type = type

    @property
    def line_appearance_id(self):
        """
        Gets the line_appearance_id of this Station.


        :return: The line_appearance_id of this Station.
        :rtype: str
        """
        return self._line_appearance_id

    @line_appearance_id.setter
    def line_appearance_id(self, line_appearance_id):
        """
        Sets the line_appearance_id of this Station.


        :param line_appearance_id: The line_appearance_id of this Station.
        :type: str
        """
        
        self._line_appearance_id = line_appearance_id

    @property
    def self_uri(self):
        """
        Gets the self_uri of this Station.
        The URI for this object

        :return: The self_uri of this Station.
        :rtype: str
        """
        return self._self_uri

    @self_uri.setter
    def self_uri(self, self_uri):
        """
        Sets the self_uri of this Station.
        The URI for this object

        :param self_uri: The self_uri of this Station.
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
