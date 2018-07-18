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


class ViewFilter(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        ViewFilter - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'media_types': 'list[str]',
            'queue_ids': 'list[str]',
            'skill_ids': 'list[str]',
            'skill_groups': 'list[str]',
            'language_ids': 'list[str]',
            'language_groups': 'list[str]',
            'directions': 'list[str]',
            'wrap_up_codes': 'list[str]',
            'dnis_list': 'list[str]',
            'user_ids': 'list[str]',
            'address_tos': 'list[str]',
            'address_froms': 'list[str]',
            'outbound_campaign_ids': 'list[str]',
            'outbound_contact_list_ids': 'list[str]',
            'contact_ids': 'list[str]',
            'ani_list': 'list[str]',
            'durations_milliseconds': 'list[NumericRange]',
            'evaluation_score': 'NumericRange',
            'evaluation_critical_score': 'NumericRange',
            'evaluation_form_ids': 'list[str]',
            'evaluated_agent_ids': 'list[str]',
            'evaluator_ids': 'list[str]',
            'transferred': 'bool',
            'abandoned': 'bool',
            'message_types': 'list[str]',
            'division_ids': 'list[str]',
            'survey_form_ids': 'list[str]',
            'survey_total_score': 'NumericRange',
            'survey_nps_score': 'NumericRange'
        }

        self.attribute_map = {
            'media_types': 'mediaTypes',
            'queue_ids': 'queueIds',
            'skill_ids': 'skillIds',
            'skill_groups': 'skillGroups',
            'language_ids': 'languageIds',
            'language_groups': 'languageGroups',
            'directions': 'directions',
            'wrap_up_codes': 'wrapUpCodes',
            'dnis_list': 'dnisList',
            'user_ids': 'userIds',
            'address_tos': 'addressTos',
            'address_froms': 'addressFroms',
            'outbound_campaign_ids': 'outboundCampaignIds',
            'outbound_contact_list_ids': 'outboundContactListIds',
            'contact_ids': 'contactIds',
            'ani_list': 'aniList',
            'durations_milliseconds': 'durationsMilliseconds',
            'evaluation_score': 'evaluationScore',
            'evaluation_critical_score': 'evaluationCriticalScore',
            'evaluation_form_ids': 'evaluationFormIds',
            'evaluated_agent_ids': 'evaluatedAgentIds',
            'evaluator_ids': 'evaluatorIds',
            'transferred': 'transferred',
            'abandoned': 'abandoned',
            'message_types': 'messageTypes',
            'division_ids': 'divisionIds',
            'survey_form_ids': 'surveyFormIds',
            'survey_total_score': 'surveyTotalScore',
            'survey_nps_score': 'surveyNpsScore'
        }

        self._media_types = None
        self._queue_ids = None
        self._skill_ids = None
        self._skill_groups = None
        self._language_ids = None
        self._language_groups = None
        self._directions = None
        self._wrap_up_codes = None
        self._dnis_list = None
        self._user_ids = None
        self._address_tos = None
        self._address_froms = None
        self._outbound_campaign_ids = None
        self._outbound_contact_list_ids = None
        self._contact_ids = None
        self._ani_list = None
        self._durations_milliseconds = None
        self._evaluation_score = None
        self._evaluation_critical_score = None
        self._evaluation_form_ids = None
        self._evaluated_agent_ids = None
        self._evaluator_ids = None
        self._transferred = None
        self._abandoned = None
        self._message_types = None
        self._division_ids = None
        self._survey_form_ids = None
        self._survey_total_score = None
        self._survey_nps_score = None

    @property
    def media_types(self):
        """
        Gets the media_types of this ViewFilter.
        The media types are used to filter the view

        :return: The media_types of this ViewFilter.
        :rtype: list[str]
        """
        return self._media_types

    @media_types.setter
    def media_types(self, media_types):
        """
        Sets the media_types of this ViewFilter.
        The media types are used to filter the view

        :param media_types: The media_types of this ViewFilter.
        :type: list[str]
        """
        
        self._media_types = media_types

    @property
    def queue_ids(self):
        """
        Gets the queue_ids of this ViewFilter.
        The queue ids are used to filter the view

        :return: The queue_ids of this ViewFilter.
        :rtype: list[str]
        """
        return self._queue_ids

    @queue_ids.setter
    def queue_ids(self, queue_ids):
        """
        Sets the queue_ids of this ViewFilter.
        The queue ids are used to filter the view

        :param queue_ids: The queue_ids of this ViewFilter.
        :type: list[str]
        """
        
        self._queue_ids = queue_ids

    @property
    def skill_ids(self):
        """
        Gets the skill_ids of this ViewFilter.
        The skill ids are used to filter the view

        :return: The skill_ids of this ViewFilter.
        :rtype: list[str]
        """
        return self._skill_ids

    @skill_ids.setter
    def skill_ids(self, skill_ids):
        """
        Sets the skill_ids of this ViewFilter.
        The skill ids are used to filter the view

        :param skill_ids: The skill_ids of this ViewFilter.
        :type: list[str]
        """
        
        self._skill_ids = skill_ids

    @property
    def skill_groups(self):
        """
        Gets the skill_groups of this ViewFilter.
        The skill groups used to filter the view

        :return: The skill_groups of this ViewFilter.
        :rtype: list[str]
        """
        return self._skill_groups

    @skill_groups.setter
    def skill_groups(self, skill_groups):
        """
        Sets the skill_groups of this ViewFilter.
        The skill groups used to filter the view

        :param skill_groups: The skill_groups of this ViewFilter.
        :type: list[str]
        """
        
        self._skill_groups = skill_groups

    @property
    def language_ids(self):
        """
        Gets the language_ids of this ViewFilter.
        The language ids are used to filter the view

        :return: The language_ids of this ViewFilter.
        :rtype: list[str]
        """
        return self._language_ids

    @language_ids.setter
    def language_ids(self, language_ids):
        """
        Sets the language_ids of this ViewFilter.
        The language ids are used to filter the view

        :param language_ids: The language_ids of this ViewFilter.
        :type: list[str]
        """
        
        self._language_ids = language_ids

    @property
    def language_groups(self):
        """
        Gets the language_groups of this ViewFilter.
        The language groups used to filter the view

        :return: The language_groups of this ViewFilter.
        :rtype: list[str]
        """
        return self._language_groups

    @language_groups.setter
    def language_groups(self, language_groups):
        """
        Sets the language_groups of this ViewFilter.
        The language groups used to filter the view

        :param language_groups: The language_groups of this ViewFilter.
        :type: list[str]
        """
        
        self._language_groups = language_groups

    @property
    def directions(self):
        """
        Gets the directions of this ViewFilter.
        The directions are used to filter the view

        :return: The directions of this ViewFilter.
        :rtype: list[str]
        """
        return self._directions

    @directions.setter
    def directions(self, directions):
        """
        Sets the directions of this ViewFilter.
        The directions are used to filter the view

        :param directions: The directions of this ViewFilter.
        :type: list[str]
        """
        
        self._directions = directions

    @property
    def wrap_up_codes(self):
        """
        Gets the wrap_up_codes of this ViewFilter.
        The wrap up codes are used to filter the view

        :return: The wrap_up_codes of this ViewFilter.
        :rtype: list[str]
        """
        return self._wrap_up_codes

    @wrap_up_codes.setter
    def wrap_up_codes(self, wrap_up_codes):
        """
        Sets the wrap_up_codes of this ViewFilter.
        The wrap up codes are used to filter the view

        :param wrap_up_codes: The wrap_up_codes of this ViewFilter.
        :type: list[str]
        """
        
        self._wrap_up_codes = wrap_up_codes

    @property
    def dnis_list(self):
        """
        Gets the dnis_list of this ViewFilter.
        The dnis list is used to filter the view

        :return: The dnis_list of this ViewFilter.
        :rtype: list[str]
        """
        return self._dnis_list

    @dnis_list.setter
    def dnis_list(self, dnis_list):
        """
        Sets the dnis_list of this ViewFilter.
        The dnis list is used to filter the view

        :param dnis_list: The dnis_list of this ViewFilter.
        :type: list[str]
        """
        
        self._dnis_list = dnis_list

    @property
    def user_ids(self):
        """
        Gets the user_ids of this ViewFilter.
        The user ids are used to filter the view

        :return: The user_ids of this ViewFilter.
        :rtype: list[str]
        """
        return self._user_ids

    @user_ids.setter
    def user_ids(self, user_ids):
        """
        Sets the user_ids of this ViewFilter.
        The user ids are used to filter the view

        :param user_ids: The user_ids of this ViewFilter.
        :type: list[str]
        """
        
        self._user_ids = user_ids

    @property
    def address_tos(self):
        """
        Gets the address_tos of this ViewFilter.
        The address To values are used to filter the view

        :return: The address_tos of this ViewFilter.
        :rtype: list[str]
        """
        return self._address_tos

    @address_tos.setter
    def address_tos(self, address_tos):
        """
        Sets the address_tos of this ViewFilter.
        The address To values are used to filter the view

        :param address_tos: The address_tos of this ViewFilter.
        :type: list[str]
        """
        
        self._address_tos = address_tos

    @property
    def address_froms(self):
        """
        Gets the address_froms of this ViewFilter.
        The address from values are used to filter the view

        :return: The address_froms of this ViewFilter.
        :rtype: list[str]
        """
        return self._address_froms

    @address_froms.setter
    def address_froms(self, address_froms):
        """
        Sets the address_froms of this ViewFilter.
        The address from values are used to filter the view

        :param address_froms: The address_froms of this ViewFilter.
        :type: list[str]
        """
        
        self._address_froms = address_froms

    @property
    def outbound_campaign_ids(self):
        """
        Gets the outbound_campaign_ids of this ViewFilter.
        The outbound campaign ids are used to filter the view

        :return: The outbound_campaign_ids of this ViewFilter.
        :rtype: list[str]
        """
        return self._outbound_campaign_ids

    @outbound_campaign_ids.setter
    def outbound_campaign_ids(self, outbound_campaign_ids):
        """
        Sets the outbound_campaign_ids of this ViewFilter.
        The outbound campaign ids are used to filter the view

        :param outbound_campaign_ids: The outbound_campaign_ids of this ViewFilter.
        :type: list[str]
        """
        
        self._outbound_campaign_ids = outbound_campaign_ids

    @property
    def outbound_contact_list_ids(self):
        """
        Gets the outbound_contact_list_ids of this ViewFilter.
        The outbound contact list ids are used to filter the view

        :return: The outbound_contact_list_ids of this ViewFilter.
        :rtype: list[str]
        """
        return self._outbound_contact_list_ids

    @outbound_contact_list_ids.setter
    def outbound_contact_list_ids(self, outbound_contact_list_ids):
        """
        Sets the outbound_contact_list_ids of this ViewFilter.
        The outbound contact list ids are used to filter the view

        :param outbound_contact_list_ids: The outbound_contact_list_ids of this ViewFilter.
        :type: list[str]
        """
        
        self._outbound_contact_list_ids = outbound_contact_list_ids

    @property
    def contact_ids(self):
        """
        Gets the contact_ids of this ViewFilter.
        The contact ids are used to filter the view

        :return: The contact_ids of this ViewFilter.
        :rtype: list[str]
        """
        return self._contact_ids

    @contact_ids.setter
    def contact_ids(self, contact_ids):
        """
        Sets the contact_ids of this ViewFilter.
        The contact ids are used to filter the view

        :param contact_ids: The contact_ids of this ViewFilter.
        :type: list[str]
        """
        
        self._contact_ids = contact_ids

    @property
    def ani_list(self):
        """
        Gets the ani_list of this ViewFilter.
        The ani list ids are used to filter the view

        :return: The ani_list of this ViewFilter.
        :rtype: list[str]
        """
        return self._ani_list

    @ani_list.setter
    def ani_list(self, ani_list):
        """
        Sets the ani_list of this ViewFilter.
        The ani list ids are used to filter the view

        :param ani_list: The ani_list of this ViewFilter.
        :type: list[str]
        """
        
        self._ani_list = ani_list

    @property
    def durations_milliseconds(self):
        """
        Gets the durations_milliseconds of this ViewFilter.
        The durations in milliseconds used to filter the view

        :return: The durations_milliseconds of this ViewFilter.
        :rtype: list[NumericRange]
        """
        return self._durations_milliseconds

    @durations_milliseconds.setter
    def durations_milliseconds(self, durations_milliseconds):
        """
        Sets the durations_milliseconds of this ViewFilter.
        The durations in milliseconds used to filter the view

        :param durations_milliseconds: The durations_milliseconds of this ViewFilter.
        :type: list[NumericRange]
        """
        
        self._durations_milliseconds = durations_milliseconds

    @property
    def evaluation_score(self):
        """
        Gets the evaluation_score of this ViewFilter.
        The evaluationScore is used to filter the view

        :return: The evaluation_score of this ViewFilter.
        :rtype: NumericRange
        """
        return self._evaluation_score

    @evaluation_score.setter
    def evaluation_score(self, evaluation_score):
        """
        Sets the evaluation_score of this ViewFilter.
        The evaluationScore is used to filter the view

        :param evaluation_score: The evaluation_score of this ViewFilter.
        :type: NumericRange
        """
        
        self._evaluation_score = evaluation_score

    @property
    def evaluation_critical_score(self):
        """
        Gets the evaluation_critical_score of this ViewFilter.
        The evaluationCriticalScore is used to filter the view

        :return: The evaluation_critical_score of this ViewFilter.
        :rtype: NumericRange
        """
        return self._evaluation_critical_score

    @evaluation_critical_score.setter
    def evaluation_critical_score(self, evaluation_critical_score):
        """
        Sets the evaluation_critical_score of this ViewFilter.
        The evaluationCriticalScore is used to filter the view

        :param evaluation_critical_score: The evaluation_critical_score of this ViewFilter.
        :type: NumericRange
        """
        
        self._evaluation_critical_score = evaluation_critical_score

    @property
    def evaluation_form_ids(self):
        """
        Gets the evaluation_form_ids of this ViewFilter.
        The evaluation form ids are used to filter the view

        :return: The evaluation_form_ids of this ViewFilter.
        :rtype: list[str]
        """
        return self._evaluation_form_ids

    @evaluation_form_ids.setter
    def evaluation_form_ids(self, evaluation_form_ids):
        """
        Sets the evaluation_form_ids of this ViewFilter.
        The evaluation form ids are used to filter the view

        :param evaluation_form_ids: The evaluation_form_ids of this ViewFilter.
        :type: list[str]
        """
        
        self._evaluation_form_ids = evaluation_form_ids

    @property
    def evaluated_agent_ids(self):
        """
        Gets the evaluated_agent_ids of this ViewFilter.
        The evaluated agent ids are used to filter the view

        :return: The evaluated_agent_ids of this ViewFilter.
        :rtype: list[str]
        """
        return self._evaluated_agent_ids

    @evaluated_agent_ids.setter
    def evaluated_agent_ids(self, evaluated_agent_ids):
        """
        Sets the evaluated_agent_ids of this ViewFilter.
        The evaluated agent ids are used to filter the view

        :param evaluated_agent_ids: The evaluated_agent_ids of this ViewFilter.
        :type: list[str]
        """
        
        self._evaluated_agent_ids = evaluated_agent_ids

    @property
    def evaluator_ids(self):
        """
        Gets the evaluator_ids of this ViewFilter.
        The evaluator ids are used to filter the view

        :return: The evaluator_ids of this ViewFilter.
        :rtype: list[str]
        """
        return self._evaluator_ids

    @evaluator_ids.setter
    def evaluator_ids(self, evaluator_ids):
        """
        Sets the evaluator_ids of this ViewFilter.
        The evaluator ids are used to filter the view

        :param evaluator_ids: The evaluator_ids of this ViewFilter.
        :type: list[str]
        """
        
        self._evaluator_ids = evaluator_ids

    @property
    def transferred(self):
        """
        Gets the transferred of this ViewFilter.
        Indicates filtering for transfers

        :return: The transferred of this ViewFilter.
        :rtype: bool
        """
        return self._transferred

    @transferred.setter
    def transferred(self, transferred):
        """
        Sets the transferred of this ViewFilter.
        Indicates filtering for transfers

        :param transferred: The transferred of this ViewFilter.
        :type: bool
        """
        
        self._transferred = transferred

    @property
    def abandoned(self):
        """
        Gets the abandoned of this ViewFilter.
        Indicates filtering for abandons

        :return: The abandoned of this ViewFilter.
        :rtype: bool
        """
        return self._abandoned

    @abandoned.setter
    def abandoned(self, abandoned):
        """
        Sets the abandoned of this ViewFilter.
        Indicates filtering for abandons

        :param abandoned: The abandoned of this ViewFilter.
        :type: bool
        """
        
        self._abandoned = abandoned

    @property
    def message_types(self):
        """
        Gets the message_types of this ViewFilter.
        The message media types used to filter the view

        :return: The message_types of this ViewFilter.
        :rtype: list[str]
        """
        return self._message_types

    @message_types.setter
    def message_types(self, message_types):
        """
        Sets the message_types of this ViewFilter.
        The message media types used to filter the view

        :param message_types: The message_types of this ViewFilter.
        :type: list[str]
        """
        
        self._message_types = message_types

    @property
    def division_ids(self):
        """
        Gets the division_ids of this ViewFilter.
        The divison Ids used to filter the view

        :return: The division_ids of this ViewFilter.
        :rtype: list[str]
        """
        return self._division_ids

    @division_ids.setter
    def division_ids(self, division_ids):
        """
        Sets the division_ids of this ViewFilter.
        The divison Ids used to filter the view

        :param division_ids: The division_ids of this ViewFilter.
        :type: list[str]
        """
        
        self._division_ids = division_ids

    @property
    def survey_form_ids(self):
        """
        Gets the survey_form_ids of this ViewFilter.
        The survey form ids used to filter the view

        :return: The survey_form_ids of this ViewFilter.
        :rtype: list[str]
        """
        return self._survey_form_ids

    @survey_form_ids.setter
    def survey_form_ids(self, survey_form_ids):
        """
        Sets the survey_form_ids of this ViewFilter.
        The survey form ids used to filter the view

        :param survey_form_ids: The survey_form_ids of this ViewFilter.
        :type: list[str]
        """
        
        self._survey_form_ids = survey_form_ids

    @property
    def survey_total_score(self):
        """
        Gets the survey_total_score of this ViewFilter.
        The survey total score used to filter the view

        :return: The survey_total_score of this ViewFilter.
        :rtype: NumericRange
        """
        return self._survey_total_score

    @survey_total_score.setter
    def survey_total_score(self, survey_total_score):
        """
        Sets the survey_total_score of this ViewFilter.
        The survey total score used to filter the view

        :param survey_total_score: The survey_total_score of this ViewFilter.
        :type: NumericRange
        """
        
        self._survey_total_score = survey_total_score

    @property
    def survey_nps_score(self):
        """
        Gets the survey_nps_score of this ViewFilter.
        The survey NPS score used to filter the view

        :return: The survey_nps_score of this ViewFilter.
        :rtype: NumericRange
        """
        return self._survey_nps_score

    @survey_nps_score.setter
    def survey_nps_score(self, survey_nps_score):
        """
        Sets the survey_nps_score of this ViewFilter.
        The survey NPS score used to filter the view

        :param survey_nps_score: The survey_nps_score of this ViewFilter.
        :type: NumericRange
        """
        
        self._survey_nps_score = survey_nps_score

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

