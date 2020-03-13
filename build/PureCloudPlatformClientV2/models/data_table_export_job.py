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

class DataTableExportJob(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        DataTableExportJob - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'name': 'str',
            'owner': 'AddressableEntityRef',
            'status': 'str',
            'date_created': 'datetime',
            'date_completed': 'datetime',
            'download_uri': 'str',
            'error_information': 'ErrorBody',
            'count_records_processed': 'int',
            'self_uri': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'owner': 'owner',
            'status': 'status',
            'date_created': 'dateCreated',
            'date_completed': 'dateCompleted',
            'download_uri': 'downloadURI',
            'error_information': 'errorInformation',
            'count_records_processed': 'countRecordsProcessed',
            'self_uri': 'selfUri'
        }

        self._id = None
        self._name = None
        self._owner = None
        self._status = None
        self._date_created = None
        self._date_completed = None
        self._download_uri = None
        self._error_information = None
        self._count_records_processed = None
        self._self_uri = None

    @property
    def id(self):
        """
        Gets the id of this DataTableExportJob.
        The globally unique identifier for the object.

        :return: The id of this DataTableExportJob.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this DataTableExportJob.
        The globally unique identifier for the object.

        :param id: The id of this DataTableExportJob.
        :type: str
        """
        
        self._id = id

    @property
    def name(self):
        """
        Gets the name of this DataTableExportJob.


        :return: The name of this DataTableExportJob.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this DataTableExportJob.


        :param name: The name of this DataTableExportJob.
        :type: str
        """
        
        self._name = name

    @property
    def owner(self):
        """
        Gets the owner of this DataTableExportJob.
        The PureCloud user who started the export job

        :return: The owner of this DataTableExportJob.
        :rtype: AddressableEntityRef
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """
        Sets the owner of this DataTableExportJob.
        The PureCloud user who started the export job

        :param owner: The owner of this DataTableExportJob.
        :type: AddressableEntityRef
        """
        
        self._owner = owner

    @property
    def status(self):
        """
        Gets the status of this DataTableExportJob.
        The status of the export job

        :return: The status of this DataTableExportJob.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this DataTableExportJob.
        The status of the export job

        :param status: The status of this DataTableExportJob.
        :type: str
        """
        allowed_values = ["Processing", "Failed", "Succeeded"]
        if status.lower() not in map(str.lower, allowed_values):
            # print "Invalid value for status -> " + status
            self._status = "outdated_sdk_version"
        else:
            self._status = status

    @property
    def date_created(self):
        """
        Gets the date_created of this DataTableExportJob.
        The timestamp of when the export began. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ

        :return: The date_created of this DataTableExportJob.
        :rtype: datetime
        """
        return self._date_created

    @date_created.setter
    def date_created(self, date_created):
        """
        Sets the date_created of this DataTableExportJob.
        The timestamp of when the export began. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ

        :param date_created: The date_created of this DataTableExportJob.
        :type: datetime
        """
        
        self._date_created = date_created

    @property
    def date_completed(self):
        """
        Gets the date_completed of this DataTableExportJob.
        The timestamp of when the export stopped (either successfully or unsuccessfully). Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ

        :return: The date_completed of this DataTableExportJob.
        :rtype: datetime
        """
        return self._date_completed

    @date_completed.setter
    def date_completed(self, date_completed):
        """
        Sets the date_completed of this DataTableExportJob.
        The timestamp of when the export stopped (either successfully or unsuccessfully). Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ

        :param date_completed: The date_completed of this DataTableExportJob.
        :type: datetime
        """
        
        self._date_completed = date_completed

    @property
    def download_uri(self):
        """
        Gets the download_uri of this DataTableExportJob.
        The URL of the location at which the caller can download the export file, when available

        :return: The download_uri of this DataTableExportJob.
        :rtype: str
        """
        return self._download_uri

    @download_uri.setter
    def download_uri(self, download_uri):
        """
        Sets the download_uri of this DataTableExportJob.
        The URL of the location at which the caller can download the export file, when available

        :param download_uri: The download_uri of this DataTableExportJob.
        :type: str
        """
        
        self._download_uri = download_uri

    @property
    def error_information(self):
        """
        Gets the error_information of this DataTableExportJob.
        Any error information, or null of the processing is not in an error state

        :return: The error_information of this DataTableExportJob.
        :rtype: ErrorBody
        """
        return self._error_information

    @error_information.setter
    def error_information(self, error_information):
        """
        Sets the error_information of this DataTableExportJob.
        Any error information, or null of the processing is not in an error state

        :param error_information: The error_information of this DataTableExportJob.
        :type: ErrorBody
        """
        
        self._error_information = error_information

    @property
    def count_records_processed(self):
        """
        Gets the count_records_processed of this DataTableExportJob.
        The current count of the number of records processed

        :return: The count_records_processed of this DataTableExportJob.
        :rtype: int
        """
        return self._count_records_processed

    @count_records_processed.setter
    def count_records_processed(self, count_records_processed):
        """
        Sets the count_records_processed of this DataTableExportJob.
        The current count of the number of records processed

        :param count_records_processed: The count_records_processed of this DataTableExportJob.
        :type: int
        """
        
        self._count_records_processed = count_records_processed

    @property
    def self_uri(self):
        """
        Gets the self_uri of this DataTableExportJob.
        The URI for this object

        :return: The self_uri of this DataTableExportJob.
        :rtype: str
        """
        return self._self_uri

    @self_uri.setter
    def self_uri(self, self_uri):
        """
        Sets the self_uri of this DataTableExportJob.
        The URI for this object

        :param self_uri: The self_uri of this DataTableExportJob.
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
