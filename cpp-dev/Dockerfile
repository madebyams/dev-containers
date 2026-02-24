FROM docker.io/ubuntu

RUN apt upgrade -y && apt update -y
RUN apt install python3 python3-pip pipx wget unzip -y

RUN wget https://github.com/Kitware/CMake/releases/download/v4.3.0-rc1/cmake-4.3.0-rc1-linux-x86_64.sh
RUN yes | bash cmake-*
RUN pipx install conan

WORKDIR /usr/bin
COPY *.py .

CMD ["bash"]