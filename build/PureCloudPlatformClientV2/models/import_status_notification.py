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


class ImportStatusNotification(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        ImportStatusNotification - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'import_state': 'str',
            'total_records': 'int',
            'completed_records': 'int',
            'percentage_complete': 'int',
            'failure_reason': 'str',
            'additional_properties': 'object'
        }

        self.attribute_map = {
            'import_state': 'importState',
            'total_records': 'totalRecords',
            'completed_records': 'completedRecords',
            'percentage_complete': 'percentageComplete',
            'failure_reason': 'failureReason',
            'additional_properties': 'additionalProperties'
        }

        self._import_state = None
        self._total_records = None
        self._completed_records = None
        self._percentage_complete = None
        self._failure_reason = None
        self._additional_properties = None

    @property
    def import_state(self):
        """
        Gets the import_state of this ImportStatusNotification.


        :return: The import_state of this ImportStatusNotification.
        :rtype: str
        """
        return self._import_state

    @import_state.setter
    def import_state(self, import_state):
        """
        Sets the import_state of this ImportStatusNotification.


        :param import_state: The import_state of this ImportStatusNotification.
        :type: str
        """
        allowed_values = ["IN_PROGRESS", "FAILED"]
        if import_state.lower() not in map(str.lower, allowed_values):
            # print "Invalid value for import_state -> " + import_state
            self._import_state = "outdated_sdk_version"
        else:
            self._import_state = import_state.lower()

    @property
    def total_records(self):
        """
        Gets the total_records of this ImportStatusNotification.


        :return: The total_records of this ImportStatusNotification.
        :rtype: int
        """
        return self._total_records

    @total_records.setter
    def total_records(self, total_records):
        """
        Sets the total_records of this ImportStatusNotification.


        :param total_records: The total_records of this ImportStatusNotification.
        :type: int
        """
        
        self._total_records = total_records

    @property
    def completed_records(self):
        """
        Gets the completed_records of this ImportStatusNotification.


        :return: The completed_records of this ImportStatusNotification.
        :rtype: int
        """
        return self._completed_records

    @completed_records.setter
    def completed_records(self, completed_records):
        """
        Sets the completed_records of this ImportStatusNotification.


        :param completed_records: The completed_records of this ImportStatusNotification.
        :type: int
        """
        
        self._completed_records = completed_records

    @property
    def percentage_complete(self):
        """
        Gets the percentage_complete of this ImportStatusNotification.


        :return: The percentage_complete of this ImportStatusNotification.
        :rtype: int
        """
        return self._percentage_complete

    @percentage_complete.setter
    def percentage_complete(self, percentage_complete):
        """
        Sets the percentage_complete of this ImportStatusNotification.


        :param percentage_complete: The percentage_complete of this ImportStatusNotification.
        :type: int
        """
        
        self._percentage_complete = percentage_complete

    @property
    def failure_reason(self):
        """
        Gets the failure_reason of this ImportStatusNotification.


        :return: The failure_reason of this ImportStatusNotification.
        :rtype: str
        """
        return self._failure_reason

    @failure_reason.setter
    def failure_reason(self, failure_reason):
        """
        Sets the failure_reason of this ImportStatusNotification.


        :param failure_reason: The failure_reason of this ImportStatusNotification.
        :type: str
        """
        
        self._failure_reason = failure_reason

    @property
    def additional_properties(self):
        """
        Gets the additional_properties of this ImportStatusNotification.


        :return: The additional_properties of this ImportStatusNotification.
        :rtype: object
        """
        return self._additional_properties

    @additional_properties.setter
    def additional_properties(self, additional_properties):
        """
        Sets the additional_properties of this ImportStatusNotification.


        :param additional_properties: The additional_properties of this ImportStatusNotification.
        :type: object
        """
        
        self._additional_properties = additional_properties

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

