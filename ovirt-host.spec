%global vdsm_version 4.20.0

Name:		ovirt-host
Version:	4.2.0
Release:	0.0.master%{?release_suffix}%{?dist}
Summary:	Track required packages for oVirt hosts
License:	ASL 2.0
URL:		http://www.ovirt.org

Source0:	LICENSE
BuildArch:	noarch

Requires:	collectd
Requires:	collectd-disk
Requires:	collectd-netlink
Requires:	collectd-virt
Requires:	collectd-write_http
%ifarch %{ix86} x86_64
Requires:	dmidecode
%endif
Requires:	fluentd
Requires:	kexec-tools
Requires:	ovirt-vmconsole
Requires:	ovirt-vmconsole-host
Requires:	rubygem-fluent-plugin-collectd-nest
Requires:	rubygem-fluent-plugin-rewrite-tag-filter
Requires:	rubygem-fluent-plugin-secure-forward
Requires:	rubygem-fluent-plugin-viaq_data_model
Requires:	socat
Requires:	tar
Requires:	tuned
Requires:	util-linux
Requires:	vdsm >= %{vdsm_version}
Requires:	vdsm-client >= %{vdsm_version}


%description
This meta package pulls in all the dependencies needed for minimal oVirt hosts.

%prep
cp %{SOURCE0} .

%files
%license LICENSE

%changelog
* Mon Jun 12 2017 - Sandro Bonazzola <sbonazzo@redhat.com> - 4.2.0
- Initial import
