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


class Phone(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        Phone - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'name': 'str',
            'description': 'str',
            'version': 'int',
            'date_created': 'datetime',
            'date_modified': 'datetime',
            'modified_by': 'str',
            'created_by': 'str',
            'state': 'str',
            'modified_by_app': 'str',
            'created_by_app': 'str',
            'site': 'UriReference',
            'phone_base_settings': 'UriReference',
            'line_base_settings': 'UriReference',
            'phone_meta_base': 'UriReference',
            'lines': 'list[Line]',
            'status': 'PhoneStatus',
            'secondary_status': 'PhoneStatus',
            'user_agent_info': 'UserAgentInfo',
            'properties': 'dict(str, object)',
            'capabilities': 'PhoneCapabilities',
            'web_rtc_user': 'UriReference',
            'primary_edge': 'Edge',
            'secondary_edge': 'Edge',
            'self_uri': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'description': 'description',
            'version': 'version',
            'date_created': 'dateCreated',
            'date_modified': 'dateModified',
            'modified_by': 'modifiedBy',
            'created_by': 'createdBy',
            'state': 'state',
            'modified_by_app': 'modifiedByApp',
            'created_by_app': 'createdByApp',
            'site': 'site',
            'phone_base_settings': 'phoneBaseSettings',
            'line_base_settings': 'lineBaseSettings',
            'phone_meta_base': 'phoneMetaBase',
            'lines': 'lines',
            'status': 'status',
            'secondary_status': 'secondaryStatus',
            'user_agent_info': 'userAgentInfo',
            'properties': 'properties',
            'capabilities': 'capabilities',
            'web_rtc_user': 'webRtcUser',
            'primary_edge': 'primaryEdge',
            'secondary_edge': 'secondaryEdge',
            'self_uri': 'selfUri'
        }

        self._id = None
        self._name = None
        self._description = None
        self._version = None
        self._date_created = None
        self._date_modified = None
        self._modified_by = None
        self._created_by = None
        self._state = None
        self._modified_by_app = None
        self._created_by_app = None
        self._site = None
        self._phone_base_settings = None
        self._line_base_settings = None
        self._phone_meta_base = None
        self._lines = None
        self._status = None
        self._secondary_status = None
        self._user_agent_info = None
        self._properties = None
        self._capabilities = None
        self._web_rtc_user = None
        self._primary_edge = None
        self._secondary_edge = None
        self._self_uri = None

    @property
    def id(self):
        """
        Gets the id of this Phone.
        The globally unique identifier for the object.

        :return: The id of this Phone.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Phone.
        The globally unique identifier for the object.

        :param id: The id of this Phone.
        :type: str
        """
        
        self._id = id

    @property
    def name(self):
        """
        Gets the name of this Phone.
        The name of the entity.

        :return: The name of this Phone.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Phone.
        The name of the entity.

        :param name: The name of this Phone.
        :type: str
        """
        
        self._name = name

    @property
    def description(self):
        """
        Gets the description of this Phone.


        :return: The description of this Phone.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this Phone.


        :param description: The description of this Phone.
        :type: str
        """
        
        self._description = description

    @property
    def version(self):
        """
        Gets the version of this Phone.


        :return: The version of this Phone.
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """
        Sets the version of this Phone.


        :param version: The version of this Phone.
        :type: int
        """
        
        self._version = version

    @property
    def date_created(self):
        """
        Gets the date_created of this Phone.
        Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ

        :return: The date_created of this Phone.
        :rtype: datetime
        """
        return self._date_created

    @date_created.setter
    def date_created(self, date_created):
        """
        Sets the date_created of this Phone.
        Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ

        :param date_created: The date_created of this Phone.
        :type: datetime
        """
        
        self._date_created = date_created

    @property
    def date_modified(self):
        """
        Gets the date_modified of this Phone.
        Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ

        :return: The date_modified of this Phone.
        :rtype: datetime
        """
        return self._date_modified

    @date_modified.setter
    def date_modified(self, date_modified):
        """
        Sets the date_modified of this Phone.
        Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ

        :param date_modified: The date_modified of this Phone.
        :type: datetime
        """
        
        self._date_modified = date_modified

    @property
    def modified_by(self):
        """
        Gets the modified_by of this Phone.


        :return: The modified_by of this Phone.
        :rtype: str
        """
        return self._modified_by

    @modified_by.setter
    def modified_by(self, modified_by):
        """
        Sets the modified_by of this Phone.


        :param modified_by: The modified_by of this Phone.
        :type: str
        """
        
        self._modified_by = modified_by

    @property
    def created_by(self):
        """
        Gets the created_by of this Phone.


        :return: The created_by of this Phone.
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """
        Sets the created_by of this Phone.


        :param created_by: The created_by of this Phone.
        :type: str
        """
        
        self._created_by = created_by

    @property
    def state(self):
        """
        Gets the state of this Phone.


        :return: The state of this Phone.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """
        Sets the state of this Phone.


        :param state: The state of this Phone.
        :type: str
        """
        allowed_values = ["active", "inactive", "deleted"]
        if state.lower() not in map(str.lower, allowed_values):
            # print "Invalid value for state -> " + state
            self._state = "outdated_sdk_version"
        else:
            self._state = state

    @property
    def modified_by_app(self):
        """
        Gets the modified_by_app of this Phone.


        :return: The modified_by_app of this Phone.
        :rtype: str
        """
        return self._modified_by_app

    @modified_by_app.setter
    def modified_by_app(self, modified_by_app):
        """
        Sets the modified_by_app of this Phone.


        :param modified_by_app: The modified_by_app of this Phone.
        :type: str
        """
        
        self._modified_by_app = modified_by_app

    @property
    def created_by_app(self):
        """
        Gets the created_by_app of this Phone.


        :return: The created_by_app of this Phone.
        :rtype: str
        """
        return self._created_by_app

    @created_by_app.setter
    def created_by_app(self, created_by_app):
        """
        Sets the created_by_app of this Phone.


        :param created_by_app: The created_by_app of this Phone.
        :type: str
        """
        
        self._created_by_app = created_by_app

    @property
    def site(self):
        """
        Gets the site of this Phone.
        The site associated to the phone.

        :return: The site of this Phone.
        :rtype: UriReference
        """
        return self._site

    @site.setter
    def site(self, site):
        """
        Sets the site of this Phone.
        The site associated to the phone.

        :param site: The site of this Phone.
        :type: UriReference
        """
        
        self._site = site

    @property
    def phone_base_settings(self):
        """
        Gets the phone_base_settings of this Phone.
        Phone Base Settings

        :return: The phone_base_settings of this Phone.
        :rtype: UriReference
        """
        return self._phone_base_settings

    @phone_base_settings.setter
    def phone_base_settings(self, phone_base_settings):
        """
        Sets the phone_base_settings of this Phone.
        Phone Base Settings

        :param phone_base_settings: The phone_base_settings of this Phone.
        :type: UriReference
        """
        
        self._phone_base_settings = phone_base_settings

    @property
    def line_base_settings(self):
        """
        Gets the line_base_settings of this Phone.


        :return: The line_base_settings of this Phone.
        :rtype: UriReference
        """
        return self._line_base_settings

    @line_base_settings.setter
    def line_base_settings(self, line_base_settings):
        """
        Sets the line_base_settings of this Phone.


        :param line_base_settings: The line_base_settings of this Phone.
        :type: UriReference
        """
        
        self._line_base_settings = line_base_settings

    @property
    def phone_meta_base(self):
        """
        Gets the phone_meta_base of this Phone.


        :return: The phone_meta_base of this Phone.
        :rtype: UriReference
        """
        return self._phone_meta_base

    @phone_meta_base.setter
    def phone_meta_base(self, phone_meta_base):
        """
        Sets the phone_meta_base of this Phone.


        :param phone_meta_base: The phone_meta_base of this Phone.
        :type: UriReference
        """
        
        self._phone_meta_base = phone_meta_base

    @property
    def lines(self):
        """
        Gets the lines of this Phone.
        Lines

        :return: The lines of this Phone.
        :rtype: list[Line]
        """
        return self._lines

    @lines.setter
    def lines(self, lines):
        """
        Sets the lines of this Phone.
        Lines

        :param lines: The lines of this Phone.
        :type: list[Line]
        """
        
        self._lines = lines

    @property
    def status(self):
        """
        Gets the status of this Phone.
        The status of the phone and lines from the primary Edge.

        :return: The status of this Phone.
        :rtype: PhoneStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this Phone.
        The status of the phone and lines from the primary Edge.

        :param status: The status of this Phone.
        :type: PhoneStatus
        """
        
        self._status = status

    @property
    def secondary_status(self):
        """
        Gets the secondary_status of this Phone.
        The status of the phone and lines from the secondary Edge.

        :return: The secondary_status of this Phone.
        :rtype: PhoneStatus
        """
        return self._secondary_status

    @secondary_status.setter
    def secondary_status(self, secondary_status):
        """
        Sets the secondary_status of this Phone.
        The status of the phone and lines from the secondary Edge.

        :param secondary_status: The secondary_status of this Phone.
        :type: PhoneStatus
        """
        
        self._secondary_status = secondary_status

    @property
    def user_agent_info(self):
        """
        Gets the user_agent_info of this Phone.
        User Agent Information for this phone. This includes model, firmware version, and manufacturer.

        :return: The user_agent_info of this Phone.
        :rtype: UserAgentInfo
        """
        return self._user_agent_info

    @user_agent_info.setter
    def user_agent_info(self, user_agent_info):
        """
        Sets the user_agent_info of this Phone.
        User Agent Information for this phone. This includes model, firmware version, and manufacturer.

        :param user_agent_info: The user_agent_info of this Phone.
        :type: UserAgentInfo
        """
        
        self._user_agent_info = user_agent_info

    @property
    def properties(self):
        """
        Gets the properties of this Phone.


        :return: The properties of this Phone.
        :rtype: dict(str, object)
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """
        Sets the properties of this Phone.


        :param properties: The properties of this Phone.
        :type: dict(str, object)
        """
        
        self._properties = properties

    @property
    def capabilities(self):
        """
        Gets the capabilities of this Phone.


        :return: The capabilities of this Phone.
        :rtype: PhoneCapabilities
        """
        return self._capabilities

    @capabilities.setter
    def capabilities(self, capabilities):
        """
        Sets the capabilities of this Phone.


        :param capabilities: The capabilities of this Phone.
        :type: PhoneCapabilities
        """
        
        self._capabilities = capabilities

    @property
    def web_rtc_user(self):
        """
        Gets the web_rtc_user of this Phone.
        This is the user associated with a WebRTC type phone.  It is required for all WebRTC phones.

        :return: The web_rtc_user of this Phone.
        :rtype: UriReference
        """
        return self._web_rtc_user

    @web_rtc_user.setter
    def web_rtc_user(self, web_rtc_user):
        """
        Sets the web_rtc_user of this Phone.
        This is the user associated with a WebRTC type phone.  It is required for all WebRTC phones.

        :param web_rtc_user: The web_rtc_user of this Phone.
        :type: UriReference
        """
        
        self._web_rtc_user = web_rtc_user

    @property
    def primary_edge(self):
        """
        Gets the primary_edge of this Phone.


        :return: The primary_edge of this Phone.
        :rtype: Edge
        """
        return self._primary_edge

    @primary_edge.setter
    def primary_edge(self, primary_edge):
        """
        Sets the primary_edge of this Phone.


        :param primary_edge: The primary_edge of this Phone.
        :type: Edge
        """
        
        self._primary_edge = primary_edge

    @property
    def secondary_edge(self):
        """
        Gets the secondary_edge of this Phone.


        :return: The secondary_edge of this Phone.
        :rtype: Edge
        """
        return self._secondary_edge

    @secondary_edge.setter
    def secondary_edge(self, secondary_edge):
        """
        Sets the secondary_edge of this Phone.


        :param secondary_edge: The secondary_edge of this Phone.
        :type: Edge
        """
        
        self._secondary_edge = secondary_edge

    @property
    def self_uri(self):
        """
        Gets the self_uri of this Phone.
        The URI for this object

        :return: The self_uri of this Phone.
        :rtype: str
        """
        return self._self_uri

    @self_uri.setter
    def self_uri(self, self_uri):
        """
        Sets the self_uri of this Phone.
        The URI for this object

        :param self_uri: The self_uri of this Phone.
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

