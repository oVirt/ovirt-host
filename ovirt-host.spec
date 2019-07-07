%global vdsm_version 4.30.15

Name:		ovirt-host
Version:	4.3.4
Release:	0.0.master%{?release_suffix}%{?dist}
Summary:	Track required packages for oVirt hosts
License:	ASL 2.0
URL:		http://www.ovirt.org

Source0:	LICENSE

# It was wrong to build as noarch, because there are
# arch-specific dependencies.
Obsoletes:	%{name}.noarch <= %{version}-%{release}
Conflicts:	%{name}.noarch

Requires:	%{name}-dependencies = %{version}-%{release}

#Inherited from oVirt Node
Requires:	cockpit
Requires:	cockpit-dashboard
Requires:	cockpit-networkmanager
Requires:	cockpit-machines-ovirt
%ifarch x86_64
Requires:	cockpit-ovirt-dashboard
%endif
Requires:	firewalld
%if 0%{?fedora} || 0%{?rhel} >= 8
Requires:	python3-firewall
%else
Requires:	python-firewall
%endif
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
%if 0%{?fedora} || 0%{?rhel} > 7
Suggests:	postfix
%endif
Requires:	mailx
Requires:	dracut-fips
Requires:	screen
Requires:	sysstat
Requires:	tcpdump
Requires:	net-snmp
Requires:	net-snmp-utils

# Hack to include the passive NM config: https://bugzilla.redhat.com/1326798
Requires:	NetworkManager-config-server

# from https://bugzilla.redhat.com/show_bug.cgi?id=1490041
Requires:	ipa-client

# Hardening packages - from https://bugzilla.redhat.com/show_bug.cgi?id=1598318
Requires:	openscap
Requires:	openscap-utils
Requires:	scap-security-guide
%if 0%{?rhel}
Requires:	pam_pkcs11
%endif
Requires:	aide

# https://bugzilla.redhat.com/show_bug.cgi?id=1722173
Requires:	iperf3

# https://bugzilla.redhat.com/show_bug.cgi?id=1725954
Requires:	libvirt-admin

%ifarch x86_64
# from https://bugzilla.redhat.com/show_bug.cgi?id=1425032
# katello-agent has been dropped from Fedora on fc22 but it's still built
# on https://fedorapeople.org/groups/katello/releases/yum/latest/client/
# packages will be imported in oVirt repo.
Requires:	katello-agent
%endif

# the following packages requires a RHGS subscription on RHEL, keeping them
# in oVirt Node only
# Requires:	gdeploy

# the following packages have dependencies which require RHGS subscription on
# RHEL, keeping them in oVirt Node only
# Requires:	vdsm-gluster -> glusterfs-server

%description
This meta package pulls in all the dependencies needed for an oVirt hosts

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
%ifarch x86_64
Requires:	v2v-conversion-host-wrapper
%endif
Requires:	vdsm >= %{vdsm_version}
Requires:	vdsm-client >= %{vdsm_version}

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
* Fri May 17 2019 - Sandro Bonazzola <sbonazzo@redhat.com> - 4.3.3-1
- 4.3.3-1
- CVE-2018-12126, CVE-2018-12127, CVE-2018-12130, CVE-2019-11091
- Resolves: BZ#1710918
- spec: require updated microcode_ctl

* Wed Mar 27 2019 - Sandro Bonazzola <sbonazzo@redhat.com> - 4.3.2-1
- 4.3.2-1
- spec: require v2v-conversion-host-wrapper
- cleaning: drop vdsm-hook-vfio-mdev dependency
- spec: require latest vdsm

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
