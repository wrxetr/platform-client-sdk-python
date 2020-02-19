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

class ScimV2SchemaAttribute(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        ScimV2SchemaAttribute - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'name': 'str',
            'type': 'str',
            'sub_attributes': 'list[ScimV2SchemaAttribute]',
            'multi_valued': 'bool',
            'description': 'str',
            'required': 'bool',
            'canonical_values': 'list[str]',
            'case_exact': 'bool',
            'mutability': 'str',
            'returned': 'str',
            'uniqueness': 'str',
            'reference_types': 'list[str]'
        }

        self.attribute_map = {
            'name': 'name',
            'type': 'type',
            'sub_attributes': 'subAttributes',
            'multi_valued': 'multiValued',
            'description': 'description',
            'required': 'required',
            'canonical_values': 'canonicalValues',
            'case_exact': 'caseExact',
            'mutability': 'mutability',
            'returned': 'returned',
            'uniqueness': 'uniqueness',
            'reference_types': 'referenceTypes'
        }

        self._name = None
        self._type = None
        self._sub_attributes = None
        self._multi_valued = None
        self._description = None
        self._required = None
        self._canonical_values = None
        self._case_exact = None
        self._mutability = None
        self._returned = None
        self._uniqueness = None
        self._reference_types = None

    @property
    def name(self):
        """
        Gets the name of this ScimV2SchemaAttribute.
        The attribute's name

        :return: The name of this ScimV2SchemaAttribute.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this ScimV2SchemaAttribute.
        The attribute's name

        :param name: The name of this ScimV2SchemaAttribute.
        :type: str
        """
        
        self._name = name

    @property
    def type(self):
        """
        Gets the type of this ScimV2SchemaAttribute.
        The attribute's data type.  Valid values are \"string\", \"boolean\", \"decimal\", \"integer\", \"dateTime\", \"reference\", and \"complex\".

        :return: The type of this ScimV2SchemaAttribute.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this ScimV2SchemaAttribute.
        The attribute's data type.  Valid values are \"string\", \"boolean\", \"decimal\", \"integer\", \"dateTime\", \"reference\", and \"complex\".

        :param type: The type of this ScimV2SchemaAttribute.
        :type: str
        """
        allowed_values = ["STRING", "BOOLEAN", "DECIMAL", "INTEGER", "DATE_TIME", "REFERENCE", "COMPLEX"]
        if type.lower() not in map(str.lower, allowed_values):
            # print "Invalid value for type -> " + type
            self._type = "outdated_sdk_version"
        else:
            self._type = type

    @property
    def sub_attributes(self):
        """
        Gets the sub_attributes of this ScimV2SchemaAttribute.
        When an attribute is of type \"complex\", \"subAttributes\" defines a set of sub-attributes. \"subAttributes\" has the same schema sub-attributes as \"attributes\"

        :return: The sub_attributes of this ScimV2SchemaAttribute.
        :rtype: list[ScimV2SchemaAttribute]
        """
        return self._sub_attributes

    @sub_attributes.setter
    def sub_attributes(self, sub_attributes):
        """
        Sets the sub_attributes of this ScimV2SchemaAttribute.
        When an attribute is of type \"complex\", \"subAttributes\" defines a set of sub-attributes. \"subAttributes\" has the same schema sub-attributes as \"attributes\"

        :param sub_attributes: The sub_attributes of this ScimV2SchemaAttribute.
        :type: list[ScimV2SchemaAttribute]
        """
        
        self._sub_attributes = sub_attributes

    @property
    def multi_valued(self):
        """
        Gets the multi_valued of this ScimV2SchemaAttribute.
        A Boolean value indicating the attribute's plurality.

        :return: The multi_valued of this ScimV2SchemaAttribute.
        :rtype: bool
        """
        return self._multi_valued

    @multi_valued.setter
    def multi_valued(self, multi_valued):
        """
        Sets the multi_valued of this ScimV2SchemaAttribute.
        A Boolean value indicating the attribute's plurality.

        :param multi_valued: The multi_valued of this ScimV2SchemaAttribute.
        :type: bool
        """
        
        self._multi_valued = multi_valued

    @property
    def description(self):
        """
        Gets the description of this ScimV2SchemaAttribute.
        The attribute's human-readable description.

        :return: The description of this ScimV2SchemaAttribute.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this ScimV2SchemaAttribute.
        The attribute's human-readable description.

        :param description: The description of this ScimV2SchemaAttribute.
        :type: str
        """
        
        self._description = description

    @property
    def required(self):
        """
        Gets the required of this ScimV2SchemaAttribute.
        A Boolean value that specifies whether or not the attribute is required.

        :return: The required of this ScimV2SchemaAttribute.
        :rtype: bool
        """
        return self._required

    @required.setter
    def required(self, required):
        """
        Sets the required of this ScimV2SchemaAttribute.
        A Boolean value that specifies whether or not the attribute is required.

        :param required: The required of this ScimV2SchemaAttribute.
        :type: bool
        """
        
        self._required = required

    @property
    def canonical_values(self):
        """
        Gets the canonical_values of this ScimV2SchemaAttribute.
        A collection of suggested canonical values that MAY be used (e.g., \"work\" and \"home\").  In some cases, service providers MAY choose to ignore unsupported values.  OPTIONAL.

        :return: The canonical_values of this ScimV2SchemaAttribute.
        :rtype: list[str]
        """
        return self._canonical_values

    @canonical_values.setter
    def canonical_values(self, canonical_values):
        """
        Sets the canonical_values of this ScimV2SchemaAttribute.
        A collection of suggested canonical values that MAY be used (e.g., \"work\" and \"home\").  In some cases, service providers MAY choose to ignore unsupported values.  OPTIONAL.

        :param canonical_values: The canonical_values of this ScimV2SchemaAttribute.
        :type: list[str]
        """
        
        self._canonical_values = canonical_values

    @property
    def case_exact(self):
        """
        Gets the case_exact of this ScimV2SchemaAttribute.
        A Boolean value that specifies whether or not a string attribute is case sensitive.  The server SHALL use case sensitivity when evaluating filters.  For attributes that are case exact, the server SHALL preserve case for any value submitted.  If the attribute is case insensitive, the server MAY alter case for a submitted value.  Case sensitivity also impacts how attribute values MAY be compared against filter values (see Section 3.4.2.2 of [RFC7644])

        :return: The case_exact of this ScimV2SchemaAttribute.
        :rtype: bool
        """
        return self._case_exact

    @case_exact.setter
    def case_exact(self, case_exact):
        """
        Sets the case_exact of this ScimV2SchemaAttribute.
        A Boolean value that specifies whether or not a string attribute is case sensitive.  The server SHALL use case sensitivity when evaluating filters.  For attributes that are case exact, the server SHALL preserve case for any value submitted.  If the attribute is case insensitive, the server MAY alter case for a submitted value.  Case sensitivity also impacts how attribute values MAY be compared against filter values (see Section 3.4.2.2 of [RFC7644])

        :param case_exact: The case_exact of this ScimV2SchemaAttribute.
        :type: bool
        """
        
        self._case_exact = case_exact

    @property
    def mutability(self):
        """
        Gets the mutability of this ScimV2SchemaAttribute.
        A single keyword indicating the circumstances under which the value of the attribute can be (re)defined. Value are readOnly, readWrite, immutable, writeOnly

        :return: The mutability of this ScimV2SchemaAttribute.
        :rtype: str
        """
        return self._mutability

    @mutability.setter
    def mutability(self, mutability):
        """
        Sets the mutability of this ScimV2SchemaAttribute.
        A single keyword indicating the circumstances under which the value of the attribute can be (re)defined. Value are readOnly, readWrite, immutable, writeOnly

        :param mutability: The mutability of this ScimV2SchemaAttribute.
        :type: str
        """
        allowed_values = ["readWrite", "readOnly", "immutable", "writeOnly"]
        if mutability.lower() not in map(str.lower, allowed_values):
            # print "Invalid value for mutability -> " + mutability
            self._mutability = "outdated_sdk_version"
        else:
            self._mutability = mutability

    @property
    def returned(self):
        """
        Gets the returned of this ScimV2SchemaAttribute.
        A single keyword that indicates when an attribute and associated values are returned in response to a GET request, or in response to a PUT, POST, or PATCH request.  Valid keywords are as follows: always, never, default, request

        :return: The returned of this ScimV2SchemaAttribute.
        :rtype: str
        """
        return self._returned

    @returned.setter
    def returned(self, returned):
        """
        Sets the returned of this ScimV2SchemaAttribute.
        A single keyword that indicates when an attribute and associated values are returned in response to a GET request, or in response to a PUT, POST, or PATCH request.  Valid keywords are as follows: always, never, default, request

        :param returned: The returned of this ScimV2SchemaAttribute.
        :type: str
        """
        allowed_values = ["ALWAYS", "NEVER", "DEFAULT", "REQUEST"]
        if returned.lower() not in map(str.lower, allowed_values):
            # print "Invalid value for returned -> " + returned
            self._returned = "outdated_sdk_version"
        else:
            self._returned = returned

    @property
    def uniqueness(self):
        """
        Gets the uniqueness of this ScimV2SchemaAttribute.
        A single keyword value that specifies how the service provider enforces uniqueness of attribute values.  A server MAY reject an invalid value based on uniqueness by returning HTTP response code 400 (Bad Request).  A client MAY enforce uniqueness on the client side to a greater degree than the service provider enforces.  For example, a client could make a value unique while the server has uniqueness of \"none\".  Valid keywords are as follows: none, server, global

        :return: The uniqueness of this ScimV2SchemaAttribute.
        :rtype: str
        """
        return self._uniqueness

    @uniqueness.setter
    def uniqueness(self, uniqueness):
        """
        Sets the uniqueness of this ScimV2SchemaAttribute.
        A single keyword value that specifies how the service provider enforces uniqueness of attribute values.  A server MAY reject an invalid value based on uniqueness by returning HTTP response code 400 (Bad Request).  A client MAY enforce uniqueness on the client side to a greater degree than the service provider enforces.  For example, a client could make a value unique while the server has uniqueness of \"none\".  Valid keywords are as follows: none, server, global

        :param uniqueness: The uniqueness of this ScimV2SchemaAttribute.
        :type: str
        """
        allowed_values = ["NONE", "SERVER", "GLOBAL"]
        if uniqueness.lower() not in map(str.lower, allowed_values):
            # print "Invalid value for uniqueness -> " + uniqueness
            self._uniqueness = "outdated_sdk_version"
        else:
            self._uniqueness = uniqueness

    @property
    def reference_types(self):
        """
        Gets the reference_types of this ScimV2SchemaAttribute.
        A multi-valued array of JSON strings that indicate the SCIM resource types that may be referenced. Values include User, Group, external and uri.

        :return: The reference_types of this ScimV2SchemaAttribute.
        :rtype: list[str]
        """
        return self._reference_types

    @reference_types.setter
    def reference_types(self, reference_types):
        """
        Sets the reference_types of this ScimV2SchemaAttribute.
        A multi-valued array of JSON strings that indicate the SCIM resource types that may be referenced. Values include User, Group, external and uri.

        :param reference_types: The reference_types of this ScimV2SchemaAttribute.
        :type: list[str]
        """
        
        self._reference_types = reference_types

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

