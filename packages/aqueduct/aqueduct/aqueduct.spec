#Aqueduct - Compliance Remediation Content
#Copyright (C) 2011,2012  Shannon Mitchell (shannon.mitchell@fusiontechnology-llc.com)
#
#This program is free software; you can redistribute it and/or
#modify it under the terms of the GNU General Public License
#as published by the Free Software Foundation; either version 2
#of the License, or (at your option) any later version.
#
#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.
#
#You should have received a copy of the GNU General Public License
#along with this program; if not, write to the Free Software
#Foundation, Inc., 51 Franklin Street, Fifth Floor,
#Boston, MA  02110-1301, USA.

Name:		aqueduct
Version:	1
Release:	0.1
Summary:	BASH scripts from the Aqueduct Project (https:/fedorahosted.org/aqueduct) that are meant to assist in the securing of a RHEL server.

Group:		Application/SystemTools
License:	GPL
Source0:	%{name}-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildArch:	noarch
Requires: 	bash filesystem gzip

%description
BASH scripts from the Aqueduct Project (https:/fedorahosted.org/aqueduct) that are meant to assist in the securing of a RHEL server.

%package CIS
Group:		Application/SystemTools
Summary: 	Compliance scripts for the CIS (Center for Internet Security) Benchmarks.
%description CIS
This package contains the compliance scripts and default profiles for the CIS Benchmarks. 

%package DISA
Group:		Application/SystemTools
Summary: 	Compliance scripts for the DISA (Defense Information Systems Agency) STIG(Security Technical Implementation Guides).
%description DISA
This package contains the compliance scripts and default profiles for the DISA STIG. 

%package DHS
Group:		Application/SystemTools
Summary: 	Compliance scripts for the DHS (Defense Homeland Security).
%description DHS
This package contains the compliance scripts and default profiles for the DHS. 

%package NISPOM
Group:		Application/SystemTools
Summary: 	Compliance scripts for the NISPOM (National Industrial Security Program Operating Manual).
%description NISPOM
This package contains the compliance scripts and default profiles for the NISPOM. 

%package PCI
Group:		Application/SystemTools
Summary: 	Compliance scripts for the PCI (Payment Card Industry).
%description PCI
This package contains the compliance scripts and default profiles for PCI compliance. 



%prep
%setup -q


%build


%install

# Main aqueduct package
install -m 0755 -d $RPM_BUILD_ROOT/etc/aqueduct
install -m 0640 etc/aqueduct/aqueduct.conf $RPM_BUILD_ROOT/etc/aqueduct/aqueduct.conf
install -m 0755 -d $RPM_BUILD_ROOT/etc/aqueduct/profiles
install -m 0755 -d $RPM_BUILD_ROOT/usr/libexec/aqueduct
install -m 0755 -d $RPM_BUILD_ROOT/usr/bin
install -m 0750 aqueduct $RPM_BUILD_ROOT/usr/bin/aqueduct
install -m 0750 -d $RPM_BUILD_ROOT/usr/share/man/man1
install -m 644 docs/man1/aqueduct.1 $RPM_BUILD_ROOT/usr/share/man/man1/aqueduct.1
gzip $RPM_BUILD_ROOT/usr/share/man/man1/aqueduct.1

# Files involved in the CIS
install -m 0755 -d $RPM_BUILD_ROOT/etc/aqueduct/profiles/CIS/rhel-5-beta
install -m 0755 -d $RPM_BUILD_ROOT/usr/libexec/aqueduct/CIS/rhel-5-beta/scripts
# install -m 0640 etc/aqueduct/profiles/CIS/rhel-5-beta/default.profile $RPM_BUILD_ROOT/etc/aqueduct/profiles/CIS/rhel-5-beta/default.profile
# install -m 0755 -d $RPM_BUILD_ROOT/etc/aqueduct/profiles/CIS/firefox
# install -m 0755 -d $RPM_BUILD_ROOT/usr/libexec/aqueduct/CIS/firefox/scripts
# install -m 0640 etc/aqueduct/profiles/CIS/firefox/default.profile $RPM_BUILD_ROOT/etc/aqueduct/profiles/CIS/firefox/default.profile
install -m 0750  -t $RPM_BUILD_ROOT/usr/libexec/aqueduct/CIS/rhel-5-beta/scripts compliance/Bash/CIS/rhel5/prod/CIS*

