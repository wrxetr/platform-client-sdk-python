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


class PhoneBase(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        PhoneBase - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'name': 'str',
            'description': 'str',
            'version': 'int',
            'date_created': 'datetime',
            'date_modified': 'datetime',
            'modified_by': 'str',
            'created_by': 'str',
            'state': 'str',
            'modified_by_app': 'str',
            'created_by_app': 'str',
            'phone_meta_base': 'UriReference',
            'lines': 'list[LineBase]',
            'properties': 'dict(str, object)',
            'capabilities': 'PhoneCapabilities',
            'self_uri': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'description': 'description',
            'version': 'version',
            'date_created': 'dateCreated',
            'date_modified': 'dateModified',
            'modified_by': 'modifiedBy',
            'created_by': 'createdBy',
            'state': 'state',
            'modified_by_app': 'modifiedByApp',
            'created_by_app': 'createdByApp',
            'phone_meta_base': 'phoneMetaBase',
            'lines': 'lines',
            'properties': 'properties',
            'capabilities': 'capabilities',
            'self_uri': 'selfUri'
        }

        self._id = None
        self._name = None
        self._description = None
        self._version = None
        self._date_created = None
        self._date_modified = None
        self._modified_by = None
        self._created_by = None
        self._state = None
        self._modified_by_app = None
        self._created_by_app = None
        self._phone_meta_base = None
        self._lines = None
        self._properties = None
        self._capabilities = None
        self._self_uri = None

    @property
    def id(self):
        """
        Gets the id of this PhoneBase.
        The globally unique identifier for the object.

        :return: The id of this PhoneBase.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this PhoneBase.
        The globally unique identifier for the object.

        :param id: The id of this PhoneBase.
        :type: str
        """
        
        self._id = id

    @property
    def name(self):
        """
        Gets the name of this PhoneBase.
        The name of the entity.

        :return: The name of this PhoneBase.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this PhoneBase.
        The name of the entity.

        :param name: The name of this PhoneBase.
        :type: str
        """
        
        self._name = name

    @property
    def description(self):
        """
        Gets the description of this PhoneBase.


        :return: The description of this PhoneBase.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this PhoneBase.


        :param description: The description of this PhoneBase.
        :type: str
        """
        
        self._description = description

    @property
    def version(self):
        """
        Gets the version of this PhoneBase.


        :return: The version of this PhoneBase.
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """
        Sets the version of this PhoneBase.


        :param version: The version of this PhoneBase.
        :type: int
        """
        
        self._version = version

    @property
    def date_created(self):
        """
        Gets the date_created of this PhoneBase.
        Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ

        :return: The date_created of this PhoneBase.
        :rtype: datetime
        """
        return self._date_created

    @date_created.setter
    def date_created(self, date_created):
        """
        Sets the date_created of this PhoneBase.
        Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ

        :param date_created: The date_created of this PhoneBase.
        :type: datetime
        """
        
        self._date_created = date_created

    @property
    def date_modified(self):
        """
        Gets the date_modified of this PhoneBase.
        Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ

        :return: The date_modified of this PhoneBase.
        :rtype: datetime
        """
        return self._date_modified

    @date_modified.setter
    def date_modified(self, date_modified):
        """
        Sets the date_modified of this PhoneBase.
        Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ

        :param date_modified: The date_modified of this PhoneBase.
        :type: datetime
        """
        
        self._date_modified = date_modified

    @property
    def modified_by(self):
        """
        Gets the modified_by of this PhoneBase.


        :return: The modified_by of this PhoneBase.
        :rtype: str
        """
        return self._modified_by

    @modified_by.setter
    def modified_by(self, modified_by):
        """
        Sets the modified_by of this PhoneBase.


        :param modified_by: The modified_by of this PhoneBase.
        :type: str
        """
        
        self._modified_by = modified_by

    @property
    def created_by(self):
        """
        Gets the created_by of this PhoneBase.


        :return: The created_by of this PhoneBase.
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """
        Sets the created_by of this PhoneBase.


        :param created_by: The created_by of this PhoneBase.
        :type: str
        """
        
        self._created_by = created_by

    @property
    def state(self):
        """
        Gets the state of this PhoneBase.


        :return: The state of this PhoneBase.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """
        Sets the state of this PhoneBase.


        :param state: The state of this PhoneBase.
        :type: str
        """
        allowed_values = ["active", "inactive", "deleted"]
        if state.lower() not in map(str.lower, allowed_values):
            # print "Invalid value for state -> " + state
            self._state = "outdated_sdk_version"
        else:
            self._state = state.lower()

    @property
    def modified_by_app(self):
        """
        Gets the modified_by_app of this PhoneBase.


        :return: The modified_by_app of this PhoneBase.
        :rtype: str
        """
        return self._modified_by_app

    @modified_by_app.setter
    def modified_by_app(self, modified_by_app):
        """
        Sets the modified_by_app of this PhoneBase.


        :param modified_by_app: The modified_by_app of this PhoneBase.
        :type: str
        """
        
        self._modified_by_app = modified_by_app

    @property
    def created_by_app(self):
        """
        Gets the created_by_app of this PhoneBase.


        :return: The created_by_app of this PhoneBase.
        :rtype: str
        """
        return self._created_by_app

    @created_by_app.setter
    def created_by_app(self, created_by_app):
        """
        Sets the created_by_app of this PhoneBase.


        :param created_by_app: The created_by_app of this PhoneBase.
        :type: str
        """
        
        self._created_by_app = created_by_app

    @property
    def phone_meta_base(self):
        """
        Gets the phone_meta_base of this PhoneBase.
        A phone metabase is essentially a database for storing phone configuration settings, which simplifies the configuration process.

        :return: The phone_meta_base of this PhoneBase.
        :rtype: UriReference
        """
        return self._phone_meta_base

    @phone_meta_base.setter
    def phone_meta_base(self, phone_meta_base):
        """
        Sets the phone_meta_base of this PhoneBase.
        A phone metabase is essentially a database for storing phone configuration settings, which simplifies the configuration process.

        :param phone_meta_base: The phone_meta_base of this PhoneBase.
        :type: UriReference
        """
        
        self._phone_meta_base = phone_meta_base

    @property
    def lines(self):
        """
        Gets the lines of this PhoneBase.
        The list of linebases associated with the phone base.

        :return: The lines of this PhoneBase.
        :rtype: list[LineBase]
        """
        return self._lines

    @lines.setter
    def lines(self, lines):
        """
        Sets the lines of this PhoneBase.
        The list of linebases associated with the phone base.

        :param lines: The lines of this PhoneBase.
        :type: list[LineBase]
        """
        
        self._lines = lines

    @property
    def properties(self):
        """
        Gets the properties of this PhoneBase.


        :return: The properties of this PhoneBase.
        :rtype: dict(str, object)
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """
        Sets the properties of this PhoneBase.


        :param properties: The properties of this PhoneBase.
        :type: dict(str, object)
        """
        
        self._properties = properties

    @property
    def capabilities(self):
        """
        Gets the capabilities of this PhoneBase.


        :return: The capabilities of this PhoneBase.
        :rtype: PhoneCapabilities
        """
        return self._capabilities

    @capabilities.setter
    def capabilities(self, capabilities):
        """
        Sets the capabilities of this PhoneBase.


        :param capabilities: The capabilities of this PhoneBase.
        :type: PhoneCapabilities
        """
        
        self._capabilities = capabilities

    @property
    def self_uri(self):
        """
        Gets the self_uri of this PhoneBase.
        The URI for this object

        :return: The self_uri of this PhoneBase.
        :rtype: str
        """
        return self._self_uri

    @self_uri.setter
    def self_uri(self, self_uri):
        """
        Sets the self_uri of this PhoneBase.
        The URI for this object

        :param self_uri: The self_uri of this PhoneBase.
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
