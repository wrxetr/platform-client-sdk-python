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


class LicenseUpdateStatus(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        LicenseUpdateStatus - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'user_id': 'str',
            'license_id': 'str',
            'result': 'str'
        }

        self.attribute_map = {
            'user_id': 'userId',
            'license_id': 'licenseId',
            'result': 'result'
        }

        self._user_id = None
        self._license_id = None
        self._result = None

    @property
    def user_id(self):
        """
        Gets the user_id of this LicenseUpdateStatus.


        :return: The user_id of this LicenseUpdateStatus.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """
        Sets the user_id of this LicenseUpdateStatus.


        :param user_id: The user_id of this LicenseUpdateStatus.
        :type: str
        """
        
        self._user_id = user_id

    @property
    def license_id(self):
        """
        Gets the license_id of this LicenseUpdateStatus.


        :return: The license_id of this LicenseUpdateStatus.
        :rtype: str
        """
        return self._license_id

    @license_id.setter
    def license_id(self, license_id):
        """
        Sets the license_id of this LicenseUpdateStatus.


        :param license_id: The license_id of this LicenseUpdateStatus.
        :type: str
        """
        
        self._license_id = license_id

    @property
    def result(self):
        """
        Gets the result of this LicenseUpdateStatus.


        :return: The result of this LicenseUpdateStatus.
        :rtype: str
        """
        return self._result

    @result.setter
    def result(self, result):
        """
        Sets the result of this LicenseUpdateStatus.


        :param result: The result of this LicenseUpdateStatus.
        :type: str
        """
        
        self._result = result

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

