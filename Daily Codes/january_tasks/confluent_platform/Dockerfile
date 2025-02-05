FROM ubuntu:20.04
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -y \
    openjdk-11-jre \
    python3.9 \
    python3-pip \
    curl \
    unzip
RUN curl -O https://packages.confluent.io/archive/7.8/confluent-7.8.0.zip
RUN unzip confluent-7.8.0.zip
RUN apt-get install nano
ENV CONFLUENT_HOME=/confluent-7.8.0
ENV PATH=$PATH:$CONFLUENT_HOME/bin
WORKDIR /confluent-platform
EXPOSE 9021 9092 2181 8081 8083 8088
CMD ["tail", "-f", "/dev/null"]
