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

class Location(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        Location - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'floorplan_id': 'str',
            'coordinates': 'dict(str, float)',
            'notes': 'str',
            'location_definition': 'LocationDefinition'
        }

        self.attribute_map = {
            'id': 'id',
            'floorplan_id': 'floorplanId',
            'coordinates': 'coordinates',
            'notes': 'notes',
            'location_definition': 'locationDefinition'
        }

        self._id = None
        self._floorplan_id = None
        self._coordinates = None
        self._notes = None
        self._location_definition = None

    @property
    def id(self):
        """
        Gets the id of this Location.
        Unique identifier for the location

        :return: The id of this Location.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Location.
        Unique identifier for the location

        :param id: The id of this Location.
        :type: str
        """
        
        self._id = id

    @property
    def floorplan_id(self):
        """
        Gets the floorplan_id of this Location.
        Unique identifier for the location floorplan image

        :return: The floorplan_id of this Location.
        :rtype: str
        """
        return self._floorplan_id

    @floorplan_id.setter
    def floorplan_id(self, floorplan_id):
        """
        Sets the floorplan_id of this Location.
        Unique identifier for the location floorplan image

        :param floorplan_id: The floorplan_id of this Location.
        :type: str
        """
        
        self._floorplan_id = floorplan_id

    @property
    def coordinates(self):
        """
        Gets the coordinates of this Location.
        Users coordinates on the floorplan. Only used when floorplanImage is set

        :return: The coordinates of this Location.
        :rtype: dict(str, float)
        """
        return self._coordinates

    @coordinates.setter
    def coordinates(self, coordinates):
        """
        Sets the coordinates of this Location.
        Users coordinates on the floorplan. Only used when floorplanImage is set

        :param coordinates: The coordinates of this Location.
        :type: dict(str, float)
        """
        
        self._coordinates = coordinates

    @property
    def notes(self):
        """
        Gets the notes of this Location.
        Optional description on the users location

        :return: The notes of this Location.
        :rtype: str
        """
        return self._notes

    @notes.setter
    def notes(self, notes):
        """
        Sets the notes of this Location.
        Optional description on the users location

        :param notes: The notes of this Location.
        :type: str
        """
        
        self._notes = notes

    @property
    def location_definition(self):
        """
        Gets the location_definition of this Location.


        :return: The location_definition of this Location.
        :rtype: LocationDefinition
        """
        return self._location_definition

    @location_definition.setter
    def location_definition(self, location_definition):
        """
        Sets the location_definition of this Location.


        :param location_definition: The location_definition of this Location.
        :type: LocationDefinition
        """
        
        self._location_definition = location_definition

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

