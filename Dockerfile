FROM ubuntu:14.04

RUN apt-get update -qq && \
    apt-get install -y autoconf \
                       automake \
                       autotools-dev \
                       libtool \
                       libusb-1.0-0-dev \
                       make \
                       pkg-config && \
    rm -rf /var/lib/apt/lists/*

COPY . /build
WORKDIR /build
RUN ./build.sh && make install && ldconfig
