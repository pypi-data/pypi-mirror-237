# coding: utf-8

"""
    Pulp 3 API

    Fetch, Upload, Organize, and Distribute Software Packages  # noqa: E501

    The version of the OpenAPI document: v3
    Contact: pulp-list@redhat.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from pulpcore.client.pulp_ansible.api_client import ApiClient
from pulpcore.client.pulp_ansible.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class VersionsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def api_v1_roles_versions_list(self, ansible_role_href,  **kwargs):  # noqa: E501
        """api_v1_roles_versions_list  # noqa: E501

        APIView for Role Versions.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_v1_roles_versions_list(ansible_role_href, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str ansible_role_href: (required)
        :param int limit: Number of results to return per page.
        :param int offset: The initial index from which to return the results.
        :param list[str] fields: A list of fields to include in the response.
        :param list[str] exclude_fields: A list of fields to exclude from the response.
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: PaginatedGalaxyRoleVersionResponseList
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.api_v1_roles_versions_list_with_http_info(ansible_role_href,  **kwargs)  # noqa: E501

    def api_v1_roles_versions_list_with_http_info(self, ansible_role_href,  **kwargs):  # noqa: E501
        """api_v1_roles_versions_list  # noqa: E501

        APIView for Role Versions.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_v1_roles_versions_list_with_http_info(ansible_role_href, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str ansible_role_href: (required)
        :param int limit: Number of results to return per page.
        :param int offset: The initial index from which to return the results.
        :param list[str] fields: A list of fields to include in the response.
        :param list[str] exclude_fields: A list of fields to exclude from the response.
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(PaginatedGalaxyRoleVersionResponseList, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'ansible_role_href',
            'limit',
            'offset',
            'fields',
            'exclude_fields'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method api_v1_roles_versions_list" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'ansible_role_href' is set
        if self.api_client.client_side_validation and ('ansible_role_href' not in local_var_params or  # noqa: E501
                                                        local_var_params['ansible_role_href'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `ansible_role_href` when calling `api_v1_roles_versions_list`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'ansible_role_href' in local_var_params:
            path_params['ansible_role_href'] = local_var_params['ansible_role_href']  # noqa: E501

        query_params = []
        if 'limit' in local_var_params and local_var_params['limit'] is not None:  # noqa: E501
            query_params.append(('limit', local_var_params['limit']))  # noqa: E501
        if 'offset' in local_var_params and local_var_params['offset'] is not None:  # noqa: E501
            query_params.append(('offset', local_var_params['offset']))  # noqa: E501
        if 'fields' in local_var_params and local_var_params['fields'] is not None:  # noqa: E501
            query_params.append(('fields', local_var_params['fields']))  # noqa: E501
            collection_formats['fields'] = 'multi'  # noqa: E501
        if 'exclude_fields' in local_var_params and local_var_params['exclude_fields'] is not None:  # noqa: E501
            query_params.append(('exclude_fields', local_var_params['exclude_fields']))  # noqa: E501
            collection_formats['exclude_fields'] = 'multi'  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '{ansible_role_href}versions/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PaginatedGalaxyRoleVersionResponseList',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def api_v2_collection_versions_list(self, ansible_collection_version_href,  **kwargs):  # noqa: E501
        """api_v2_collection_versions_list  # noqa: E501

        APIView for Collections by namespace/name.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_v2_collection_versions_list(ansible_collection_version_href, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str ansible_collection_version_href: (required)
        :param int page: A page number within the paginated result set.
        :param list[str] fields: A list of fields to include in the response.
        :param list[str] exclude_fields: A list of fields to exclude from the response.
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: PaginatedGalaxyCollectionVersionResponseList
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.api_v2_collection_versions_list_with_http_info(ansible_collection_version_href,  **kwargs)  # noqa: E501

    def api_v2_collection_versions_list_with_http_info(self, ansible_collection_version_href,  **kwargs):  # noqa: E501
        """api_v2_collection_versions_list  # noqa: E501

        APIView for Collections by namespace/name.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_v2_collection_versions_list_with_http_info(ansible_collection_version_href, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str ansible_collection_version_href: (required)
        :param int page: A page number within the paginated result set.
        :param list[str] fields: A list of fields to include in the response.
        :param list[str] exclude_fields: A list of fields to exclude from the response.
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(PaginatedGalaxyCollectionVersionResponseList, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'ansible_collection_version_href',
            'page',
            'fields',
            'exclude_fields'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method api_v2_collection_versions_list" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'ansible_collection_version_href' is set
        if self.api_client.client_side_validation and ('ansible_collection_version_href' not in local_var_params or  # noqa: E501
                                                        local_var_params['ansible_collection_version_href'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `ansible_collection_version_href` when calling `api_v2_collection_versions_list`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'ansible_collection_version_href' in local_var_params:
            path_params['ansible_collection_version_href'] = local_var_params['ansible_collection_version_href']  # noqa: E501

        query_params = []
        if 'page' in local_var_params and local_var_params['page'] is not None:  # noqa: E501
            query_params.append(('page', local_var_params['page']))  # noqa: E501
        if 'fields' in local_var_params and local_var_params['fields'] is not None:  # noqa: E501
            query_params.append(('fields', local_var_params['fields']))  # noqa: E501
            collection_formats['fields'] = 'multi'  # noqa: E501
        if 'exclude_fields' in local_var_params and local_var_params['exclude_fields'] is not None:  # noqa: E501
            query_params.append(('exclude_fields', local_var_params['exclude_fields']))  # noqa: E501
            collection_formats['exclude_fields'] = 'multi'  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '{ansible_collection_version_href}versions/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PaginatedGalaxyCollectionVersionResponseList',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
