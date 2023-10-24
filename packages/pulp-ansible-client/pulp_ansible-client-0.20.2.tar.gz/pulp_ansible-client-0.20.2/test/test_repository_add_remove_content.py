# coding: utf-8

"""
    Pulp 3 API

    Fetch, Upload, Organize, and Distribute Software Packages  # noqa: E501

    The version of the OpenAPI document: v3
    Contact: pulp-list@redhat.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import pulpcore.client.pulp_ansible
from pulpcore.client.pulp_ansible.models.repository_add_remove_content import RepositoryAddRemoveContent  # noqa: E501
from pulpcore.client.pulp_ansible.rest import ApiException

class TestRepositoryAddRemoveContent(unittest.TestCase):
    """RepositoryAddRemoveContent unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test RepositoryAddRemoveContent
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = pulpcore.client.pulp_ansible.models.repository_add_remove_content.RepositoryAddRemoveContent()  # noqa: E501
        if include_optional :
            return RepositoryAddRemoveContent(
                add_content_units = [
                    '0'
                    ], 
                remove_content_units = [
                    '0'
                    ], 
                base_version = '0'
            )
        else :
            return RepositoryAddRemoveContent(
        )

    def testRepositoryAddRemoveContent(self):
        """Test RepositoryAddRemoveContent"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
