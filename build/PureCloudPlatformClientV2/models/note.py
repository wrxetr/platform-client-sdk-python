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


class Note(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        Note - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'name': 'str',
            'note_text': 'str',
            'modify_date': 'datetime',
            'create_date': 'datetime',
            'created_by': 'User',
            'external_data_sources': 'list[ExternalDataSource]',
            'self_uri': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'note_text': 'noteText',
            'modify_date': 'modifyDate',
            'create_date': 'createDate',
            'created_by': 'createdBy',
            'external_data_sources': 'externalDataSources',
            'self_uri': 'selfUri'
        }

        self._id = None
        self._name = None
        self._note_text = None
        self._modify_date = None
        self._create_date = None
        self._created_by = None
        self._external_data_sources = None
        self._self_uri = None

    @property
    def id(self):
        """
        Gets the id of this Note.
        The globally unique identifier for the object.

        :return: The id of this Note.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Note.
        The globally unique identifier for the object.

        :param id: The id of this Note.
        :type: str
        """
        
        self._id = id

    @property
    def name(self):
        """
        Gets the name of this Note.


        :return: The name of this Note.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Note.


        :param name: The name of this Note.
        :type: str
        """
        
        self._name = name

    @property
    def note_text(self):
        """
        Gets the note_text of this Note.


        :return: The note_text of this Note.
        :rtype: str
        """
        return self._note_text

    @note_text.setter
    def note_text(self, note_text):
        """
        Sets the note_text of this Note.


        :param note_text: The note_text of this Note.
        :type: str
        """
        
        self._note_text = note_text

    @property
    def modify_date(self):
        """
        Gets the modify_date of this Note.
        Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ

        :return: The modify_date of this Note.
        :rtype: datetime
        """
        return self._modify_date

    @modify_date.setter
    def modify_date(self, modify_date):
        """
        Sets the modify_date of this Note.
        Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ

        :param modify_date: The modify_date of this Note.
        :type: datetime
        """
        
        self._modify_date = modify_date

    @property
    def create_date(self):
        """
        Gets the create_date of this Note.
        Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ

        :return: The create_date of this Note.
        :rtype: datetime
        """
        return self._create_date

    @create_date.setter
    def create_date(self, create_date):
        """
        Sets the create_date of this Note.
        Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ

        :param create_date: The create_date of this Note.
        :type: datetime
        """
        
        self._create_date = create_date

    @property
    def created_by(self):
        """
        Gets the created_by of this Note.
        The author of this note

        :return: The created_by of this Note.
        :rtype: User
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """
        Sets the created_by of this Note.
        The author of this note

        :param created_by: The created_by of this Note.
        :type: User
        """
        
        self._created_by = created_by

    @property
    def external_data_sources(self):
        """
        Gets the external_data_sources of this Note.
        Links to the sources of data (e.g. one source might be a CRM) that contributed data to this record.  Read-only, and only populated when requested via expand param.

        :return: The external_data_sources of this Note.
        :rtype: list[ExternalDataSource]
        """
        return self._external_data_sources

    @external_data_sources.setter
    def external_data_sources(self, external_data_sources):
        """
        Sets the external_data_sources of this Note.
        Links to the sources of data (e.g. one source might be a CRM) that contributed data to this record.  Read-only, and only populated when requested via expand param.

        :param external_data_sources: The external_data_sources of this Note.
        :type: list[ExternalDataSource]
        """
        
        self._external_data_sources = external_data_sources

    @property
    def self_uri(self):
        """
        Gets the self_uri of this Note.
        The URI for this object

        :return: The self_uri of this Note.
        :rtype: str
        """
        return self._self_uri

    @self_uri.setter
    def self_uri(self, self_uri):
        """
        Sets the self_uri of this Note.
        The URI for this object

        :param self_uri: The self_uri of this Note.
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

