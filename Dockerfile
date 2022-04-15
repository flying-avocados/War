# Ubuntu Linux as the base image
FROM ubuntu:18.04

# Set UTF-8 encoding
ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8

# Install Python
RUN apt-get -y update && \
    apt-get -y upgrade && \
    apt-get -y install python3-pip python3-dev


RUN mkdir /War_game
ADD War.py /War_game


# Change the permissions of programs
CMD ["chmod 777 /War_game/*"]

# Set working dir as /QA
WORKDIR /War_game
ENTRYPOINT ["/bin/bash", "-c"]