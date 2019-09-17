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

class WidgetDeployment(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        WidgetDeployment - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'name': 'str',
            'description': 'str',
            'authentication_required': 'bool',
            'disabled': 'bool',
            'flow': 'DomainEntityRef',
            'allowed_domains': 'list[str]',
            'client_type': 'str',
            'client_config': 'WidgetClientConfig',
            'self_uri': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'description': 'description',
            'authentication_required': 'authenticationRequired',
            'disabled': 'disabled',
            'flow': 'flow',
            'allowed_domains': 'allowedDomains',
            'client_type': 'clientType',
            'client_config': 'clientConfig',
            'self_uri': 'selfUri'
        }

        self._id = None
        self._name = None
        self._description = None
        self._authentication_required = None
        self._disabled = None
        self._flow = None
        self._allowed_domains = None
        self._client_type = None
        self._client_config = None
        self._self_uri = None

    @property
    def id(self):
        """
        Gets the id of this WidgetDeployment.
        The globally unique identifier for the object.

        :return: The id of this WidgetDeployment.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this WidgetDeployment.
        The globally unique identifier for the object.

        :param id: The id of this WidgetDeployment.
        :type: str
        """
        
        self._id = id

    @property
    def name(self):
        """
        Gets the name of this WidgetDeployment.


        :return: The name of this WidgetDeployment.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this WidgetDeployment.


        :param name: The name of this WidgetDeployment.
        :type: str
        """
        
        self._name = name

    @property
    def description(self):
        """
        Gets the description of this WidgetDeployment.
        A human-readable description of this Deployment.

        :return: The description of this WidgetDeployment.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this WidgetDeployment.
        A human-readable description of this Deployment.

        :param description: The description of this WidgetDeployment.
        :type: str
        """
        
        self._description = description

    @property
    def authentication_required(self):
        """
        Gets the authentication_required of this WidgetDeployment.
        When true, the customer members starting a chat must be authenticated by supplying their JWT to the create operation.

        :return: The authentication_required of this WidgetDeployment.
        :rtype: bool
        """
        return self._authentication_required

    @authentication_required.setter
    def authentication_required(self, authentication_required):
        """
        Sets the authentication_required of this WidgetDeployment.
        When true, the customer members starting a chat must be authenticated by supplying their JWT to the create operation.

        :param authentication_required: The authentication_required of this WidgetDeployment.
        :type: bool
        """
        
        self._authentication_required = authentication_required

    @property
    def disabled(self):
        """
        Gets the disabled of this WidgetDeployment.
        When true, all create chat operations using this Deployment will be rejected.

        :return: The disabled of this WidgetDeployment.
        :rtype: bool
        """
        return self._disabled

    @disabled.setter
    def disabled(self, disabled):
        """
        Sets the disabled of this WidgetDeployment.
        When true, all create chat operations using this Deployment will be rejected.

        :param disabled: The disabled of this WidgetDeployment.
        :type: bool
        """
        
        self._disabled = disabled

    @property
    def flow(self):
        """
        Gets the flow of this WidgetDeployment.
        The URI of the Inbound Chat Flow to run when new chats are initiated under this Deployment.

        :return: The flow of this WidgetDeployment.
        :rtype: DomainEntityRef
        """
        return self._flow

    @flow.setter
    def flow(self, flow):
        """
        Sets the flow of this WidgetDeployment.
        The URI of the Inbound Chat Flow to run when new chats are initiated under this Deployment.

        :param flow: The flow of this WidgetDeployment.
        :type: DomainEntityRef
        """
        
        self._flow = flow

    @property
    def allowed_domains(self):
        """
        Gets the allowed_domains of this WidgetDeployment.
        The list of domains that are approved to use this Deployment; the list will be added to CORS headers for ease of web use.

        :return: The allowed_domains of this WidgetDeployment.
        :rtype: list[str]
        """
        return self._allowed_domains

    @allowed_domains.setter
    def allowed_domains(self, allowed_domains):
        """
        Sets the allowed_domains of this WidgetDeployment.
        The list of domains that are approved to use this Deployment; the list will be added to CORS headers for ease of web use.

        :param allowed_domains: The allowed_domains of this WidgetDeployment.
        :type: list[str]
        """
        
        self._allowed_domains = allowed_domains

    @property
    def client_type(self):
        """
        Gets the client_type of this WidgetDeployment.
        The type of display widget for which this Deployment is configured, which controls the administrator settings shown.

        :return: The client_type of this WidgetDeployment.
        :rtype: str
        """
        return self._client_type

    @client_type.setter
    def client_type(self, client_type):
        """
        Sets the client_type of this WidgetDeployment.
        The type of display widget for which this Deployment is configured, which controls the administrator settings shown.

        :param client_type: The client_type of this WidgetDeployment.
        :type: str
        """
        allowed_values = ["v1", "v2", "v1-http", "third-party"]
        if client_type.lower() not in map(str.lower, allowed_values):
            # print "Invalid value for client_type -> " + client_type
            self._client_type = "outdated_sdk_version"
        else:
            self._client_type = client_type

    @property
    def client_config(self):
        """
        Gets the client_config of this WidgetDeployment.
        The client configuration options that should be made available to the clients of this Deployment.

        :return: The client_config of this WidgetDeployment.
        :rtype: WidgetClientConfig
        """
        return self._client_config

    @client_config.setter
    def client_config(self, client_config):
        """
        Sets the client_config of this WidgetDeployment.
        The client configuration options that should be made available to the clients of this Deployment.

        :param client_config: The client_config of this WidgetDeployment.
        :type: WidgetClientConfig
        """
        
        self._client_config = client_config

    @property
    def self_uri(self):
        """
        Gets the self_uri of this WidgetDeployment.
        The URI for this object

        :return: The self_uri of this WidgetDeployment.
        :rtype: str
        """
        return self._self_uri

    @self_uri.setter
    def self_uri(self, self_uri):
        """
        Sets the self_uri of this WidgetDeployment.
        The URI for this object

        :param self_uri: The self_uri of this WidgetDeployment.
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

