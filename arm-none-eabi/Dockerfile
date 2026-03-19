FROM ubuntu:latest
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y wget python3 build-essential gcc-arm-none-eabi libnewlib-arm-none-eabi libstdc++-arm-none-eabi-newlib git
RUN wget https://github.com/Kitware/CMake/releases/download/v4.2.0/cmake-4.2.0-linux-x86_64.tar.gz
RUN tar -xvzf cmake-4.2.0-linux-x86_64.tar.gz
WORKDIR cmake-4.2.0-linux-x86_64
RUN cp -rf bin/* /usr/local/bin
RUN cp -rf man/* /usr/local/man
RUN cp -rf share/* /usr/local/share
WORKDIR /home/root
RUN cmake --version
