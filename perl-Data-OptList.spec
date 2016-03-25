#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Data-OptList
Version  : 0.110
Release  : 8
URL      : http://search.cpan.org/CPAN/authors/id/R/RJ/RJBS/Data-OptList-0.110.tar.gz
Source0  : http://search.cpan.org/CPAN/authors/id/R/RJ/RJBS/Data-OptList-0.110.tar.gz
Summary  : 'parse and validate simple name/value option pairs'
Group    : Development/Tools
License  : Artistic-1.0-Perl
Requires: perl-Data-OptList-doc
BuildRequires : perl(Params::Util)
BuildRequires : perl(Sub::Install)

%description
This archive contains the distribution Data-OptList,
version 0.110:
parse and validate simple name/value option pairs

%package doc
Summary: doc components for the perl-Data-OptList package.
Group: Documentation

%description doc
doc components for the perl-Data-OptList package.


%prep
%setup -q -n Data-OptList-0.110

%build
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make V=1  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot}
else
./Build install --installdirs=site --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/site_perl/5.22.0/Data/OptList.pm

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man3/*
