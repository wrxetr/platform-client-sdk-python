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


class ArrayNode(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        ArrayNode - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'node_type': 'str',
            'object': 'bool',
            'boolean': 'bool',
            'number': 'bool',
            'float': 'bool',
            'floating_point_number': 'bool',
            'value_node': 'bool',
            'container_node': 'bool',
            'missing_node': 'bool',
            'pojo': 'bool',
            'integral_number': 'bool',
            'short': 'bool',
            'int': 'bool',
            'long': 'bool',
            'double': 'bool',
            'big_decimal': 'bool',
            'big_integer': 'bool',
            'textual': 'bool',
            'binary': 'bool',
            'array': 'bool',
            'null': 'bool'
        }

        self.attribute_map = {
            'node_type': 'nodeType',
            'object': 'object',
            'boolean': 'boolean',
            'number': 'number',
            'float': 'float',
            'floating_point_number': 'floatingPointNumber',
            'value_node': 'valueNode',
            'container_node': 'containerNode',
            'missing_node': 'missingNode',
            'pojo': 'pojo',
            'integral_number': 'integralNumber',
            'short': 'short',
            'int': 'int',
            'long': 'long',
            'double': 'double',
            'big_decimal': 'bigDecimal',
            'big_integer': 'bigInteger',
            'textual': 'textual',
            'binary': 'binary',
            'array': 'array',
            'null': 'null'
        }

        self._node_type = None
        self._object = None
        self._boolean = None
        self._number = None
        self._float = None
        self._floating_point_number = None
        self._value_node = None
        self._container_node = None
        self._missing_node = None
        self._pojo = None
        self._integral_number = None
        self._short = None
        self._int = None
        self._long = None
        self._double = None
        self._big_decimal = None
        self._big_integer = None
        self._textual = None
        self._binary = None
        self._array = None
        self._null = None

    @property
    def node_type(self):
        """
        Gets the node_type of this ArrayNode.


        :return: The node_type of this ArrayNode.
        :rtype: str
        """
        return self._node_type

    @node_type.setter
    def node_type(self, node_type):
        """
        Sets the node_type of this ArrayNode.


        :param node_type: The node_type of this ArrayNode.
        :type: str
        """
        allowed_values = ["ARRAY", "BINARY", "BOOLEAN", "MISSING", "NULL", "NUMBER", "OBJECT", "POJO", "STRING"]
        if node_type.lower() not in map(str.lower, allowed_values):
            # print "Invalid value for node_type -> " + node_type
            self._node_type = "outdated_sdk_version"
        else:
            self._node_type = node_type

    @property
    def object(self):
        """
        Gets the object of this ArrayNode.


        :return: The object of this ArrayNode.
        :rtype: bool
        """
        return self._object

    @object.setter
    def object(self, object):
        """
        Sets the object of this ArrayNode.


        :param object: The object of this ArrayNode.
        :type: bool
        """
        
        self._object = object

    @property
    def boolean(self):
        """
        Gets the boolean of this ArrayNode.


        :return: The boolean of this ArrayNode.
        :rtype: bool
        """
        return self._boolean

    @boolean.setter
    def boolean(self, boolean):
        """
        Sets the boolean of this ArrayNode.


        :param boolean: The boolean of this ArrayNode.
        :type: bool
        """
        
        self._boolean = boolean

    @property
    def number(self):
        """
        Gets the number of this ArrayNode.


        :return: The number of this ArrayNode.
        :rtype: bool
        """
        return self._number

    @number.setter
    def number(self, number):
        """
        Sets the number of this ArrayNode.


        :param number: The number of this ArrayNode.
        :type: bool
        """
        
        self._number = number

    @property
    def float(self):
        """
        Gets the float of this ArrayNode.


        :return: The float of this ArrayNode.
        :rtype: bool
        """
        return self._float

    @float.setter
    def float(self, float):
        """
        Sets the float of this ArrayNode.


        :param float: The float of this ArrayNode.
        :type: bool
        """
        
        self._float = float

    @property
    def floating_point_number(self):
        """
        Gets the floating_point_number of this ArrayNode.


        :return: The floating_point_number of this ArrayNode.
        :rtype: bool
        """
        return self._floating_point_number

    @floating_point_number.setter
    def floating_point_number(self, floating_point_number):
        """
        Sets the floating_point_number of this ArrayNode.


        :param floating_point_number: The floating_point_number of this ArrayNode.
        :type: bool
        """
        
        self._floating_point_number = floating_point_number

    @property
    def value_node(self):
        """
        Gets the value_node of this ArrayNode.


        :return: The value_node of this ArrayNode.
        :rtype: bool
        """
        return self._value_node

    @value_node.setter
    def value_node(self, value_node):
        """
        Sets the value_node of this ArrayNode.


        :param value_node: The value_node of this ArrayNode.
        :type: bool
        """
        
        self._value_node = value_node

    @property
    def container_node(self):
        """
        Gets the container_node of this ArrayNode.


        :return: The container_node of this ArrayNode.
        :rtype: bool
        """
        return self._container_node

    @container_node.setter
    def container_node(self, container_node):
        """
        Sets the container_node of this ArrayNode.


        :param container_node: The container_node of this ArrayNode.
        :type: bool
        """
        
        self._container_node = container_node

    @property
    def missing_node(self):
        """
        Gets the missing_node of this ArrayNode.


        :return: The missing_node of this ArrayNode.
        :rtype: bool
        """
        return self._missing_node

    @missing_node.setter
    def missing_node(self, missing_node):
        """
        Sets the missing_node of this ArrayNode.


        :param missing_node: The missing_node of this ArrayNode.
        :type: bool
        """
        
        self._missing_node = missing_node

    @property
    def pojo(self):
        """
        Gets the pojo of this ArrayNode.


        :return: The pojo of this ArrayNode.
        :rtype: bool
        """
        return self._pojo

    @pojo.setter
    def pojo(self, pojo):
        """
        Sets the pojo of this ArrayNode.


        :param pojo: The pojo of this ArrayNode.
        :type: bool
        """
        
        self._pojo = pojo

    @property
    def integral_number(self):
        """
        Gets the integral_number of this ArrayNode.


        :return: The integral_number of this ArrayNode.
        :rtype: bool
        """
        return self._integral_number

    @integral_number.setter
    def integral_number(self, integral_number):
        """
        Sets the integral_number of this ArrayNode.


        :param integral_number: The integral_number of this ArrayNode.
        :type: bool
        """
        
        self._integral_number = integral_number

    @property
    def short(self):
        """
        Gets the short of this ArrayNode.


        :return: The short of this ArrayNode.
        :rtype: bool
        """
        return self._short

    @short.setter
    def short(self, short):
        """
        Sets the short of this ArrayNode.


        :param short: The short of this ArrayNode.
        :type: bool
        """
        
        self._short = short

    @property
    def int(self):
        """
        Gets the int of this ArrayNode.


        :return: The int of this ArrayNode.
        :rtype: bool
        """
        return self._int

    @int.setter
    def int(self, int):
        """
        Sets the int of this ArrayNode.


        :param int: The int of this ArrayNode.
        :type: bool
        """
        
        self._int = int

    @property
    def long(self):
        """
        Gets the long of this ArrayNode.


        :return: The long of this ArrayNode.
        :rtype: bool
        """
        return self._long

    @long.setter
    def long(self, long):
        """
        Sets the long of this ArrayNode.


        :param long: The long of this ArrayNode.
        :type: bool
        """
        
        self._long = long

    @property
    def double(self):
        """
        Gets the double of this ArrayNode.


        :return: The double of this ArrayNode.
        :rtype: bool
        """
        return self._double

    @double.setter
    def double(self, double):
        """
        Sets the double of this ArrayNode.


        :param double: The double of this ArrayNode.
        :type: bool
        """
        
        self._double = double

    @property
    def big_decimal(self):
        """
        Gets the big_decimal of this ArrayNode.


        :return: The big_decimal of this ArrayNode.
        :rtype: bool
        """
        return self._big_decimal

    @big_decimal.setter
    def big_decimal(self, big_decimal):
        """
        Sets the big_decimal of this ArrayNode.


        :param big_decimal: The big_decimal of this ArrayNode.
        :type: bool
        """
        
        self._big_decimal = big_decimal

    @property
    def big_integer(self):
        """
        Gets the big_integer of this ArrayNode.


        :return: The big_integer of this ArrayNode.
        :rtype: bool
        """
        return self._big_integer

    @big_integer.setter
    def big_integer(self, big_integer):
        """
        Sets the big_integer of this ArrayNode.


        :param big_integer: The big_integer of this ArrayNode.
        :type: bool
        """
        
        self._big_integer = big_integer

    @property
    def textual(self):
        """
        Gets the textual of this ArrayNode.


        :return: The textual of this ArrayNode.
        :rtype: bool
        """
        return self._textual

    @textual.setter
    def textual(self, textual):
        """
        Sets the textual of this ArrayNode.


        :param textual: The textual of this ArrayNode.
        :type: bool
        """
        
        self._textual = textual

    @property
    def binary(self):
        """
        Gets the binary of this ArrayNode.


        :return: The binary of this ArrayNode.
        :rtype: bool
        """
        return self._binary

    @binary.setter
    def binary(self, binary):
        """
        Sets the binary of this ArrayNode.


        :param binary: The binary of this ArrayNode.
        :type: bool
        """
        
        self._binary = binary

    @property
    def array(self):
        """
        Gets the array of this ArrayNode.


        :return: The array of this ArrayNode.
        :rtype: bool
        """
        return self._array

    @array.setter
    def array(self, array):
        """
        Sets the array of this ArrayNode.


        :param array: The array of this ArrayNode.
        :type: bool
        """
        
        self._array = array

    @property
    def null(self):
        """
        Gets the null of this ArrayNode.


        :return: The null of this ArrayNode.
        :rtype: bool
        """
        return self._null

    @null.setter
    def null(self, null):
        """
        Sets the null of this ArrayNode.


        :param null: The null of this ArrayNode.
        :type: bool
        """
        
        self._null = null

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
