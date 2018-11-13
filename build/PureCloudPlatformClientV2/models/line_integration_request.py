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


class LineIntegrationRequest(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        LineIntegrationRequest - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'name': 'str',
            'channel_id': 'str',
            'channel_secret': 'str',
            'switcher_secret': 'str',
            'self_uri': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'channel_id': 'channelId',
            'channel_secret': 'channelSecret',
            'switcher_secret': 'switcherSecret',
            'self_uri': 'selfUri'
        }

        self._id = None
        self._name = None
        self._channel_id = None
        self._channel_secret = None
        self._switcher_secret = None
        self._self_uri = None

    @property
    def id(self):
        """
        Gets the id of this LineIntegrationRequest.
        The globally unique identifier for the object.

        :return: The id of this LineIntegrationRequest.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this LineIntegrationRequest.
        The globally unique identifier for the object.

        :param id: The id of this LineIntegrationRequest.
        :type: str
        """
        
        self._id = id

    @property
    def name(self):
        """
        Gets the name of this LineIntegrationRequest.
        The name of the LINE Integration

        :return: The name of this LineIntegrationRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this LineIntegrationRequest.
        The name of the LINE Integration

        :param name: The name of this LineIntegrationRequest.
        :type: str
        """
        
        self._name = name

    @property
    def channel_id(self):
        """
        Gets the channel_id of this LineIntegrationRequest.
        The Channel Id from LINE messenger. New Official LINE account: To create a new official account, LINE requires a Webhook URL. It can be created without specifying Channel Id & Channel Secret. Once the Official account is created by LINE, use the update LINE Integration API to update Channel Id and Channel Secret.  All other accounts: Channel Id is mandatory

        :return: The channel_id of this LineIntegrationRequest.
        :rtype: str
        """
        return self._channel_id

    @channel_id.setter
    def channel_id(self, channel_id):
        """
        Sets the channel_id of this LineIntegrationRequest.
        The Channel Id from LINE messenger. New Official LINE account: To create a new official account, LINE requires a Webhook URL. It can be created without specifying Channel Id & Channel Secret. Once the Official account is created by LINE, use the update LINE Integration API to update Channel Id and Channel Secret.  All other accounts: Channel Id is mandatory

        :param channel_id: The channel_id of this LineIntegrationRequest.
        :type: str
        """
        
        self._channel_id = channel_id

    @property
    def channel_secret(self):
        """
        Gets the channel_secret of this LineIntegrationRequest.
        The Channel Secret from LINE messenger. New Official LINE account: To create a new official account, LINE requires a Webhook URL. It can be created without specifying Channel Id & Channel Secret. Once the Official account is created by LINE, use the update LINE Integration API to update Channel Id and Channel Secret.  All other accounts: Channel Secret is mandatory

        :return: The channel_secret of this LineIntegrationRequest.
        :rtype: str
        """
        return self._channel_secret

    @channel_secret.setter
    def channel_secret(self, channel_secret):
        """
        Sets the channel_secret of this LineIntegrationRequest.
        The Channel Secret from LINE messenger. New Official LINE account: To create a new official account, LINE requires a Webhook URL. It can be created without specifying Channel Id & Channel Secret. Once the Official account is created by LINE, use the update LINE Integration API to update Channel Id and Channel Secret.  All other accounts: Channel Secret is mandatory

        :param channel_secret: The channel_secret of this LineIntegrationRequest.
        :type: str
        """
        
        self._channel_secret = channel_secret

    @property
    def switcher_secret(self):
        """
        Gets the switcher_secret of this LineIntegrationRequest.
        The Switcher Secret from LINE messenger. Some line official accounts are switcher functionality enabled. If the LINE account used for this integration is switcher enabled, then switcher secret is a required field. This secret can be found in your create documentation provided by LINE

        :return: The switcher_secret of this LineIntegrationRequest.
        :rtype: str
        """
        return self._switcher_secret

    @switcher_secret.setter
    def switcher_secret(self, switcher_secret):
        """
        Sets the switcher_secret of this LineIntegrationRequest.
        The Switcher Secret from LINE messenger. Some line official accounts are switcher functionality enabled. If the LINE account used for this integration is switcher enabled, then switcher secret is a required field. This secret can be found in your create documentation provided by LINE

        :param switcher_secret: The switcher_secret of this LineIntegrationRequest.
        :type: str
        """
        
        self._switcher_secret = switcher_secret

    @property
    def self_uri(self):
        """
        Gets the self_uri of this LineIntegrationRequest.
        The URI for this object

        :return: The self_uri of this LineIntegrationRequest.
        :rtype: str
        """
        return self._self_uri

    @self_uri.setter
    def self_uri(self, self_uri):
        """
        Sets the self_uri of this LineIntegrationRequest.
        The URI for this object

        :param self_uri: The self_uri of this LineIntegrationRequest.
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
