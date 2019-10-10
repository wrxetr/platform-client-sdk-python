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

class SipDownloadResponse(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        SipDownloadResponse - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'download_id': 'str',
            'document_id': 'str'
        }

        self.attribute_map = {
            'download_id': 'downloadId',
            'document_id': 'documentId'
        }

        self._download_id = None
        self._document_id = None

    @property
    def download_id(self):
        """
        Gets the download_id of this SipDownloadResponse.
        unique id of the downloaded file

        :return: The download_id of this SipDownloadResponse.
        :rtype: str
        """
        return self._download_id

    @download_id.setter
    def download_id(self, download_id):
        """
        Sets the download_id of this SipDownloadResponse.
        unique id of the downloaded file

        :param download_id: The download_id of this SipDownloadResponse.
        :type: str
        """
        
        self._download_id = download_id

    @property
    def document_id(self):
        """
        Gets the document_id of this SipDownloadResponse.
        Document id of pcap file

        :return: The document_id of this SipDownloadResponse.
        :rtype: str
        """
        return self._document_id

    @document_id.setter
    def document_id(self, document_id):
        """
        Sets the document_id of this SipDownloadResponse.
        Document id of pcap file

        :param document_id: The document_id of this SipDownloadResponse.
        :type: str
        """
        
        self._document_id = document_id

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

