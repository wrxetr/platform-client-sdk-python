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


class CampaignProgress(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        CampaignProgress - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'campaign': 'UriReference',
            'contact_list': 'UriReference',
            'number_of_contacts_called': 'int',
            'total_number_of_contacts': 'int',
            'percentage': 'int'
        }

        self.attribute_map = {
            'campaign': 'campaign',
            'contact_list': 'contactList',
            'number_of_contacts_called': 'numberOfContactsCalled',
            'total_number_of_contacts': 'totalNumberOfContacts',
            'percentage': 'percentage'
        }

        self._campaign = None
        self._contact_list = None
        self._number_of_contacts_called = None
        self._total_number_of_contacts = None
        self._percentage = None

    @property
    def campaign(self):
        """
        Gets the campaign of this CampaignProgress.
        Identifier of the campaign

        :return: The campaign of this CampaignProgress.
        :rtype: UriReference
        """
        return self._campaign

    @campaign.setter
    def campaign(self, campaign):
        """
        Sets the campaign of this CampaignProgress.
        Identifier of the campaign

        :param campaign: The campaign of this CampaignProgress.
        :type: UriReference
        """
        
        self._campaign = campaign

    @property
    def contact_list(self):
        """
        Gets the contact_list of this CampaignProgress.
        Identifier of the contact list

        :return: The contact_list of this CampaignProgress.
        :rtype: UriReference
        """
        return self._contact_list

    @contact_list.setter
    def contact_list(self, contact_list):
        """
        Sets the contact_list of this CampaignProgress.
        Identifier of the contact list

        :param contact_list: The contact_list of this CampaignProgress.
        :type: UriReference
        """
        
        self._contact_list = contact_list

    @property
    def number_of_contacts_called(self):
        """
        Gets the number_of_contacts_called of this CampaignProgress.
        Number of contacts processed during the campaign

        :return: The number_of_contacts_called of this CampaignProgress.
        :rtype: int
        """
        return self._number_of_contacts_called

    @number_of_contacts_called.setter
    def number_of_contacts_called(self, number_of_contacts_called):
        """
        Sets the number_of_contacts_called of this CampaignProgress.
        Number of contacts processed during the campaign

        :param number_of_contacts_called: The number_of_contacts_called of this CampaignProgress.
        :type: int
        """
        
        self._number_of_contacts_called = number_of_contacts_called

    @property
    def total_number_of_contacts(self):
        """
        Gets the total_number_of_contacts of this CampaignProgress.
        Total number of contacts in the campaign

        :return: The total_number_of_contacts of this CampaignProgress.
        :rtype: int
        """
        return self._total_number_of_contacts

    @total_number_of_contacts.setter
    def total_number_of_contacts(self, total_number_of_contacts):
        """
        Sets the total_number_of_contacts of this CampaignProgress.
        Total number of contacts in the campaign

        :param total_number_of_contacts: The total_number_of_contacts of this CampaignProgress.
        :type: int
        """
        
        self._total_number_of_contacts = total_number_of_contacts

    @property
    def percentage(self):
        """
        Gets the percentage of this CampaignProgress.
        Percentage of contacts processed during the campaign

        :return: The percentage of this CampaignProgress.
        :rtype: int
        """
        return self._percentage

    @percentage.setter
    def percentage(self, percentage):
        """
        Sets the percentage of this CampaignProgress.
        Percentage of contacts processed during the campaign

        :param percentage: The percentage of this CampaignProgress.
        :type: int
        """
        
        self._percentage = percentage

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

