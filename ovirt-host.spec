%global vdsm_version 4.50.0.11

Name:		ovirt-host
Version:	4.5.0
Release:	3%{?dist}
Summary:	Track required packages for oVirt hosts
License:	ASL 2.0
URL:		https://www.ovirt.org/

Source0:	LICENSE

Requires:	%{name}-dependencies = %{version}-%{release}

#Inherited from oVirt Node
Requires:	cockpit
Requires:	cockpit-system

%ifarch x86_64
# Hosted Engine is supported only on x86_64 architecture.
Requires:	glusterfs
Requires:	ovirt-hosted-engine-setup
Requires:	ovirt-provider-ovn-driver
%if 0%{?rhel} < 9
# On CentOS Stream 9 we are going to use ansible 2.11
# The whole way of consuming anisble roles is going to change:
# skipping cockpit-ovirt-dashboard dependencies
Requires:	cockpit-ovirt-dashboard
%endif
%endif

Requires:	firewalld
Requires:	libvirt
Requires:	python3-firewall
Requires:	rng-tools
Requires:	server(smtp)
Suggests:	postfix
Requires:	dracut-fips
Requires:	sysstat
Requires:	tcpdump
Requires:	tmux
Requires:	net-snmp
Requires:	net-snmp-utils

# from https://bugzilla.redhat.com/1335503
%if 0%{?rhel} >= 9
# mailx has been replaced by s-nail on RHEL 9
# https://bugzilla.redhat.com/2001537
Requires:	s-nail
%else
Requires:	mailx
%endif

# Hack to include the passive NM config: https://bugzilla.redhat.com/1326798
Requires:	NetworkManager-config-server

# from https://bugzilla.redhat.com/show_bug.cgi?id=1490041
Requires:	ipa-client

# Hardening packages - from https://bugzilla.redhat.com/show_bug.cgi?id=1598318
Requires:	openscap
Requires:	scap-security-guide >= 0.1.60-4
Requires:	aide
# additional packages now required by STIG security profile
# from https://bugzilla.redhat.com/show_bug.cgi?id=1836026
Requires:	opensc
Requires:	pcsc-lite
Requires:	audispd-plugins
# Helping cockpit when hardening: https://bugzilla.redhat.com/show_bug.cgi?id=1835661
Requires:	sscg

# https://bugzilla.redhat.com/show_bug.cgi?id=1722173
Requires:	iperf3

# https://bugzilla.redhat.com/show_bug.cgi?id=1725954
Requires:	libvirt-admin

# https://bugzilla.redhat.com/show_bug.cgi?id=1741792
Requires:	clevis-dracut

# https://bugzilla.redhat.com/show_bug.cgi?id=1812014
Requires: cracklib-dicts

# https://bugzilla.redhat.com/show_bug.cgi?id=1933245
Requires: smartmontools

# https://bugzilla.redhat.com/show_bug.cgi?id=2058177
Requires: nvme-cli

# the following packages have dependencies which require RHGS subscription on
# RHEL, keeping them in oVirt Node only
# Requires:	vdsm-gluster -> glusterfs-server

%description
This meta package pulls in all the dependencies needed for an oVirt hosts.

%package dependencies
Summary:	This meta package pulls in all the dependencies needed for minimal oVirt hosts
%ifnarch s390x
# Not available for s390x yet
Requires:	collectd >= 5.12.0-7
Requires:	collectd-disk >= 5.12.0-7
Requires:	collectd-netlink >= 5.12.0-7
Requires:	collectd-write_http >= 5.12.0-7
Requires:	collectd-virt >= 5.12.0-7

%if 0%{?rhel}
# collectd-write_syslog is available only on RHEL and similar
Requires:	collectd-write_syslog >= 5.12.0-7
%endif

%endif
# end of s390x collectd exclusion

%ifarch %{ix86} x86_64
Requires:	dmidecode
%endif
Requires:	kexec-tools
Requires:	ovirt-vmconsole
Requires:	ovirt-vmconsole-host

# Requirements for ovirt-engine-metrics
Requires:	rsyslog
Requires:	rsyslog-elasticsearch
Requires:	rsyslog-mmjsonparse
Requires:	rsyslog-mmnormalize

