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


class QueueConversationSocialExpressionEventTopicVoicemail(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        QueueConversationSocialExpressionEventTopicVoicemail - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'upload_status': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'upload_status': 'uploadStatus'
        }

        self._id = None
        self._upload_status = None

    @property
    def id(self):
        """
        Gets the id of this QueueConversationSocialExpressionEventTopicVoicemail.


        :return: The id of this QueueConversationSocialExpressionEventTopicVoicemail.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this QueueConversationSocialExpressionEventTopicVoicemail.


        :param id: The id of this QueueConversationSocialExpressionEventTopicVoicemail.
        :type: str
        """
        
        self._id = id

    @property
    def upload_status(self):
        """
        Gets the upload_status of this QueueConversationSocialExpressionEventTopicVoicemail.


        :return: The upload_status of this QueueConversationSocialExpressionEventTopicVoicemail.
        :rtype: str
        """
        return self._upload_status

    @upload_status.setter
    def upload_status(self, upload_status):
        """
        Sets the upload_status of this QueueConversationSocialExpressionEventTopicVoicemail.


        :param upload_status: The upload_status of this QueueConversationSocialExpressionEventTopicVoicemail.
        :type: str
        """
        allowed_values = ["PENDING", "COMPLETE", "FAILED", "TIMEOUT"]
        if upload_status.lower() not in map(str.lower, allowed_values):
            # print "Invalid value for upload_status -> " + upload_status
            self._upload_status = "outdated_sdk_version"
        else:
            self._upload_status = upload_status

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

