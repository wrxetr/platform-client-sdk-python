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


class DomainLogicalInterface(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        DomainLogicalInterface - a model defined in Swagger

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
            'edge_uri': 'str',
            'edge_assigned_id': 'str',
            'friendly_name': 'str',
            'vlan_tag_id': 'int',
            'hardware_address': 'str',
            'physical_adapter_id': 'str',
            'if_status': 'str',
            'interface_type': 'str',
            'routes': 'list[DomainNetworkRoute]',
            'addresses': 'list[DomainNetworkAddress]',
            'ipv4_capabilities': 'DomainCapabilities',
            'ipv6_capabilities': 'DomainCapabilities',
            'current_state': 'str',
            'last_modified_user_id': 'str',
            'last_modified_correlation_id': 'str',
            'command_responses': 'list[DomainNetworkCommandResponse]',
            'inherit_phone_trunk_bases_i_pv4': 'bool',
            'inherit_phone_trunk_bases_i_pv6': 'bool',
            'use_for_internal_edge_communication': 'bool',
            'external_trunk_base_assignments': 'list[TrunkBaseAssignment]',
            'phone_trunk_base_assignments': 'list[TrunkBaseAssignment]',
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
            'edge_uri': 'edgeUri',
            'edge_assigned_id': 'edgeAssignedId',
            'friendly_name': 'friendlyName',
            'vlan_tag_id': 'vlanTagId',
            'hardware_address': 'hardwareAddress',
            'physical_adapter_id': 'physicalAdapterId',
            'if_status': 'ifStatus',
            'interface_type': 'interfaceType',
            'routes': 'routes',
            'addresses': 'addresses',
            'ipv4_capabilities': 'ipv4Capabilities',
            'ipv6_capabilities': 'ipv6Capabilities',
            'current_state': 'currentState',
            'last_modified_user_id': 'lastModifiedUserId',
            'last_modified_correlation_id': 'lastModifiedCorrelationId',
            'command_responses': 'commandResponses',
            'inherit_phone_trunk_bases_i_pv4': 'inheritPhoneTrunkBasesIPv4',
            'inherit_phone_trunk_bases_i_pv6': 'inheritPhoneTrunkBasesIPv6',
            'use_for_internal_edge_communication': 'useForInternalEdgeCommunication',
            'external_trunk_base_assignments': 'externalTrunkBaseAssignments',
            'phone_trunk_base_assignments': 'phoneTrunkBaseAssignments',
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
        self._edge_uri = None
        self._edge_assigned_id = None
        self._friendly_name = None
        self._vlan_tag_id = None
        self._hardware_address = None
        self._physical_adapter_id = None
        self._if_status = None
        self._interface_type = None
        self._routes = None
        self._addresses = None
        self._ipv4_capabilities = None
        self._ipv6_capabilities = None
        self._current_state = None
        self._last_modified_user_id = None
        self._last_modified_correlation_id = None
        self._command_responses = None
        self._inherit_phone_trunk_bases_i_pv4 = None
        self._inherit_phone_trunk_bases_i_pv6 = None
        self._use_for_internal_edge_communication = None
        self._external_trunk_base_assignments = None
        self._phone_trunk_base_assignments = None
        self._self_uri = None

    @property
    def id(self):
        """
        Gets the id of this DomainLogicalInterface.
        The globally unique identifier for the object.

        :return: The id of this DomainLogicalInterface.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this DomainLogicalInterface.
        The globally unique identifier for the object.

        :param id: The id of this DomainLogicalInterface.
        :type: str
        """
        
        self._id = id

    @property
    def name(self):
        """
        Gets the name of this DomainLogicalInterface.
        The name of the entity.

        :return: The name of this DomainLogicalInterface.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this DomainLogicalInterface.
        The name of the entity.

        :param name: The name of this DomainLogicalInterface.
        :type: str
        """
        
        self._name = name

    @property
    def description(self):
        """
        Gets the description of this DomainLogicalInterface.


        :return: The description of this DomainLogicalInterface.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this DomainLogicalInterface.


        :param description: The description of this DomainLogicalInterface.
        :type: str
        """
        
        self._description = description

    @property
    def version(self):
        """
        Gets the version of this DomainLogicalInterface.


        :return: The version of this DomainLogicalInterface.
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """
        Sets the version of this DomainLogicalInterface.


        :param version: The version of this DomainLogicalInterface.
        :type: int
        """
        
        self._version = version

    @property
    def date_created(self):
        """
        Gets the date_created of this DomainLogicalInterface.
        Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ

        :return: The date_created of this DomainLogicalInterface.
        :rtype: datetime
        """
        return self._date_created

    @date_created.setter
    def date_created(self, date_created):
        """
        Sets the date_created of this DomainLogicalInterface.
        Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ

        :param date_created: The date_created of this DomainLogicalInterface.
        :type: datetime
        """
        
        self._date_created = date_created

    @property
    def date_modified(self):
        """
        Gets the date_modified of this DomainLogicalInterface.
        Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ

        :return: The date_modified of this DomainLogicalInterface.
        :rtype: datetime
        """
        return self._date_modified

    @date_modified.setter
    def date_modified(self, date_modified):
        """
        Sets the date_modified of this DomainLogicalInterface.
        Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ

        :param date_modified: The date_modified of this DomainLogicalInterface.
        :type: datetime
        """
        
        self._date_modified = date_modified

    @property
    def modified_by(self):
        """
        Gets the modified_by of this DomainLogicalInterface.


        :return: The modified_by of this DomainLogicalInterface.
        :rtype: str
        """
        return self._modified_by

    @modified_by.setter
    def modified_by(self, modified_by):
        """
        Sets the modified_by of this DomainLogicalInterface.


        :param modified_by: The modified_by of this DomainLogicalInterface.
        :type: str
        """
        
        self._modified_by = modified_by

    @property
    def created_by(self):
        """
        Gets the created_by of this DomainLogicalInterface.


        :return: The created_by of this DomainLogicalInterface.
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """
        Sets the created_by of this DomainLogicalInterface.


        :param created_by: The created_by of this DomainLogicalInterface.
        :type: str
        """
        
        self._created_by = created_by

    @property
    def state(self):
        """
        Gets the state of this DomainLogicalInterface.


        :return: The state of this DomainLogicalInterface.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """
        Sets the state of this DomainLogicalInterface.


        :param state: The state of this DomainLogicalInterface.
        :type: str
        """
        allowed_values = ["active", "inactive", "deleted"]
        if state.lower() not in map(str.lower, allowed_values):
            # print "Invalid value for state -> " + state
            self._state = "outdated_sdk_version"
        else:
            self._state = state.lower()

    @property
    def modified_by_app(self):
        """
        Gets the modified_by_app of this DomainLogicalInterface.


        :return: The modified_by_app of this DomainLogicalInterface.
        :rtype: str
        """
        return self._modified_by_app

    @modified_by_app.setter
    def modified_by_app(self, modified_by_app):
        """
        Sets the modified_by_app of this DomainLogicalInterface.


        :param modified_by_app: The modified_by_app of this DomainLogicalInterface.
        :type: str
        """
        
        self._modified_by_app = modified_by_app

    @property
    def created_by_app(self):
        """
        Gets the created_by_app of this DomainLogicalInterface.


        :return: The created_by_app of this DomainLogicalInterface.
        :rtype: str
        """
        return self._created_by_app

    @created_by_app.setter
    def created_by_app(self, created_by_app):
        """
        Sets the created_by_app of this DomainLogicalInterface.


        :param created_by_app: The created_by_app of this DomainLogicalInterface.
        :type: str
        """
        
        self._created_by_app = created_by_app

    @property
    def edge_uri(self):
        """
        Gets the edge_uri of this DomainLogicalInterface.


        :return: The edge_uri of this DomainLogicalInterface.
        :rtype: str
        """
        return self._edge_uri

    @edge_uri.setter
    def edge_uri(self, edge_uri):
        """
        Sets the edge_uri of this DomainLogicalInterface.


        :param edge_uri: The edge_uri of this DomainLogicalInterface.
        :type: str
        """
        
        self._edge_uri = edge_uri

    @property
    def edge_assigned_id(self):
        """
        Gets the edge_assigned_id of this DomainLogicalInterface.


        :return: The edge_assigned_id of this DomainLogicalInterface.
        :rtype: str
        """
        return self._edge_assigned_id

    @edge_assigned_id.setter
    def edge_assigned_id(self, edge_assigned_id):
        """
        Sets the edge_assigned_id of this DomainLogicalInterface.


        :param edge_assigned_id: The edge_assigned_id of this DomainLogicalInterface.
        :type: str
        """
        
        self._edge_assigned_id = edge_assigned_id

    @property
    def friendly_name(self):
        """
        Gets the friendly_name of this DomainLogicalInterface.
        Friendly Name

        :return: The friendly_name of this DomainLogicalInterface.
        :rtype: str
        """
        return self._friendly_name

    @friendly_name.setter
    def friendly_name(self, friendly_name):
        """
        Sets the friendly_name of this DomainLogicalInterface.
        Friendly Name

        :param friendly_name: The friendly_name of this DomainLogicalInterface.
        :type: str
        """
        
        self._friendly_name = friendly_name

    @property
    def vlan_tag_id(self):
        """
        Gets the vlan_tag_id of this DomainLogicalInterface.


        :return: The vlan_tag_id of this DomainLogicalInterface.
        :rtype: int
        """
        return self._vlan_tag_id

    @vlan_tag_id.setter
    def vlan_tag_id(self, vlan_tag_id):
        """
        Sets the vlan_tag_id of this DomainLogicalInterface.


        :param vlan_tag_id: The vlan_tag_id of this DomainLogicalInterface.
        :type: int
        """
        
        self._vlan_tag_id = vlan_tag_id

    @property
    def hardware_address(self):
        """
        Gets the hardware_address of this DomainLogicalInterface.
        Hardware Address

        :return: The hardware_address of this DomainLogicalInterface.
        :rtype: str
        """
        return self._hardware_address

    @hardware_address.setter
    def hardware_address(self, hardware_address):
        """
        Sets the hardware_address of this DomainLogicalInterface.
        Hardware Address

        :param hardware_address: The hardware_address of this DomainLogicalInterface.
        :type: str
        """
        
        self._hardware_address = hardware_address

    @property
    def physical_adapter_id(self):
        """
        Gets the physical_adapter_id of this DomainLogicalInterface.
        Physical Adapter Id

        :return: The physical_adapter_id of this DomainLogicalInterface.
        :rtype: str
        """
        return self._physical_adapter_id

    @physical_adapter_id.setter
    def physical_adapter_id(self, physical_adapter_id):
        """
        Sets the physical_adapter_id of this DomainLogicalInterface.
        Physical Adapter Id

        :param physical_adapter_id: The physical_adapter_id of this DomainLogicalInterface.
        :type: str
        """
        
        self._physical_adapter_id = physical_adapter_id

    @property
    def if_status(self):
        """
        Gets the if_status of this DomainLogicalInterface.


        :return: The if_status of this DomainLogicalInterface.
        :rtype: str
        """
        return self._if_status

    @if_status.setter
    def if_status(self, if_status):
        """
        Sets the if_status of this DomainLogicalInterface.


        :param if_status: The if_status of this DomainLogicalInterface.
        :type: str
        """
        
        self._if_status = if_status

    @property
    def interface_type(self):
        """
        Gets the interface_type of this DomainLogicalInterface.
        The type of this network interface.

        :return: The interface_type of this DomainLogicalInterface.
        :rtype: str
        """
        return self._interface_type

    @interface_type.setter
    def interface_type(self, interface_type):
        """
        Sets the interface_type of this DomainLogicalInterface.
        The type of this network interface.

        :param interface_type: The interface_type of this DomainLogicalInterface.
        :type: str
        """
        allowed_values = ["DIAGNOSTIC", "SYSTEM"]
        if interface_type.lower() not in map(str.lower, allowed_values):
            # print "Invalid value for interface_type -> " + interface_type
            self._interface_type = "outdated_sdk_version"
        else:
            self._interface_type = interface_type.lower()

    @property
    def routes(self):
        """
        Gets the routes of this DomainLogicalInterface.
        The list of routes assigned to this interface.

        :return: The routes of this DomainLogicalInterface.
        :rtype: list[DomainNetworkRoute]
        """
        return self._routes

    @routes.setter
    def routes(self, routes):
        """
        Sets the routes of this DomainLogicalInterface.
        The list of routes assigned to this interface.

        :param routes: The routes of this DomainLogicalInterface.
        :type: list[DomainNetworkRoute]
        """
        
        self._routes = routes

    @property
    def addresses(self):
        """
        Gets the addresses of this DomainLogicalInterface.
        The list of IP addresses on this interface.  Priority of dns addresses are based on order in the list.

        :return: The addresses of this DomainLogicalInterface.
        :rtype: list[DomainNetworkAddress]
        """
        return self._addresses

    @addresses.setter
    def addresses(self, addresses):
        """
        Sets the addresses of this DomainLogicalInterface.
        The list of IP addresses on this interface.  Priority of dns addresses are based on order in the list.

        :param addresses: The addresses of this DomainLogicalInterface.
        :type: list[DomainNetworkAddress]
        """
        
        self._addresses = addresses

    @property
    def ipv4_capabilities(self):
        """
        Gets the ipv4_capabilities of this DomainLogicalInterface.
        IPv4 interface settings.

        :return: The ipv4_capabilities of this DomainLogicalInterface.
        :rtype: DomainCapabilities
        """
        return self._ipv4_capabilities

    @ipv4_capabilities.setter
    def ipv4_capabilities(self, ipv4_capabilities):
        """
        Sets the ipv4_capabilities of this DomainLogicalInterface.
        IPv4 interface settings.

        :param ipv4_capabilities: The ipv4_capabilities of this DomainLogicalInterface.
        :type: DomainCapabilities
        """
        
        self._ipv4_capabilities = ipv4_capabilities

    @property
    def ipv6_capabilities(self):
        """
        Gets the ipv6_capabilities of this DomainLogicalInterface.
        IPv6 interface settings.

        :return: The ipv6_capabilities of this DomainLogicalInterface.
        :rtype: DomainCapabilities
        """
        return self._ipv6_capabilities

    @ipv6_capabilities.setter
    def ipv6_capabilities(self, ipv6_capabilities):
        """
        Sets the ipv6_capabilities of this DomainLogicalInterface.
        IPv6 interface settings.

        :param ipv6_capabilities: The ipv6_capabilities of this DomainLogicalInterface.
        :type: DomainCapabilities
        """
        
        self._ipv6_capabilities = ipv6_capabilities

    @property
    def current_state(self):
        """
        Gets the current_state of this DomainLogicalInterface.


        :return: The current_state of this DomainLogicalInterface.
        :rtype: str
        """
        return self._current_state

    @current_state.setter
    def current_state(self, current_state):
        """
        Sets the current_state of this DomainLogicalInterface.


        :param current_state: The current_state of this DomainLogicalInterface.
        :type: str
        """
        allowed_values = ["INIT", "CREATING", "UPDATING", "OK", "EXCEPTION", "DELETING"]
        if current_state.lower() not in map(str.lower, allowed_values):
            # print "Invalid value for current_state -> " + current_state
            self._current_state = "outdated_sdk_version"
        else:
            self._current_state = current_state.lower()

    @property
    def last_modified_user_id(self):
        """
        Gets the last_modified_user_id of this DomainLogicalInterface.


        :return: The last_modified_user_id of this DomainLogicalInterface.
        :rtype: str
        """
        return self._last_modified_user_id

    @last_modified_user_id.setter
    def last_modified_user_id(self, last_modified_user_id):
        """
        Sets the last_modified_user_id of this DomainLogicalInterface.


        :param last_modified_user_id: The last_modified_user_id of this DomainLogicalInterface.
        :type: str
        """
        
        self._last_modified_user_id = last_modified_user_id

    @property
    def last_modified_correlation_id(self):
        """
        Gets the last_modified_correlation_id of this DomainLogicalInterface.


        :return: The last_modified_correlation_id of this DomainLogicalInterface.
        :rtype: str
        """
        return self._last_modified_correlation_id

    @last_modified_correlation_id.setter
    def last_modified_correlation_id(self, last_modified_correlation_id):
        """
        Sets the last_modified_correlation_id of this DomainLogicalInterface.


        :param last_modified_correlation_id: The last_modified_correlation_id of this DomainLogicalInterface.
        :type: str
        """
        
        self._last_modified_correlation_id = last_modified_correlation_id

    @property
    def command_responses(self):
        """
        Gets the command_responses of this DomainLogicalInterface.


        :return: The command_responses of this DomainLogicalInterface.
        :rtype: list[DomainNetworkCommandResponse]
        """
        return self._command_responses

    @command_responses.setter
    def command_responses(self, command_responses):
        """
        Sets the command_responses of this DomainLogicalInterface.


        :param command_responses: The command_responses of this DomainLogicalInterface.
        :type: list[DomainNetworkCommandResponse]
        """
        
        self._command_responses = command_responses

    @property
    def inherit_phone_trunk_bases_i_pv4(self):
        """
        Gets the inherit_phone_trunk_bases_i_pv4 of this DomainLogicalInterface.
        The IPv4 phone trunk base assignment will be inherited from the Edge Group.

        :return: The inherit_phone_trunk_bases_i_pv4 of this DomainLogicalInterface.
        :rtype: bool
        """
        return self._inherit_phone_trunk_bases_i_pv4

    @inherit_phone_trunk_bases_i_pv4.setter
    def inherit_phone_trunk_bases_i_pv4(self, inherit_phone_trunk_bases_i_pv4):
        """
        Sets the inherit_phone_trunk_bases_i_pv4 of this DomainLogicalInterface.
        The IPv4 phone trunk base assignment will be inherited from the Edge Group.

        :param inherit_phone_trunk_bases_i_pv4: The inherit_phone_trunk_bases_i_pv4 of this DomainLogicalInterface.
        :type: bool
        """
        
        self._inherit_phone_trunk_bases_i_pv4 = inherit_phone_trunk_bases_i_pv4

    @property
    def inherit_phone_trunk_bases_i_pv6(self):
        """
        Gets the inherit_phone_trunk_bases_i_pv6 of this DomainLogicalInterface.
        The IPv6 phone trunk base assignment will be inherited from the Edge Group.

        :return: The inherit_phone_trunk_bases_i_pv6 of this DomainLogicalInterface.
        :rtype: bool
        """
        return self._inherit_phone_trunk_bases_i_pv6

    @inherit_phone_trunk_bases_i_pv6.setter
    def inherit_phone_trunk_bases_i_pv6(self, inherit_phone_trunk_bases_i_pv6):
        """
        Sets the inherit_phone_trunk_bases_i_pv6 of this DomainLogicalInterface.
        The IPv6 phone trunk base assignment will be inherited from the Edge Group.

        :param inherit_phone_trunk_bases_i_pv6: The inherit_phone_trunk_bases_i_pv6 of this DomainLogicalInterface.
        :type: bool
        """
        
        self._inherit_phone_trunk_bases_i_pv6 = inherit_phone_trunk_bases_i_pv6

    @property
    def use_for_internal_edge_communication(self):
        """
        Gets the use_for_internal_edge_communication of this DomainLogicalInterface.
        This interface will be used for all internal edge-to-edge communication using settings from the edgeTrunkBaseAssignment on the Edge Group.

        :return: The use_for_internal_edge_communication of this DomainLogicalInterface.
        :rtype: bool
        """
        return self._use_for_internal_edge_communication

    @use_for_internal_edge_communication.setter
    def use_for_internal_edge_communication(self, use_for_internal_edge_communication):
        """
        Sets the use_for_internal_edge_communication of this DomainLogicalInterface.
        This interface will be used for all internal edge-to-edge communication using settings from the edgeTrunkBaseAssignment on the Edge Group.

        :param use_for_internal_edge_communication: The use_for_internal_edge_communication of this DomainLogicalInterface.
        :type: bool
        """
        
        self._use_for_internal_edge_communication = use_for_internal_edge_communication

    @property
    def external_trunk_base_assignments(self):
        """
        Gets the external_trunk_base_assignments of this DomainLogicalInterface.
        External trunk base settings to use for external communication from this interface.

        :return: The external_trunk_base_assignments of this DomainLogicalInterface.
        :rtype: list[TrunkBaseAssignment]
        """
        return self._external_trunk_base_assignments

    @external_trunk_base_assignments.setter
    def external_trunk_base_assignments(self, external_trunk_base_assignments):
        """
        Sets the external_trunk_base_assignments of this DomainLogicalInterface.
        External trunk base settings to use for external communication from this interface.

        :param external_trunk_base_assignments: The external_trunk_base_assignments of this DomainLogicalInterface.
        :type: list[TrunkBaseAssignment]
        """
        
        self._external_trunk_base_assignments = external_trunk_base_assignments

    @property
    def phone_trunk_base_assignments(self):
        """
        Gets the phone_trunk_base_assignments of this DomainLogicalInterface.
        Phone trunk base settings to use for phone communication from this interface.  These settings will be ignored when \"inheritPhoneTrunkBases\" is true.

        :return: The phone_trunk_base_assignments of this DomainLogicalInterface.
        :rtype: list[TrunkBaseAssignment]
        """
        return self._phone_trunk_base_assignments

    @phone_trunk_base_assignments.setter
    def phone_trunk_base_assignments(self, phone_trunk_base_assignments):
        """
        Sets the phone_trunk_base_assignments of this DomainLogicalInterface.
        Phone trunk base settings to use for phone communication from this interface.  These settings will be ignored when \"inheritPhoneTrunkBases\" is true.

        :param phone_trunk_base_assignments: The phone_trunk_base_assignments of this DomainLogicalInterface.
        :type: list[TrunkBaseAssignment]
        """
        
        self._phone_trunk_base_assignments = phone_trunk_base_assignments

    @property
    def self_uri(self):
        """
        Gets the self_uri of this DomainLogicalInterface.
        The URI for this object

        :return: The self_uri of this DomainLogicalInterface.
        :rtype: str
        """
        return self._self_uri

    @self_uri.setter
    def self_uri(self, self_uri):
        """
        Sets the self_uri of this DomainLogicalInterface.
        The URI for this object

        :param self_uri: The self_uri of this DomainLogicalInterface.
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
