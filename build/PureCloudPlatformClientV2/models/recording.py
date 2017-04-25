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


class Recording(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        Recording - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'name': 'str',
            'conversation_id': 'str',
            'path': 'str',
            'start_time': 'str',
            'end_time': 'str',
            'media': 'str',
            'annotations': 'list[Annotation]',
            'transcript': 'list[ChatMessage]',
            'email_transcript': 'list[RecordingEmailMessage]',
            'file_state': 'str',
            'restore_expiration_time': 'datetime',
            'media_uris': 'dict(str, MediaResult)',
            'estimated_transcode_time_ms': 'int',
            'actual_transcode_time_ms': 'int',
            'archive_date': 'datetime',
            'archive_medium': 'str',
            'delete_date': 'datetime',
            'max_allowed_restorations_for_org': 'int',
            'remaining_restorations_allowed_for_org': 'int',
            'session_id': 'str',
            'self_uri': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'conversation_id': 'conversationId',
            'path': 'path',
            'start_time': 'startTime',
            'end_time': 'endTime',
            'media': 'media',
            'annotations': 'annotations',
            'transcript': 'transcript',
            'email_transcript': 'emailTranscript',
            'file_state': 'fileState',
            'restore_expiration_time': 'restoreExpirationTime',
            'media_uris': 'mediaUris',
            'estimated_transcode_time_ms': 'estimatedTranscodeTimeMs',
            'actual_transcode_time_ms': 'actualTranscodeTimeMs',
            'archive_date': 'archiveDate',
            'archive_medium': 'archiveMedium',
            'delete_date': 'deleteDate',
            'max_allowed_restorations_for_org': 'maxAllowedRestorationsForOrg',
            'remaining_restorations_allowed_for_org': 'remainingRestorationsAllowedForOrg',
            'session_id': 'sessionId',
            'self_uri': 'selfUri'
        }

        self._id = None
        self._name = None
        self._conversation_id = None
        self._path = None
        self._start_time = None
        self._end_time = None
        self._media = None
        self._annotations = None
        self._transcript = None
        self._email_transcript = None
        self._file_state = None
        self._restore_expiration_time = None
        self._media_uris = None
        self._estimated_transcode_time_ms = None
        self._actual_transcode_time_ms = None
        self._archive_date = None
        self._archive_medium = None
        self._delete_date = None
        self._max_allowed_restorations_for_org = None
        self._remaining_restorations_allowed_for_org = None
        self._session_id = None
        self._self_uri = None

    @property
    def id(self):
        """
        Gets the id of this Recording.
        The globally unique identifier for the object.

        :return: The id of this Recording.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Recording.
        The globally unique identifier for the object.

        :param id: The id of this Recording.
        :type: str
        """
        
        self._id = id

    @property
    def name(self):
        """
        Gets the name of this Recording.


        :return: The name of this Recording.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Recording.


        :param name: The name of this Recording.
        :type: str
        """
        
        self._name = name

    @property
    def conversation_id(self):
        """
        Gets the conversation_id of this Recording.


        :return: The conversation_id of this Recording.
        :rtype: str
        """
        return self._conversation_id

    @conversation_id.setter
    def conversation_id(self, conversation_id):
        """
        Sets the conversation_id of this Recording.


        :param conversation_id: The conversation_id of this Recording.
        :type: str
        """
        
        self._conversation_id = conversation_id

    @property
    def path(self):
        """
        Gets the path of this Recording.


        :return: The path of this Recording.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """
        Sets the path of this Recording.


        :param path: The path of this Recording.
        :type: str
        """
        
        self._path = path

    @property
    def start_time(self):
        """
        Gets the start_time of this Recording.


        :return: The start_time of this Recording.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """
        Sets the start_time of this Recording.


        :param start_time: The start_time of this Recording.
        :type: str
        """
        
        self._start_time = start_time

    @property
    def end_time(self):
        """
        Gets the end_time of this Recording.


        :return: The end_time of this Recording.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """
        Sets the end_time of this Recording.


        :param end_time: The end_time of this Recording.
        :type: str
        """
        
        self._end_time = end_time

    @property
    def media(self):
        """
        Gets the media of this Recording.
        The type of media that the recording is. At the moment that could be audio, chat, or email.

        :return: The media of this Recording.
        :rtype: str
        """
        return self._media

    @media.setter
    def media(self, media):
        """
        Sets the media of this Recording.
        The type of media that the recording is. At the moment that could be audio, chat, or email.

        :param media: The media of this Recording.
        :type: str
        """
        
        self._media = media

    @property
    def annotations(self):
        """
        Gets the annotations of this Recording.
        Annotations that belong to the recording.

        :return: The annotations of this Recording.
        :rtype: list[Annotation]
        """
        return self._annotations

    @annotations.setter
    def annotations(self, annotations):
        """
        Sets the annotations of this Recording.
        Annotations that belong to the recording.

        :param annotations: The annotations of this Recording.
        :type: list[Annotation]
        """
        
        self._annotations = annotations

    @property
    def transcript(self):
        """
        Gets the transcript of this Recording.
        Represents a chat transcript

        :return: The transcript of this Recording.
        :rtype: list[ChatMessage]
        """
        return self._transcript

    @transcript.setter
    def transcript(self, transcript):
        """
        Sets the transcript of this Recording.
        Represents a chat transcript

        :param transcript: The transcript of this Recording.
        :type: list[ChatMessage]
        """
        
        self._transcript = transcript

    @property
    def email_transcript(self):
        """
        Gets the email_transcript of this Recording.
        Represents an email transcript

        :return: The email_transcript of this Recording.
        :rtype: list[RecordingEmailMessage]
        """
        return self._email_transcript

    @email_transcript.setter
    def email_transcript(self, email_transcript):
        """
        Sets the email_transcript of this Recording.
        Represents an email transcript

        :param email_transcript: The email_transcript of this Recording.
        :type: list[RecordingEmailMessage]
        """
        
        self._email_transcript = email_transcript

    @property
    def file_state(self):
        """
        Gets the file_state of this Recording.
        Represents the current file state for a recording. Examples: Uploading, Archived, etc

        :return: The file_state of this Recording.
        :rtype: str
        """
        return self._file_state

    @file_state.setter
    def file_state(self, file_state):
        """
        Sets the file_state of this Recording.
        Represents the current file state for a recording. Examples: Uploading, Archived, etc

        :param file_state: The file_state of this Recording.
        :type: str
        """
        allowed_values = ["ARCHIVED", "AVAILABLE", "DELETED", "RESTORED", "RESTORING", "UPLOADING"]
        if file_state.lower() not in map(str.lower, allowed_values):
            # print "Invalid value for file_state -> " + file_state
            self._file_state = "outdated_sdk_version"
        else:
            self._file_state = file_state

    @property
    def restore_expiration_time(self):
        """
        Gets the restore_expiration_time of this Recording.
        The amount of time a restored recording will remain restored before being archived again. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ

        :return: The restore_expiration_time of this Recording.
        :rtype: datetime
        """
        return self._restore_expiration_time

    @restore_expiration_time.setter
    def restore_expiration_time(self, restore_expiration_time):
        """
        Sets the restore_expiration_time of this Recording.
        The amount of time a restored recording will remain restored before being archived again. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ

        :param restore_expiration_time: The restore_expiration_time of this Recording.
        :type: datetime
        """
        
        self._restore_expiration_time = restore_expiration_time

    @property
    def media_uris(self):
        """
        Gets the media_uris of this Recording.
        The different mediaUris for the recording.

        :return: The media_uris of this Recording.
        :rtype: dict(str, MediaResult)
        """
        return self._media_uris

    @media_uris.setter
    def media_uris(self, media_uris):
        """
        Sets the media_uris of this Recording.
        The different mediaUris for the recording.

        :param media_uris: The media_uris of this Recording.
        :type: dict(str, MediaResult)
        """
        
        self._media_uris = media_uris

    @property
    def estimated_transcode_time_ms(self):
        """
        Gets the estimated_transcode_time_ms of this Recording.


        :return: The estimated_transcode_time_ms of this Recording.
        :rtype: int
        """
        return self._estimated_transcode_time_ms

    @estimated_transcode_time_ms.setter
    def estimated_transcode_time_ms(self, estimated_transcode_time_ms):
        """
        Sets the estimated_transcode_time_ms of this Recording.


        :param estimated_transcode_time_ms: The estimated_transcode_time_ms of this Recording.
        :type: int
        """
        
        self._estimated_transcode_time_ms = estimated_transcode_time_ms

    @property
    def actual_transcode_time_ms(self):
        """
        Gets the actual_transcode_time_ms of this Recording.


        :return: The actual_transcode_time_ms of this Recording.
        :rtype: int
        """
        return self._actual_transcode_time_ms

    @actual_transcode_time_ms.setter
    def actual_transcode_time_ms(self, actual_transcode_time_ms):
        """
        Sets the actual_transcode_time_ms of this Recording.


        :param actual_transcode_time_ms: The actual_transcode_time_ms of this Recording.
        :type: int
        """
        
        self._actual_transcode_time_ms = actual_transcode_time_ms

    @property
    def archive_date(self):
        """
        Gets the archive_date of this Recording.
        The date the recording will be archived. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ

        :return: The archive_date of this Recording.
        :rtype: datetime
        """
        return self._archive_date

    @archive_date.setter
    def archive_date(self, archive_date):
        """
        Sets the archive_date of this Recording.
        The date the recording will be archived. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ

        :param archive_date: The archive_date of this Recording.
        :type: datetime
        """
        
        self._archive_date = archive_date

    @property
    def archive_medium(self):
        """
        Gets the archive_medium of this Recording.
        The type of archive medium used. Example: CloudArchive

        :return: The archive_medium of this Recording.
        :rtype: str
        """
        return self._archive_medium

    @archive_medium.setter
    def archive_medium(self, archive_medium):
        """
        Sets the archive_medium of this Recording.
        The type of archive medium used. Example: CloudArchive

        :param archive_medium: The archive_medium of this Recording.
        :type: str
        """
        allowed_values = ["CLOUDARCHIVE"]
        if archive_medium.lower() not in map(str.lower, allowed_values):
            # print "Invalid value for archive_medium -> " + archive_medium
            self._archive_medium = "outdated_sdk_version"
        else:
            self._archive_medium = archive_medium

    @property
    def delete_date(self):
        """
        Gets the delete_date of this Recording.
        The date the recording will be deleted. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ

        :return: The delete_date of this Recording.
        :rtype: datetime
        """
        return self._delete_date

    @delete_date.setter
    def delete_date(self, delete_date):
        """
        Sets the delete_date of this Recording.
        The date the recording will be deleted. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ

        :param delete_date: The delete_date of this Recording.
        :type: datetime
        """
        
        self._delete_date = delete_date

    @property
    def max_allowed_restorations_for_org(self):
        """
        Gets the max_allowed_restorations_for_org of this Recording.
        How many archive restorations the organization is allowed to have.

        :return: The max_allowed_restorations_for_org of this Recording.
        :rtype: int
        """
        return self._max_allowed_restorations_for_org

    @max_allowed_restorations_for_org.setter
    def max_allowed_restorations_for_org(self, max_allowed_restorations_for_org):
        """
        Sets the max_allowed_restorations_for_org of this Recording.
        How many archive restorations the organization is allowed to have.

        :param max_allowed_restorations_for_org: The max_allowed_restorations_for_org of this Recording.
        :type: int
        """
        
        self._max_allowed_restorations_for_org = max_allowed_restorations_for_org

    @property
    def remaining_restorations_allowed_for_org(self):
        """
        Gets the remaining_restorations_allowed_for_org of this Recording.
        The remaining archive restorations the organization has.

        :return: The remaining_restorations_allowed_for_org of this Recording.
        :rtype: int
        """
        return self._remaining_restorations_allowed_for_org

    @remaining_restorations_allowed_for_org.setter
    def remaining_restorations_allowed_for_org(self, remaining_restorations_allowed_for_org):
        """
        Sets the remaining_restorations_allowed_for_org of this Recording.
        The remaining archive restorations the organization has.

        :param remaining_restorations_allowed_for_org: The remaining_restorations_allowed_for_org of this Recording.
        :type: int
        """
        
        self._remaining_restorations_allowed_for_org = remaining_restorations_allowed_for_org

    @property
    def session_id(self):
        """
        Gets the session_id of this Recording.
        The session id represents an external resource id, such as email, call, chat, etc

        :return: The session_id of this Recording.
        :rtype: str
        """
        return self._session_id

    @session_id.setter
    def session_id(self, session_id):
        """
        Sets the session_id of this Recording.
        The session id represents an external resource id, such as email, call, chat, etc

        :param session_id: The session_id of this Recording.
        :type: str
        """
        
        self._session_id = session_id

    @property
    def self_uri(self):
        """
        Gets the self_uri of this Recording.
        The URI for this object

        :return: The self_uri of this Recording.
        :rtype: str
        """
        return self._self_uri

    @self_uri.setter
    def self_uri(self, self_uri):
        """
        Sets the self_uri of this Recording.
        The URI for this object

        :param self_uri: The self_uri of this Recording.
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

