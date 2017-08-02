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


class Campaign(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        Campaign - a model defined in Swagger

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
            'contact_list': 'UriReference',
            'queue': 'UriReference',
            'dialing_mode': 'str',
            'script': 'UriReference',
            'edge_group': 'UriReference',
            'campaign_status': 'str',
            'phone_columns': 'list[PhoneColumn]',
            'abandon_rate': 'float',
            'dnc_lists': 'list[UriReference]',
            'callable_time_set': 'UriReference',
            'call_analysis_response_set': 'UriReference',
            'errors': 'list[RestErrorDetail]',
            'caller_name': 'str',
            'caller_address': 'str',
            'outbound_line_count': 'int',
            'rule_sets': 'list[UriReference]',
            'skip_preview_disabled': 'bool',
            'preview_time_out_seconds': 'int',
            'contact_sort': 'ContactSort',
            'contact_sorts': 'list[ContactSort]',
            'no_answer_timeout': 'int',
            'call_analysis_language': 'str',
            'priority': 'int',
            'contact_list_filters': 'list[UriReference]',
            'self_uri': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'date_created': 'dateCreated',
            'date_modified': 'dateModified',
            'version': 'version',
            'contact_list': 'contactList',
            'queue': 'queue',
            'dialing_mode': 'dialingMode',
            'script': 'script',
            'edge_group': 'edgeGroup',
            'campaign_status': 'campaignStatus',
            'phone_columns': 'phoneColumns',
            'abandon_rate': 'abandonRate',
            'dnc_lists': 'dncLists',
            'callable_time_set': 'callableTimeSet',
            'call_analysis_response_set': 'callAnalysisResponseSet',
            'errors': 'errors',
            'caller_name': 'callerName',
            'caller_address': 'callerAddress',
            'outbound_line_count': 'outboundLineCount',
            'rule_sets': 'ruleSets',
            'skip_preview_disabled': 'skipPreviewDisabled',
            'preview_time_out_seconds': 'previewTimeOutSeconds',
            'contact_sort': 'contactSort',
            'contact_sorts': 'contactSorts',
            'no_answer_timeout': 'noAnswerTimeout',
            'call_analysis_language': 'callAnalysisLanguage',
            'priority': 'priority',
            'contact_list_filters': 'contactListFilters',
            'self_uri': 'selfUri'
        }

        self._id = None
        self._name = None
        self._date_created = None
        self._date_modified = None
        self._version = None
        self._contact_list = None
        self._queue = None
        self._dialing_mode = None
        self._script = None
        self._edge_group = None
        self._campaign_status = None
        self._phone_columns = None
        self._abandon_rate = None
        self._dnc_lists = None
        self._callable_time_set = None
        self._call_analysis_response_set = None
        self._errors = None
        self._caller_name = None
        self._caller_address = None
        self._outbound_line_count = None
        self._rule_sets = None
        self._skip_preview_disabled = None
        self._preview_time_out_seconds = None
        self._contact_sort = None
        self._contact_sorts = None
        self._no_answer_timeout = None
        self._call_analysis_language = None
        self._priority = None
        self._contact_list_filters = None
        self._self_uri = None

    @property
    def id(self):
        """
        Gets the id of this Campaign.
        The globally unique identifier for the object.

        :return: The id of this Campaign.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Campaign.
        The globally unique identifier for the object.

        :param id: The id of this Campaign.
        :type: str
        """
        
        self._id = id

    @property
    def name(self):
        """
        Gets the name of this Campaign.


        :return: The name of this Campaign.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Campaign.


        :param name: The name of this Campaign.
        :type: str
        """
        
        self._name = name

    @property
    def date_created(self):
        """
        Gets the date_created of this Campaign.
        Creation time of the entity. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ

        :return: The date_created of this Campaign.
        :rtype: datetime
        """
        return self._date_created

    @date_created.setter
    def date_created(self, date_created):
        """
        Sets the date_created of this Campaign.
        Creation time of the entity. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ

        :param date_created: The date_created of this Campaign.
        :type: datetime
        """
        
        self._date_created = date_created

    @property
    def date_modified(self):
        """
        Gets the date_modified of this Campaign.
        Last modified time of the entity. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ

        :return: The date_modified of this Campaign.
        :rtype: datetime
        """
        return self._date_modified

    @date_modified.setter
    def date_modified(self, date_modified):
        """
        Sets the date_modified of this Campaign.
        Last modified time of the entity. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ

        :param date_modified: The date_modified of this Campaign.
        :type: datetime
        """
        
        self._date_modified = date_modified

    @property
    def version(self):
        """
        Gets the version of this Campaign.
        Required for updates, must match the version number of the most recent update

        :return: The version of this Campaign.
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """
        Sets the version of this Campaign.
        Required for updates, must match the version number of the most recent update

        :param version: The version of this Campaign.
        :type: int
        """
        
        self._version = version

    @property
    def contact_list(self):
        """
        Gets the contact_list of this Campaign.
        identifier of the contact list for the campaign

        :return: The contact_list of this Campaign.
        :rtype: UriReference
        """
        return self._contact_list

    @contact_list.setter
    def contact_list(self, contact_list):
        """
        Sets the contact_list of this Campaign.
        identifier of the contact list for the campaign

        :param contact_list: The contact_list of this Campaign.
        :type: UriReference
        """
        
        self._contact_list = contact_list

    @property
    def queue(self):
        """
        Gets the queue of this Campaign.
        identifier of the agent assignment queue, required for all dialing modes other than agentless

        :return: The queue of this Campaign.
        :rtype: UriReference
        """
        return self._queue

    @queue.setter
    def queue(self, queue):
        """
        Sets the queue of this Campaign.
        identifier of the agent assignment queue, required for all dialing modes other than agentless

        :param queue: The queue of this Campaign.
        :type: UriReference
        """
        
        self._queue = queue

    @property
    def dialing_mode(self):
        """
        Gets the dialing_mode of this Campaign.
        dialing mode of the campaign

        :return: The dialing_mode of this Campaign.
        :rtype: str
        """
        return self._dialing_mode

    @dialing_mode.setter
    def dialing_mode(self, dialing_mode):
        """
        Sets the dialing_mode of this Campaign.
        dialing mode of the campaign

        :param dialing_mode: The dialing_mode of this Campaign.
        :type: str
        """
        allowed_values = ["agentless", "preview", "power", "predictive", "progressive"]
        if dialing_mode.lower() not in map(str.lower, allowed_values):
            # print "Invalid value for dialing_mode -> " + dialing_mode
            self._dialing_mode = "outdated_sdk_version"
        else:
            self._dialing_mode = dialing_mode

    @property
    def script(self):
        """
        Gets the script of this Campaign.
        identifier of the campaign script, required for all dialing modes other than agentless

        :return: The script of this Campaign.
        :rtype: UriReference
        """
        return self._script

    @script.setter
    def script(self, script):
        """
        Sets the script of this Campaign.
        identifier of the campaign script, required for all dialing modes other than agentless

        :param script: The script of this Campaign.
        :type: UriReference
        """
        
        self._script = script

    @property
    def edge_group(self):
        """
        Gets the edge_group of this Campaign.
        identifier of the edge group, required for all dialing modes other than preview

        :return: The edge_group of this Campaign.
        :rtype: UriReference
        """
        return self._edge_group

    @edge_group.setter
    def edge_group(self, edge_group):
        """
        Sets the edge_group of this Campaign.
        identifier of the edge group, required for all dialing modes other than preview

        :param edge_group: The edge_group of this Campaign.
        :type: UriReference
        """
        
        self._edge_group = edge_group

    @property
    def campaign_status(self):
        """
        Gets the campaign_status of this Campaign.
        status of the campaign; can be set to 'on' or 'off'

        :return: The campaign_status of this Campaign.
        :rtype: str
        """
        return self._campaign_status

    @campaign_status.setter
    def campaign_status(self, campaign_status):
        """
        Sets the campaign_status of this Campaign.
        status of the campaign; can be set to 'on' or 'off'

        :param campaign_status: The campaign_status of this Campaign.
        :type: str
        """
        allowed_values = ["on", "stopping", "off", "complete", "invalid"]
        if campaign_status.lower() not in map(str.lower, allowed_values):
            # print "Invalid value for campaign_status -> " + campaign_status
            self._campaign_status = "outdated_sdk_version"
        else:
            self._campaign_status = campaign_status

    @property
    def phone_columns(self):
        """
        Gets the phone_columns of this Campaign.
        the contact list phone columns to be called for the campaign

        :return: The phone_columns of this Campaign.
        :rtype: list[PhoneColumn]
        """
        return self._phone_columns

    @phone_columns.setter
    def phone_columns(self, phone_columns):
        """
        Sets the phone_columns of this Campaign.
        the contact list phone columns to be called for the campaign

        :param phone_columns: The phone_columns of this Campaign.
        :type: list[PhoneColumn]
        """
        
        self._phone_columns = phone_columns

    @property
    def abandon_rate(self):
        """
        Gets the abandon_rate of this Campaign.
        the targeted abandon rate percentage

        :return: The abandon_rate of this Campaign.
        :rtype: float
        """
        return self._abandon_rate

    @abandon_rate.setter
    def abandon_rate(self, abandon_rate):
        """
        Sets the abandon_rate of this Campaign.
        the targeted abandon rate percentage

        :param abandon_rate: The abandon_rate of this Campaign.
        :type: float
        """
        
        self._abandon_rate = abandon_rate

    @property
    def dnc_lists(self):
        """
        Gets the dnc_lists of this Campaign.
        identifiers of the do not call lists

        :return: The dnc_lists of this Campaign.
        :rtype: list[UriReference]
        """
        return self._dnc_lists

    @dnc_lists.setter
    def dnc_lists(self, dnc_lists):
        """
        Sets the dnc_lists of this Campaign.
        identifiers of the do not call lists

        :param dnc_lists: The dnc_lists of this Campaign.
        :type: list[UriReference]
        """
        
        self._dnc_lists = dnc_lists

    @property
    def callable_time_set(self):
        """
        Gets the callable_time_set of this Campaign.
        the identifier of the callable time set

        :return: The callable_time_set of this Campaign.
        :rtype: UriReference
        """
        return self._callable_time_set

    @callable_time_set.setter
    def callable_time_set(self, callable_time_set):
        """
        Sets the callable_time_set of this Campaign.
        the identifier of the callable time set

        :param callable_time_set: The callable_time_set of this Campaign.
        :type: UriReference
        """
        
        self._callable_time_set = callable_time_set

    @property
    def call_analysis_response_set(self):
        """
        Gets the call_analysis_response_set of this Campaign.
        the identifier of the call analysis response set, required for all dialing modes other than preview

        :return: The call_analysis_response_set of this Campaign.
        :rtype: UriReference
        """
        return self._call_analysis_response_set

    @call_analysis_response_set.setter
    def call_analysis_response_set(self, call_analysis_response_set):
        """
        Sets the call_analysis_response_set of this Campaign.
        the identifier of the call analysis response set, required for all dialing modes other than preview

        :param call_analysis_response_set: The call_analysis_response_set of this Campaign.
        :type: UriReference
        """
        
        self._call_analysis_response_set = call_analysis_response_set

    @property
    def errors(self):
        """
        Gets the errors of this Campaign.
        a list of current error conditions associated with the campaign

        :return: The errors of this Campaign.
        :rtype: list[RestErrorDetail]
        """
        return self._errors

    @errors.setter
    def errors(self, errors):
        """
        Sets the errors of this Campaign.
        a list of current error conditions associated with the campaign

        :param errors: The errors of this Campaign.
        :type: list[RestErrorDetail]
        """
        
        self._errors = errors

    @property
    def caller_name(self):
        """
        Gets the caller_name of this Campaign.
        caller id name to be displayed on the outbound call

        :return: The caller_name of this Campaign.
        :rtype: str
        """
        return self._caller_name

    @caller_name.setter
    def caller_name(self, caller_name):
        """
        Sets the caller_name of this Campaign.
        caller id name to be displayed on the outbound call

        :param caller_name: The caller_name of this Campaign.
        :type: str
        """
        
        self._caller_name = caller_name

    @property
    def caller_address(self):
        """
        Gets the caller_address of this Campaign.
        caller id phone number to be displayed on the outbound call

        :return: The caller_address of this Campaign.
        :rtype: str
        """
        return self._caller_address

    @caller_address.setter
    def caller_address(self, caller_address):
        """
        Sets the caller_address of this Campaign.
        caller id phone number to be displayed on the outbound call

        :param caller_address: The caller_address of this Campaign.
        :type: str
        """
        
        self._caller_address = caller_address

    @property
    def outbound_line_count(self):
        """
        Gets the outbound_line_count of this Campaign.
        for agentless campaigns, the number of outbound lines to be concurrently dialed

        :return: The outbound_line_count of this Campaign.
        :rtype: int
        """
        return self._outbound_line_count

    @outbound_line_count.setter
    def outbound_line_count(self, outbound_line_count):
        """
        Sets the outbound_line_count of this Campaign.
        for agentless campaigns, the number of outbound lines to be concurrently dialed

        :param outbound_line_count: The outbound_line_count of this Campaign.
        :type: int
        """
        
        self._outbound_line_count = outbound_line_count

    @property
    def rule_sets(self):
        """
        Gets the rule_sets of this Campaign.
        identifiers of the rule sets

        :return: The rule_sets of this Campaign.
        :rtype: list[UriReference]
        """
        return self._rule_sets

    @rule_sets.setter
    def rule_sets(self, rule_sets):
        """
        Sets the rule_sets of this Campaign.
        identifiers of the rule sets

        :param rule_sets: The rule_sets of this Campaign.
        :type: list[UriReference]
        """
        
        self._rule_sets = rule_sets

    @property
    def skip_preview_disabled(self):
        """
        Gets the skip_preview_disabled of this Campaign.
        for preview campaigns, indicator of whether the agent can skip a preview without placing a call

        :return: The skip_preview_disabled of this Campaign.
        :rtype: bool
        """
        return self._skip_preview_disabled

    @skip_preview_disabled.setter
    def skip_preview_disabled(self, skip_preview_disabled):
        """
        Sets the skip_preview_disabled of this Campaign.
        for preview campaigns, indicator of whether the agent can skip a preview without placing a call

        :param skip_preview_disabled: The skip_preview_disabled of this Campaign.
        :type: bool
        """
        
        self._skip_preview_disabled = skip_preview_disabled

    @property
    def preview_time_out_seconds(self):
        """
        Gets the preview_time_out_seconds of this Campaign.
        for preview campaigns, number of seconds before a call will be automatically placed. A value of 0 indicates no automatic placement of calls

        :return: The preview_time_out_seconds of this Campaign.
        :rtype: int
        """
        return self._preview_time_out_seconds

    @preview_time_out_seconds.setter
    def preview_time_out_seconds(self, preview_time_out_seconds):
        """
        Sets the preview_time_out_seconds of this Campaign.
        for preview campaigns, number of seconds before a call will be automatically placed. A value of 0 indicates no automatic placement of calls

        :param preview_time_out_seconds: The preview_time_out_seconds of this Campaign.
        :type: int
        """
        
        self._preview_time_out_seconds = preview_time_out_seconds

    @property
    def contact_sort(self):
        """
        Gets the contact_sort of this Campaign.
        information determining the order in which the contacts will be dialed

        :return: The contact_sort of this Campaign.
        :rtype: ContactSort
        """
        return self._contact_sort

    @contact_sort.setter
    def contact_sort(self, contact_sort):
        """
        Sets the contact_sort of this Campaign.
        information determining the order in which the contacts will be dialed

        :param contact_sort: The contact_sort of this Campaign.
        :type: ContactSort
        """
        
        self._contact_sort = contact_sort

    @property
    def contact_sorts(self):
        """
        Gets the contact_sorts of this Campaign.
        column prioritized information determining the order in which the contacts will be dialed

        :return: The contact_sorts of this Campaign.
        :rtype: list[ContactSort]
        """
        return self._contact_sorts

    @contact_sorts.setter
    def contact_sorts(self, contact_sorts):
        """
        Sets the contact_sorts of this Campaign.
        column prioritized information determining the order in which the contacts will be dialed

        :param contact_sorts: The contact_sorts of this Campaign.
        :type: list[ContactSort]
        """
        
        self._contact_sorts = contact_sorts

    @property
    def no_answer_timeout(self):
        """
        Gets the no_answer_timeout of this Campaign.
        for non-preview campaigns, how long to wait before dispositioning as 'no-answer', default 30 seconds

        :return: The no_answer_timeout of this Campaign.
        :rtype: int
        """
        return self._no_answer_timeout

    @no_answer_timeout.setter
    def no_answer_timeout(self, no_answer_timeout):
        """
        Sets the no_answer_timeout of this Campaign.
        for non-preview campaigns, how long to wait before dispositioning as 'no-answer', default 30 seconds

        :param no_answer_timeout: The no_answer_timeout of this Campaign.
        :type: int
        """
        
        self._no_answer_timeout = no_answer_timeout

    @property
    def call_analysis_language(self):
        """
        Gets the call_analysis_language of this Campaign.
        The language the edge will use to analyse the call

        :return: The call_analysis_language of this Campaign.
        :rtype: str
        """
        return self._call_analysis_language

    @call_analysis_language.setter
    def call_analysis_language(self, call_analysis_language):
        """
        Sets the call_analysis_language of this Campaign.
        The language the edge will use to analyse the call

        :param call_analysis_language: The call_analysis_language of this Campaign.
        :type: str
        """
        
        self._call_analysis_language = call_analysis_language

    @property
    def priority(self):
        """
        Gets the priority of this Campaign.
        The priority of this campaign relative to other campaigns

        :return: The priority of this Campaign.
        :rtype: int
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        """
        Sets the priority of this Campaign.
        The priority of this campaign relative to other campaigns

        :param priority: The priority of this Campaign.
        :type: int
        """
        
        self._priority = priority

    @property
    def contact_list_filters(self):
        """
        Gets the contact_list_filters of this Campaign.
        Filter defining a subset of contacts from the contact list to be dialed

        :return: The contact_list_filters of this Campaign.
        :rtype: list[UriReference]
        """
        return self._contact_list_filters

    @contact_list_filters.setter
    def contact_list_filters(self, contact_list_filters):
        """
        Sets the contact_list_filters of this Campaign.
        Filter defining a subset of contacts from the contact list to be dialed

        :param contact_list_filters: The contact_list_filters of this Campaign.
        :type: list[UriReference]
        """
        
        self._contact_list_filters = contact_list_filters

    @property
    def self_uri(self):
        """
        Gets the self_uri of this Campaign.
        The URI for this object

        :return: The self_uri of this Campaign.
        :rtype: str
        """
        return self._self_uri

    @self_uri.setter
    def self_uri(self, self_uri):
        """
        Sets the self_uri of this Campaign.
        The URI for this object

        :param self_uri: The self_uri of this Campaign.
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

