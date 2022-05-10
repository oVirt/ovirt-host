.PHONY: installdeps srpm git_config_pre

installdeps:
	dnf -y install git

git_config_pre:
	# From git 2.35.2 we need to mark temporary directory, where the project is cloned to, as safe, otherwise
	# git commands won't work
	$(eval REPO_DIR=$(shell pwd))
	git config --global --add safe.directory ${REPO_DIR}

srpm: installdeps git_config_pre
	$(eval SUFFIX=$(shell sh -c " echo '.$$(date -u +%Y%m%d%H%M%S).git$$(git rev-parse --short HEAD)'"))
	# changing the spec file as passing -D won't preserve the suffix when rebuilding in mock
	sed "s:%{?release_suffix}:${SUFFIX}:" -i ovirt-host.spec
	mkdir -p tmp.repos/SOURCES
	cp LICENSE tmp.repos/SOURCES/
	rpmbuild \
		-D "_topdir tmp.repos" \
		-bs ovirt-host.spec
	cp tmp.repos/SRPMS/*.src.rpm $(outdir)
