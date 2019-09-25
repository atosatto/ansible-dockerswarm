# Molecule managed

FROM {{ item.image }}

RUN if [ $(command -v apt-get) ]; then apt-get update && apt-get upgrade -y && apt-get install -y systemd && apt-get clean; fi
RUN if [ ! -e /sbin/init ]; then ln -s /lib/systemd/systemd /sbin/init ; fi

ENV container docker

# Don't start the optional systemd services. 
RUN find /etc/systemd/system \
         /lib/systemd/system \
         -path '*.wants/*' \
         -not -name '*journald*' \
         -not -name '*systemd-tmpfiles*' \
         -not -name '*systemd-user-sessions*' \
         -exec rm \{} \;

RUN systemctl set-default multi-user.target

VOLUME [ "/sys/fs/cgroup" ]

CMD ["/sbin/init"]

RUN if [ $(command -v apt-get) ]; then apt-get update && apt-get upgrade -y && apt-get install -y python sudo bash net-tools ca-certificates && apt-get clean; fi
