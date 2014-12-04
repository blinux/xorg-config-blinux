#-
# Copyright 2014 Emmanuel Vadot <elbarto@bocal.org>
# All rights reserved
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted providing that the following conditions 
# are met:
# 1. Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE AUTHOR ``AS IS'' AND ANY EXPRESS OR
# IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED.  IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY
# DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS
# OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
# HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT,
# STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING
# IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

Name:		xorg-config-BLINUX
Version:        0.1
Release:        1
Summary:        Xorg Configuration
License:        BSD-2-Clause
Group:          System Environment/X11

Source0:        50-device-840.conf
Source1:	xorg-config-BLINUX

BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

Packager:       Emmanuel Vadot <elbarto@bocal.org>
Url:            http://www.blinux.fr

%description
Xorg configuration files for BLINUX

%prep

%build

%post
/usr/sbin/xorg-config-BLINUX

%install
mkdir -p %{buildroot}/%{_sysconfdir}/X11/xorg.conf.blinux/
mkdir -p %{buildroot}/%{_sbindir}
install -D -p -m 755 %{SOURCE0} %{buildroot}/%{_sysconfdir}/X11/xorg.conf.blinux/
install -D -p -m 755 %{SOURCE1} %{buildroot}/%{_sbindir}/

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_sysconfdir}/X11/xorg.conf.blinux/50-device-840.conf
%{_sbindir}/xorg-config-BLINUX

%changelog
* Sat Oct 04 2014 Emmanuel Vadot <elbarto@bocal.org> - 0.1-0
- Package creation
