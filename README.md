Ansible Role: Docker Swarm
===============================

[![Build Status](https://travis-ci.org/atosatto/ansible-dockerswarm.svg?branch=master)](https://travis-ci.org/atosatto/ansible-dockerswarm)

Setup a Docker Swarm cluster on RHEL/CentOS and Debian/Ubuntu servers
using the new Docker Engine's "Swarm Mode" (https://docs.docker.com/engine/swarm/).

Requirements
------------

None.

Role Variables
--------------

Available variables are listed below, along with default values (see defaults/main.yml):

    docker_engine_version: 1.12.0-rc3

The version of the commercially supported docker engine to install.

    docker_ucp_admin_username: admin
    docker_ucp_admin_password: admin

Login credentials to the docker universal control plane.

    local_docker_ucp_subscription_file: "{{ playbook_dir}}/files/docker_subscription.lic"

The local path of the docker universal control plane subscription file.
The file will be uploaded to the first controller node to the following
location and mounted as a volume into the UCP installer container.
To download the license file follow this guide: https://success.docker.com/Datacenter/Solve/How_to_download_your_Docker_license_key.

    docker_ucp_subscription_file: "/root/docker_subscription.lic"

Overriding the following variables

    docker_ucp_swarm_port: 2376
    docker_ucp_controller_port: 443

it is possibile to modify the binding ports of the docker swarm and UCP controller daemons.
Optionally, it is possible to specify a custom public interface for the UCP nodes,
or provide a subject alternative name for the cluster nodes overriding the following
variables using the proper Ansible facts:

    docker_ucp_host_address: "{{ ansible_default_ipv4['address'] }}"
    docker_ucp_san: ""

Extra arguments to the UCP installation utility, can be provided with
the `docker_ucp_extra_args`

    docker_ucp_extra_args: ""
    #docker_ucp_extra_args: "--disable-tracking --disable-usage --binpack"

HA provisioning requires to dump from the first controller node some PKI and
configuration informations. The path where to store these files can be
customized acting on the following variables.

    docker_ucp_backup_passfrase: ""
    docker_ucp_backup_file: /root/ucp-backup.tar
    local_docker_ucp_backup_file: /tmp/ucp-backup.tar


Dependencies
------------

None.

Example Playbook
----------------

    $ cat inventory
    swarm-01 ansible_ssh_host=172.10.10.1
    swarm-02 ansible_ssh_host=172.10.10.2
    swarm-03 ansible_ssh_host=172.10.10.2

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
        - role: ansible-dockerswarm

License
-------

MIT

Author Information
------------------

Andrea Tosatto ([@\_hilbert\_](https://twitter.com/_hilbert_))
