import os
import testinfra.utils.ansible_runner

runner = testinfra.utils.ansible_runner.AnsibleRunner(os.environ['MOLECULE_INVENTORY_FILE'])

ALL_HOSTS = runner.get_hosts('all')
MANAGER_HOSTS = runner.get_hosts('docker_swarm_manager')
WORKER_HOSTS = runner.get_hosts('docker_swarm_worker')

testinfra_hosts = ALL_HOSTS


def test_docker_swarm_enabled(host):

    assert 'Swarm: active' in host.check_output('docker info')


def test_docker_swarm_status(host):

    docker_info = host.check_output('docker info')
    hostname = host.check_output('hostname -s')

    if hostname in MANAGER_HOSTS:
        assert 'Is Manager: true' in docker_info
        assert 'Nodes: 3' in docker_info       # the test cluster is of 3 nodes
        assert 'Managers: 1' in docker_info    # with 1 managers

    elif hostname in WORKER_HOSTS:
        assert 'Is Manager: false' in docker_info
