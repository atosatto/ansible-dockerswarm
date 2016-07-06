Ansible Role: Docker Swarm
==========================

[![Build Status](https://travis-ci.org/atosatto/ansible-dockerswarm.svg?branch=master)](https://travis-ci.org/atosatto/ansible-dockerswarm)

Setup a Docker Swarm cluster on RHEL/CentOS and Debian/Ubuntu servers
using the new Docker Engine's "Swarm Mode" (https://docs.docker.com/engine/swarm/).

**Disclaimer:** This role uses the new Docker Engine's "Swarm Mode".
                Make sure to override the `docker_repo` variable to download the
                laster docker-engine 1.12 release-candidate.

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

    [docker_swarm_node]
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
