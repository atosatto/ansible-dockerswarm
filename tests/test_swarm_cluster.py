import testinfra.utils.ansible_runner

runner = testinfra.utils.ansible_runner.AnsibleRunner(
    '.molecule/ansible_inventory')

ALL_HOSTS = runner.get_hosts('all')
MANAGER_HOSTS = runner.get_hosts('docker_swarm_manager')
WORKER_HOSTS = runner.get_hosts('docker_swarm_worker')

testinfra_hosts = ALL_HOSTS


def test_docker_swarm_enabled(Command):

    assert 'Swarm: active' in Command.check_output('docker info')


def test_docker_swarm_status(Command, TestinfraBackend):

    docker_info = Command.check_output('docker info')

    if TestinfraBackend.get_hostname() in MANAGER_HOSTS:
        assert 'Is Manager: true' in docker_info
        assert 'Nodes: 3' in docker_info       # the test cluster is of 3 nodes
        assert 'Managers: 2' in docker_info    # with 2 managers

    elif TestinfraBackend.get_hostname() in WORKER_HOSTS:
        assert 'Is Manager: false' in Command.check_output('docker info')
