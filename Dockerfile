#
# Python Dockerfile
#
#
#

# Pull base image.
FROM osixia/ubuntu-light-baseimage
MAINTAINER Nicolas Venegas nvnegas.oliva@gmail.com

# Install Python.
RUN \
	apt-get update && \
	apt-get install -y python3-pip && \
	pip3 install boto3
RUN echo 'print("buena buena")' > /home/script.py

CMD python3 /home/script.py