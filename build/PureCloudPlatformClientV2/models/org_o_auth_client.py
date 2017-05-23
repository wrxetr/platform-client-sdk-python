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


class OrgOAuthClient(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        OrgOAuthClient - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'name': 'str',
            'authorized_grant_type': 'str',
            'organization': 'Entity'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'authorized_grant_type': 'authorizedGrantType',
            'organization': 'organization'
        }

        self._id = None
        self._name = None
        self._authorized_grant_type = None
        self._organization = None

    @property
    def id(self):
        """
        Gets the id of this OrgOAuthClient.
        The globally unique identifier for the object.

        :return: The id of this OrgOAuthClient.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this OrgOAuthClient.
        The globally unique identifier for the object.

        :param id: The id of this OrgOAuthClient.
        :type: str
        """
        
        self._id = id

    @property
    def name(self):
        """
        Gets the name of this OrgOAuthClient.
        The name of the OAuth client.

        :return: The name of this OrgOAuthClient.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this OrgOAuthClient.
        The name of the OAuth client.

        :param name: The name of this OrgOAuthClient.
        :type: str
        """
        
        self._name = name

    @property
    def authorized_grant_type(self):
        """
        Gets the authorized_grant_type of this OrgOAuthClient.
        The OAuth Grant/Client type supported by this client. Code Authorization Grant/Client type - Preferred client type where the Client ID and Secret are required to create tokens. Used where the secret can be secured. Implicit grant type - Client ID only is required to create tokens. Used in browser and mobile apps where the secret can not be secured. SAML2-Bearer extension grant type - SAML2 assertion provider for user authentication at the token endpoint. Client Credential grant type - Used to created access tokens that are tied only to the client. 

        :return: The authorized_grant_type of this OrgOAuthClient.
        :rtype: str
        """
        return self._authorized_grant_type

    @authorized_grant_type.setter
    def authorized_grant_type(self, authorized_grant_type):
        """
        Sets the authorized_grant_type of this OrgOAuthClient.
        The OAuth Grant/Client type supported by this client. Code Authorization Grant/Client type - Preferred client type where the Client ID and Secret are required to create tokens. Used where the secret can be secured. Implicit grant type - Client ID only is required to create tokens. Used in browser and mobile apps where the secret can not be secured. SAML2-Bearer extension grant type - SAML2 assertion provider for user authentication at the token endpoint. Client Credential grant type - Used to created access tokens that are tied only to the client. 

        :param authorized_grant_type: The authorized_grant_type of this OrgOAuthClient.
        :type: str
        """
        allowed_values = ["CODE", "TOKEN", "SAML2BEARER", "PASSWORD", "CLIENT_CREDENTIALS"]
        if authorized_grant_type.lower() not in map(str.lower, allowed_values):
            # print "Invalid value for authorized_grant_type -> " + authorized_grant_type
            self._authorized_grant_type = "outdated_sdk_version"
        else:
            self._authorized_grant_type = authorized_grant_type

    @property
    def organization(self):
        """
        Gets the organization of this OrgOAuthClient.
        The  oauth client's organization.

        :return: The organization of this OrgOAuthClient.
        :rtype: Entity
        """
        return self._organization

    @organization.setter
    def organization(self, organization):
        """
        Sets the organization of this OrgOAuthClient.
        The  oauth client's organization.

        :param organization: The organization of this OrgOAuthClient.
        :type: Entity
        """
        
        self._organization = organization

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
