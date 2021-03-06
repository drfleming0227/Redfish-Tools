# Copyright Notice:
# Copyright 2018 Distributed Management Task Force, Inc. All rights reserved.
# License: BSD 3-Clause License. For full text see link: https://github.com/DMTF/Redfish-Tools/blob/master/LICENSE.md

"""
File: test_version_added.py

Brief: test(s) for correct detection of "Version Added".
"""

import os
import copy
from unittest.mock import patch
import pytest
from doc_generator import DocGenerator
from .discrepancy_list import DiscrepancyList

testcase_path = os.path.join('tests', 'samples')

base_config = {
    'expand_defs_from_non_output_schemas': False,
    'excluded_by_match': ['@odata.count', '@odata.navigationLink'],
    'profile_resources': {},
    'units_translation': {},
    'excluded_annotations_by_match': ['@odata.count', '@odata.navigationLink'],
    'excluded_schemas': [],
    'excluded_properties': ['@odata.id', '@odata.context', '@odata.type'],
    'uri_replacements': {},

    'profile': {},
    'escape_chars': [],

    'output_format': 'markdown',
}

@patch('urllib.request') # so we don't make HTTP requests. NB: samples should not call for outside resources.
def test_version_added_metadata(mockRequest):
    """ Verify metadata contains expected version_added info.
    Note that there is an additional step, after generating this metadata, for generating metadata
    within property data ... so possibly this test should be replaced.
    """

    config = copy.deepcopy(base_config)
    input_dir = os.path.abspath(os.path.join(testcase_path, 'version_added', 'AccountService'))

    # This is a partial list of versions that should be detected.
    expected_versions = {
        'AccountLockoutThreshold': {},
        'LDAP': {'version': '1.3.0'},
        'LocalAccountAuth': {'version': '1.3.0'},
        'PrivilegeMap': {'version': '1.1.0'},
        'Actions': {'version': '1.2.0',
                    'Oem': { 'version': '1.2.0'},
                    },
        'AdditionalExternalAccountProviders': { 'version': '1.3.0' },
        'definitions': { 'AccountProviderTypes': {'enum': {'ActiveDirectoryService': {'version': '1.3.0'},
                                                           'RedfishService': {'version': '1.3.0'},
                                                           'OEM': {'version': '1.3.0'},
                                                           'LDAPService': {'version': '1.3.0'},
                                                           },
                                                  'version': '1.3.0',
                                                  },
                         # WORKAROUND for properties incorrectly included in errata versions:
                         # 'Actions': { 'version': '1.2.2',
                         #              'Oem': { 'version': '1.2.2' },
                         #              },
                         'Actions': { 'version': '1.3.0',
                                      'Oem': { 'version': '1.3.0' },
                                      },
                         'LDAPSearchSettings': { 'version': '1.3.0',
                                                 'BaseDistinguishedNames': {'version': '1.3.0'},
                                                 },
                         'AccountService': { 'LDAP': { 'version': '1.3.0' },
                                             'LocalAccountAuth': { 'version': '1.3.0' },
                                             'AccountLockoutThreshold': { },
                                             'PrivilegeMap': { 'version': '1.1.0'},
                                             'Actions': { 'version': '1.2.0' }
                                             },
                         }
        }

    config['uri_to_local'] = {'redfish.dmtf.org/schemas/v1': input_dir}
    config['local_to_uri'] = { input_dir : 'redfish.dmtf.org/schemas/v1'}

    docGen = DocGenerator([ input_dir ], '/dev/null', config)
    output = docGen.generate_docs()

    meta = docGen.property_data['redfish.dmtf.org/schemas/v1/AccountService.json']['doc_generator_meta']

    discrepancies = DiscrepancyList()
    for name, data in expected_versions.items():
        if name == 'version': continue
        _version_compare(meta, name, data, discrepancies, [])

    assert [] == discrepancies


def _version_compare(meta, name, data, discrepancies, context):

    context = copy.copy(context)
    context.append(name)

    key_meta = meta.get(name)
    if key_meta is None:
        discrepancies.append(' > '.join(context) + ' not found in metadata')

    else:
        if data.get('version', '1.0.0') != key_meta.get('version', '1.0.0'):
            discrepancies.append(' > '.join(context) + ' version is "' + key_meta.get('version', '(none)') + '", expected "'
                                 + data.get('version', '1.0.0') + '"')

        for childname, childdata in data.items():
            if childname == 'version': continue
            _version_compare(key_meta, childname, childdata, discrepancies, context)




@patch('urllib.request') # so we don't make HTTP requests. NB: samples should not call for outside resources.
def test_version_added_output_AccountService(mockRequest):
    """ Verify markdown output contains expected version_added info.
    This means pulling the correct version strings from the metadata
    """

    config = copy.deepcopy(base_config)
    input_dir = os.path.abspath(os.path.join(testcase_path, 'version_added', 'AccountService'))

    expected_version_strings = [ '**LDAP** *(v1.3+)*', '**LDAPService** {',
                                 '**LocalAccountAuth** *(v1.3+)*',
                                 '**PrivilegeMap** *(v1.1+)*', '**Actions** *(v1.2+)*'
                                 ]


    config['uri_to_local'] = {'redfish.dmtf.org/schemas/v1': input_dir}
    config['local_to_uri'] = { input_dir : 'redfish.dmtf.org/schemas/v1'}

    docGen = DocGenerator([ input_dir ], '/dev/null', config)
    output = docGen.generate_docs()
    discrepancies = DiscrepancyList()

    for expected in expected_version_strings:
        if expected not in output:
            discrepancies.append('"' + expected + '" not found')

    assert [] == discrepancies


@patch('urllib.request') # so we don't make HTTP requests. NB: samples should not call for outside resources.
def test_version_added_output_Chassis(mockRequest):
    """ Verify markdown output contains expected version_added info.
    This means pulling the correct version strings from the metadata.
    The Chassis example gave us some distinct scenarios.
    """

    config = copy.deepcopy(base_config)
    input_dir = os.path.abspath(os.path.join(testcase_path, 'version_added', 'Chassis'))

    expected_version_strings = ['| **Actions** { |', '| **Links** { |',  # string to match property without version
                                # WORKAROUND for properties incorrectly included in errata versions:
                                # '**PowerState** *(v1.0.1+)*'
                                '**PowerState** *(v1.1+)*']


    config['uri_to_local'] = {'redfish.dmtf.org/schemas/v1': input_dir}
    config['local_to_uri'] = { input_dir : 'redfish.dmtf.org/schemas/v1'}

    docGen = DocGenerator([ input_dir ], '/dev/null', config)
    output = docGen.generate_docs()
    discrepancies = DiscrepancyList()

    for expected in expected_version_strings:
        if expected not in output:
            discrepancies.append('"' + expected + '" not found')

    assert [] == discrepancies
