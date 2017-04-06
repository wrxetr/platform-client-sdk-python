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


class ContactListNotification(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        ContactListNotification - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'name': 'str',
            'date_created': 'datetime',
            'date_modified': 'datetime',
            'version': 'int',
            'column_names': 'list[str]',
            'phone_columns': 'list[ContactListNotificationPhoneColumns]',
            'import_status': 'ContactListNotificationImportStatus',
            'preview_mode_column_name': 'str',
            'preview_mode_accepted_values': 'list[str]',
            'size': 'int',
            'attempt_limits': 'DocumentDataV2NotificationCreatedBy',
            'additional_properties': 'object'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'date_created': 'dateCreated',
            'date_modified': 'dateModified',
            'version': 'version',
            'column_names': 'columnNames',
            'phone_columns': 'phoneColumns',
            'import_status': 'importStatus',
            'preview_mode_column_name': 'previewModeColumnName',
            'preview_mode_accepted_values': 'previewModeAcceptedValues',
            'size': 'size',
            'attempt_limits': 'attemptLimits',
            'additional_properties': 'additionalProperties'
        }

        self._id = None
        self._name = None
        self._date_created = None
        self._date_modified = None
        self._version = None
        self._column_names = None
        self._phone_columns = None
        self._import_status = None
        self._preview_mode_column_name = None
        self._preview_mode_accepted_values = None
        self._size = None
        self._attempt_limits = None
        self._additional_properties = None

    @property
    def id(self):
        """
        Gets the id of this ContactListNotification.


        :return: The id of this ContactListNotification.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ContactListNotification.


        :param id: The id of this ContactListNotification.
        :type: str
        """
        
        self._id = id

    @property
    def name(self):
        """
        Gets the name of this ContactListNotification.


        :return: The name of this ContactListNotification.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this ContactListNotification.


        :param name: The name of this ContactListNotification.
        :type: str
        """
        
        self._name = name

    @property
    def date_created(self):
        """
        Gets the date_created of this ContactListNotification.


        :return: The date_created of this ContactListNotification.
        :rtype: datetime
        """
        return self._date_created

    @date_created.setter
    def date_created(self, date_created):
        """
        Sets the date_created of this ContactListNotification.


        :param date_created: The date_created of this ContactListNotification.
        :type: datetime
        """
        
        self._date_created = date_created

    @property
    def date_modified(self):
        """
        Gets the date_modified of this ContactListNotification.


        :return: The date_modified of this ContactListNotification.
        :rtype: datetime
        """
        return self._date_modified

    @date_modified.setter
    def date_modified(self, date_modified):
        """
        Sets the date_modified of this ContactListNotification.


        :param date_modified: The date_modified of this ContactListNotification.
        :type: datetime
        """
        
        self._date_modified = date_modified

    @property
    def version(self):
        """
        Gets the version of this ContactListNotification.


        :return: The version of this ContactListNotification.
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """
        Sets the version of this ContactListNotification.


        :param version: The version of this ContactListNotification.
        :type: int
        """
        
        self._version = version

    @property
    def column_names(self):
        """
        Gets the column_names of this ContactListNotification.


        :return: The column_names of this ContactListNotification.
        :rtype: list[str]
        """
        return self._column_names

    @column_names.setter
    def column_names(self, column_names):
        """
        Sets the column_names of this ContactListNotification.


        :param column_names: The column_names of this ContactListNotification.
        :type: list[str]
        """
        
        self._column_names = column_names

    @property
    def phone_columns(self):
        """
        Gets the phone_columns of this ContactListNotification.


        :return: The phone_columns of this ContactListNotification.
        :rtype: list[ContactListNotificationPhoneColumns]
        """
        return self._phone_columns

    @phone_columns.setter
    def phone_columns(self, phone_columns):
        """
        Sets the phone_columns of this ContactListNotification.


        :param phone_columns: The phone_columns of this ContactListNotification.
        :type: list[ContactListNotificationPhoneColumns]
        """
        
        self._phone_columns = phone_columns

    @property
    def import_status(self):
        """
        Gets the import_status of this ContactListNotification.


        :return: The import_status of this ContactListNotification.
        :rtype: ContactListNotificationImportStatus
        """
        return self._import_status

    @import_status.setter
    def import_status(self, import_status):
        """
        Sets the import_status of this ContactListNotification.


        :param import_status: The import_status of this ContactListNotification.
        :type: ContactListNotificationImportStatus
        """
        
        self._import_status = import_status

    @property
    def preview_mode_column_name(self):
        """
        Gets the preview_mode_column_name of this ContactListNotification.


        :return: The preview_mode_column_name of this ContactListNotification.
        :rtype: str
        """
        return self._preview_mode_column_name

    @preview_mode_column_name.setter
    def preview_mode_column_name(self, preview_mode_column_name):
        """
        Sets the preview_mode_column_name of this ContactListNotification.


        :param preview_mode_column_name: The preview_mode_column_name of this ContactListNotification.
        :type: str
        """
        
        self._preview_mode_column_name = preview_mode_column_name

    @property
    def preview_mode_accepted_values(self):
        """
        Gets the preview_mode_accepted_values of this ContactListNotification.


        :return: The preview_mode_accepted_values of this ContactListNotification.
        :rtype: list[str]
        """
        return self._preview_mode_accepted_values

    @preview_mode_accepted_values.setter
    def preview_mode_accepted_values(self, preview_mode_accepted_values):
        """
        Sets the preview_mode_accepted_values of this ContactListNotification.


        :param preview_mode_accepted_values: The preview_mode_accepted_values of this ContactListNotification.
        :type: list[str]
        """
        
        self._preview_mode_accepted_values = preview_mode_accepted_values

    @property
    def size(self):
        """
        Gets the size of this ContactListNotification.


        :return: The size of this ContactListNotification.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """
        Sets the size of this ContactListNotification.


        :param size: The size of this ContactListNotification.
        :type: int
        """
        
        self._size = size

    @property
    def attempt_limits(self):
        """
        Gets the attempt_limits of this ContactListNotification.


        :return: The attempt_limits of this ContactListNotification.
        :rtype: DocumentDataV2NotificationCreatedBy
        """
        return self._attempt_limits

    @attempt_limits.setter
    def attempt_limits(self, attempt_limits):
        """
        Sets the attempt_limits of this ContactListNotification.


        :param attempt_limits: The attempt_limits of this ContactListNotification.
        :type: DocumentDataV2NotificationCreatedBy
        """
        
        self._attempt_limits = attempt_limits

    @property
    def additional_properties(self):
        """
        Gets the additional_properties of this ContactListNotification.


        :return: The additional_properties of this ContactListNotification.
        :rtype: object
        """
        return self._additional_properties

    @additional_properties.setter
    def additional_properties(self, additional_properties):
        """
        Sets the additional_properties of this ContactListNotification.


        :param additional_properties: The additional_properties of this ContactListNotification.
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
