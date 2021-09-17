FROM python:3.8-buster
# Create app directory
WORKDIR /usr/src/configs

# Install app dependencies
COPY . .

RUN ["pip3", "install", "-U","pip"]
RUN ["pip3", "install", "-U","pygments"]
RUN ["pip3", "install", "-U","requests"]
RUN ["pip3", "install", "-U","flask"]
RUN ["pip3", "install", "-U","requests"]
RUN ["pip3", "install", "-r","requirements/common.txt"]

RUN ["chmod", "+x", "./start.sh"]
CMD ["./start.sh"]
