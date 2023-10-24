# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.pod_affinity_term import PodAffinityTerm
from openapi_server.models.weighted_pod_affinity_term import WeightedPodAffinityTerm
from openapi_server import util

from openapi_server.models.pod_affinity_term import PodAffinityTerm  # noqa: E501
from openapi_server.models.weighted_pod_affinity_term import WeightedPodAffinityTerm  # noqa: E501

class PodAffinity(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, required_during_scheduling_ignored_during_execution=None, preferred_during_scheduling_ignored_during_execution=None):  # noqa: E501
        """PodAffinity - a model defined in OpenAPI

        :param required_during_scheduling_ignored_during_execution: The required_during_scheduling_ignored_during_execution of this PodAffinity.  # noqa: E501
        :type required_during_scheduling_ignored_during_execution: List[PodAffinityTerm]
        :param preferred_during_scheduling_ignored_during_execution: The preferred_during_scheduling_ignored_during_execution of this PodAffinity.  # noqa: E501
        :type preferred_during_scheduling_ignored_during_execution: List[WeightedPodAffinityTerm]
        """
        self.openapi_types = {
            'required_during_scheduling_ignored_during_execution': List[PodAffinityTerm],
            'preferred_during_scheduling_ignored_during_execution': List[WeightedPodAffinityTerm]
        }

        self.attribute_map = {
            'required_during_scheduling_ignored_during_execution': 'required_during_scheduling_ignored_during_execution',
            'preferred_during_scheduling_ignored_during_execution': 'preferred_during_scheduling_ignored_during_execution'
        }

        self._required_during_scheduling_ignored_during_execution = required_during_scheduling_ignored_during_execution
        self._preferred_during_scheduling_ignored_during_execution = preferred_during_scheduling_ignored_during_execution

    @classmethod
    def from_dict(cls, dikt) -> 'PodAffinity':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The PodAffinity of this PodAffinity.  # noqa: E501
        :rtype: PodAffinity
        """
        return util.deserialize_model(dikt, cls)

    @property
    def required_during_scheduling_ignored_during_execution(self):
        """Gets the required_during_scheduling_ignored_during_execution of this PodAffinity.


        :return: The required_during_scheduling_ignored_during_execution of this PodAffinity.
        :rtype: List[PodAffinityTerm]
        """
        return self._required_during_scheduling_ignored_during_execution

    @required_during_scheduling_ignored_during_execution.setter
    def required_during_scheduling_ignored_during_execution(self, required_during_scheduling_ignored_during_execution):
        """Sets the required_during_scheduling_ignored_during_execution of this PodAffinity.


        :param required_during_scheduling_ignored_during_execution: The required_during_scheduling_ignored_during_execution of this PodAffinity.
        :type required_during_scheduling_ignored_during_execution: List[PodAffinityTerm]
        """

        self._required_during_scheduling_ignored_during_execution = required_during_scheduling_ignored_during_execution

    @property
    def preferred_during_scheduling_ignored_during_execution(self):
        """Gets the preferred_during_scheduling_ignored_during_execution of this PodAffinity.


        :return: The preferred_during_scheduling_ignored_during_execution of this PodAffinity.
        :rtype: List[WeightedPodAffinityTerm]
        """
        return self._preferred_during_scheduling_ignored_during_execution

    @preferred_during_scheduling_ignored_during_execution.setter
    def preferred_during_scheduling_ignored_during_execution(self, preferred_during_scheduling_ignored_during_execution):
        """Sets the preferred_during_scheduling_ignored_during_execution of this PodAffinity.


        :param preferred_during_scheduling_ignored_during_execution: The preferred_during_scheduling_ignored_during_execution of this PodAffinity.
        :type preferred_during_scheduling_ignored_during_execution: List[WeightedPodAffinityTerm]
        """

        self._preferred_during_scheduling_ignored_during_execution = preferred_during_scheduling_ignored_during_execution
