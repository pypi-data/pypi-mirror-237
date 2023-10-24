# coding: utf-8

"""
    Pulp 3 API

    Fetch, Upload, Organize, and Distribute Software Packages  # noqa: E501

    The version of the OpenAPI document: v3
    Contact: pulp-list@redhat.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from pulpcore.client.pulp_ansible.configuration import Configuration


class NamespaceLinkResponse(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'url': 'str',
        'name': 'str'
    }

    attribute_map = {
        'url': 'url',
        'name': 'name'
    }

    def __init__(self, url=None, name=None, local_vars_configuration=None):  # noqa: E501
        """NamespaceLinkResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._url = None
        self._name = None
        self.discriminator = None

        self.url = url
        self.name = name

    @property
    def url(self):
        """Gets the url of this NamespaceLinkResponse.  # noqa: E501


        :return: The url of this NamespaceLinkResponse.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this NamespaceLinkResponse.


        :param url: The url of this NamespaceLinkResponse.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and url is None:  # noqa: E501
            raise ValueError("Invalid value for `url`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                url is not None and len(url) > 256):
            raise ValueError("Invalid value for `url`, length must be less than or equal to `256`")  # noqa: E501

        self._url = url

    @property
    def name(self):
        """Gets the name of this NamespaceLinkResponse.  # noqa: E501


        :return: The name of this NamespaceLinkResponse.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this NamespaceLinkResponse.


        :param name: The name of this NamespaceLinkResponse.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) > 256):
            raise ValueError("Invalid value for `name`, length must be less than or equal to `256`")  # noqa: E501

        self._name = name

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, NamespaceLinkResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, NamespaceLinkResponse):
            return True

        return self.to_dict() != other.to_dict()
