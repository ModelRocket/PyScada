FROM python:latest
LABEL maintainer="pymodbus | Nicholas Mayne"

#RUN apt-get -y update && \
#    apt-get -y upgrade && \
#    apt-get -y install python3-mysqldb libmysqlclient-dev && \
#    apt-get purge && \
#    apt-get clean && \
#    rm -rf /var/lib/apt/lists/*

WORKDIR /src/pymodbus

RUN pip3 install pymodbus
RUN pip3 install aiohttp
CMD ["pymodbus.simulator"]
