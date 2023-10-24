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
from pulpcore.client.pulp_ansible.models.ansible_collection_version_mark_response import AnsibleCollectionVersionMarkResponse  # noqa: E501
from pulpcore.client.pulp_ansible.rest import ApiException

class TestAnsibleCollectionVersionMarkResponse(unittest.TestCase):
    """AnsibleCollectionVersionMarkResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test AnsibleCollectionVersionMarkResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = pulpcore.client.pulp_ansible.models.ansible_collection_version_mark_response.AnsibleCollectionVersionMarkResponse()  # noqa: E501
        if include_optional :
            return AnsibleCollectionVersionMarkResponse(
                pulp_created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                pulp_href = '0', 
                marked_collection = '0', 
                value = 'a'
            )
        else :
            return AnsibleCollectionVersionMarkResponse(
                marked_collection = '0',
                value = 'a',
        )

    def testAnsibleCollectionVersionMarkResponse(self):
        """Test AnsibleCollectionVersionMarkResponse"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
