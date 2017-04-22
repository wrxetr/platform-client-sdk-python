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


class CampaignNotification(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        CampaignNotification - a model defined in Swagger

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
            'contact_list': 'DependencyTrackingBuildNotificationNotificationUser',
            'queue': 'CampaignNotificationUriReference',
            'dialing_mode': 'str',
            'script': 'CampaignNotificationUriReference',
            'edge_group': 'CampaignNotificationUriReference',
            'campaign_status': 'str',
            'phone_columns': 'list[CampaignNotificationPhoneColumns]',
            'abandon_rate': 'float',
            'dnc_lists': 'list[CampaignNotificationUriReference]',
            'callable_time_set': 'CampaignNotificationUriReference',
            'call_analysis_response_set': 'CampaignNotificationUriReference',
            'caller_name': 'str',
            'caller_address': 'str',
            'outbound_line_count': 'int',
            'errors': 'list[CampaignNotificationErrors]',
            'rule_sets': 'list[CampaignNotificationUriReference]',
            'skip_preview_disabled': 'bool',
            'preview_time_out_seconds': 'int',
            'single_number_preview': 'bool',
            'contact_sort': 'CampaignNotificationContactSort',
            'contact_sorts': 'list[CampaignNotificationContactSort]',
            'no_answer_timeout': 'int',
            'call_analysis_language': 'str',
            'priority': 'int',
            'contact_list_filters': 'list[CampaignNotificationUriReference]',
            'additional_properties': 'object'
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
            'caller_name': 'callerName',
            'caller_address': 'callerAddress',
            'outbound_line_count': 'outboundLineCount',
            'errors': 'errors',
            'rule_sets': 'ruleSets',
            'skip_preview_disabled': 'skipPreviewDisabled',
            'preview_time_out_seconds': 'previewTimeOutSeconds',
            'single_number_preview': 'singleNumberPreview',
            'contact_sort': 'contactSort',
            'contact_sorts': 'contactSorts',
            'no_answer_timeout': 'noAnswerTimeout',
            'call_analysis_language': 'callAnalysisLanguage',
            'priority': 'priority',
            'contact_list_filters': 'contactListFilters',
            'additional_properties': 'additionalProperties'
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
        self._caller_name = None
        self._caller_address = None
        self._outbound_line_count = None
        self._errors = None
        self._rule_sets = None
        self._skip_preview_disabled = None
        self._preview_time_out_seconds = None
        self._single_number_preview = None
        self._contact_sort = None
        self._contact_sorts = None
        self._no_answer_timeout = None
        self._call_analysis_language = None
        self._priority = None
        self._contact_list_filters = None
        self._additional_properties = None

    @property
    def id(self):
        """
        Gets the id of this CampaignNotification.


        :return: The id of this CampaignNotification.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this CampaignNotification.


        :param id: The id of this CampaignNotification.
        :type: str
        """
        
        self._id = id

    @property
    def name(self):
        """
        Gets the name of this CampaignNotification.


        :return: The name of this CampaignNotification.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this CampaignNotification.


        :param name: The name of this CampaignNotification.
        :type: str
        """
        
        self._name = name

    @property
    def date_created(self):
        """
        Gets the date_created of this CampaignNotification.


        :return: The date_created of this CampaignNotification.
        :rtype: datetime
        """
        return self._date_created

    @date_created.setter
    def date_created(self, date_created):
        """
        Sets the date_created of this CampaignNotification.


        :param date_created: The date_created of this CampaignNotification.
        :type: datetime
        """
        
        self._date_created = date_created

    @property
    def date_modified(self):
        """
        Gets the date_modified of this CampaignNotification.


        :return: The date_modified of this CampaignNotification.
        :rtype: datetime
        """
        return self._date_modified

    @date_modified.setter
    def date_modified(self, date_modified):
        """
        Sets the date_modified of this CampaignNotification.


        :param date_modified: The date_modified of this CampaignNotification.
        :type: datetime
        """
        
        self._date_modified = date_modified

    @property
    def version(self):
        """
        Gets the version of this CampaignNotification.


        :return: The version of this CampaignNotification.
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """
        Sets the version of this CampaignNotification.


        :param version: The version of this CampaignNotification.
        :type: int
        """
        
        self._version = version

    @property
    def contact_list(self):
        """
        Gets the contact_list of this CampaignNotification.


        :return: The contact_list of this CampaignNotification.
        :rtype: DependencyTrackingBuildNotificationNotificationUser
        """
        return self._contact_list

    @contact_list.setter
    def contact_list(self, contact_list):
        """
        Sets the contact_list of this CampaignNotification.


        :param contact_list: The contact_list of this CampaignNotification.
        :type: DependencyTrackingBuildNotificationNotificationUser
        """
        
        self._contact_list = contact_list

    @property
    def queue(self):
        """
        Gets the queue of this CampaignNotification.


        :return: The queue of this CampaignNotification.
        :rtype: CampaignNotificationUriReference
        """
        return self._queue

    @queue.setter
    def queue(self, queue):
        """
        Sets the queue of this CampaignNotification.


        :param queue: The queue of this CampaignNotification.
        :type: CampaignNotificationUriReference
        """
        
        self._queue = queue

    @property
    def dialing_mode(self):
        """
        Gets the dialing_mode of this CampaignNotification.


        :return: The dialing_mode of this CampaignNotification.
        :rtype: str
        """
        return self._dialing_mode

    @dialing_mode.setter
    def dialing_mode(self, dialing_mode):
        """
        Sets the dialing_mode of this CampaignNotification.


        :param dialing_mode: The dialing_mode of this CampaignNotification.
        :type: str
        """
        allowed_values = ["AGENTLESS", "PREVIEW", "POWER", "PREDICTIVE", "PROGRESSIVE"]
        if dialing_mode.lower() not in map(str.lower, allowed_values):
            # print "Invalid value for dialing_mode -> " + dialing_mode
            self._dialing_mode = "outdated_sdk_version"
        else:
            self._dialing_mode = dialing_mode.lower()

    @property
    def script(self):
        """
        Gets the script of this CampaignNotification.


        :return: The script of this CampaignNotification.
        :rtype: CampaignNotificationUriReference
        """
        return self._script

    @script.setter
    def script(self, script):
        """
        Sets the script of this CampaignNotification.


        :param script: The script of this CampaignNotification.
        :type: CampaignNotificationUriReference
        """
        
        self._script = script

    @property
    def edge_group(self):
        """
        Gets the edge_group of this CampaignNotification.


        :return: The edge_group of this CampaignNotification.
        :rtype: CampaignNotificationUriReference
        """
        return self._edge_group

    @edge_group.setter
    def edge_group(self, edge_group):
        """
        Sets the edge_group of this CampaignNotification.


        :param edge_group: The edge_group of this CampaignNotification.
        :type: CampaignNotificationUriReference
        """
        
        self._edge_group = edge_group

    @property
    def campaign_status(self):
        """
        Gets the campaign_status of this CampaignNotification.


        :return: The campaign_status of this CampaignNotification.
        :rtype: str
        """
        return self._campaign_status

    @campaign_status.setter
    def campaign_status(self, campaign_status):
        """
        Sets the campaign_status of this CampaignNotification.


        :param campaign_status: The campaign_status of this CampaignNotification.
        :type: str
        """
        allowed_values = ["ON", "OFF", "COMPLETE", "STOPPING", "INVALID"]
        if campaign_status.lower() not in map(str.lower, allowed_values):
            # print "Invalid value for campaign_status -> " + campaign_status
            self._campaign_status = "outdated_sdk_version"
        else:
            self._campaign_status = campaign_status.lower()

    @property
    def phone_columns(self):
        """
        Gets the phone_columns of this CampaignNotification.


        :return: The phone_columns of this CampaignNotification.
        :rtype: list[CampaignNotificationPhoneColumns]
        """
        return self._phone_columns

    @phone_columns.setter
    def phone_columns(self, phone_columns):
        """
        Sets the phone_columns of this CampaignNotification.


        :param phone_columns: The phone_columns of this CampaignNotification.
        :type: list[CampaignNotificationPhoneColumns]
        """
        
        self._phone_columns = phone_columns

    @property
    def abandon_rate(self):
        """
        Gets the abandon_rate of this CampaignNotification.


        :return: The abandon_rate of this CampaignNotification.
        :rtype: float
        """
        return self._abandon_rate

    @abandon_rate.setter
    def abandon_rate(self, abandon_rate):
        """
        Sets the abandon_rate of this CampaignNotification.


        :param abandon_rate: The abandon_rate of this CampaignNotification.
        :type: float
        """
        
        self._abandon_rate = abandon_rate

    @property
    def dnc_lists(self):
        """
        Gets the dnc_lists of this CampaignNotification.


        :return: The dnc_lists of this CampaignNotification.
        :rtype: list[CampaignNotificationUriReference]
        """
        return self._dnc_lists

    @dnc_lists.setter
    def dnc_lists(self, dnc_lists):
        """
        Sets the dnc_lists of this CampaignNotification.


        :param dnc_lists: The dnc_lists of this CampaignNotification.
        :type: list[CampaignNotificationUriReference]
        """
        
        self._dnc_lists = dnc_lists

    @property
    def callable_time_set(self):
        """
        Gets the callable_time_set of this CampaignNotification.


        :return: The callable_time_set of this CampaignNotification.
        :rtype: CampaignNotificationUriReference
        """
        return self._callable_time_set

    @callable_time_set.setter
    def callable_time_set(self, callable_time_set):
        """
        Sets the callable_time_set of this CampaignNotification.


        :param callable_time_set: The callable_time_set of this CampaignNotification.
        :type: CampaignNotificationUriReference
        """
        
        self._callable_time_set = callable_time_set

    @property
    def call_analysis_response_set(self):
        """
        Gets the call_analysis_response_set of this CampaignNotification.


        :return: The call_analysis_response_set of this CampaignNotification.
        :rtype: CampaignNotificationUriReference
        """
        return self._call_analysis_response_set

    @call_analysis_response_set.setter
    def call_analysis_response_set(self, call_analysis_response_set):
        """
        Sets the call_analysis_response_set of this CampaignNotification.


        :param call_analysis_response_set: The call_analysis_response_set of this CampaignNotification.
        :type: CampaignNotificationUriReference
        """
        
        self._call_analysis_response_set = call_analysis_response_set

    @property
    def caller_name(self):
        """
        Gets the caller_name of this CampaignNotification.


        :return: The caller_name of this CampaignNotification.
        :rtype: str
        """
        return self._caller_name

    @caller_name.setter
    def caller_name(self, caller_name):
        """
        Sets the caller_name of this CampaignNotification.


        :param caller_name: The caller_name of this CampaignNotification.
        :type: str
        """
        
        self._caller_name = caller_name

    @property
    def caller_address(self):
        """
        Gets the caller_address of this CampaignNotification.


        :return: The caller_address of this CampaignNotification.
        :rtype: str
        """
        return self._caller_address

    @caller_address.setter
    def caller_address(self, caller_address):
        """
        Sets the caller_address of this CampaignNotification.


        :param caller_address: The caller_address of this CampaignNotification.
        :type: str
        """
        
        self._caller_address = caller_address

    @property
    def outbound_line_count(self):
        """
        Gets the outbound_line_count of this CampaignNotification.


        :return: The outbound_line_count of this CampaignNotification.
        :rtype: int
        """
        return self._outbound_line_count

    @outbound_line_count.setter
    def outbound_line_count(self, outbound_line_count):
        """
        Sets the outbound_line_count of this CampaignNotification.


        :param outbound_line_count: The outbound_line_count of this CampaignNotification.
        :type: int
        """
        
        self._outbound_line_count = outbound_line_count

    @property
    def errors(self):
        """
        Gets the errors of this CampaignNotification.


        :return: The errors of this CampaignNotification.
        :rtype: list[CampaignNotificationErrors]
        """
        return self._errors

    @errors.setter
    def errors(self, errors):
        """
        Sets the errors of this CampaignNotification.


        :param errors: The errors of this CampaignNotification.
        :type: list[CampaignNotificationErrors]
        """
        
        self._errors = errors

    @property
    def rule_sets(self):
        """
        Gets the rule_sets of this CampaignNotification.


        :return: The rule_sets of this CampaignNotification.
        :rtype: list[CampaignNotificationUriReference]
        """
        return self._rule_sets

    @rule_sets.setter
    def rule_sets(self, rule_sets):
        """
        Sets the rule_sets of this CampaignNotification.


        :param rule_sets: The rule_sets of this CampaignNotification.
        :type: list[CampaignNotificationUriReference]
        """
        
        self._rule_sets = rule_sets

    @property
    def skip_preview_disabled(self):
        """
        Gets the skip_preview_disabled of this CampaignNotification.


        :return: The skip_preview_disabled of this CampaignNotification.
        :rtype: bool
        """
        return self._skip_preview_disabled

    @skip_preview_disabled.setter
    def skip_preview_disabled(self, skip_preview_disabled):
        """
        Sets the skip_preview_disabled of this CampaignNotification.


        :param skip_preview_disabled: The skip_preview_disabled of this CampaignNotification.
        :type: bool
        """
        
        self._skip_preview_disabled = skip_preview_disabled

    @property
    def preview_time_out_seconds(self):
        """
        Gets the preview_time_out_seconds of this CampaignNotification.


        :return: The preview_time_out_seconds of this CampaignNotification.
        :rtype: int
        """
        return self._preview_time_out_seconds

    @preview_time_out_seconds.setter
    def preview_time_out_seconds(self, preview_time_out_seconds):
        """
        Sets the preview_time_out_seconds of this CampaignNotification.


        :param preview_time_out_seconds: The preview_time_out_seconds of this CampaignNotification.
        :type: int
        """
        
        self._preview_time_out_seconds = preview_time_out_seconds

    @property
    def single_number_preview(self):
        """
        Gets the single_number_preview of this CampaignNotification.


        :return: The single_number_preview of this CampaignNotification.
        :rtype: bool
        """
        return self._single_number_preview

    @single_number_preview.setter
    def single_number_preview(self, single_number_preview):
        """
        Sets the single_number_preview of this CampaignNotification.


        :param single_number_preview: The single_number_preview of this CampaignNotification.
        :type: bool
        """
        
        self._single_number_preview = single_number_preview

    @property
    def contact_sort(self):
        """
        Gets the contact_sort of this CampaignNotification.


        :return: The contact_sort of this CampaignNotification.
        :rtype: CampaignNotificationContactSort
        """
        return self._contact_sort

    @contact_sort.setter
    def contact_sort(self, contact_sort):
        """
        Sets the contact_sort of this CampaignNotification.


        :param contact_sort: The contact_sort of this CampaignNotification.
        :type: CampaignNotificationContactSort
        """
        
        self._contact_sort = contact_sort

    @property
    def contact_sorts(self):
        """
        Gets the contact_sorts of this CampaignNotification.


        :return: The contact_sorts of this CampaignNotification.
        :rtype: list[CampaignNotificationContactSort]
        """
        return self._contact_sorts

    @contact_sorts.setter
    def contact_sorts(self, contact_sorts):
        """
        Sets the contact_sorts of this CampaignNotification.


        :param contact_sorts: The contact_sorts of this CampaignNotification.
        :type: list[CampaignNotificationContactSort]
        """
        
        self._contact_sorts = contact_sorts

    @property
    def no_answer_timeout(self):
        """
        Gets the no_answer_timeout of this CampaignNotification.


        :return: The no_answer_timeout of this CampaignNotification.
        :rtype: int
        """
        return self._no_answer_timeout

    @no_answer_timeout.setter
    def no_answer_timeout(self, no_answer_timeout):
        """
        Sets the no_answer_timeout of this CampaignNotification.


        :param no_answer_timeout: The no_answer_timeout of this CampaignNotification.
        :type: int
        """
        
        self._no_answer_timeout = no_answer_timeout

    @property
    def call_analysis_language(self):
        """
        Gets the call_analysis_language of this CampaignNotification.


        :return: The call_analysis_language of this CampaignNotification.
        :rtype: str
        """
        return self._call_analysis_language

    @call_analysis_language.setter
    def call_analysis_language(self, call_analysis_language):
        """
        Sets the call_analysis_language of this CampaignNotification.


        :param call_analysis_language: The call_analysis_language of this CampaignNotification.
        :type: str
        """
        
        self._call_analysis_language = call_analysis_language

    @property
    def priority(self):
        """
        Gets the priority of this CampaignNotification.


        :return: The priority of this CampaignNotification.
        :rtype: int
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        """
        Sets the priority of this CampaignNotification.


        :param priority: The priority of this CampaignNotification.
        :type: int
        """
        
        self._priority = priority

    @property
    def contact_list_filters(self):
        """
        Gets the contact_list_filters of this CampaignNotification.


        :return: The contact_list_filters of this CampaignNotification.
        :rtype: list[CampaignNotificationUriReference]
        """
        return self._contact_list_filters

    @contact_list_filters.setter
    def contact_list_filters(self, contact_list_filters):
        """
        Sets the contact_list_filters of this CampaignNotification.


        :param contact_list_filters: The contact_list_filters of this CampaignNotification.
        :type: list[CampaignNotificationUriReference]
        """
        
        self._contact_list_filters = contact_list_filters

    @property
    def additional_properties(self):
        """
        Gets the additional_properties of this CampaignNotification.


        :return: The additional_properties of this CampaignNotification.
        :rtype: object
        """
        return self._additional_properties

    @additional_properties.setter
    def additional_properties(self, additional_properties):
        """
        Sets the additional_properties of this CampaignNotification.


        :param additional_properties: The additional_properties of this CampaignNotification.
        :type: object
        """
        
        self._additional_properties = additional_properties

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

