Name:           mysql-connector-net
Version:        5.1.7
Release:        %mkrel 2
License:        GPL+
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch: noarch
BuildRequires:  nant
URL: http://dev.mysql.com/downloads/connector/net/
Source:         %{name}-%{version}-src.zip
Group:          Development/Other
Summary:        MySQL Connector/Net

%description
MySQL Connector/Net is an ADO.NET driver for MySQL.

%prep
%setup -q -c

%build
nant -buildfile:Client.build  mono-2.0

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
