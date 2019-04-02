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


class MatchShiftTradeRequest(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        MatchShiftTradeRequest - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'receiving_schedule_id': 'str',
            'receiving_shift_id': 'str',
            'metadata': 'WfmVersionedEntityMetadata'
        }

        self.attribute_map = {
            'receiving_schedule_id': 'receivingScheduleId',
            'receiving_shift_id': 'receivingShiftId',
            'metadata': 'metadata'
        }

        self._receiving_schedule_id = None
        self._receiving_shift_id = None
        self._metadata = None

    @property
    def receiving_schedule_id(self):
        """
        Gets the receiving_schedule_id of this MatchShiftTradeRequest.
        The ID of the schedule with which the shift trade is associated

        :return: The receiving_schedule_id of this MatchShiftTradeRequest.
        :rtype: str
        """
        return self._receiving_schedule_id

    @receiving_schedule_id.setter
    def receiving_schedule_id(self, receiving_schedule_id):
        """
        Sets the receiving_schedule_id of this MatchShiftTradeRequest.
        The ID of the schedule with which the shift trade is associated

        :param receiving_schedule_id: The receiving_schedule_id of this MatchShiftTradeRequest.
        :type: str
        """
        
        self._receiving_schedule_id = receiving_schedule_id

    @property
    def receiving_shift_id(self):
        """
        Gets the receiving_shift_id of this MatchShiftTradeRequest.
        The ID of the shift the receiving user is giving up in trade, if applicable

        :return: The receiving_shift_id of this MatchShiftTradeRequest.
        :rtype: str
        """
        return self._receiving_shift_id

    @receiving_shift_id.setter
    def receiving_shift_id(self, receiving_shift_id):
        """
        Sets the receiving_shift_id of this MatchShiftTradeRequest.
        The ID of the shift the receiving user is giving up in trade, if applicable

        :param receiving_shift_id: The receiving_shift_id of this MatchShiftTradeRequest.
        :type: str
        """
        
        self._receiving_shift_id = receiving_shift_id

    @property
    def metadata(self):
        """
        Gets the metadata of this MatchShiftTradeRequest.
        Version metadata for the shift trade

        :return: The metadata of this MatchShiftTradeRequest.
        :rtype: WfmVersionedEntityMetadata
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """
        Sets the metadata of this MatchShiftTradeRequest.
        Version metadata for the shift trade

        :param metadata: The metadata of this MatchShiftTradeRequest.
        :type: WfmVersionedEntityMetadata
        """
        
        self._metadata = metadata

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

