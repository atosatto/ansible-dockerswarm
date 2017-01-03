Ansible Role: Docker Swarm
==========================

[![Build Status](https://travis-ci.org/atosatto/ansible-dockerswarm.svg?branch=master)](https://travis-ci.org/atosatto/ansible-dockerswarm)

Setup a Docker Swarm cluster on RHEL/CentOS and Debian/Ubuntu servers
using the new Docker Engine's "Swarm Mode" (https://docs.docker.com/engine/swarm/).

Requirements
------------

None.

Role Variables
--------------

Available variables are listed below, along with default values (see defaults/main.yml):

    docker_repo: main
    # docker_repo: testing
    # docker_repo: experimental

The repo from which install Docker. Override the default to install
testing or experimental docker builds.

    docker_dependencies: "{{ default_docker_dependencies }}"

Extra packages that have to installed together with Docker.
The value of `default_docker_dependencies` depends on the target OS family.
> **NB**: If you are installing Docker on a Raspberry running Raspbian or any other Debian-like OS make sure to set
`docker_dependencies: [ ]` otherwise Ansible will fail because the `linux-image-extra-virtual` package is not available for the `arm` architecture (see issue #4).

    docker_swarm_interface: "{{ ansible_default_ipv4['alias'] }}"

Setting `docker_swarm_interface` allows you to define which network interface will be used for cluster inter-communication.

    docker_swarm_addr: "{{ hostvars[inventory_hostname]['ansible_' + docker_swarm_interface]['ipv4']['address'] }}"

By default, the ip address for raft API will be taken from desired interface.
You can setup listening address where the raft APIs will be exposed, overriding
the `docker_swarm_addr` variable value in your playbook.

    docker_swarm_port: 2377

Listening port where the raft APIs will be exposed.

    docker_admin_users:
      - "{{ ansible_user }}"

The list of users that has to be added to the `docker_group` to interact with the Docker daemon.
**NB**: The users must already exist in the system.

    skip_engine: False
    skip_group: False
    skip_swarm: False
    skip_docker_py: False

Setting `skip_engine: True` will make the role skip the installation of `docker-engine`.
If you want to use this role to just install `docker-engine` without enabling `swarm-mode` set `skip_swarm: True`.
To skip the tasks adding the `docker_admin_users` to the `docker_group` set `skip_group: True`.
Finally, the `docker-py` installation task can be skipped setting `skip_docker_py` to `True`.

Dependencies
------------

None.

Example Playbook
----------------

    $ cat inventory
    swarm-01 ansible_ssh_host=172.10.10.1
    swarm-02 ansible_ssh_host=172.10.10.2
    swarm-03 ansible_ssh_host=172.10.10.3

    [docker_engine]
    swarm-01
    swarm-02
    swarm-03

    [docker_swarm_manager]
    swarm-01

    [docker_swarm_worker]
    swarm-02
    swarm-03

    $ cat playbook.yml
    - name: "Provision Docker Swarm Cluster"
      hosts: all
      roles:
        - { role: atosatto.docker-swarm }

License
-------

MIT

Author Information
------------------

Andrea Tosatto ([@\_hilbert\_](https://twitter.com/_hilbert_))
