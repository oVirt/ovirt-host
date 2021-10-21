srpm:
	dnf -y install git
	$(eval SUFFIX=$(shell sh -c " echo '.$$(date -u +%Y%m%d%H%M%S).git$$(git rev-parse --short HEAD)'"))
	mkdir -p tmp.repos/SOURCES
	cp LICENSE tmp.repos/SOURCES/
	rpmbuild \
		-D "_topdir tmp.repos" \
		-D "release_suffix $(SUFFIX)" \
		-bs ovirt-host.spec
	cp tmp.repos/SRPMS/*.src.rpm $(outdir)
