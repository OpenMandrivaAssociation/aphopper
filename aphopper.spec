%define name	aphopper
%define version	0.3
%define release %mkrel 7

Name: 	 	%{name}
Summary: 	Automatic wireless access point hopper
Version: 	%{version}
Release: 	%{release}

Source:		%{name}-%{version}.tar.bz2
URL:		http://aphopper.sourceforge.net/
License:	GPL
Group:		System/Configuration/Networking
BuildRoot:	%{_tmppath}/%{name}-buildroot

%description
AP Hopper is a program that automatically hops between access points of
different wireless networks. It checks for DHCP and Internet Access on all
the networks found. It logs successful and unsuccessful attempts.

P.S. The binary is called 'hopper'.

%prep
%setup -q -n %name

%build
%configure
%make
										
%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%_sbindir
cp hopper $RPM_BUILD_ROOT/%_sbindir

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog COPYING
%{_sbindir}/hopper