# Files involved in the DISA STIG
install -m 0755 -d $RPM_BUILD_ROOT/etc/aqueduct/profiles/DISA/rhel-5-beta
install -m 0755 -d $RPM_BUILD_ROOT/usr/libexec/aqueduct/DISA/rhel-5-beta/scripts
install -m 0640 etc/aqueduct/profiles/DISA/rhel-5-beta/default.profile $RPM_BUILD_ROOT/etc/aqueduct/profiles/DISA/rhel-5-beta/default.profile
install -m 0755 -d $RPM_BUILD_ROOT/etc/aqueduct/profiles/DISA/firefox
install -m 0755 -d $RPM_BUILD_ROOT/usr/libexec/aqueduct/DISA/firefox/scripts
install -m 0640 etc/aqueduct/profiles/DISA/firefox/default.profile $RPM_BUILD_ROOT/etc/aqueduct/profiles/DISA/firefox/default.profile
install -m 0750  -t $RPM_BUILD_ROOT/usr/libexec/aqueduct/DISA/rhel-5-beta/scripts compliance/Bash/STIG/rhel-5-beta/prod/GEN*

# Files involved in the DHS
install -m 0755 -d $RPM_BUILD_ROOT/etc/aqueduct/profiles/DHS/rhel-6-beta
install -m 0755 -d $RPM_BUILD_ROOT/usr/libexec/aqueduct/DHS/rhel-6-beta/scripts/basic
install -m 0755 -d $RPM_BUILD_ROOT/usr/libexec/aqueduct/DHS/rhel-6-beta/scripts/enhanced
# install -m 0640 etc/aqueduct/profiles/DHS/rhel-6-beta/default.profile $RPM_BUILD_ROOT/etc/aqueduct/profiles/DHS/rhel-5-beta/default.profile
# install -m 0755 -d $RPM_BUILD_ROOT/etc/aqueduct/profiles/DHS/firefox
# install -m 0755 -d $RPM_BUILD_ROOT/usr/libexec/aqueduct/DHS/firefox/scripts
# install -m 0640 etc/aqueduct/profiles/DHS/firefox/default.profile $RPM_BUILD_ROOT/etc/aqueduct/profiles/DHS/firefox/default.profile
install -m 0750  -t $RPM_BUILD_ROOT/usr/libexec/aqueduct/DHS/rhel-6-beta/scripts/basic compliance/Bash/DHS/rhel6/basic/prod/DHS*
install -m 0750  -t $RPM_BUILD_ROOT/usr/libexec/aqueduct/DHS/rhel-6-beta/scripts/enhanced compliance/Bash/DHS/rhel6/enhanced/prod/DHS*

# Files involved in the NISPOM
install -m 0755 -d $RPM_BUILD_ROOT/etc/aqueduct/profiles/NISPOM/rhel-6-beta
install -m 0755 -d $RPM_BUILD_ROOT/usr/libexec/aqueduct/NISPOM/rhel-6-beta/scripts
# install -m 0640 etc/aqueduct/profiles/NISPOM/rhel-6-beta/default.profile $RPM_BUILD_ROOT/etc/aqueduct/profiles/NISPOM/rhel-6-beta/default.profile
# install -m 0755 -d $RPM_BUILD_ROOT/etc/aqueduct/profiles/NISPOM/firefox
# install -m 0755 -d $RPM_BUILD_ROOT/usr/libexec/aqueduct/NISPOM/firefox/scripts
# install -m 0640 etc/aqueduct/profiles/NISPOM/firefox/default.profile $RPM_BUILD_ROOT/etc/aqueduct/profiles/NISPOM/firefox/default.profile
install -m 0750  -t $RPM_BUILD_ROOT/usr/libexec/aqueduct/NISPOM/rhel-6-beta/scripts compliance/Bash/NISPOM/rhel6/prod/NISPOM*

