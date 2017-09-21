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


class Site(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        Site - a model defined in Swagger

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
            'primary_sites': 'list[UriReference]',
            'secondary_sites': 'list[UriReference]',
            'primary_edges': 'list[Edge]',
            'secondary_edges': 'list[Edge]',
            'addresses': 'list[Contact]',
            'edges': 'list[Edge]',
            'edge_auto_update_config': 'EdgeAutoUpdateConfig',
            'location': 'LocationDefinition',
            'managed': 'bool',
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
            'primary_sites': 'primarySites',
            'secondary_sites': 'secondarySites',
            'primary_edges': 'primaryEdges',
            'secondary_edges': 'secondaryEdges',
            'addresses': 'addresses',
            'edges': 'edges',
            'edge_auto_update_config': 'edgeAutoUpdateConfig',
            'location': 'location',
            'managed': 'managed',
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
        self._primary_sites = None
        self._secondary_sites = None
        self._primary_edges = None
        self._secondary_edges = None
        self._addresses = None
        self._edges = None
        self._edge_auto_update_config = None
        self._location = None
        self._managed = None
        self._self_uri = None

    @property
    def id(self):
        """
        Gets the id of this Site.
        The globally unique identifier for the object.

        :return: The id of this Site.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Site.
        The globally unique identifier for the object.

        :param id: The id of this Site.
        :type: str
        """
        
        self._id = id

    @property
    def name(self):
        """
        Gets the name of this Site.
        The name of the entity.

        :return: The name of this Site.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Site.
        The name of the entity.

        :param name: The name of this Site.
        :type: str
        """
        
        self._name = name

    @property
    def description(self):
        """
        Gets the description of this Site.
        The resource's description.

        :return: The description of this Site.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this Site.
        The resource's description.

        :param description: The description of this Site.
        :type: str
        """
        
        self._description = description

    @property
    def version(self):
        """
        Gets the version of this Site.
        The current version of the resource.

        :return: The version of this Site.
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """
        Sets the version of this Site.
        The current version of the resource.

        :param version: The version of this Site.
        :type: int
        """
        
        self._version = version

    @property
    def date_created(self):
        """
        Gets the date_created of this Site.
        The date the resource was created. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ

        :return: The date_created of this Site.
        :rtype: datetime
        """
        return self._date_created

    @date_created.setter
    def date_created(self, date_created):
        """
        Sets the date_created of this Site.
        The date the resource was created. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ

        :param date_created: The date_created of this Site.
        :type: datetime
        """
        
        self._date_created = date_created

    @property
    def date_modified(self):
        """
        Gets the date_modified of this Site.
        The date of the last modification to the resource. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ

        :return: The date_modified of this Site.
        :rtype: datetime
        """
        return self._date_modified

    @date_modified.setter
    def date_modified(self, date_modified):
        """
        Sets the date_modified of this Site.
        The date of the last modification to the resource. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ

        :param date_modified: The date_modified of this Site.
        :type: datetime
        """
        
        self._date_modified = date_modified

    @property
    def modified_by(self):
        """
        Gets the modified_by of this Site.
        The ID of the user that last modified the resource.

        :return: The modified_by of this Site.
        :rtype: str
        """
        return self._modified_by

    @modified_by.setter
    def modified_by(self, modified_by):
        """
        Sets the modified_by of this Site.
        The ID of the user that last modified the resource.

        :param modified_by: The modified_by of this Site.
        :type: str
        """
        
        self._modified_by = modified_by

    @property
    def created_by(self):
        """
        Gets the created_by of this Site.
        The ID of the user that created the resource.

        :return: The created_by of this Site.
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """
        Sets the created_by of this Site.
        The ID of the user that created the resource.

        :param created_by: The created_by of this Site.
        :type: str
        """
        
        self._created_by = created_by

    @property
    def state(self):
        """
        Gets the state of this Site.
        Indicates if the resource is active, inactive, or deleted.

        :return: The state of this Site.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """
        Sets the state of this Site.
        Indicates if the resource is active, inactive, or deleted.

        :param state: The state of this Site.
        :type: str
        """
        allowed_values = ["active", "inactive", "deleted"]
        if state.lower() not in map(str.lower, allowed_values):
            # print "Invalid value for state -> " + state
            self._state = "outdated_sdk_version"
        else:
            self._state = state

    @property
    def modified_by_app(self):
        """
        Gets the modified_by_app of this Site.
        The application that last modified the resource.

        :return: The modified_by_app of this Site.
        :rtype: str
        """
        return self._modified_by_app

    @modified_by_app.setter
    def modified_by_app(self, modified_by_app):
        """
        Sets the modified_by_app of this Site.
        The application that last modified the resource.

        :param modified_by_app: The modified_by_app of this Site.
        :type: str
        """
        
        self._modified_by_app = modified_by_app

    @property
    def created_by_app(self):
        """
        Gets the created_by_app of this Site.
        The application that created the resource.

        :return: The created_by_app of this Site.
        :rtype: str
        """
        return self._created_by_app

    @created_by_app.setter
    def created_by_app(self, created_by_app):
        """
        Sets the created_by_app of this Site.
        The application that created the resource.

        :param created_by_app: The created_by_app of this Site.
        :type: str
        """
        
        self._created_by_app = created_by_app

    @property
    def primary_sites(self):
        """
        Gets the primary_sites of this Site.


        :return: The primary_sites of this Site.
        :rtype: list[UriReference]
        """
        return self._primary_sites

    @primary_sites.setter
    def primary_sites(self, primary_sites):
        """
        Sets the primary_sites of this Site.


        :param primary_sites: The primary_sites of this Site.
        :type: list[UriReference]
        """
        
        self._primary_sites = primary_sites

    @property
    def secondary_sites(self):
        """
        Gets the secondary_sites of this Site.


        :return: The secondary_sites of this Site.
        :rtype: list[UriReference]
        """
        return self._secondary_sites

    @secondary_sites.setter
    def secondary_sites(self, secondary_sites):
        """
        Sets the secondary_sites of this Site.


        :param secondary_sites: The secondary_sites of this Site.
        :type: list[UriReference]
        """
        
        self._secondary_sites = secondary_sites

    @property
    def primary_edges(self):
        """
        Gets the primary_edges of this Site.


        :return: The primary_edges of this Site.
        :rtype: list[Edge]
        """
        return self._primary_edges

    @primary_edges.setter
    def primary_edges(self, primary_edges):
        """
        Sets the primary_edges of this Site.


        :param primary_edges: The primary_edges of this Site.
        :type: list[Edge]
        """
        
        self._primary_edges = primary_edges

    @property
    def secondary_edges(self):
        """
        Gets the secondary_edges of this Site.


        :return: The secondary_edges of this Site.
        :rtype: list[Edge]
        """
        return self._secondary_edges

    @secondary_edges.setter
    def secondary_edges(self, secondary_edges):
        """
        Sets the secondary_edges of this Site.


        :param secondary_edges: The secondary_edges of this Site.
        :type: list[Edge]
        """
        
        self._secondary_edges = secondary_edges

    @property
    def addresses(self):
        """
        Gets the addresses of this Site.


        :return: The addresses of this Site.
        :rtype: list[Contact]
        """
        return self._addresses

    @addresses.setter
    def addresses(self, addresses):
        """
        Sets the addresses of this Site.


        :param addresses: The addresses of this Site.
        :type: list[Contact]
        """
        
        self._addresses = addresses

    @property
    def edges(self):
        """
        Gets the edges of this Site.


        :return: The edges of this Site.
        :rtype: list[Edge]
        """
        return self._edges

    @edges.setter
    def edges(self, edges):
        """
        Sets the edges of this Site.


        :param edges: The edges of this Site.
        :type: list[Edge]
        """
        
        self._edges = edges

    @property
    def edge_auto_update_config(self):
        """
        Gets the edge_auto_update_config of this Site.
        Recurrance rule, time zone, and start/end settings for automatic edge updates for this site

        :return: The edge_auto_update_config of this Site.
        :rtype: EdgeAutoUpdateConfig
        """
        return self._edge_auto_update_config

    @edge_auto_update_config.setter
    def edge_auto_update_config(self, edge_auto_update_config):
        """
        Sets the edge_auto_update_config of this Site.
        Recurrance rule, time zone, and start/end settings for automatic edge updates for this site

        :param edge_auto_update_config: The edge_auto_update_config of this Site.
        :type: EdgeAutoUpdateConfig
        """
        
        self._edge_auto_update_config = edge_auto_update_config

    @property
    def location(self):
        """
        Gets the location of this Site.
        Location

        :return: The location of this Site.
        :rtype: LocationDefinition
        """
        return self._location

    @location.setter
    def location(self, location):
        """
        Sets the location of this Site.
        Location

        :param location: The location of this Site.
        :type: LocationDefinition
        """
        
        self._location = location

    @property
    def managed(self):
        """
        Gets the managed of this Site.


        :return: The managed of this Site.
        :rtype: bool
        """
        return self._managed

    @managed.setter
    def managed(self, managed):
        """
        Sets the managed of this Site.


        :param managed: The managed of this Site.
        :type: bool
        """
        
        self._managed = managed

    @property
    def self_uri(self):
        """
        Gets the self_uri of this Site.
        The URI for this object

        :return: The self_uri of this Site.
        :rtype: str
        """
        return self._self_uri

    @self_uri.setter
    def self_uri(self, self_uri):
        """
        Sets the self_uri of this Site.
        The URI for this object

        :param self_uri: The self_uri of this Site.
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

