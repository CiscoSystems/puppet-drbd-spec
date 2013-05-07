Name:		puppet-drbd	
Version:	0.2
Release:	1cisco%{?dist}
Summary:	Puppet drbd module

Group:		System Environment/Base
License: 	Apache License 2.0	
URL:		https://github.com/CiscoSystems/puppet-drbd.git
Source0: 	%{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%define tmpname %(echo %{name} | cut -d- -f 2-)

%description
configures drbd and ensures that it is running

%prep
%setup -q


%build

%install
rm -rf %{buildroot}
install -d %{buildroot}/%{_usr}/share/puppet/modules/%{tmpname}/
cp -R * %{buildroot}/%{_usr}/share/puppet/modules/%{tmpname}/

%files
%dir %{_usr}/share/puppet/modules/%{tmpname}/
%{_usr}/share/puppet/modules/%{tmpname}/*


%defattr(-,root,root,-)
%doc README examples/

%clean
rm -rf %{buildroot}

%changelog
* Tue May 07 2013 Pradeep Kilambi <pkilambi@cisco.com> 0.2-1cisco
- new package built with tito

* Tue Apr 25 2013 Pradeep Kilambi <pkilambi@cisco.com> - 0.1-1cisco
- Initial package.

