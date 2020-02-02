import os
import testinfra.utils.ansible_runner

runner = testinfra.utils.ansible_runner.AnsibleRunner(os.environ['MOLECULE_INVENTORY_FILE'])
testinfra_hosts = runner.get_hosts('all')


def test_docker_swarm_enabled(host):

    assert 'Swarm: active' in host.check_output('docker info')


def test_docker_swarm_status(host):

    docker_info = host.check_output('docker info')
    assert 'Is Manager: true' in docker_info
    assert 'Nodes: 1' in docker_info
    assert 'Managers: 1' in docker_info
