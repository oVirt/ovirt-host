%global vdsm_version 4.17.0

Name:		ovirt-host
Version:	3.6.0
Release:	0.0.master%{?release_suffix}%{?dist}
Summary:	Track required packages for oVirt hosts
License:	ASL 2.0
URL:		http://www.ovirt.org

Source0:	LICENSE
BuildArch:	noarch

%ifarch %{ix86} x86_64
Requires:	dmidecode
%endif
Requires:	kexec-tools
Requires:	ovirt-vmconsole
Requires:	ovirt-vmconsole-host
Requires:	socat
Requires:	tar
Requires:	tuned
Requires:	util-linux
Requires:	vdsm >= %{vdsm_version}
Requires:	vdsm-cli >= %{vdsm_version}


%description
This meta package pulls in all the dependencies needed for minimal oVirt hosts.

%prep
cp %{SOURCE0} .

%files
%license LICENSE

%changelog
* Wed Sep 13 2017 - Yedidyah Bar David <didi@redhat.com> - 3.6.0
- Initial 3.6 version
