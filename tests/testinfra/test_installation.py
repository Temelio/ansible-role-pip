"""
Role tests
"""
import pytest

# To run all the tests on given docker images:
pytestmark = pytest.mark.docker_images(
    'infopen/ubuntu-trusty-ssh:0.1.0',
    'infopen/ubuntu-xenial-ssh-py27:0.2.0'
)


def test_install_on_debian_family(Package, SystemInfo):
    """
    Test package installation on Debian family
    """

    if SystemInfo.distribution not in ['debian', 'ubuntu']:
        pytest.skip('Not apply to %s' % SystemInfo.distribution)

    assert Package('python-pip').is_installed
