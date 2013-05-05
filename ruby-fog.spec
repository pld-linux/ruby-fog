#
# Conditional build:
%bcond_without	tests		# build without tests

%define	pkgname	fog
Summary:	The Ruby cloud services library
Name:		ruby-%{pkgname}
Version:	1.7.0
Release:	1
License:	MIT
Group:		Development/Languages
Source0:	https://github.com/fog/fog/archive/v%{version}.tar.gz
# Source0-md5:	5a44426761b54a8497f4c55caf0ffbe4
URL:		http://fog.io/
BuildRequires:	rpm-rubyprov
BuildRequires:	rpmbuild(macros) >= 1.656
BuildRequires:	sed >= 4.0
Requires:	ruby-builder
Requires:	ruby-excon < 1
Requires:	ruby-excon >= 0.14
Requires:	ruby-formatador < 0.3
Requires:	ruby-formatador >= 0.2.0
Requires:	ruby-hmac
Requires:	ruby-mime-types
Requires:	ruby-multi_json < 2
Requires:	ruby-multi_json >= 1.0
Requires:	ruby-net-scp >= 1.0.4
Requires:	ruby-net-ssh >= 2.1.3
Requires:	ruby-nokogiri < 1.6
Requires:	ruby-nokogiri >= 1.5.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Ruby cloud services library. Supports all major cloud providers
including AWS, Rackspace, Linode, Blue Box, StormOnDemand, and many
others. Full support for most AWS services including EC2, S3,
CloudWatch, SimpleDB, ELB, and RDS.

%prep
%setup -q -n %{pkgname}-%{version}
%{__sed} -i -e '1 s,#!.*ruby,#!%{__ruby},' bin/*

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_vendorlibdir},%{_bindir}}
cp -a lib/* $RPM_BUILD_ROOT%{ruby_vendorlibdir}
cp -a bin/* $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/fog
%{ruby_vendorlibdir}/%{pkgname}.rb
%{ruby_vendorlibdir}/%{pkgname}
