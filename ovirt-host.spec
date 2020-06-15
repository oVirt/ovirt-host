%global vdsm_version 4.40.18

Name:		ovirt-host
Version:	4.4.2
Release:	0.0%{?release_suffix}%{?dist}
Summary:	Track required packages for oVirt hosts
License:	ASL 2.0
URL:		https://www.ovirt.org/

Source0:	LICENSE

Requires:	%{name}-dependencies = %{version}-%{release}

#Inherited from oVirt Node
Requires:	cockpit
Requires:	cockpit-dashboard
Requires:	cockpit-networkmanager
%ifarch x86_64
Requires:	cockpit-ovirt-dashboard
%endif
Requires:	firewalld
Requires:	python3-firewall
Requires:	rng-tools
Requires:	vdsm-hook-fcoe
Requires:	vdsm-hook-vhostmd
Requires:	vdsm-hook-openstacknet
Requires:	vdsm-hook-ethtool-options
Requires:	vdsm-hook-vmfex-dev
%ifarch x86_64
Requires:	glusterfs-rdma
Requires:	ovirt-hosted-engine-setup
Requires:	ovirt-provider-ovn-driver
%endif
Requires:	server(smtp)
Suggests:	postfix
Requires:	mailx
Requires:	dracut-fips
Requires:	sysstat
Requires:	tcpdump
Requires:	tmux
Requires:	net-snmp
Requires:	net-snmp-utils

# Hack to include the passive NM config: https://bugzilla.redhat.com/1326798
Requires:	NetworkManager-config-server

# from https://bugzilla.redhat.com/show_bug.cgi?id=1490041
Requires:	ipa-client

# Hardening packages - from https://bugzilla.redhat.com/show_bug.cgi?id=1598318
Requires:	openscap
Requires:	scap-security-guide
Requires:	aide
# additional packages now required by STIG security profile
# from https://bugzilla.redhat.com/show_bug.cgi?id=1836026
Requires:	opensc
Requires:	pcsc-lite
Requires:	audispd-plugins

# https://bugzilla.redhat.com/show_bug.cgi?id=1722173
Requires:	iperf3

# https://bugzilla.redhat.com/show_bug.cgi?id=1725954
Requires:	libvirt-admin

# https://bugzilla.redhat.com/show_bug.cgi?id=1741792
Requires:	clevis-dracut

# https://bugzilla.redhat.com/show_bug.cgi?id=1812014
Requires: cracklib-dicts

# the following packages requires a RHGS subscription on RHEL, keeping them
# in oVirt Node only
# Requires:	gdeploy

# the following packages have dependencies which require RHGS subscription on
# RHEL, keeping them in oVirt Node only
# Requires:	vdsm-gluster -> glusterfs-server

%description
This meta package pulls in all the dependencies needed for an oVirt hosts.

%package dependencies
Summary:	This meta package pulls in all the dependencies needed for minimal oVirt hosts.
Requires:	collectd
Requires:	collectd-disk
Requires:	collectd-netlink
Requires:	collectd-write_http
Requires:	collectd-virt

%if 0%{?rhel}
# collectd-write_syslog is available only on EL7
Requires:	collectd-write_syslog
%endif

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

%ifarch x86_64
#{ CVE-2018-12126, CVE-2018-12127, CVE-2018-12130, CVE-2019-11091
%if 0%{?rhel}
Requires:	microcode_ctl >= 2.1-47.2
%else
Requires:	microcode_ctl >= 2.1-29
%endif
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
