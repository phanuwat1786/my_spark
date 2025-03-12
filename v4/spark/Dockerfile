FROM bitnami/spark:latest

USER root
COPY requirements.txt .
RUN pip install -r requirements.txt \
    && apt update \
    && apt install -y --no-install-recommends curl wget \
    && apt-get clean 

COPY ./config/spark-defaults.conf ./conf/spark-defaults.conf
# CMD ["bash"]