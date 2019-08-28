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

class AnalyticsFlow(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        AnalyticsFlow - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'flow_id': 'str',
            'flow_name': 'str',
            'flow_version': 'str',
            'flow_type': 'str',
            'exit_reason': 'str',
            'entry_reason': 'str',
            'entry_type': 'str',
            'transfer_type': 'str',
            'transfer_target_name': 'str',
            'transfer_target_address': 'str',
            'issued_callback': 'bool',
            'starting_language': 'str',
            'ending_language': 'str',
            'outcomes': 'list[AnalyticsFlowOutcome]'
        }

        self.attribute_map = {
            'flow_id': 'flowId',
            'flow_name': 'flowName',
            'flow_version': 'flowVersion',
            'flow_type': 'flowType',
            'exit_reason': 'exitReason',
            'entry_reason': 'entryReason',
            'entry_type': 'entryType',
            'transfer_type': 'transferType',
            'transfer_target_name': 'transferTargetName',
            'transfer_target_address': 'transferTargetAddress',
            'issued_callback': 'issuedCallback',
            'starting_language': 'startingLanguage',
            'ending_language': 'endingLanguage',
            'outcomes': 'outcomes'
        }

        self._flow_id = None
        self._flow_name = None
        self._flow_version = None
        self._flow_type = None
        self._exit_reason = None
        self._entry_reason = None
        self._entry_type = None
        self._transfer_type = None
        self._transfer_target_name = None
        self._transfer_target_address = None
        self._issued_callback = None
        self._starting_language = None
        self._ending_language = None
        self._outcomes = None

    @property
    def flow_id(self):
        """
        Gets the flow_id of this AnalyticsFlow.
        The unique identifier of this flow

        :return: The flow_id of this AnalyticsFlow.
        :rtype: str
        """
        return self._flow_id

    @flow_id.setter
    def flow_id(self, flow_id):
        """
        Sets the flow_id of this AnalyticsFlow.
        The unique identifier of this flow

        :param flow_id: The flow_id of this AnalyticsFlow.
        :type: str
        """
        
        self._flow_id = flow_id

    @property
    def flow_name(self):
        """
        Gets the flow_name of this AnalyticsFlow.
        The name of this flow

        :return: The flow_name of this AnalyticsFlow.
        :rtype: str
        """
        return self._flow_name

    @flow_name.setter
    def flow_name(self, flow_name):
        """
        Sets the flow_name of this AnalyticsFlow.
        The name of this flow

        :param flow_name: The flow_name of this AnalyticsFlow.
        :type: str
        """
        
        self._flow_name = flow_name

    @property
    def flow_version(self):
        """
        Gets the flow_version of this AnalyticsFlow.
        The version of this flow

        :return: The flow_version of this AnalyticsFlow.
        :rtype: str
        """
        return self._flow_version

    @flow_version.setter
    def flow_version(self, flow_version):
        """
        Sets the flow_version of this AnalyticsFlow.
        The version of this flow

        :param flow_version: The flow_version of this AnalyticsFlow.
        :type: str
        """
        
        self._flow_version = flow_version

    @property
    def flow_type(self):
        """
        Gets the flow_type of this AnalyticsFlow.
        The type of this flow

        :return: The flow_type of this AnalyticsFlow.
        :rtype: str
        """
        return self._flow_type

    @flow_type.setter
    def flow_type(self, flow_type):
        """
        Sets the flow_type of this AnalyticsFlow.
        The type of this flow

        :param flow_type: The flow_type of this AnalyticsFlow.
        :type: str
        """
        allowed_values = ["COMMONMODULE", "INBOUNDCALL", "INBOUNDCHAT", "INBOUNDEMAIL", "INBOUNDSHORTMESSAGE", "INQUEUECALL", "OUTBOUNDCALL", "SECURECALL", "SPEECH", "SURVEYINVITE"]
        if flow_type.lower() not in map(str.lower, allowed_values):
            # print "Invalid value for flow_type -> " + flow_type
            self._flow_type = "outdated_sdk_version"
        else:
            self._flow_type = flow_type

    @property
    def exit_reason(self):
        """
        Gets the exit_reason of this AnalyticsFlow.
        The exit reason for this flow, e.g. DISCONNECT

        :return: The exit_reason of this AnalyticsFlow.
        :rtype: str
        """
        return self._exit_reason

    @exit_reason.setter
    def exit_reason(self, exit_reason):
        """
        Sets the exit_reason of this AnalyticsFlow.
        The exit reason for this flow, e.g. DISCONNECT

        :param exit_reason: The exit_reason of this AnalyticsFlow.
        :type: str
        """
        
        self._exit_reason = exit_reason

    @property
    def entry_reason(self):
        """
        Gets the entry_reason of this AnalyticsFlow.
        The particular entry reason for this flow, e.g. an address, userId, or flowId

        :return: The entry_reason of this AnalyticsFlow.
        :rtype: str
        """
        return self._entry_reason

    @entry_reason.setter
    def entry_reason(self, entry_reason):
        """
        Sets the entry_reason of this AnalyticsFlow.
        The particular entry reason for this flow, e.g. an address, userId, or flowId

        :param entry_reason: The entry_reason of this AnalyticsFlow.
        :type: str
        """
        
        self._entry_reason = entry_reason

    @property
    def entry_type(self):
        """
        Gets the entry_type of this AnalyticsFlow.
        The entry type for this flow

        :return: The entry_type of this AnalyticsFlow.
        :rtype: str
        """
        return self._entry_type

    @entry_type.setter
    def entry_type(self, entry_type):
        """
        Sets the entry_type of this AnalyticsFlow.
        The entry type for this flow

        :param entry_type: The entry_type of this AnalyticsFlow.
        :type: str
        """
        allowed_values = ["dnis", "direct", "flow", "agent", "outbound"]
        if entry_type.lower() not in map(str.lower, allowed_values):
            # print "Invalid value for entry_type -> " + entry_type
            self._entry_type = "outdated_sdk_version"
        else:
            self._entry_type = entry_type

    @property
    def transfer_type(self):
        """
        Gets the transfer_type of this AnalyticsFlow.
        The type of transfer for flows that ended with a transfer

        :return: The transfer_type of this AnalyticsFlow.
        :rtype: str
        """
        return self._transfer_type

    @transfer_type.setter
    def transfer_type(self, transfer_type):
        """
        Sets the transfer_type of this AnalyticsFlow.
        The type of transfer for flows that ended with a transfer

        :param transfer_type: The transfer_type of this AnalyticsFlow.
        :type: str
        """
        
        self._transfer_type = transfer_type

    @property
    def transfer_target_name(self):
        """
        Gets the transfer_target_name of this AnalyticsFlow.
        The name of a transfer target

        :return: The transfer_target_name of this AnalyticsFlow.
        :rtype: str
        """
        return self._transfer_target_name

    @transfer_target_name.setter
    def transfer_target_name(self, transfer_target_name):
        """
        Sets the transfer_target_name of this AnalyticsFlow.
        The name of a transfer target

        :param transfer_target_name: The transfer_target_name of this AnalyticsFlow.
        :type: str
        """
        
        self._transfer_target_name = transfer_target_name

    @property
    def transfer_target_address(self):
        """
        Gets the transfer_target_address of this AnalyticsFlow.
        The address of a transfer target

        :return: The transfer_target_address of this AnalyticsFlow.
        :rtype: str
        """
        return self._transfer_target_address

    @transfer_target_address.setter
    def transfer_target_address(self, transfer_target_address):
        """
        Sets the transfer_target_address of this AnalyticsFlow.
        The address of a transfer target

        :param transfer_target_address: The transfer_target_address of this AnalyticsFlow.
        :type: str
        """
        
        self._transfer_target_address = transfer_target_address

    @property
    def issued_callback(self):
        """
        Gets the issued_callback of this AnalyticsFlow.
        Flag indicating whether the flow issued a callback

        :return: The issued_callback of this AnalyticsFlow.
        :rtype: bool
        """
        return self._issued_callback

    @issued_callback.setter
    def issued_callback(self, issued_callback):
        """
        Sets the issued_callback of this AnalyticsFlow.
        Flag indicating whether the flow issued a callback

        :param issued_callback: The issued_callback of this AnalyticsFlow.
        :type: bool
        """
        
        self._issued_callback = issued_callback

    @property
    def starting_language(self):
        """
        Gets the starting_language of this AnalyticsFlow.
        Flow starting language, e.g. en-us

        :return: The starting_language of this AnalyticsFlow.
        :rtype: str
        """
        return self._starting_language

    @starting_language.setter
    def starting_language(self, starting_language):
        """
        Sets the starting_language of this AnalyticsFlow.
        Flow starting language, e.g. en-us

        :param starting_language: The starting_language of this AnalyticsFlow.
        :type: str
        """
        
        self._starting_language = starting_language

    @property
    def ending_language(self):
        """
        Gets the ending_language of this AnalyticsFlow.
        Flow ending language, e.g. en-us

        :return: The ending_language of this AnalyticsFlow.
        :rtype: str
        """
        return self._ending_language

    @ending_language.setter
    def ending_language(self, ending_language):
        """
        Sets the ending_language of this AnalyticsFlow.
        Flow ending language, e.g. en-us

        :param ending_language: The ending_language of this AnalyticsFlow.
        :type: str
        """
        
        self._ending_language = ending_language

    @property
    def outcomes(self):
        """
        Gets the outcomes of this AnalyticsFlow.
        Flow outcomes

        :return: The outcomes of this AnalyticsFlow.
        :rtype: list[AnalyticsFlowOutcome]
        """
        return self._outcomes

    @outcomes.setter
    def outcomes(self, outcomes):
        """
        Sets the outcomes of this AnalyticsFlow.
        Flow outcomes

        :param outcomes: The outcomes of this AnalyticsFlow.
        :type: list[AnalyticsFlowOutcome]
        """
        
        self._outcomes = outcomes

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

