FROM ubuntu:latest

RUN apt update && apt install -y \
    openssh-server \
    python3 \
    python3-apt \
    sudo && \
    apt clean

RUN mkdir /var/run/sshd
RUN echo 'root:ancible' | chpasswd

RUN sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config
RUN sed -i 's/UsePAM yes/UsePAM no/' /etc/ssh/sshd_config

EXPOSE 22

CMD ["/usr/sbin/sshd", "-D"]
