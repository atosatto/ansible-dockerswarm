import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')

debian_os = ['debian', 'ubuntu']
rhel_os = ['redhat', 'centos']


def test_docker_ce_config(host):

    d = host.file('/etc/docker')
    assert d.exists
    assert d.user == 'root'
    assert d.group == 'root'
    assert d.mode == 0o755

    f = host.file('/etc/docker/daemon.json')
    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'
    assert f.mode == 0o640


def test_docker_ce_stable_repository_exists(host):

    f = None
    if host.system_info.distribution.lower() in debian_os:
        f = host.file('/etc/apt/sources.list.d/docker_ce_stable.list')
    if host.system_info.distribution.lower() in rhel_os:
        f = host.file('/etc/yum.repos.d/docker_ce_stable.repo')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'
    assert f.mode == 0o644


def test_docker_ce_installed(host):

    assert host.package('docker-ce').is_installed


def test_docker_ce_service(host):

    s = host.service('docker')
    assert s.is_running
    assert s.is_enabled
