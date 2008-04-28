Name:           mysql-connector-net
Version:        5.0.9
Release:        %mkrel 1
License:        GPL
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch: noarch
BuildRequires:  nant
#BuildRequires:  nunit
URL: http://dev.mysql.com/downloads/connector/net/
Source:         %{name}-%{version}-src.zip
Patch:          disable-test-suite.patch
Group:          Development/Other
Summary:        MySQL Connector/Net

%description
MySQL Connector/Net is an ADO.NET driver for MySQL.

%prep
%setup -q -c
%patch

%build
nant -buildfile:Client.build -D:nunit2.dir=/usr/lib/nunit mono-2.0

%install
rm -rf "$RPM_BUILD_ROOT"
gacutil -i Driver/bin/mono-2.0/release/MySql.Data.dll -package mysql-connector-net -root ${RPM_BUILD_ROOT}%{_prefix}/lib

%clean
rm -rf "$RPM_BUILD_ROOT"

%files
%defattr(-,root,root)
%doc README CHANGES COPYING EXCEPTIONS Release\ Notes.txt
%{_prefix}/lib/mono/gac/MySql.Data/
%{_prefix}/lib/mono/mysql-connector-net/MySql.Data.dll
