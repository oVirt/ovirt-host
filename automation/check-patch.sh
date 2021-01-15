#!/bin/bash -xe

LC_ALL=en_US.UTF-8 rpmlint ovirt-host.spec

./automation/build-artifacts.sh

DISTVER="$(rpm --eval "%dist"|cut -c2-4)"
ARCH="$(rpm --eval "%_arch")"
PACKAGER=dnf
export PACKAGER

on_exit() {
    ${PACKAGER} --verbose clean all
}

trap on_exit EXIT



find \
    "$PWD/tmp.repos" \
    -iname \*.rpm \
    -exec mv {} exported-artifacts/ \;
pushd exported-artifacts
    #Restoring sane yum environment
    rm -f /etc/yum.conf
    ${PACKAGER} reinstall -y system-release ${PACKAGER}
    [[ -d /etc/dnf ]] && [[ -x /usr/bin/dnf ]] && dnf -y reinstall dnf-conf
    [[ -d /etc/dnf ]] && sed -i -re 's#^(reposdir *= *).*$#\1/etc/yum.repos.d#' '/etc/dnf/dnf.conf'
    [[ -e /etc/dnf/dnf.conf ]] && echo "deltarpm=False" >> /etc/dnf/dnf.conf
    ${PACKAGER} install -y ovirt-release-master
    rm -f /etc/yum/yum.conf
    ${PACKAGER} repolist enabled
    ${PACKAGER} clean all
    if [[ "${ARCH}" == "s390x" ]]; then
        # s390x support is broken, just provide a hint on what's missing
        # without causing the test to fail.
        ${PACKAGER} --downloadonly install *$(arch).rpm || true
    elif
     [[ "$(rpm --eval "%dist")" == ".el8" ]]; then
        if [[ "${ARCH}" == "ppc64le" ]]; then
            # ppc64le support is broken, just provide a hint on what's missing
            # without causing the test to fail.
            ${PACKAGER} --downloadonly install *$(arch).rpm || true
        else
            ${PACKAGER} --downloadonly install *$(arch).rpm
        fi
        echo "Testing CentOS Stream"
        ${PACKAGER} remove ovirt-release-master
        ${PACKAGER} install -y centos-release-stream
        ${PACKAGER} repolist enabled
        ${PACKAGER} --releasever=8-stream --disablerepo=* --enablerepo=Stream-BaseOS download centos-stream-repos
        ${PACKAGER} install -y centos-stream-release
        rpm -e --nodeps centos-linux-repos
        rpm -i centos-stream-repo*
        rm -fv centos-stream-repo*
        ls -l /etc/yum.repos.d/
        ${PACKAGER} distro-sync -y
        ${PACKAGER} install -y ovirt-release-master
        ${PACKAGER} repolist enabled
        ${PACKAGER} clean all
        if [[ "$(rpm --eval "%_arch")" == "ppc64le" ]]; then
            # ppc64le support is broken, just provide a hint on what's missing
            # without causing the test to fail.
            ${PACKAGER} --downloadonly install *$(arch).rpm || true
        else
            ${PACKAGER} --downloadonly install *$(arch).rpm
        fi
    fi
popd
