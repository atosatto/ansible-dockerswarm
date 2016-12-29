import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    '.molecule/ansible_inventory').get_hosts('all')


def test_docker_repository_exists(File, SystemInfo):

    f = None
    dist = SystemInfo.distribution
    if dist == 'debian' or dist == 'ubuntu':
        f = File('/etc/apt/sources.list.d/docker.list')
    if dist == 'redhat' or dist == 'centos' or dist == 'fedora':
        f = File('/etc/yum.repos.d/docker.repo')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'
    assert oct(f.mode) == '0644'


def test_docker_engine_installed(Package):

    assert Package('docker-engine').is_installed


def test_docker_service(Service, Command, SystemInfo):

    # Testinfra fails on Ubuntu trying to use systemd to get
    # the status of the Docker daemon
    dist = SystemInfo.distribution
    if dist == 'debian' or dist == 'ubuntu':
        Command("/etc/init.d/docker status").rc == 0
    else:
        s = Service('docker')
        assert s.is_running
        assert s.is_enabled
