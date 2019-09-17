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

class ScimV2User(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        ScimV2User - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'schemas': 'list[str]',
            'active': 'bool',
            'user_name': 'str',
            'display_name': 'str',
            'password': 'str',
            'title': 'str',
            'phone_numbers': 'list[ScimPhoneNumber]',
            'emails': 'list[ScimEmail]',
            'photos': 'list[Photo]',
            'external_id': 'str',
            'groups': 'list[ScimV2GroupReference]',
            'roles': 'list[str]',
            'urnietfparamsscimschemasextensionenterprise2_0_user': 'ScimV2EnterpriseUser',
            'meta': 'ScimMetadata'
        }

        self.attribute_map = {
            'id': 'id',
            'schemas': 'schemas',
            'active': 'active',
            'user_name': 'userName',
            'display_name': 'displayName',
            'password': 'password',
            'title': 'title',
            'phone_numbers': 'phoneNumbers',
            'emails': 'emails',
            'photos': 'photos',
            'external_id': 'externalId',
            'groups': 'groups',
            'roles': 'roles',
            'urnietfparamsscimschemasextensionenterprise2_0_user': 'urn:ietf:params:scim:schemas:extension:enterprise:2.0:User',
            'meta': 'meta'
        }

        self._id = None
        self._schemas = None
        self._active = None
        self._user_name = None
        self._display_name = None
        self._password = None
        self._title = None
        self._phone_numbers = None
        self._emails = None
        self._photos = None
        self._external_id = None
        self._groups = None
        self._roles = None
        self._urnietfparamsscimschemasextensionenterprise2_0_user = None
        self._meta = None

    @property
    def id(self):
        """
        Gets the id of this ScimV2User.
        The ID of the SCIM resource. Set by the service provider. caseExact is set to true. Mutability is set to readOnly. Returned is set to always.

        :return: The id of this ScimV2User.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ScimV2User.
        The ID of the SCIM resource. Set by the service provider. caseExact is set to true. Mutability is set to readOnly. Returned is set to always.

        :param id: The id of this ScimV2User.
        :type: str
        """
        
        self._id = id

    @property
    def schemas(self):
        """
        Gets the schemas of this ScimV2User.
        The list of supported schemas.

        :return: The schemas of this ScimV2User.
        :rtype: list[str]
        """
        return self._schemas

    @schemas.setter
    def schemas(self, schemas):
        """
        Sets the schemas of this ScimV2User.
        The list of supported schemas.

        :param schemas: The schemas of this ScimV2User.
        :type: list[str]
        """
        
        self._schemas = schemas

    @property
    def active(self):
        """
        Gets the active of this ScimV2User.
        Indicates whether the user's administrative status is active.

        :return: The active of this ScimV2User.
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """
        Sets the active of this ScimV2User.
        Indicates whether the user's administrative status is active.

        :param active: The active of this ScimV2User.
        :type: bool
        """
        
        self._active = active

    @property
    def user_name(self):
        """
        Gets the user_name of this ScimV2User.
        The user's PureCloud email address. Must be unique.

        :return: The user_name of this ScimV2User.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """
        Sets the user_name of this ScimV2User.
        The user's PureCloud email address. Must be unique.

        :param user_name: The user_name of this ScimV2User.
        :type: str
        """
        
        self._user_name = user_name

    @property
    def display_name(self):
        """
        Gets the display_name of this ScimV2User.
        The display name for the user.

        :return: The display_name of this ScimV2User.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this ScimV2User.
        The display name for the user.

        :param display_name: The display_name of this ScimV2User.
        :type: str
        """
        
        self._display_name = display_name

    @property
    def password(self):
        """
        Gets the password of this ScimV2User.
        A new password for a PureCloud user. Does not return an existing password.

        :return: The password of this ScimV2User.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """
        Sets the password of this ScimV2User.
        A new password for a PureCloud user. Does not return an existing password.

        :param password: The password of this ScimV2User.
        :type: str
        """
        
        self._password = password

    @property
    def title(self):
        """
        Gets the title of this ScimV2User.
        The user's title.

        :return: The title of this ScimV2User.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """
        Sets the title of this ScimV2User.
        The user's title.

        :param title: The title of this ScimV2User.
        :type: str
        """
        
        self._title = title

    @property
    def phone_numbers(self):
        """
        Gets the phone_numbers of this ScimV2User.
        A list of the user's phone numbers.

        :return: The phone_numbers of this ScimV2User.
        :rtype: list[ScimPhoneNumber]
        """
        return self._phone_numbers

    @phone_numbers.setter
    def phone_numbers(self, phone_numbers):
        """
        Sets the phone_numbers of this ScimV2User.
        A list of the user's phone numbers.

        :param phone_numbers: The phone_numbers of this ScimV2User.
        :type: list[ScimPhoneNumber]
        """
        
        self._phone_numbers = phone_numbers

    @property
    def emails(self):
        """
        Gets the emails of this ScimV2User.
        A list of the user's email addresses.

        :return: The emails of this ScimV2User.
        :rtype: list[ScimEmail]
        """
        return self._emails

    @emails.setter
    def emails(self, emails):
        """
        Sets the emails of this ScimV2User.
        A list of the user's email addresses.

        :param emails: The emails of this ScimV2User.
        :type: list[ScimEmail]
        """
        
        self._emails = emails

    @property
    def photos(self):
        """
        Gets the photos of this ScimV2User.
        A list of the user's photos.

        :return: The photos of this ScimV2User.
        :rtype: list[Photo]
        """
        return self._photos

    @photos.setter
    def photos(self, photos):
        """
        Sets the photos of this ScimV2User.
        A list of the user's photos.

        :param photos: The photos of this ScimV2User.
        :type: list[Photo]
        """
        
        self._photos = photos

    @property
    def external_id(self):
        """
        Gets the external_id of this ScimV2User.
        The external ID of the user. Set by the provisioning client. caseExact is set to true. mutability is set to readWrite.

        :return: The external_id of this ScimV2User.
        :rtype: str
        """
        return self._external_id

    @external_id.setter
    def external_id(self, external_id):
        """
        Sets the external_id of this ScimV2User.
        The external ID of the user. Set by the provisioning client. caseExact is set to true. mutability is set to readWrite.

        :param external_id: The external_id of this ScimV2User.
        :type: str
        """
        
        self._external_id = external_id

    @property
    def groups(self):
        """
        Gets the groups of this ScimV2User.
        A list of groups that the user is a member of.

        :return: The groups of this ScimV2User.
        :rtype: list[ScimV2GroupReference]
        """
        return self._groups

    @groups.setter
    def groups(self, groups):
        """
        Sets the groups of this ScimV2User.
        A list of groups that the user is a member of.

        :param groups: The groups of this ScimV2User.
        :type: list[ScimV2GroupReference]
        """
        
        self._groups = groups

    @property
    def roles(self):
        """
        Gets the roles of this ScimV2User.
        A list of roles assigned to the user.

        :return: The roles of this ScimV2User.
        :rtype: list[str]
        """
        return self._roles

    @roles.setter
    def roles(self, roles):
        """
        Sets the roles of this ScimV2User.
        A list of roles assigned to the user.

        :param roles: The roles of this ScimV2User.
        :type: list[str]
        """
        
        self._roles = roles

    @property
    def urnietfparamsscimschemasextensionenterprise2_0_user(self):
        """
        Gets the urnietfparamsscimschemasextensionenterprise2_0_user of this ScimV2User.


        :return: The urnietfparamsscimschemasextensionenterprise2_0_user of this ScimV2User.
        :rtype: ScimV2EnterpriseUser
        """
        return self._urnietfparamsscimschemasextensionenterprise2_0_user

    @urnietfparamsscimschemasextensionenterprise2_0_user.setter
    def urnietfparamsscimschemasextensionenterprise2_0_user(self, urnietfparamsscimschemasextensionenterprise2_0_user):
        """
        Sets the urnietfparamsscimschemasextensionenterprise2_0_user of this ScimV2User.


        :param urnietfparamsscimschemasextensionenterprise2_0_user: The urnietfparamsscimschemasextensionenterprise2_0_user of this ScimV2User.
        :type: ScimV2EnterpriseUser
        """
        
        self._urnietfparamsscimschemasextensionenterprise2_0_user = urnietfparamsscimschemasextensionenterprise2_0_user

    @property
    def meta(self):
        """
        Gets the meta of this ScimV2User.
        Resource SCIM meta

        :return: The meta of this ScimV2User.
        :rtype: ScimMetadata
        """
        return self._meta

    @meta.setter
    def meta(self, meta):
        """
        Sets the meta of this ScimV2User.
        Resource SCIM meta

        :param meta: The meta of this ScimV2User.
        :type: ScimMetadata
        """
        
        self._meta = meta

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

