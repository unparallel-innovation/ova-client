FROM python:3.8-buster
# Create app directory

# Install app dependencies
RUN ["git", "clone", "https://github.com/openvisionapi/ova-server"]
WORKDIR "/ova-server"
RUN ["git", "checkout", "69bfb85d52d0ff1752804d66539e94be517b15f4"]
#WORKDIR /usr/src/configs

# Install app dependencies
#COPY . .

RUN make setup-tensorflow-lite
RUN /bin/bash -c "source .venv/bin/activate; ./cli.py download --model=yolov4 --framework=tensorflow_lite --hardware=cpu"


CMD ["make", "run"]
