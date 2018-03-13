%global vdsm_version 4.20.2

Name:		ovirt-host
Version:	4.2.3
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
%ifarch x86_64
Requires:	cockpit-ovirt-dashboard
%endif
Requires:	firewalld
Requires:	python-firewall
Requires:	rng-tools
Requires:	vdsm-hook-fcoe
Requires:	vdsm-hook-vhostmd
Requires:	vdsm-hook-openstacknet
Requires:	vdsm-hook-ethtool-options
Requires:	vdsm-hook-vfio-mdev
Requires:	vdsm-hook-vmfex-dev
%ifarch x86_64
Requires:	glusterfs-rdma
Requires:	ovirt-hosted-engine-setup
Requires:	ovirt-provider-ovn-driver
%endif
Requires:	postfix
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
This meta package pulls in all the dependencies needed for an oVirt hosts.

%package dependencies
Summary:	This meta package pulls in all the dependencies needed for minimal oVirt hosts.
Requires:	collectd
Requires:	collectd-disk
Requires:	collectd-netlink
Requires:	collectd-write_http
Requires:	collectd-virt
%ifarch %{ix86} x86_64
Requires:	dmidecode
%endif
%ifnarch s390 s390x
Requires:	fluentd
%endif
Requires:	kexec-tools
Requires:	ovirt-vmconsole
Requires:	ovirt-vmconsole-host
%ifnarch s390 s390x
Requires:	rubygem-fluent-plugin-collectd-nest
Requires:	rubygem-fluent-plugin-rewrite-tag-filter
Requires:	rubygem-fluent-plugin-secure-forward
Requires:	rubygem-fluent-plugin-viaq_data_model
Requires:	rubygem-fluent-plugin-elasticsearch
%endif
Requires:	socat
Requires:	tar
Requires:	tuned
Requires:	util-linux
Requires:	vdsm >= %{vdsm_version}
Requires:	vdsm-client >= %{vdsm_version}

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
* Mon Feb 19 2018 - Sandro Bonazzola <sbonazzo@redhat.com> - 4.2.2-1
- 4.2.2-1

* Wed Jan 10 2018 - Sandro Bonazzola <sbonazzo@redhat.com> - 4.2.1-1
- 4.2.1-1

* Wed Nov 29 2017 - Sandro Bonazzola <sbonazzo@redhat.com> - 4.2.0-1
- 4.2.0-1

* Mon Jun 12 2017 - Sandro Bonazzola <sbonazzo@redhat.com> - 4.2.0
- Initial import
