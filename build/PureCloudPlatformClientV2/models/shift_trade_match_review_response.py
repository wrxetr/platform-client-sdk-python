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


class ShiftTradeMatchReviewResponse(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        ShiftTradeMatchReviewResponse - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'initiating_user': 'ShiftTradeMatchReviewUserResponse',
            'receiving_user': 'ShiftTradeMatchReviewUserResponse',
            'violations': 'list[ShiftTradeMatchViolation]',
            'admin_review_violations': 'list[ShiftTradeMatchViolation]'
        }

        self.attribute_map = {
            'initiating_user': 'initiatingUser',
            'receiving_user': 'receivingUser',
            'violations': 'violations',
            'admin_review_violations': 'adminReviewViolations'
        }

        self._initiating_user = None
        self._receiving_user = None
        self._violations = None
        self._admin_review_violations = None

    @property
    def initiating_user(self):
        """
        Gets the initiating_user of this ShiftTradeMatchReviewResponse.
        Details for the initiatingUser side of the shift trade

        :return: The initiating_user of this ShiftTradeMatchReviewResponse.
        :rtype: ShiftTradeMatchReviewUserResponse
        """
        return self._initiating_user

    @initiating_user.setter
    def initiating_user(self, initiating_user):
        """
        Sets the initiating_user of this ShiftTradeMatchReviewResponse.
        Details for the initiatingUser side of the shift trade

        :param initiating_user: The initiating_user of this ShiftTradeMatchReviewResponse.
        :type: ShiftTradeMatchReviewUserResponse
        """
        
        self._initiating_user = initiating_user

    @property
    def receiving_user(self):
        """
        Gets the receiving_user of this ShiftTradeMatchReviewResponse.
        Details for the receivingUser side of the shift trade

        :return: The receiving_user of this ShiftTradeMatchReviewResponse.
        :rtype: ShiftTradeMatchReviewUserResponse
        """
        return self._receiving_user

    @receiving_user.setter
    def receiving_user(self, receiving_user):
        """
        Sets the receiving_user of this ShiftTradeMatchReviewResponse.
        Details for the receivingUser side of the shift trade

        :param receiving_user: The receiving_user of this ShiftTradeMatchReviewResponse.
        :type: ShiftTradeMatchReviewUserResponse
        """
        
        self._receiving_user = receiving_user

    @property
    def violations(self):
        """
        Gets the violations of this ShiftTradeMatchReviewResponse.
        Constraint violations introduced after being matched that would normally disallow a trade, but which can still be overridden by the shift trade administrator

        :return: The violations of this ShiftTradeMatchReviewResponse.
        :rtype: list[ShiftTradeMatchViolation]
        """
        return self._violations

    @violations.setter
    def violations(self, violations):
        """
        Sets the violations of this ShiftTradeMatchReviewResponse.
        Constraint violations introduced after being matched that would normally disallow a trade, but which can still be overridden by the shift trade administrator

        :param violations: The violations of this ShiftTradeMatchReviewResponse.
        :type: list[ShiftTradeMatchViolation]
        """
        
        self._violations = violations

    @property
    def admin_review_violations(self):
        """
        Gets the admin_review_violations of this ShiftTradeMatchReviewResponse.
        Constraint violations associated with this shift trade which require shift trade administrator review

        :return: The admin_review_violations of this ShiftTradeMatchReviewResponse.
        :rtype: list[ShiftTradeMatchViolation]
        """
        return self._admin_review_violations

    @admin_review_violations.setter
    def admin_review_violations(self, admin_review_violations):
        """
        Sets the admin_review_violations of this ShiftTradeMatchReviewResponse.
        Constraint violations associated with this shift trade which require shift trade administrator review

        :param admin_review_violations: The admin_review_violations of this ShiftTradeMatchReviewResponse.
        :type: list[ShiftTradeMatchViolation]
        """
        
        self._admin_review_violations = admin_review_violations

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

