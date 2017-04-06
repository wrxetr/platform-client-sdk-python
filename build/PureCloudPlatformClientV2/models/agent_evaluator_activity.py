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


class AgentEvaluatorActivity(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        AgentEvaluatorActivity - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'name': 'str',
            'agent': 'User',
            'evaluator': 'User',
            'num_evaluations': 'int',
            'average_evaluation_score': 'int',
            'self_uri': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'agent': 'agent',
            'evaluator': 'evaluator',
            'num_evaluations': 'numEvaluations',
            'average_evaluation_score': 'averageEvaluationScore',
            'self_uri': 'selfUri'
        }

        self._id = None
        self._name = None
        self._agent = None
        self._evaluator = None
        self._num_evaluations = None
        self._average_evaluation_score = None
        self._self_uri = None

    @property
    def id(self):
        """
        Gets the id of this AgentEvaluatorActivity.
        The globally unique identifier for the object.

        :return: The id of this AgentEvaluatorActivity.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this AgentEvaluatorActivity.
        The globally unique identifier for the object.

        :param id: The id of this AgentEvaluatorActivity.
        :type: str
        """
        
        self._id = id

    @property
    def name(self):
        """
        Gets the name of this AgentEvaluatorActivity.


        :return: The name of this AgentEvaluatorActivity.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this AgentEvaluatorActivity.


        :param name: The name of this AgentEvaluatorActivity.
        :type: str
        """
        
        self._name = name

    @property
    def agent(self):
        """
        Gets the agent of this AgentEvaluatorActivity.


        :return: The agent of this AgentEvaluatorActivity.
        :rtype: User
        """
        return self._agent

    @agent.setter
    def agent(self, agent):
        """
        Sets the agent of this AgentEvaluatorActivity.


        :param agent: The agent of this AgentEvaluatorActivity.
        :type: User
        """
        
        self._agent = agent

    @property
    def evaluator(self):
        """
        Gets the evaluator of this AgentEvaluatorActivity.


        :return: The evaluator of this AgentEvaluatorActivity.
        :rtype: User
        """
        return self._evaluator

    @evaluator.setter
    def evaluator(self, evaluator):
        """
        Sets the evaluator of this AgentEvaluatorActivity.


        :param evaluator: The evaluator of this AgentEvaluatorActivity.
        :type: User
        """
        
        self._evaluator = evaluator

    @property
    def num_evaluations(self):
        """
        Gets the num_evaluations of this AgentEvaluatorActivity.


        :return: The num_evaluations of this AgentEvaluatorActivity.
        :rtype: int
        """
        return self._num_evaluations

    @num_evaluations.setter
    def num_evaluations(self, num_evaluations):
        """
        Sets the num_evaluations of this AgentEvaluatorActivity.


        :param num_evaluations: The num_evaluations of this AgentEvaluatorActivity.
        :type: int
        """
        
        self._num_evaluations = num_evaluations

    @property
    def average_evaluation_score(self):
        """
        Gets the average_evaluation_score of this AgentEvaluatorActivity.


        :return: The average_evaluation_score of this AgentEvaluatorActivity.
        :rtype: int
        """
        return self._average_evaluation_score

    @average_evaluation_score.setter
    def average_evaluation_score(self, average_evaluation_score):
        """
        Sets the average_evaluation_score of this AgentEvaluatorActivity.


        :param average_evaluation_score: The average_evaluation_score of this AgentEvaluatorActivity.
        :type: int
        """
        
        self._average_evaluation_score = average_evaluation_score

    @property
    def self_uri(self):
        """
        Gets the self_uri of this AgentEvaluatorActivity.
        The URI for this object

        :return: The self_uri of this AgentEvaluatorActivity.
        :rtype: str
        """
        return self._self_uri

    @self_uri.setter
    def self_uri(self, self_uri):
        """
        Sets the self_uri of this AgentEvaluatorActivity.
        The URI for this object

        :param self_uri: The self_uri of this AgentEvaluatorActivity.
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

