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


class RecordingDataV2Notification(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        RecordingDataV2Notification - a model defined in Swagger

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
            'workspace': 'DocumentDataV2NotificationWorkspace',
            'created_by': 'DocumentDataV2NotificationCreatedBy',
            'content_type': 'str',
            'content_length': 'int',
            'filename': 'str',
            'change_number': 'int',
            'date_uploaded': 'datetime',
            'uploaded_by': 'RecordingDataV2NotificationUserData',
            'lock_info': 'RecordingDataV2NotificationLockInfo',
            'self_uri': 'str',
            'duration_millieconds': 'int',
            'conversation': 'DocumentDataV2NotificationWorkspace',
            'read': 'bool'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'date_created': 'dateCreated',
            'date_modified': 'dateModified',
            'workspace': 'workspace',
            'created_by': 'createdBy',
            'content_type': 'contentType',
            'content_length': 'contentLength',
            'filename': 'filename',
            'change_number': 'changeNumber',
            'date_uploaded': 'dateUploaded',
            'uploaded_by': 'uploadedBy',
            'lock_info': 'lockInfo',
            'self_uri': 'selfUri',
            'duration_millieconds': 'durationMillieconds',
            'conversation': 'conversation',
            'read': 'read'
        }

        self._id = None
        self._name = None
        self._date_created = None
        self._date_modified = None
        self._workspace = None
        self._created_by = None
        self._content_type = None
        self._content_length = None
        self._filename = None
        self._change_number = None
        self._date_uploaded = None
        self._uploaded_by = None
        self._lock_info = None
        self._self_uri = None
        self._duration_millieconds = None
        self._conversation = None
        self._read = None

    @property
    def id(self):
        """
        Gets the id of this RecordingDataV2Notification.


        :return: The id of this RecordingDataV2Notification.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this RecordingDataV2Notification.


        :param id: The id of this RecordingDataV2Notification.
        :type: str
        """
        
        self._id = id

    @property
    def name(self):
        """
        Gets the name of this RecordingDataV2Notification.


        :return: The name of this RecordingDataV2Notification.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this RecordingDataV2Notification.


        :param name: The name of this RecordingDataV2Notification.
        :type: str
        """
        
        self._name = name

    @property
    def date_created(self):
        """
        Gets the date_created of this RecordingDataV2Notification.


        :return: The date_created of this RecordingDataV2Notification.
        :rtype: datetime
        """
        return self._date_created

    @date_created.setter
    def date_created(self, date_created):
        """
        Sets the date_created of this RecordingDataV2Notification.


        :param date_created: The date_created of this RecordingDataV2Notification.
        :type: datetime
        """
        
        self._date_created = date_created

    @property
    def date_modified(self):
        """
        Gets the date_modified of this RecordingDataV2Notification.


        :return: The date_modified of this RecordingDataV2Notification.
        :rtype: datetime
        """
        return self._date_modified

    @date_modified.setter
    def date_modified(self, date_modified):
        """
        Sets the date_modified of this RecordingDataV2Notification.


        :param date_modified: The date_modified of this RecordingDataV2Notification.
        :type: datetime
        """
        
        self._date_modified = date_modified

    @property
    def workspace(self):
        """
        Gets the workspace of this RecordingDataV2Notification.


        :return: The workspace of this RecordingDataV2Notification.
        :rtype: DocumentDataV2NotificationWorkspace
        """
        return self._workspace

    @workspace.setter
    def workspace(self, workspace):
        """
        Sets the workspace of this RecordingDataV2Notification.


        :param workspace: The workspace of this RecordingDataV2Notification.
        :type: DocumentDataV2NotificationWorkspace
        """
        
        self._workspace = workspace

    @property
    def created_by(self):
        """
        Gets the created_by of this RecordingDataV2Notification.


        :return: The created_by of this RecordingDataV2Notification.
        :rtype: DocumentDataV2NotificationCreatedBy
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """
        Sets the created_by of this RecordingDataV2Notification.


        :param created_by: The created_by of this RecordingDataV2Notification.
        :type: DocumentDataV2NotificationCreatedBy
        """
        
        self._created_by = created_by

    @property
    def content_type(self):
        """
        Gets the content_type of this RecordingDataV2Notification.


        :return: The content_type of this RecordingDataV2Notification.
        :rtype: str
        """
        return self._content_type

    @content_type.setter
    def content_type(self, content_type):
        """
        Sets the content_type of this RecordingDataV2Notification.


        :param content_type: The content_type of this RecordingDataV2Notification.
        :type: str
        """
        
        self._content_type = content_type

    @property
    def content_length(self):
        """
        Gets the content_length of this RecordingDataV2Notification.


        :return: The content_length of this RecordingDataV2Notification.
        :rtype: int
        """
        return self._content_length

    @content_length.setter
    def content_length(self, content_length):
        """
        Sets the content_length of this RecordingDataV2Notification.


        :param content_length: The content_length of this RecordingDataV2Notification.
        :type: int
        """
        
        self._content_length = content_length

    @property
    def filename(self):
        """
        Gets the filename of this RecordingDataV2Notification.


        :return: The filename of this RecordingDataV2Notification.
        :rtype: str
        """
        return self._filename

    @filename.setter
    def filename(self, filename):
        """
        Sets the filename of this RecordingDataV2Notification.


        :param filename: The filename of this RecordingDataV2Notification.
        :type: str
        """
        
        self._filename = filename

    @property
    def change_number(self):
        """
        Gets the change_number of this RecordingDataV2Notification.


        :return: The change_number of this RecordingDataV2Notification.
        :rtype: int
        """
        return self._change_number

    @change_number.setter
    def change_number(self, change_number):
        """
        Sets the change_number of this RecordingDataV2Notification.


        :param change_number: The change_number of this RecordingDataV2Notification.
        :type: int
        """
        
        self._change_number = change_number

    @property
    def date_uploaded(self):
        """
        Gets the date_uploaded of this RecordingDataV2Notification.


        :return: The date_uploaded of this RecordingDataV2Notification.
        :rtype: datetime
        """
        return self._date_uploaded

    @date_uploaded.setter
    def date_uploaded(self, date_uploaded):
        """
        Sets the date_uploaded of this RecordingDataV2Notification.


        :param date_uploaded: The date_uploaded of this RecordingDataV2Notification.
        :type: datetime
        """
        
        self._date_uploaded = date_uploaded

    @property
    def uploaded_by(self):
        """
        Gets the uploaded_by of this RecordingDataV2Notification.


        :return: The uploaded_by of this RecordingDataV2Notification.
        :rtype: RecordingDataV2NotificationUserData
        """
        return self._uploaded_by

    @uploaded_by.setter
    def uploaded_by(self, uploaded_by):
        """
        Sets the uploaded_by of this RecordingDataV2Notification.


        :param uploaded_by: The uploaded_by of this RecordingDataV2Notification.
        :type: RecordingDataV2NotificationUserData
        """
        
        self._uploaded_by = uploaded_by

    @property
    def lock_info(self):
        """
        Gets the lock_info of this RecordingDataV2Notification.


        :return: The lock_info of this RecordingDataV2Notification.
        :rtype: RecordingDataV2NotificationLockInfo
        """
        return self._lock_info

    @lock_info.setter
    def lock_info(self, lock_info):
        """
        Sets the lock_info of this RecordingDataV2Notification.


        :param lock_info: The lock_info of this RecordingDataV2Notification.
        :type: RecordingDataV2NotificationLockInfo
        """
        
        self._lock_info = lock_info

    @property
    def self_uri(self):
        """
        Gets the self_uri of this RecordingDataV2Notification.


        :return: The self_uri of this RecordingDataV2Notification.
        :rtype: str
        """
        return self._self_uri

    @self_uri.setter
    def self_uri(self, self_uri):
        """
        Sets the self_uri of this RecordingDataV2Notification.


        :param self_uri: The self_uri of this RecordingDataV2Notification.
        :type: str
        """
        
        self._self_uri = self_uri

    @property
    def duration_millieconds(self):
        """
        Gets the duration_millieconds of this RecordingDataV2Notification.


        :return: The duration_millieconds of this RecordingDataV2Notification.
        :rtype: int
        """
        return self._duration_millieconds

    @duration_millieconds.setter
    def duration_millieconds(self, duration_millieconds):
        """
        Sets the duration_millieconds of this RecordingDataV2Notification.


        :param duration_millieconds: The duration_millieconds of this RecordingDataV2Notification.
        :type: int
        """
        
        self._duration_millieconds = duration_millieconds

    @property
    def conversation(self):
        """
        Gets the conversation of this RecordingDataV2Notification.


        :return: The conversation of this RecordingDataV2Notification.
        :rtype: DocumentDataV2NotificationWorkspace
        """
        return self._conversation

    @conversation.setter
    def conversation(self, conversation):
        """
        Sets the conversation of this RecordingDataV2Notification.


        :param conversation: The conversation of this RecordingDataV2Notification.
        :type: DocumentDataV2NotificationWorkspace
        """
        
        self._conversation = conversation

    @property
    def read(self):
        """
        Gets the read of this RecordingDataV2Notification.


        :return: The read of this RecordingDataV2Notification.
        :rtype: bool
        """
        return self._read

    @read.setter
    def read(self, read):
        """
        Sets the read of this RecordingDataV2Notification.


        :param read: The read of this RecordingDataV2Notification.
        :type: bool
        """
        
        self._read = read

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

