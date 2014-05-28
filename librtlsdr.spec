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
#
# By default, the RPM will install to the standard REDHAWK SDR root location (/var/redhawk/sdr)
# You can override this at install time using --prefix /new/sdr/root when invoking rpm (preferred method, if you must)

#reflects the name in the configure.ac file
Name:		librtlsdr
Version:	0.5.2
Release:	1%{?dist}
Summary:	The librtlsdr library used to interface with rtl dongles.
Prefix:		/usr/local

Group:		Applications/Engineering
License:	GPL
URL:		http://redhawksdr.org/	
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

Requires:      libusb1 >= 1.0.0
BuildRequires: libusb1-devel >= 1.0.0

BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot


%description
The librtlsdr Library for use with REDHAWK.
 * Commit: __REVISION__
 * Source Date/Time: __DATETIME__


%prep
%setup -q


%build
autoreconf -i
SDRROOT=%{_sdrroot} %configure
make 


%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}


%clean
rm -rf %{buildroot}


%files
%defattr(644,redhawk,redhawk)
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
%{_docdir}/librtlsdr/librtlsdr-0.5.2/html/annotated.html
%{_docdir}/librtlsdr/librtlsdr-0.5.2/html/classes.html
%{_docdir}/librtlsdr/librtlsdr-0.5.2/html/doxygen.css
%{_docdir}/librtlsdr/librtlsdr-0.5.2/html/doxygen.png
%{_docdir}/librtlsdr/librtlsdr-0.5.2/html/files.html
%{_docdir}/librtlsdr/librtlsdr-0.5.2/html/ftv2blank.png
%{_docdir}/librtlsdr/librtlsdr-0.5.2/html/ftv2doc.png
%{_docdir}/librtlsdr/librtlsdr-0.5.2/html/ftv2folderclosed.png
%{_docdir}/librtlsdr/librtlsdr-0.5.2/html/ftv2folderopen.png
%{_docdir}/librtlsdr/librtlsdr-0.5.2/html/ftv2lastnode.png
%{_docdir}/librtlsdr/librtlsdr-0.5.2/html/ftv2link.png
%{_docdir}/librtlsdr/librtlsdr-0.5.2/html/ftv2mlastnode.png
%{_docdir}/librtlsdr/librtlsdr-0.5.2/html/ftv2mnode.png
%{_docdir}/librtlsdr/librtlsdr-0.5.2/html/ftv2node.png
%{_docdir}/librtlsdr/librtlsdr-0.5.2/html/ftv2plastnode.png
%{_docdir}/librtlsdr/librtlsdr-0.5.2/html/ftv2pnode.png
%{_docdir}/librtlsdr/librtlsdr-0.5.2/html/ftv2vertline.png
%{_docdir}/librtlsdr/librtlsdr-0.5.2/html/getopt_8h_source.html
%{_docdir}/librtlsdr/librtlsdr-0.5.2/html/index.html
%{_docdir}/librtlsdr/librtlsdr-0.5.2/html/main.html
%{_docdir}/librtlsdr/librtlsdr-0.5.2/html/reg__field_8h_source.html
%{_docdir}/librtlsdr/librtlsdr-0.5.2/html/rtl-sdr_8h_source.html
%{_docdir}/librtlsdr/librtlsdr-0.5.2/html/rtl-sdr__export_8h_source.html
%{_docdir}/librtlsdr/librtlsdr-0.5.2/html/rtlsdr__i2c_8h_source.html
%{_docdir}/librtlsdr/librtlsdr-0.5.2/html/structcmd.html
%{_docdir}/librtlsdr/librtlsdr-0.5.2/html/structcmd__state.html
%{_docdir}/librtlsdr/librtlsdr-0.5.2/html/structcommand.html
%{_docdir}/librtlsdr/librtlsdr-0.5.2/html/structdongle__info__t.html
%{_docdir}/librtlsdr/librtlsdr-0.5.2/html/structe4k__pll__params.html
%{_docdir}/librtlsdr/librtlsdr-0.5.2/html/structe4k__state.html
%{_docdir}/librtlsdr/librtlsdr-0.5.2/html/structfm__state.html
%{_docdir}/librtlsdr/librtlsdr-0.5.2/html/structgain__comb.html
%{_docdir}/librtlsdr/librtlsdr-0.5.2/html/structllist.html
%{_docdir}/librtlsdr/librtlsdr-0.5.2/html/structoption.html
%{_docdir}/librtlsdr/librtlsdr-0.5.2/html/structpll__settings.html
%{_docdir}/librtlsdr/librtlsdr-0.5.2/html/structr82xx__config.html
%{_docdir}/librtlsdr/librtlsdr-0.5.2/html/structr82xx__freq__range.html
%{_docdir}/librtlsdr/librtlsdr-0.5.2/html/structr82xx__priv.html
%{_docdir}/librtlsdr/librtlsdr-0.5.2/html/structreg__field.html
%{_docdir}/librtlsdr/librtlsdr-0.5.2/html/structreg__field__ops.html
%{_docdir}/librtlsdr/librtlsdr-0.5.2/html/structrtlsdr__config.html
%{_docdir}/librtlsdr/librtlsdr-0.5.2/html/structrtlsdr__dev.html
%{_docdir}/librtlsdr/librtlsdr-0.5.2/html/structrtlsdr__dongle.html
%{_docdir}/librtlsdr/librtlsdr-0.5.2/html/structrtlsdr__tuner__iface.html
%{_docdir}/librtlsdr/librtlsdr-0.5.2/html/structstrbuf.html
%{_docdir}/librtlsdr/librtlsdr-0.5.2/html/structtuning__state.html
%{_docdir}/librtlsdr/librtlsdr-0.5.2/html/tab_b.gif
%{_docdir}/librtlsdr/librtlsdr-0.5.2/html/tab_l.gif
%{_docdir}/librtlsdr/librtlsdr-0.5.2/html/tab_r.gif
%{_docdir}/librtlsdr/librtlsdr-0.5.2/html/tabs.css
%{_docdir}/librtlsdr/librtlsdr-0.5.2/html/tree.html
%{_docdir}/librtlsdr/librtlsdr-0.5.2/html/tuner__e4k_8h_source.html
%{_docdir}/librtlsdr/librtlsdr-0.5.2/html/tuner__fc0012_8h_source.html
%{_docdir}/librtlsdr/librtlsdr-0.5.2/html/tuner__fc0013_8h_source.html
%{_docdir}/librtlsdr/librtlsdr-0.5.2/html/tuner__fc2580_8h_source.html
%{_docdir}/librtlsdr/librtlsdr-0.5.2/html/tuner__r82xx_8h_source.html
