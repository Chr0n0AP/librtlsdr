#
# This file is protected by Copyright. Please refer to the COPYRIGHT file
# distributed with this source distribution.
#
# This file is part of REDHAWK.
#
# REDHAWK is free software: you can redistribute it and/or modify it
# under the terms of the GNU Lesser General Public License as published by the
# Free Software Foundation, either version 3 of the License, or (at your
# option) any later version.
#
# REDHAWK is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE.  See the GNU Lesser General Public License
# for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with this program.  If not, see http://www.gnu.org/licenses/.

#reflects the name in the configure.ac file
Name:		librtlsdr
Version:	0.5.2
Release:	4%{?dist}
Summary:	The librtlsdr library used to interface with rtl dongles.

Group:		Applications/Engineering
License:	GPL
Source0:	%{name}-%{version}.tar.gz

AutoReqProv: yes

BuildRequires:	autoconf automake libtool

%if "%{?rhel}" == "6"
Requires: libuuid
BuildRequires: libuuid-devel
%else
Requires: e2fsprogs
BuildRequires: e2fsprogs-devel
%endif

# libusb requirements
Requires:      libusb1 >= 1.0.0
BuildRequires: libusb1-devel >= 1.0.0

# Required to generate documentation
BuildRequires: doxygen

BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot


%description
The librtlsdr Library for use with REDHAWK.
 * Commit: __REVISION__
 * Source Date/Time: __DATETIME__


%prep
%setup -q


%build
autoreconf -i
%configure
make %{?_smp_mflags} 


%install
rm -rf %{buildroot}
make install install-udev-rules DESTDIR=%{buildroot}
make install install-blacklist DESTDIR=%{buildroot}


%post
rmmod dvb_usb_rtl28xxu &> /dev/null || true


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%{_includedir}/rtl-sdr.h 
%{_includedir}/rtl-sdr_export.h
%{_libdir}/librtlsdr.la
%{_libdir}/librtlsdr.a
%{_libdir}/librtlsdr.so
%{_libdir}/librtlsdr.so.0
%{_libdir}/librtlsdr.so.0.0.5
%{_libdir}/pkgconfig/librtlsdr.pc
%{_bindir}/rtl_sdr
%{_bindir}/rtl_tcp
%{_bindir}/rtl_test
%{_bindir}/rtl_fm
%{_bindir}/rtl_eeprom
%{_bindir}/rtl_adsb
%{_bindir}/rtl_power
%{_docdir}/%{name}
%{_sysconfdir}/udev/rules.d
%{_sysconfdir}/modprobe.d/blacklist-dvb_usb_rtl28xxu.conf
