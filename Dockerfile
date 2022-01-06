FROM python:3.8-buster
# Create app directory
WORKDIR /usr/src/configs

# Install app dependencies
COPY . .

#RUN rm /usr/src/configs/static/predictions.json
#RUN rm /usr/src/configs/static/result.png

RUN ["pip3", "install", "-U","pip"]
RUN ["pip3", "install", "-r","requirements/common.txt"]
RUN ["pip3", "install", "-U","flask"]

RUN ["chmod", "+x", "./start.sh"]
CMD ["./start.sh"]
