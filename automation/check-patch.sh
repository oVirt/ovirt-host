#!/bin/bash -xe

./automation/build-artifacts.sh

find \
    "$PWD/tmp.repos" \
    -iname \*.rpm \
    -exec mv {} exported-artifacts/ \;
pushd exported-artifacts
    #Restoring sane yum environment
    rm -f /etc/yum.conf
    yum reinstall -y system-release yum
    [[ -d /etc/dnf ]] && [[ -x /usr/bin/dnf ]] && dnf -y reinstall dnf-conf
    [[ -d /etc/dnf ]] && sed -i -re 's#^(reposdir *= *).*$#\1/etc/yum.repos.d#' '/etc/dnf/dnf.conf'
    yum install -y ovirt-release-master
    rm -f /etc/yum/yum.conf
    DISTVER="$(rpm --eval "%dist"|cut -c2-)"
    if [[ "${DISTVER}" == "el7.centos" ]]; then
        #Enable CR repo
        sed -i "s:enabled=0:enabled=1:" /etc/yum.repos.d/CentOS-CR.repo
    fi
    yum repolist enabled
    yum clean all
    if [[ "${DISTVER}" == "fc27" ]]; then
        # Fedora 27 support is broken, just provide a hint on what's missing
        # without causing the test to fail.
        yum --downloadonly install *$(arch).rpm || true
    elif [[ "${DISTVER}" == "fc28" ]]; then
        # Fedora 28 support is broken, just provide a hint on what's missing
        # without causing the test to fail.
        yum --downloadonly install *$(arch).rpm || true
    else
        yum --downloadonly install *$(arch).rpm
    fi
popd

