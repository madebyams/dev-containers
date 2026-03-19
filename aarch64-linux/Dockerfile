FROM ubuntu:22.04

RUN apt-get update && apt-get upgrade -y && \
    apt-get install -y \
        wget \
        git \
        python3 \
        build-essential \
        cmake \
        binutils-aarch64-linux-gnu \
        gcc-aarch64-linux-gnu \
        g++-aarch64-linux-gnu \
        libc6-dev-arm64-cross \
        pkg-config \
        libpthread-stubs0-dev

RUN wget https://github.com/Kitware/CMake/releases/download/v4.2.0/cmake-4.2.0-linux-x86_64.tar.gz && \
    tar -xvzf cmake-4.2.0-linux-x86_64.tar.gz && \
    cp -rf cmake-4.2.0-linux-x86_64/bin/* /usr/local/bin && \
    cp -rf cmake-4.2.0-linux-x86_64/share/* /usr/local/share && \
    cp -rf cmake-4.2.0-linux-x86_64/man/* /usr/local/man && \
    rm -rf cmake-4.2.0-linux-x86_64 cmake-4.2.0-linux-x86_64.tar.gz

RUN mkdir -p /opt/conan && \
    wget https://github.com/conan-io/conan/releases/download/2.25.2/conan-2.25.2-linux-x86_64.tgz && \
    tar -xvf conan-2.25.2-linux-x86_64.tgz -C /opt/conan && \
    ln -s /opt/conan/bin/conan /usr/local/bin/conan && \
    rm conan-2.25.2-linux-x86_64.tgz

WORKDIR /home/root
RUN cmake --version
RUN conan --version
