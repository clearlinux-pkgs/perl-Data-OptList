#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cpan
#
Name     : perl-Data-OptList
Version  : 0.114
Release  : 41
URL      : https://cpan.metacpan.org/authors/id/R/RJ/RJBS/Data-OptList-0.114.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/R/RJ/RJBS/Data-OptList-0.114.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libd/libdata-optlist-perl/libdata-optlist-perl_0.110-1.debian.tar.xz
Summary  : 'parse and validate simple name/value option pairs'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-Data-OptList-license = %{version}-%{release}
Requires: perl-Data-OptList-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(Sub::Install)
BuildRequires : perl-Params-Util
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
This archive contains the distribution Data-OptList,
version 0.114:
parse and validate simple name/value option pairs

%package dev
Summary: dev components for the perl-Data-OptList package.
Group: Development
Provides: perl-Data-OptList-devel = %{version}-%{release}
Requires: perl-Data-OptList = %{version}-%{release}

%description dev
dev components for the perl-Data-OptList package.


%package license
Summary: license components for the perl-Data-OptList package.
Group: Default

%description license
license components for the perl-Data-OptList package.


%package perl
Summary: perl components for the perl-Data-OptList package.
Group: Default
Requires: perl-Data-OptList = %{version}-%{release}

%description perl
perl components for the perl-Data-OptList package.


%prep
%setup -q -n Data-OptList-0.114
cd %{_builddir}
tar xf %{_sourcedir}/libdata-optlist-perl_0.110-1.debian.tar.xz
cd %{_builddir}/Data-OptList-0.114
mkdir -p deblicense/
cp -r %{_builddir}/debian/* %{_builddir}/Data-OptList-0.114/deblicense/
pushd ..
cp -a Data-OptList-0.114 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} -I. Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Data-OptList
cp %{_builddir}/Data-OptList-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/perl-Data-OptList/09c99293be0a7029d91f0c990e097696ca0e78de || :
cp %{_builddir}/debian/copyright %{buildroot}/usr/share/package-licenses/perl-Data-OptList/6e2929637fd4a11394110fd2c25cb98cea29cdee || :
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Data::OptList.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Data-OptList/09c99293be0a7029d91f0c990e097696ca0e78de
/usr/share/package-licenses/perl-Data-OptList/6e2929637fd4a11394110fd2c25cb98cea29cdee

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
