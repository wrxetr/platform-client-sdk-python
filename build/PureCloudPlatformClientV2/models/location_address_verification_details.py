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

class LocationAddressVerificationDetails(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        LocationAddressVerificationDetails - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'status': 'str',
            'date_finished': 'datetime',
            'date_started': 'datetime',
            'service': 'str'
        }

        self.attribute_map = {
            'status': 'status',
            'date_finished': 'dateFinished',
            'date_started': 'dateStarted',
            'service': 'service'
        }

        self._status = None
        self._date_finished = None
        self._date_started = None
        self._service = None

    @property
    def status(self):
        """
        Gets the status of this LocationAddressVerificationDetails.
        Status of address verification process

        :return: The status of this LocationAddressVerificationDetails.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this LocationAddressVerificationDetails.
        Status of address verification process

        :param status: The status of this LocationAddressVerificationDetails.
        :type: str
        """
        allowed_values = ["Pending", "InProgress", "Retry", "Complete", "Failed"]
        if status.lower() not in map(str.lower, allowed_values):
            # print "Invalid value for status -> " + status
            self._status = "outdated_sdk_version"
        else:
            self._status = status

    @property
    def date_finished(self):
        """
        Gets the date_finished of this LocationAddressVerificationDetails.
        Finished time of address verification process. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ

        :return: The date_finished of this LocationAddressVerificationDetails.
        :rtype: datetime
        """
        return self._date_finished

    @date_finished.setter
    def date_finished(self, date_finished):
        """
        Sets the date_finished of this LocationAddressVerificationDetails.
        Finished time of address verification process. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ

        :param date_finished: The date_finished of this LocationAddressVerificationDetails.
        :type: datetime
        """
        
        self._date_finished = date_finished

    @property
    def date_started(self):
        """
        Gets the date_started of this LocationAddressVerificationDetails.
        Time started of address verification process. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ

        :return: The date_started of this LocationAddressVerificationDetails.
        :rtype: datetime
        """
        return self._date_started

    @date_started.setter
    def date_started(self, date_started):
        """
        Sets the date_started of this LocationAddressVerificationDetails.
        Time started of address verification process. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ

        :param date_started: The date_started of this LocationAddressVerificationDetails.
        :type: datetime
        """
        
        self._date_started = date_started

    @property
    def service(self):
        """
        Gets the service of this LocationAddressVerificationDetails.
        Third party service used for address verification

        :return: The service of this LocationAddressVerificationDetails.
        :rtype: str
        """
        return self._service

    @service.setter
    def service(self, service):
        """
        Sets the service of this LocationAddressVerificationDetails.
        Third party service used for address verification

        :param service: The service of this LocationAddressVerificationDetails.
        :type: str
        """
        
        self._service = service

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

