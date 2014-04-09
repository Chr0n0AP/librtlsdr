#RTLSDR library
## Description
This is the forked version of RTLSDR library for building the REDHAWK rtldevice

## Build Requirements 
To building the rtlsdr library you will need the following packages:
libusb1.0-devel

## Build and Installation
To build the library run the following commands:

autoreconf -i
./configure
make
sudo make install
sudo ldconfig

In order to be able to use the dongle as a non-root user, you may install the appropriate udev rules file by calling

sudo make install-udev-rules

## REDHAWK Documentation

REDHAWK Website: [www.redhawkSDR.org](http://www.redhawksdr.org)

Overview and Getting Started Guide: [PDF](http://sourceforge.net/projects/redhawksdr/files/redhawk-doc/1.9.0/REDHAWK_Overview_v1.9.0.pdf/download "PDF") [HTML](http://redhawksdr.github.com/Documentation/gettingstarted/main.html "HTML")

Full REDHAWK Manual: [PDF](http://sourceforge.net/projects/redhawksdr/files/redhawk-doc/1.9.0/REDHAWK_Manual_v1.9.0.pdf/download "PDF") [HTML](http://redhawksdr.github.com/Documentation/main.html "HTML")
 
## Copyrights

This work is protected by Copyright. Please refer to the [Copyright File](COPYRIGHT) for updated copyright information.

## License

REDHAWK RTLSDR device is licensed under the GNU General Public License (GPL).
RTLSDR library is licensed under the GNU General Public License (GPL).

