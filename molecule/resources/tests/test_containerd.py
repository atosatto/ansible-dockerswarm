import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_containerd_installed(host):

    assert host.package('containerd.io').is_installed


def test_containerd_service(host):

    s = host.service('containerd')
    assert s.is_running
    assert s.is_enabled
