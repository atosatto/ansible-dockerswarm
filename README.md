# Ansible Role: Docker

[![Build Status](https://travis-ci.org/atosatto/ansible-dockerswarm.svg?branch=master)](https://travis-ci.org/atosatto/ansible-dockerswarm)
[![License](https://img.shields.io/badge/license-MIT%20License-brightgreen.svg)](https://opensource.org/licenses/MIT)
[![Ansible Role](http://img.shields.io/badge/galaxy-atosatto.docker--swarm-blue.svg?style=flat-square)](https://galaxy.ansible.com/atosatto/docker-swarm)
[![GitHub tag](https://img.shields.io/github/tag/atosatto/ansible-dockerswarm.svg)](https://github.com/atosatto/ansible-dockerswarm/tags)

Setup a Docker on RHEL/CentOS and Debian/Ubuntu servers.
The role supports Docker Engine's "Swarm Mode" (https://docs.docker.com/engine/swarm/) to create a cluster of Docker nodes.

## Requirements

An Ansible 2.3 or higher installation.

## Dependencies

None.

## Role Variables

Available variables are listed below, along with default values (see defaults/main.yml):

    docker_repo: "{{ docker_repo_ce_stable }}"

The repository proving the Docker packages. By default [Docker Community](https://www.docker.com/docker-community) stable repository is configured by the role. See `vars/main.yml` for the configuration of the Docker Community edge, test and nightly repositories.

    docker_package_name: "docker-ce"

Name of the Docker package providing.

      docker_package_version: ""

Version of the Docker package to be installed on the target hosts. By default, the latest available version will be installed.

    docker_dependencies: "{{ default_docker_dependencies }}"

Additional packages to install together with Docker.
See `vars/RedHat.yml` and `vars/Debian.yml` for the definition of the `default_docker_dependencies` variable.

    docker_service_state: "started"
    docker_service_enabled: "yes"

State of the Docker service.

    docker_daemon_config: {}

Dictionary of Docker Deamon configuration options to be written to the `/etc/docker/daemon.json` file.

    docker_swarm_interface: "{{ ansible_default_ipv4['alias'] }}"

Setting `docker_swarm_interface` allows you to define which network interface will be used for cluster inter-communication.

    docker_swarm_addr: "{{ hostvars[inventory_hostname]['ansible_' + docker_swarm_interface]['ipv4']['address'] }}"

By default, the ip address for raft API will be taken from desired interface.
You can setup listening address where the raft APIs will be exposed, overriding
the `docker_swarm_addr` variable value in your playbook.

    docker_swarm_port: 2377

Listening port where the raft APIs will be exposed.

    docker_group_name: "docker"
    docker_group_users:
      - "{{ ansible_user }}"

Name of the Docker group and list of of users to be added to the `docker_group_name` to interact with the Docker daemon.
**NB**: The users must already exist in the system.

    skip_repo: false
    skip_engine: false
    skip_group: false
    skip_swarm: false
    skip_docker_py: false

Switches allowing to disable specific functionalities of the role.
If you want to use this role to just install `docker-engine` without enabling `swarm-mode` set `skip_swarm: true`.

Swarm node labels
-----------------

[Node labels](https://docs.docker.com/engine/swarm/manage-nodes/#add-or-remove-label-metadata) provide a
flexible method of node organization. You can also use node labels in service constraints.
Apply constraints when you create a service to limit the nodes where the scheduler assigns tasks for the service.
You can define labels by `swarm_labels` variable, e.g:

    $ cat inventory
    ...
    [docker_swarm_manager]
    swarm-01 swarm_labels=deploy

    [docker_swarm_worker]
    swarm-02 swarm_labels='["libvirt", "docker", "foo", "bar"]'
    swarm-03
    ...

In this case:

    $ docker inspect --format '{{json .Spec.Labels}}'  swarm-02 | jq
    {
       "bar": "true",
       "docker": "true",
       "foo": "true",
       "libvirt": "true",
    }

You can assign labels to cluster running playbook with `--tags=swarm_labels`

**NB**: Please note, all labels that are not defined in inventory will be removed

## Example Playbook

    $ cat inventory
    swarm-01 ansible_ssh_host=172.10.10.1
    swarm-02 ansible_ssh_host=172.10.10.2
    swarm-03 ansible_ssh_host=172.10.10.3

    [docker_engine]
    swarm-01
    swarm-02
    swarm-03

    [docker_swarm_manager]
    swarm-01 swarm_labels=deploy

    [docker_swarm_worker]
    swarm-02 swarm_labels='["libvirt", "docker", "foo", "bar"]'
    swarm-03

    $ cat playbook.yml
    - name: "Provision Docker Swarm Cluster"
      hosts: all
      roles:
        - { role: atosatto.docker-swarm }

Testing
-------

Tests are performed by [Molecule](http://molecule.readthedocs.org/en/latest/).

    $ pip install tox

To test all the scenarios run

    $ tox

To run a custom molecule command

    $ tox -e py27-ansible23 -- molecule test -s swarm-cluster

The `MOLECULE_DRIVER_NAME` and `MOLECULE_TARGET_DISTRO` allows to change the Molecule driver from Docker to Vagrant and the tests target OS

    $ MOLECULE_DRIVER_NAME=vagrant MOLECULE_TARGET_DISTRO=ubuntu-1604 tox

To test the role on Ubuntu instead of CentOS set the

License
-------

MIT

Author Information
------------------

Andrea Tosatto ([@\_hilbert\_](https://twitter.com/_hilbert_))
