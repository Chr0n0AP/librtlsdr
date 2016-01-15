#RTLSDR library
## Description
This is the forked version of RTLSDR library for building the REDHAWK rtldevice

## Build Requirements
The following dependencies are needed to build the rtlsdr library:

    libusb-1.0

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

REDHAWK Website: [www.redhawksdrorg](http://www.redhawksdr.org)

## Copyrights

This work is protected by Copyright. Please refer to the [Copyright File](COPYRIGHT) for updated copyright information.

## License

REDHAWK RTLSDR device is licensed under the GNU General Public License (GPL).
RTLSDR library is licensed under the GNU General Public License (GPL).

