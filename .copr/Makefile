.PHONY: installdeps srpm

installdeps:
	dnf -y install git

srpm:
	$(eval SUFFIX=$(shell sh -c " echo '.$$(date -u +%Y%m%d%H%M%S).git$$(git rev-parse --short HEAD)'"))
	# changing the spec file as passing -D won't preserve the suffix when rebuilding in mock
	sed "s:%{?release_suffix}:${SUFFIX}:" -i ovirt-host.spec
	mkdir -p tmp.repos/SOURCES
	cp LICENSE tmp.repos/SOURCES/
	rpmbuild \
		-D "_topdir tmp.repos" \
		-bs ovirt-host.spec
	cp tmp.repos/SRPMS/*.src.rpm $(outdir)
