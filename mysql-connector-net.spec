Name:           mysql-connector-net
Version:        6.1.3
Release:        %mkrel 2
License:        GPL+
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch: noarch
BuildRequires:  mono-devel >= 2.4.3
URL: http://dev.mysql.com/downloads/connector/net/
Source:         %{name}-%{version}-src.zip
Patch: mysql-connector-net-6.1.3-fix-buildfile.patch
Group:          Development/Other
Summary:        MySQL Connector/Net

%description
MySQL Connector/Net is an ADO.NET driver for MySQL.

%prep
%setup -q -c
%patch -p1

%build
xbuild MySQLClient-mono.sln

%install
rm -rf "$RPM_BUILD_ROOT"
gacutil -i ./MySql.Data/Provider/bin/Release/MySql.Data.dll -package mysql-connector-net -root ${RPM_BUILD_ROOT}%{_prefix}/lib

%clean
rm -rf "$RPM_BUILD_ROOT"

%files
%defattr(-,root,root)
%doc README CHANGES COPYING EXCEPTIONS Release\ Notes.txt
%{_prefix}/lib/mono/gac/MySql.Data/
%{_prefix}/lib/mono/mysql-connector-net/MySql.Data.dll
