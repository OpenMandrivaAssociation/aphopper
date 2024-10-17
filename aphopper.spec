%define name	aphopper
%define version	0.3
%define release 9

Name: 	 	%{name}
Summary: 	Automatic wireless access point hopper
Version: 	%{version}
Release: 	%{release}

Source:		%{name}-%{version}.tar.bz2
URL:		https://aphopper.sourceforge.net/
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
%configure2_5x
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




%changelog
* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 0.3-8mdv2011.0
+ Revision: 616597
- the mass rebuild of 2010.0 packages

* Wed Sep 02 2009 Thierry Vignaud <tv@mandriva.org> 0.3-7mdv2010.0
+ Revision: 424798
- fix build (use %%configure2_5x)
- rebuild
- rebuild

* Tue Jul 22 2008 Thierry Vignaud <tv@mandriva.org> 0.3-5mdv2009.0
+ Revision: 240306
- rebuild
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot


* Sun Feb 04 2007 Nicolas Lécureuil <neoclust@mandriva.org> 0.3-3mdv2007.0
+ Revision: 116144
- Rebuild
- Import aphopper

* Tue Nov 08 2005 Austin Acton <austin@mandriva.org> 0.3-2mdk
- Rebuild

