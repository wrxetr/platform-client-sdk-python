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


class CampaignSequence(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        CampaignSequence - a model defined in Swagger

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
            'campaigns': 'list[UriReference]',
            'current_campaign': 'int',
            'status': 'str',
            'stop_message': 'str',
            'repeat': 'bool',
            'self_uri': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'date_created': 'dateCreated',
            'date_modified': 'dateModified',
            'version': 'version',
            'campaigns': 'campaigns',
            'current_campaign': 'currentCampaign',
            'status': 'status',
            'stop_message': 'stopMessage',
            'repeat': 'repeat',
            'self_uri': 'selfUri'
        }

        self._id = None
        self._name = None
        self._date_created = None
        self._date_modified = None
        self._version = None
        self._campaigns = None
        self._current_campaign = None
        self._status = None
        self._stop_message = None
        self._repeat = None
        self._self_uri = None

    @property
    def id(self):
        """
        Gets the id of this CampaignSequence.
        The globally unique identifier for the object.

        :return: The id of this CampaignSequence.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this CampaignSequence.
        The globally unique identifier for the object.

        :param id: The id of this CampaignSequence.
        :type: str
        """
        
        self._id = id

    @property
    def name(self):
        """
        Gets the name of this CampaignSequence.


        :return: The name of this CampaignSequence.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this CampaignSequence.


        :param name: The name of this CampaignSequence.
        :type: str
        """
        
        self._name = name

    @property
    def date_created(self):
        """
        Gets the date_created of this CampaignSequence.
        Creation time of the entity. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ

        :return: The date_created of this CampaignSequence.
        :rtype: datetime
        """
        return self._date_created

    @date_created.setter
    def date_created(self, date_created):
        """
        Sets the date_created of this CampaignSequence.
        Creation time of the entity. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ

        :param date_created: The date_created of this CampaignSequence.
        :type: datetime
        """
        
        self._date_created = date_created

    @property
    def date_modified(self):
        """
        Gets the date_modified of this CampaignSequence.
        Last modified time of the entity. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ

        :return: The date_modified of this CampaignSequence.
        :rtype: datetime
        """
        return self._date_modified

    @date_modified.setter
    def date_modified(self, date_modified):
        """
        Sets the date_modified of this CampaignSequence.
        Last modified time of the entity. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ

        :param date_modified: The date_modified of this CampaignSequence.
        :type: datetime
        """
        
        self._date_modified = date_modified

    @property
    def version(self):
        """
        Gets the version of this CampaignSequence.
        Required for updates, must match the version number of the most recent update

        :return: The version of this CampaignSequence.
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """
        Sets the version of this CampaignSequence.
        Required for updates, must match the version number of the most recent update

        :param version: The version of this CampaignSequence.
        :type: int
        """
        
        self._version = version

    @property
    def campaigns(self):
        """
        Gets the campaigns of this CampaignSequence.
        The ordered list of Campaigns that this CampaignSequence will run.

        :return: The campaigns of this CampaignSequence.
        :rtype: list[UriReference]
        """
        return self._campaigns

    @campaigns.setter
    def campaigns(self, campaigns):
        """
        Sets the campaigns of this CampaignSequence.
        The ordered list of Campaigns that this CampaignSequence will run.

        :param campaigns: The campaigns of this CampaignSequence.
        :type: list[UriReference]
        """
        
        self._campaigns = campaigns

    @property
    def current_campaign(self):
        """
        Gets the current_campaign of this CampaignSequence.
        A zero-based index indicating which Campaign this CampaignSequence is currently on.

        :return: The current_campaign of this CampaignSequence.
        :rtype: int
        """
        return self._current_campaign

    @current_campaign.setter
    def current_campaign(self, current_campaign):
        """
        Sets the current_campaign of this CampaignSequence.
        A zero-based index indicating which Campaign this CampaignSequence is currently on.

        :param current_campaign: The current_campaign of this CampaignSequence.
        :type: int
        """
        
        self._current_campaign = current_campaign

    @property
    def status(self):
        """
        Gets the status of this CampaignSequence.
        The current status of the CampaignSequence. A CampaignSequence can be turned 'on' or 'off'.

        :return: The status of this CampaignSequence.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this CampaignSequence.
        The current status of the CampaignSequence. A CampaignSequence can be turned 'on' or 'off'.

        :param status: The status of this CampaignSequence.
        :type: str
        """
        allowed_values = ["on", "off", "complete"]
        if status.lower() not in map(str.lower, allowed_values):
            # print "Invalid value for status -> " + status
            self._status = "outdated_sdk_version"
        else:
            self._status = status

    @property
    def stop_message(self):
        """
        Gets the stop_message of this CampaignSequence.
        A message indicating if and why a CampaignSequence has stopped unexpectedly.

        :return: The stop_message of this CampaignSequence.
        :rtype: str
        """
        return self._stop_message

    @stop_message.setter
    def stop_message(self, stop_message):
        """
        Sets the stop_message of this CampaignSequence.
        A message indicating if and why a CampaignSequence has stopped unexpectedly.

        :param stop_message: The stop_message of this CampaignSequence.
        :type: str
        """
        
        self._stop_message = stop_message

    @property
    def repeat(self):
        """
        Gets the repeat of this CampaignSequence.
        Indicates if a sequence should repeat from the beginning after the last campaign completes. Default is false.

        :return: The repeat of this CampaignSequence.
        :rtype: bool
        """
        return self._repeat

    @repeat.setter
    def repeat(self, repeat):
        """
        Sets the repeat of this CampaignSequence.
        Indicates if a sequence should repeat from the beginning after the last campaign completes. Default is false.

        :param repeat: The repeat of this CampaignSequence.
        :type: bool
        """
        
        self._repeat = repeat

    @property
    def self_uri(self):
        """
        Gets the self_uri of this CampaignSequence.
        The URI for this object

        :return: The self_uri of this CampaignSequence.
        :rtype: str
        """
        return self._self_uri

    @self_uri.setter
    def self_uri(self, self_uri):
        """
        Sets the self_uri of this CampaignSequence.
        The URI for this object

        :param self_uri: The self_uri of this CampaignSequence.
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