# Files involved in the PCI
install -m 0755 -d $RPM_BUILD_ROOT/etc/aqueduct/profiles/PCI/rhel-6-beta
install -m 0755 -d $RPM_BUILD_ROOT/usr/libexec/aqueduct/PCI/rhel-6-beta/scripts
# install -m 0640 etc/aqueduct/profiles/PCI/rhel-6-beta/default.profile $RPM_BUILD_ROOT/etc/aqueduct/profiles/PCI/rhel-6-beta/default.profile
# install -m 0755 -d $RPM_BUILD_ROOT/etc/aqueduct/profiles/PCI/firefox
install -m 0755 -d $RPM_BUILD_ROOT/usr/libexec/aqueduct/PCI/firefox/scripts
# install -m 0640 etc/aqueduct/profiles/PCI/firefox/default.profile $RPM_BUILD_ROOT/etc/aqueduct/profiles/PCI/firefox/default.profile
install -m 0750  -t $RPM_BUILD_ROOT/usr/libexec/aqueduct/PCI/rhel-6-beta/scripts compliance/Bash/PCI/rhel6/prod/pci*


%clean
rm -rf $RPM_BUILD_ROOT


%files
%dir /etc/aqueduct
%dir /etc/aqueduct/profiles
%dir /usr/libexec/aqueduct
%doc /usr/share/man/man1/aqueduct.1.gz
/etc/aqueduct/aqueduct.conf
/usr/bin/aqueduct

%files CIS
%dir /etc/aqueduct/profiles/CIS
%dir /etc/aqueduct/profiles/CIS/rhel-5-beta
# %dir /etc/aqueduct/profiles/CIS/firefox
# /etc/aqueduct/profiles/CIS/rhel-5-beta/default.profile
# /etc/aqueduct/profiles/CIS/firefox/default.profile
/usr/libexec/aqueduct/CIS/rhel-5-beta/scripts
#/usr/libexec/aqueduct/CIS/firefox/scripts

%files DISA
%dir /etc/aqueduct/profiles/DISA
%dir /etc/aqueduct/profiles/DISA/rhel-5-beta
%dir /etc/aqueduct/profiles/DISA/firefox
/etc/aqueduct/profiles/DISA/rhel-5-beta/default.profile
/etc/aqueduct/profiles/DISA/firefox/default.profile
/usr/libexec/aqueduct/DISA/rhel-5-beta/scripts
/usr/libexec/aqueduct/DISA/firefox/scripts

%files DHS
%dir /etc/aqueduct/profiles/DHS
%dir /etc/aqueduct/profiles/DHS/rhel-6-beta
# %dir /etc/aqueduct/profiles/DHS/firefox
# /etc/aqueduct/profiles/DHS/rhel-6-beta/default.profile
# /etc/aqueduct/profiles/DHS/firefox/default.profile
/usr/libexec/aqueduct/DHS/rhel-6-beta/scripts/basic
/usr/libexec/aqueduct/DHS/rhel-6-beta/scripts/enhanced
# /usr/libexec/aqueduct/DHS/firefox/scripts

%files NISPOM
%dir /etc/aqueduct/profiles/NISPOM
%dir /etc/aqueduct/profiles/NISPOM/rhel-6-beta
# %dir /etc/aqueduct/profiles/NISPOM/firefox
# /etc/aqueduct/profiles/NISPOM/rhel-6-beta/default.profile
# /etc/aqueduct/profiles/NISPOM/firefox/default.profile
/usr/libexec/aqueduct/NISPOM/rhel-6-beta/scripts
# /usr/libexec/aqueduct/NISPOM/firefox/scripts

%files PCI
%dir /etc/aqueduct/profiles/PCI
%dir /etc/aqueduct/profiles/PCI/rhel-6-beta
# %dir /etc/aqueduct/profiles/PCI/firefox
# /etc/aqueduct/profiles/PCI/rhel-6-beta/default.profile
# /etc/aqueduct/profiles/PCI/firefox/default.profile
/usr/libexec/aqueduct/PCI/rhel-6-beta/scripts
/usr/libexec/aqueduct/PCI/firefox/scripts


%post

%changelog
* Sun Apr 8 2012 Shannon Mitchell <shannon.mitchell@fusiontechnology-llc.com>
  - Initial Spec file creation
* Tue May 4 2012 Ted Brunell <tbrunell@redhat.com>
  - CIS, DHS, NISPOM, & PCI sections added to Spec file.
