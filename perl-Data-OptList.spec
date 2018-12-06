#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Data-OptList
Version  : 0.110
Release  : 24
URL      : https://cpan.metacpan.org/authors/id/R/RJ/RJBS/Data-OptList-0.110.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/R/RJ/RJBS/Data-OptList-0.110.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libd/libdata-optlist-perl/libdata-optlist-perl_0.110-1.debian.tar.xz
Summary  : 'parse and validate simple name/value option pairs'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-Data-OptList-license = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(Sub::Install)
BuildRequires : perl-Params-Util

%description
This archive contains the distribution Data-OptList,
version 0.110:
parse and validate simple name/value option pairs

%package dev
Summary: dev components for the perl-Data-OptList package.
Group: Development
Provides: perl-Data-OptList-devel = %{version}-%{release}

%description dev
dev components for the perl-Data-OptList package.


%package license
Summary: license components for the perl-Data-OptList package.
Group: Default

%description license
license components for the perl-Data-OptList package.


%prep
%setup -q -n Data-OptList-0.110
cd ..
%setup -q -T -D -n Data-OptList-0.110 -b 1
mkdir -p deblicense/
mv %{_topdir}/BUILD/debian/* %{_topdir}/BUILD/Data-OptList-0.110/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Data-OptList
cp LICENSE %{buildroot}/usr/share/package-licenses/perl-Data-OptList/LICENSE
cp deblicense/copyright %{buildroot}/usr/share/package-licenses/perl-Data-OptList/deblicense_copyright
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.1/Data/OptList.pm

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Data::OptList.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Data-OptList/LICENSE
/usr/share/package-licenses/perl-Data-OptList/deblicense_copyright
