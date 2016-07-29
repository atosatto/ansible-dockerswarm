Ansible Role: Docker Swarm
==========================

[![Build Status](https://travis-ci.org/atosatto/ansible-dockerswarm.svg?branch=master)](https://travis-ci.org/atosatto/ansible-dockerswarm)

Setup a Docker Swarm cluster on RHEL/CentOS and Debian/Ubuntu servers
using the new Docker Engine's "Swarm Mode" (https://docs.docker.com/engine/swarm/).

**Disclaimer:** This role uses the new Docker Engine's "Swarm Mode".
                Make sure to set the value of the `docker_repo` variable to
                `testing` to download the laster docker-engine `1.12.0-rc`.

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

    docker_swarm_addr: "{{ ansible_default_ipv4['address'] }}"

Listening address where the raft APIs will be exposed.
Special case `0.0.0.0` will be replaced with default route ip (see https://github.com/docker/docker/issues/23784 for more details).

    docker_swarm_port: 2377

Listening port where the raft APIs will be exposed.

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
        - { role: ansible-dockerswarm,
            docker_repo: testing }

License
-------

MIT

Author Information
------------------

Andrea Tosatto ([@\_hilbert\_](https://twitter.com/_hilbert_))
