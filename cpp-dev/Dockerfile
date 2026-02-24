FROM docker.io/ubuntu

ENV PATH="/root/.local/bin:${PATH}"

RUN apt upgrade -y && apt update -y
RUN apt install python3 python3-pip pipx wget unzip dos2unix -y

RUN wget https://github.com/Kitware/CMake/releases/download/v4.3.0-rc1/cmake-4.3.0-rc1-linux-x86_64.sh
RUN yes | bash cmake-*

RUN wget https://github.com/conan-io/conan/releases/download/2.25.2/conan-2.25.2-linux-x86_64.tgz
RUN tar -xvf conan-2.25.2-linux-x86_64.tgz
RUN cp -rf conan-*/bin/* /usr/bin

WORKDIR /usr/bin

COPY *.py .
RUN chmod +x build.py
RUN chmod +x run.py

RUN dos2unix /usr/bin/*.py

CMD ["bash"]