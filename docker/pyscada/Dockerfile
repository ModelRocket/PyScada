FROM python:latest
LABEL maintainer="PyScada | Martin Schröder"
ENV DEBIAN_FRONTEND noninteractive

#RUN apt-get -y update && \
#    apt-get -y upgrade && \
#    apt-get -y install python3-mysqldb libmysqlclient-dev && \
#    apt-get purge && \
#    apt-get clean && \
#    rm -rf /var/lib/apt/lists/*

ENV LANG C.UTF-8

COPY project_template.zip /src/pyscada/
COPY pyscada.zip /src/pyscada/
COPY pyscada /src/pyscada/
COPY pyscada_init /src/pyscada/
RUN touch /src/pyscada/pyscada_debug.log
WORKDIR /src/pyscada
RUN apt-get update
RUN apt-get -y install vim

RUN pip3 install gunicorn
RUN pip3 install mysqlclient
RUN pip3 install /src/pyscada/pyscada.zip

WORKDIR /src
RUN git clone https://github.com/pyscada/PyScada-Modbus.git
RUN pip3 install -e /src/PyScada-Modbus
# RUN pip3 install pyscada-modbus
WORKDIR /src/pyscada
RUN django-admin startproject PyScadaServer /src/pyscada/ --template /src/pyscada/project_template.zip
RUN chmod +x /src/pyscada/pyscada
RUN chmod +x /src/pyscada/pyscada_init

CMD ["/src/pyscada/pyscada"]
