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

class SurveyQuestionGroupScore(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        SurveyQuestionGroupScore - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'question_group_id': 'str',
            'total_score': 'float',
            'max_total_score': 'float',
            'marked_na': 'bool',
            'question_scores': 'list[SurveyQuestionScore]'
        }

        self.attribute_map = {
            'question_group_id': 'questionGroupId',
            'total_score': 'totalScore',
            'max_total_score': 'maxTotalScore',
            'marked_na': 'markedNA',
            'question_scores': 'questionScores'
        }

        self._question_group_id = None
        self._total_score = None
        self._max_total_score = None
        self._marked_na = None
        self._question_scores = None

    @property
    def question_group_id(self):
        """
        Gets the question_group_id of this SurveyQuestionGroupScore.


        :return: The question_group_id of this SurveyQuestionGroupScore.
        :rtype: str
        """
        return self._question_group_id

    @question_group_id.setter
    def question_group_id(self, question_group_id):
        """
        Sets the question_group_id of this SurveyQuestionGroupScore.


        :param question_group_id: The question_group_id of this SurveyQuestionGroupScore.
        :type: str
        """
        
        self._question_group_id = question_group_id

    @property
    def total_score(self):
        """
        Gets the total_score of this SurveyQuestionGroupScore.


        :return: The total_score of this SurveyQuestionGroupScore.
        :rtype: float
        """
        return self._total_score

    @total_score.setter
    def total_score(self, total_score):
        """
        Sets the total_score of this SurveyQuestionGroupScore.


        :param total_score: The total_score of this SurveyQuestionGroupScore.
        :type: float
        """
        
        self._total_score = total_score

    @property
    def max_total_score(self):
        """
        Gets the max_total_score of this SurveyQuestionGroupScore.


        :return: The max_total_score of this SurveyQuestionGroupScore.
        :rtype: float
        """
        return self._max_total_score

    @max_total_score.setter
    def max_total_score(self, max_total_score):
        """
        Sets the max_total_score of this SurveyQuestionGroupScore.


        :param max_total_score: The max_total_score of this SurveyQuestionGroupScore.
        :type: float
        """
        
        self._max_total_score = max_total_score

    @property
    def marked_na(self):
        """
        Gets the marked_na of this SurveyQuestionGroupScore.


        :return: The marked_na of this SurveyQuestionGroupScore.
        :rtype: bool
        """
        return self._marked_na

    @marked_na.setter
    def marked_na(self, marked_na):
        """
        Sets the marked_na of this SurveyQuestionGroupScore.


        :param marked_na: The marked_na of this SurveyQuestionGroupScore.
        :type: bool
        """
        
        self._marked_na = marked_na

    @property
    def question_scores(self):
        """
        Gets the question_scores of this SurveyQuestionGroupScore.


        :return: The question_scores of this SurveyQuestionGroupScore.
        :rtype: list[SurveyQuestionScore]
        """
        return self._question_scores

    @question_scores.setter
    def question_scores(self, question_scores):
        """
        Sets the question_scores of this SurveyQuestionGroupScore.


        :param question_scores: The question_scores of this SurveyQuestionGroupScore.
        :type: list[SurveyQuestionScore]
        """
        
        self._question_scores = question_scores

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

