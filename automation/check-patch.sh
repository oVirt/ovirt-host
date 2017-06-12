#!/bin/bash -xe

./automation/build-artifacts.sh

find \
    "$PWD/tmp.repos" \
    -iname \*.rpm \
    -exec mv {} exported-artifacts/ \;
pushd exported-artifacts
    #Restoring sane yum environment
    yum reinstall -y system-release yum
    [[ -d /etc/dnf ]] && dnf -y reinstall dnf-conf
    [[ -d /etc/dnf ]] && sed -i -re 's#^(reposdir *= *).*$#\1/etc/yum.repos.d#' '/etc/dnf/dnf.conf'
    yum install -y ovirt-release-master
    rm -f /etc/yum/yum.conf
    yum repolist enabled
    yum --downloadonly install *noarch.rpm
popd
