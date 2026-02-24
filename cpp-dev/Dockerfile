FROM docker.io/ubuntu

ENV PATH="/root/.local/bin:${PATH}"

RUN apt upgrade -y && apt update -y
RUN apt install python3 python3-pip pipx wget unzip dos2unix -y

RUN pip install --break-system-packages conan

WORKDIR /usr

RUN wget https://github.com/Kitware/CMake/releases/download/v4.3.0-rc1/cmake-4.3.0-rc1-linux-x86_64.sh
RUN printf "y\nn\n" | bash cmake-*


WORKDIR /usr/bin


COPY *.py .
RUN chmod +x build.py
RUN chmod +x run.py

RUN dos2unix /usr/bin/*.py

CMD ["bash"]