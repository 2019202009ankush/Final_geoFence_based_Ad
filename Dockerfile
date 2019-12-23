FROM python:3.6.1-alpine
COPY requirements.txt requirements.txt
COPY new_redis_mqtt.py new_redis_mqtt.py
COPY new_web_socket.py new_web_socket.py
COPY periodic_update.py periodic_update.py
COPY geo_fence_reg.py geo_fence_reg.py
COPY redis_key_value.py redis_key_value.py
COPY sample.py sample.py
COPY loading_environment.py loading_environment.py
COPY new_server_pb2.py new_server_pb2.py
COPY .env .env
RUN pip3 install -r requirements.txt
