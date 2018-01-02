import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    '.molecule/ansible_inventory.yml').get_hosts('all')

debian_os = ['debian', 'ubuntu']
rhel_os = ['redhat', 'centos']


def test_docker_repository_exists(host):

    f = None
    if host.system_info.distribution.lower() in debian_os:
        f = host.file('/etc/apt/sources.list.d/docker.list')
    if host.system_info.distribution.lower() in rhel_os:
        f = host.file('/etc/yum.repos.d/docker.repo')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'
    assert oct(f.mode) == '0644'


def test_docker_engine_installed(host):

    assert host.package('docker-engine').is_installed


def test_docker_service(host):

    # Testinfra fails on Ubuntu trying to use systemd to get
    # the status of the Docker daemon
    if host.system_info.distribution.lower() in debian_os:
        host.run("/etc/init.d/docker status").rc == 0
    else:
        s = host.service('docker')
        assert s.is_running
        assert s.is_enabled