# https://bugzilla.redhat.com/show_bug.cgi?id=1984886
Requires:	rsyslog-openssl

Requires:	libfastjson
Requires:	liblognorm
Requires:	libestr

Requires:	socat
Requires:	tar
Requires:	tuned
Requires:	util-linux
Requires:	vdsm >= %{vdsm_version}
Requires:	vdsm-client >= %{vdsm_version}

# https://bugzilla.redhat.com/show_bug.cgi?id=1836645
Requires:	ovirt-imageio-client

# cinderlib integration
# https://bugzilla.redhat.com/1955375
%ifarch x86_64
Requires:   ceph-common
Requires:   python3-os-brick
%endif

%ifarch x86_64
#{ CVE-2020-24489
Requires:      microcode_ctl >= 2021021
#}
%endif


%description dependencies
This meta package pulls in all the dependencies needed for minimal oVirt hosts.
This excludes oVirt Hosted Engine packages and other packages available in
an oVirt Node host.


%prep
cp %{SOURCE0} .

%build
# No build needed

%install
# No build needed

%files
%license LICENSE

%files dependencies
%license LICENSE

%changelog
* Fri Apr 08 2022 Sandro Bonazzola <sbonazzo@redhat.com> - 4.5.0-3
- Bump to 4.5.0-3

* Wed Mar 30 2022 Sandro Bonazzola <sbonazzo@redhat.com> - 4.5.0-2
- Bump to 4.5.0-2

* Fri Mar 04 2022 Sandro Bonazzola <sbonazzo@redhat.com> - 4.5.0-1
- Bump to 4.5.0

* Wed Oct 13 2021 Sandro Bonazzola <sbonazzo@redhat.com> - 4.4.9-2
- Require cinderlib only on x86_64

* Fri Oct 01 2021 Sandro Bonazzola <sbonazzo@redhat.com> - 4.4.9-1
- Bump to 4.4.9

* Fri Jul 16 2021 Sandro Bonazzola <sbonazzo@redhat.com> - 4.4.8-1
- Bump to 4.4.8
- Resolves: BZ#1955375

* Thu May 06 2021 Sandro Bonazzola <sbonazzo@redhat.com> - 4.4.7-1
- Bump to 4.4.7
- Resolves: BZ#1947450

* Wed Mar 24 2021 Sandro Bonazzola <sbonazzo@redhat.com> - 4.4.6-1
- Bump to 4.4.6

* Wed Jan 27 2021 Sandro Bonazzola <sbonazzo@redhat.com> - 4.4.5-1
- Bump to 4.4.5

* Mon Jun 15 2020 Sandro Bonazzola <sbonazzo@redhat.com> - 4.4.1-4
- Fixes rhbz#1836026

* Wed Jun 03 2020 Lev Veyde <lveyde@redhat.com> - 4.4.1-3
- revert spec: require v2v-conversion-host-wrapper where available

* Wed May 27 2020 Lev Veyde <lveyde@redhat.com> - 4.4.1-2
- spec: require v2v-conversion-host-wrapper where available

* Mon May 18 2020 Sandro Bonazzola <sbonazzo@redhat.com> - 4.4.1-1
- Rebase on 4.4.1

* Thu Apr 23 2020 Sandro Bonazzola <sbonazzo@redhat.com> - 4.4.0-1
- Rebase on 4.4.0

* Mon Feb 18 2019 - Sandro Bonazzola <sbonazzo@redhat.com> - 4.3.1-1
- 4.3.1-1
- spec: require collectd-write_syslog where available

* Tue Jan 15 2019 - Sandro Bonazzola <sbonazzo@redhat.com> - 4.3.0-2
- 4.3.0-2
- metrics: replace fluentd with rsyslog

* Tue Jan 08 2019 - Sandro Bonazzola <sbonazzo@redhat.com> - 4.3.0-1
- 4.3.0-1

* Wed Jan 10 2018 - Sandro Bonazzola <sbonazzo@redhat.com> - 4.2.1-1
- 4.2.1-1

* Wed Nov 29 2017 - Sandro Bonazzola <sbonazzo@redhat.com> - 4.2.0-1
- 4.2.0-1

* Mon Jun 12 2017 - Sandro Bonazzola <sbonazzo@redhat.com> - 4.2.0
- Initial import
