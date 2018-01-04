"""
Role tests
"""

import os
import pytest

from testinfra.utils.ansible_runner import AnsibleRunner

testinfra_hosts = AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_install_on_debian_family(host):
    """
    Test package installation on Debian family
    """

    if host.system_info.distribution not in ['debian', 'ubuntu']:
        pytest.skip('Not apply to %s' % host.system_info.distribution)

    assert host.package('python-pip').is_installed
