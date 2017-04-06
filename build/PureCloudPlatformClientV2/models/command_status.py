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


class CommandStatus(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        CommandStatus - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'name': 'str',
            'expiration': 'datetime',
            'user_id': 'str',
            'status_code': 'str',
            'command_type': 'str',
            'document': 'Document',
            'self_uri': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'expiration': 'expiration',
            'user_id': 'userId',
            'status_code': 'statusCode',
            'command_type': 'commandType',
            'document': 'document',
            'self_uri': 'selfUri'
        }

        self._id = None
        self._name = None
        self._expiration = None
        self._user_id = None
        self._status_code = None
        self._command_type = None
        self._document = None
        self._self_uri = None

    @property
    def id(self):
        """
        Gets the id of this CommandStatus.
        The globally unique identifier for the object.

        :return: The id of this CommandStatus.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this CommandStatus.
        The globally unique identifier for the object.

        :param id: The id of this CommandStatus.
        :type: str
        """
        
        self._id = id

    @property
    def name(self):
        """
        Gets the name of this CommandStatus.


        :return: The name of this CommandStatus.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this CommandStatus.


        :param name: The name of this CommandStatus.
        :type: str
        """
        
        self._name = name

    @property
    def expiration(self):
        """
        Gets the expiration of this CommandStatus.
        Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ

        :return: The expiration of this CommandStatus.
        :rtype: datetime
        """
        return self._expiration

    @expiration.setter
    def expiration(self, expiration):
        """
        Sets the expiration of this CommandStatus.
        Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ

        :param expiration: The expiration of this CommandStatus.
        :type: datetime
        """
        
        self._expiration = expiration

    @property
    def user_id(self):
        """
        Gets the user_id of this CommandStatus.


        :return: The user_id of this CommandStatus.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """
        Sets the user_id of this CommandStatus.


        :param user_id: The user_id of this CommandStatus.
        :type: str
        """
        
        self._user_id = user_id

    @property
    def status_code(self):
        """
        Gets the status_code of this CommandStatus.


        :return: The status_code of this CommandStatus.
        :rtype: str
        """
        return self._status_code

    @status_code.setter
    def status_code(self, status_code):
        """
        Sets the status_code of this CommandStatus.


        :param status_code: The status_code of this CommandStatus.
        :type: str
        """
        allowed_values = ["INPROGRESS", "COMPLETE", "ERROR", "CANCELING", "CANCELED"]
        if status_code.lower() not in map(str.lower, allowed_values):
            # print "Invalid value for status_code -> " + status_code
            self._status_code = "outdated_sdk_version"
        else:
            self._status_code = status_code.lower()

    @property
    def command_type(self):
        """
        Gets the command_type of this CommandStatus.


        :return: The command_type of this CommandStatus.
        :rtype: str
        """
        return self._command_type

    @command_type.setter
    def command_type(self, command_type):
        """
        Sets the command_type of this CommandStatus.


        :param command_type: The command_type of this CommandStatus.
        :type: str
        """
        allowed_values = ["UPLOAD", "COPYDOCUMENT", "MOVEDOCUMENT", "DELETEWORKSPACE", "DELETEDOCUMENT", "DELETETAG", "UPDATETAG", "REINDEX", "CLEANUP", "REPLACEDOCUMENT"]
        if command_type.lower() not in map(str.lower, allowed_values):
            # print "Invalid value for command_type -> " + command_type
            self._command_type = "outdated_sdk_version"
        else:
            self._command_type = command_type.lower()

    @property
    def document(self):
        """
        Gets the document of this CommandStatus.


        :return: The document of this CommandStatus.
        :rtype: Document
        """
        return self._document

    @document.setter
    def document(self, document):
        """
        Sets the document of this CommandStatus.


        :param document: The document of this CommandStatus.
        :type: Document
        """
        
        self._document = document

    @property
    def self_uri(self):
        """
        Gets the self_uri of this CommandStatus.
        The URI for this object

        :return: The self_uri of this CommandStatus.
        :rtype: str
        """
        return self._self_uri

    @self_uri.setter
    def self_uri(self, self_uri):
        """
        Sets the self_uri of this CommandStatus.
        The URI for this object

        :param self_uri: The self_uri of this CommandStatus.
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
