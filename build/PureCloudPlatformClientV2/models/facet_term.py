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


class FacetTerm(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        FacetTerm - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'term': 'str',
            'key': 'int',
            'id': 'str',
            'name': 'str',
            'count': 'int',
            'time': 'datetime'
        }

        self.attribute_map = {
            'term': 'term',
            'key': 'key',
            'id': 'id',
            'name': 'name',
            'count': 'count',
            'time': 'time'
        }

        self._term = None
        self._key = None
        self._id = None
        self._name = None
        self._count = None
        self._time = None

    @property
    def term(self):
        """
        Gets the term of this FacetTerm.


        :return: The term of this FacetTerm.
        :rtype: str
        """
        return self._term

    @term.setter
    def term(self, term):
        """
        Sets the term of this FacetTerm.


        :param term: The term of this FacetTerm.
        :type: str
        """
        
        self._term = term

    @property
    def key(self):
        """
        Gets the key of this FacetTerm.


        :return: The key of this FacetTerm.
        :rtype: int
        """
        return self._key

    @key.setter
    def key(self, key):
        """
        Sets the key of this FacetTerm.


        :param key: The key of this FacetTerm.
        :type: int
        """
        
        self._key = key

    @property
    def id(self):
        """
        Gets the id of this FacetTerm.


        :return: The id of this FacetTerm.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this FacetTerm.


        :param id: The id of this FacetTerm.
        :type: str
        """
        
        self._id = id

    @property
    def name(self):
        """
        Gets the name of this FacetTerm.


        :return: The name of this FacetTerm.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this FacetTerm.


        :param name: The name of this FacetTerm.
        :type: str
        """
        
        self._name = name

    @property
    def count(self):
        """
        Gets the count of this FacetTerm.


        :return: The count of this FacetTerm.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """
        Sets the count of this FacetTerm.


        :param count: The count of this FacetTerm.
        :type: int
        """
        
        self._count = count

    @property
    def time(self):
        """
        Gets the time of this FacetTerm.
        Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ

        :return: The time of this FacetTerm.
        :rtype: datetime
        """
        return self._time

    @time.setter
    def time(self, time):
        """
        Sets the time of this FacetTerm.
        Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ

        :param time: The time of this FacetTerm.
        :type: datetime
        """
        
        self._time = time

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

