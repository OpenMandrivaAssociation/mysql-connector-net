Name:           mysql-connector-net
Version:        6.2.4
Release:        %mkrel 2
License:        GPL+
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch: noarch
BuildRequires:  mono-devel >= 2.4.3
URL: http://dev.mysql.com/downloads/connector/net/
Source:         %{name}-%{version}-src.zip
Patch: mysql-connector-net-6.2.4-fix-buildfile.patch
Group:          Development/Other
Summary:        MySQL Connector/Net

%description
MySQL Connector/Net is an ADO.NET driver for MySQL.

%prep
%setup -q -c
%autopatch -p1

%build
xbuild MySQLClient-mono.sln

%install
rm -rf "$RPM_BUILD_ROOT"
gacutil -i ./MySql.Data/Provider/bin/Release/MySql.Data.dll -package mysql-connector-net -root ${RPM_BUILD_ROOT}%{_prefix}/lib

%clean
rm -rf "$RPM_BUILD_ROOT"

%files
%defattr(-,root,root)
%doc README CHANGES COPYING Release\ Notes.txt
%{_prefix}/lib/mono/gac/MySql.Data/
%{_prefix}/lib/mono/mysql-connector-net/MySql.Data.dll


%changelog
* Tue Oct 11 2011 Götz Waschk <waschk@mandriva.org> 6.2.4-2mdv2012.0
+ Revision: 704154
- rebuild

* Sun Oct 10 2010 Götz Waschk <waschk@mandriva.org> 6.2.4-1mdv2011.0
+ Revision: 584531
- new version
- rediff patch
- update file list

* Thu Dec 17 2009 Götz Waschk <waschk@mandriva.org> 6.1.3-2mdv2010.1
+ Revision: 479709
- new version
- fix build
- fix installation

* Mon Sep 14 2009 Thierry Vignaud <tv@mandriva.org> 5.1.7-2mdv2010.0
+ Revision: 440177
- rebuild

  + Götz Waschk <waschk@mandriva.org>
    - update license

* Mon Dec 01 2008 Götz Waschk <waschk@mandriva.org> 5.1.7-1mdv2009.1
+ Revision: 308776
- new version
- drop patch

* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 5.0.9-2mdv2009.0
+ Revision: 268226
- rebuild early 2009.0 package (before pixel changes)

* Fri Feb 08 2008 Götz Waschk <waschk@mandriva.org> 5.0.8.1-1mdv2008.1
+ Revision: 164051
- import mysql-connector-net


