#!/bin/sh
#
# This file is protected by Copyright. Please refer to the COPYRIGHT file
# distributed with this source distribution.
#
# This file is part of librtlsdr Device.
#
# librtlsdr is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the
# Free Software Foundation, either version 3 of the License, or (at your
# option) any later version.
#
# librtlsdr is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License
# for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see http://www.gnu.org/licenses/.
#

if [ "$1" = "rpm" ]; then
    # A very simplistic RPM build scenario
    if [ -e librtlsdr.spec ]; then
        mydir=`dirname $0`
        tmpdir=`mktemp -d`
        cp -r ${mydir} ${tmpdir}/librtlsdr-0.5.2
        tar czf ${tmpdir}/librtlsdr-0.5.2.tar.gz --exclude=".git" -C ${tmpdir} librtlsdr-0.5.2
        echo `ls ${tmpdir}`
        rpmbuild -ta ${tmpdir}/librtlsdr-0.5.2.tar.gz
        echo "1"
        rm -rf $tmpdir
    else
        echo "Missing RPM spec file in" `pwd`
        exit 1
    fi
else
    autoreconf -i
    ./configure
    make -j
fi
