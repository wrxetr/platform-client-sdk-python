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


class SchedulingStatusResponse(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        SchedulingStatusResponse - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'status': 'str',
            'error_details': 'list[SchedulingProcessingError]',
            'scheduling_result_uri': 'str',
            'percent_complete': 'int'
        }

        self.attribute_map = {
            'id': 'id',
            'status': 'status',
            'error_details': 'errorDetails',
            'scheduling_result_uri': 'schedulingResultUri',
            'percent_complete': 'percentComplete'
        }

        self._id = None
        self._status = None
        self._error_details = None
        self._scheduling_result_uri = None
        self._percent_complete = None

    @property
    def id(self):
        """
        Gets the id of this SchedulingStatusResponse.
        The ID generated for the scheduling job.  Use to GET result when job is completed.

        :return: The id of this SchedulingStatusResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this SchedulingStatusResponse.
        The ID generated for the scheduling job.  Use to GET result when job is completed.

        :param id: The id of this SchedulingStatusResponse.
        :type: str
        """
        
        self._id = id

    @property
    def status(self):
        """
        Gets the status of this SchedulingStatusResponse.
        The status of the scheduling job.

        :return: The status of this SchedulingStatusResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this SchedulingStatusResponse.
        The status of the scheduling job.

        :param status: The status of this SchedulingStatusResponse.
        :type: str
        """
        allowed_values = ["Pending", "Success", "Failed", "Ongoing", "PartialFailure"]
        if status.lower() not in map(str.lower, allowed_values):
            # print "Invalid value for status -> " + status
            self._status = "outdated_sdk_version"
        else:
            self._status = status

    @property
    def error_details(self):
        """
        Gets the error_details of this SchedulingStatusResponse.
        If the request could not be properly processed, error details will be given here.

        :return: The error_details of this SchedulingStatusResponse.
        :rtype: list[SchedulingProcessingError]
        """
        return self._error_details

    @error_details.setter
    def error_details(self, error_details):
        """
        Sets the error_details of this SchedulingStatusResponse.
        If the request could not be properly processed, error details will be given here.

        :param error_details: The error_details of this SchedulingStatusResponse.
        :type: list[SchedulingProcessingError]
        """
        
        self._error_details = error_details

    @property
    def scheduling_result_uri(self):
        """
        Gets the scheduling_result_uri of this SchedulingStatusResponse.
        The uri of the scheduling result. It has a value if the status is 'Success'.

        :return: The scheduling_result_uri of this SchedulingStatusResponse.
        :rtype: str
        """
        return self._scheduling_result_uri

    @scheduling_result_uri.setter
    def scheduling_result_uri(self, scheduling_result_uri):
        """
        Sets the scheduling_result_uri of this SchedulingStatusResponse.
        The uri of the scheduling result. It has a value if the status is 'Success'.

        :param scheduling_result_uri: The scheduling_result_uri of this SchedulingStatusResponse.
        :type: str
        """
        
        self._scheduling_result_uri = scheduling_result_uri

    @property
    def percent_complete(self):
        """
        Gets the percent_complete of this SchedulingStatusResponse.
        The percentage of the job that is complete.

        :return: The percent_complete of this SchedulingStatusResponse.
        :rtype: int
        """
        return self._percent_complete

    @percent_complete.setter
    def percent_complete(self, percent_complete):
        """
        Sets the percent_complete of this SchedulingStatusResponse.
        The percentage of the job that is complete.

        :param percent_complete: The percent_complete of this SchedulingStatusResponse.
        :type: int
        """
        
        self._percent_complete = percent_complete

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
