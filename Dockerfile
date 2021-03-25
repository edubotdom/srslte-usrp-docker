ARG UBUNTU_VERSION=focal

FROM ubuntu:${UBUNTU_VERSION} as builder
ARG UBUNTU_VERSION
ARG SRSLTE_REPO=https://github.com/srsLTE/srsLTE
ARG SRSLTE_CHECKOUT=master

# Installing the UHD driver
RUN apt-get update \
 && apt-get install -y software-properties-common \
 && add-apt-repository ppa:ettusresearch/uhd \
 && apt-get update \
 && apt-get install -y \
        build-essential \
        git \
        cmake \
        libuhd-dev \
        uhd-host \
	libuhd3.15.0 \
	python3-pip \
 && rm -rf /var/lib/apt/lists/*

#Download uhd images
RUN /usr/lib/uhd/utils/uhd_images_downloader.py


#Installing srsLTE
RUN add-apt-repository ppa:srslte/releases \
 && apt-get update \
 && pip3 install six \
 && apt-get install -y \
        srsenb \
        srsepc \
 && rm -rf /var/lib/apt/lists/*

RUN srslte_install_configs.sh user

#Download config repo
RUN git clone https://github.com/edubotdom/srslte-usrp-docker.git ./srslte-usrp-docker

# Set up paths
ENV LD_LIBRARY_PATH /opt/srslte/lib:$LD_LIBRARY_PATH
ENV PATH /opt/srslte/bin:$PATH

WORKDIR /conf
