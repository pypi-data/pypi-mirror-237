# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.ingress_rule import IngressRule
from openapi_server.models.ingress_tls import IngressTLS
from openapi_server import util

from openapi_server.models.ingress_rule import IngressRule  # noqa: E501
from openapi_server.models.ingress_tls import IngressTLS  # noqa: E501

class Ingress(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, name=None, namespace=None, annotations=None, labels=None, rules=None, tls=None):  # noqa: E501
        """Ingress - a model defined in OpenAPI

        :param name: The name of this Ingress.  # noqa: E501
        :type name: str
        :param namespace: The namespace of this Ingress.  # noqa: E501
        :type namespace: str
        :param annotations: The annotations of this Ingress.  # noqa: E501
        :type annotations: List[str]
        :param labels: The labels of this Ingress.  # noqa: E501
        :type labels: List[str]
        :param rules: The rules of this Ingress.  # noqa: E501
        :type rules: List[IngressRule]
        :param tls: The tls of this Ingress.  # noqa: E501
        :type tls: List[IngressTLS]
        """
        self.openapi_types = {
            'name': str,
            'namespace': str,
            'annotations': List[str],
            'labels': List[str],
            'rules': List[IngressRule],
            'tls': List[IngressTLS]
        }

        self.attribute_map = {
            'name': 'name',
            'namespace': 'namespace',
            'annotations': 'annotations',
            'labels': 'labels',
            'rules': 'rules',
            'tls': 'tls'
        }

        self._name = name
        self._namespace = namespace
        self._annotations = annotations
        self._labels = labels
        self._rules = rules
        self._tls = tls

    @classmethod
    def from_dict(cls, dikt) -> 'Ingress':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Ingress of this Ingress.  # noqa: E501
        :rtype: Ingress
        """
        return util.deserialize_model(dikt, cls)

    @property
    def name(self):
        """Gets the name of this Ingress.

        ingress name.  # noqa: E501

        :return: The name of this Ingress.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Ingress.

        ingress name.  # noqa: E501

        :param name: The name of this Ingress.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def namespace(self):
        """Gets the namespace of this Ingress.

        namespace for resource.  # noqa: E501

        :return: The namespace of this Ingress.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """Sets the namespace of this Ingress.

        namespace for resource.  # noqa: E501

        :param namespace: The namespace of this Ingress.
        :type namespace: str
        """

        self._namespace = namespace

    @property
    def annotations(self):
        """Gets the annotations of this Ingress.

        An unstructured key value map that can be used to attach arbitrary metadata  # noqa: E501

        :return: The annotations of this Ingress.
        :rtype: List[str]
        """
        return self._annotations

    @annotations.setter
    def annotations(self, annotations):
        """Sets the annotations of this Ingress.

        An unstructured key value map that can be used to attach arbitrary metadata  # noqa: E501

        :param annotations: The annotations of this Ingress.
        :type annotations: List[str]
        """

        self._annotations = annotations

    @property
    def labels(self):
        """Gets the labels of this Ingress.

        Map of string keys and values that can be used to organize and categorize (scope and select) objects  # noqa: E501

        :return: The labels of this Ingress.
        :rtype: List[str]
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        """Sets the labels of this Ingress.

        Map of string keys and values that can be used to organize and categorize (scope and select) objects  # noqa: E501

        :param labels: The labels of this Ingress.
        :type labels: List[str]
        """

        self._labels = labels

    @property
    def rules(self):
        """Gets the rules of this Ingress.


        :return: The rules of this Ingress.
        :rtype: List[IngressRule]
        """
        return self._rules

    @rules.setter
    def rules(self, rules):
        """Sets the rules of this Ingress.


        :param rules: The rules of this Ingress.
        :type rules: List[IngressRule]
        """

        self._rules = rules

    @property
    def tls(self):
        """Gets the tls of this Ingress.


        :return: The tls of this Ingress.
        :rtype: List[IngressTLS]
        """
        return self._tls

    @tls.setter
    def tls(self, tls):
        """Sets the tls of this Ingress.


        :param tls: The tls of this Ingress.
        :type tls: List[IngressTLS]
        """

        self._tls = tls
